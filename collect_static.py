import serial
import time
import argparse

# from: https://gist.github.com/justinmklam/d8d1c60678827fc4d3943c548cf4d1c2
class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--initial_distance', type=int, default=0)
    parser.add_argument('--step', type=int, default=5)
    parser.add_argument('--device', type=str, default='/dev/cu.usbmodem101')

    args = parser.parse_args()
    ser = serial.Serial(args.device, 9600)
    rl = ReadLine(ser)

    timer = time.perf_counter()
    i = args.initial_distance
    data = []
    while True:
        data.append(rl.readline().decode("utf-8").strip())
        if time.perf_counter() - timer > 10:
            with open(f"data_{i}.csv", "w") as f:
                f.write("\n".join(data))
            print("Do you want to continue (y/n) ?")
            while True:
                a = input()
                if (a.strip() == "y"):
                    data = []
                    timer = time.perf_counter()
                    i += args.step
                    break
                else:
                    exit()

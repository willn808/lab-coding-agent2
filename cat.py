'''
This program prints stdin to the screen.
'''
import sys

BUF_SIZE = 64 * 1024

def cat(file):
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        sys.stdout.buffer.write(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)

import os


def encode():
    filename = os.path.abspath('test1.txt')
    out_file = open('new_file.txt', 'w')
    file = open(filename, 'r')
    for line in file:
        for char in line:
            if not char == '\n':
                out_file.write(str(ord(char)))
            else:
                out_file.write(char)
    out_file.close()


def decode():
    filename = os.path.abspath('new_file.txt')
    out_file = open('new_file2.txt', 'w')
    file = open(filename, 'r')
    for line in file:
        for char in line:
            if not char == '\n':
                out_file.write(chr(char))
            else:
                out_file.write(char)
    out_file.close()


if __name__ == '__main__':
    encode()
    decode()

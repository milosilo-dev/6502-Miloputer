import sys

# IO is on 7F00 - 7FFF

def convert():
    if len(sys.argv) < 3:
        print("Did not provide both an input and an output file!")
        return

    code = []
    with open(sys.argv[1], "rb") as in_file:
        print(str(in_file))
        in_file = str(in_file.read()).split("0x")
        for byte in in_file:
            print(byte)
            byte = "0x" + str(byte)
            code.append(hex(byte))

    rom = code + bytearray([0xea] * (32768 - len(code)))

    rom[0x7ffc] = 0x00
    rom[0x7ffd] = 0x80

    with open(sys.argv[2], "w") as out_file:
        out_file.write("v2.0 raw\n")
        for hexcode in rom:
            out_file.write(str(hex(hexcode)).split("0x")[1])
            out_file.write(" ")

if __name__ == "__main__":
    convert()
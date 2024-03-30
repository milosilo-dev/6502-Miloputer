# IO is on 7F00 - 7FFF

code = bytearray([
    0xa9, 0x55,         # lda #$55
    0x8d, 0x00, 0x7F,   # sta $7F00
    
    0xa9, 0x55,         # lda #$55
    0x8d, 0xFF, 0x7F,   # sta $7FFF
    
    0x4c, 0x05, 0x80    # jmp $8005
])
rom = code + bytearray([0xea] * (32768 - len(code)))

rom[0x7ffc] = 0x00
rom[0x7ffd] = 0x80

with open("rom.bin", "w") as out_file:
    out_file.write("v2.0 raw\n")
    for hexcode in rom:
        out_file.write(str(hex(hexcode)).split("0x")[1])
        out_file.write(" ")
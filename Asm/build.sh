./vbcc/bin/vasm6502_oldstyle -Fbin main.s
cp a.out out.hex
rm a.out
python3 bin-to-logisim.py out.hex rom.bin
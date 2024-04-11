./vbcc/bin/vasm6502_oldstyle -Fbin -dotdir -opt-branch main.s
cp a.out out.rom
rm a.out
python3 bin-to-hex.py -logisim
echo "Assembling the file..."
./vasm/vasm6502_oldstyle -Fbin -dotdir src/main.s
echo "Finished Assembly..."
echo "Formating..."
hexdump -C a.out
echo "v2.0 raw" > out/a.bin
hexdump -e '16/1 "%02x " "\n"' -n 65000 -v a.out | tr '\r\n' ' ' | sed 's/^\s*\|\s*$//g' >> out/a.bin
echo "Cleaning up!"
rm a.out
echo "Done!"
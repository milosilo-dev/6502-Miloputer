 .org $8000
loop:
 lda #$ff
 sta $7F00
     
 lda #$ff
 sta $7FFF
 
 jmp loop

 .org $fffd
 .word loop
 .word loop
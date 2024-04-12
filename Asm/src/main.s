SCREEN = $EF00
 
    .org $F000
reset:
    lda #$00
    sta SCREEN
loop:
    ldx #"H"
    jsr printchar
 
    jmp loop
printchar:
    lda SCREEN,X
    sta SCREEN
    rts

    .org $fffc
    .word reset
    .word $0000
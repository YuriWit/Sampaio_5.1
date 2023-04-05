# Processador



## ISA
Definição de como montar uma instrução

``` asm
;   opcode  R destino   R origem    literal (se tiver)
;   0000    00          00          00000000

                        opcode  R destino   R origem    literal
    MOV Rd, Ro      ;   0000    Rd1 Rd0     Ro1 Ro0
    MOV Rd, k       ;   0001    Rd1 Rd0     X   X       K7 K6 K5 K4 K3 K2 K1 K0
    ADD Rd, Ro      ;   0010    Rd1 Rd0     Ro1 Ro0     
    MOV [Rd], Ro    ;   0011    Rd1 Rd0     Ro1 Ro0     
    MOV Rd, [Ro]    ;   0100    Rd1 Rd0     Ro1 Ro0     
    JZ R            ;   0101    R1  R0                  


;   exemplo de codigo
    MOV R0, 1       ;   0001 0000 0000 0001
    MOV R1, 6       ;   0001 0100 0000 0101
    MOV R2, R1      ;   0000 1001
    ADD R2, R1      ;   0010 1001
    MOV [R2], R1    ;   0011 1001
    MOV R3, [R2]    ;   0100 1110
    JZ R2           ;   0101 1000
    MOV R1, 255     ;   0001 0100 1111 1111
    ADD R1, R0      ;   0010 0100
    JZ R1           ;   0101 0100


```

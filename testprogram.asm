; programa test

    mov R0, 1       ; Carrega o valor 1 no R0
    mov R1, 6       ; Carrega o valor 6 no R1
    mov R2, R1      ; Carrega o valor de R1 no R2
    add R2, R1      ; Carrega o valor de R1 + R2 no R2 (soma 0Ch)
    mov [R2], R1    ; Salva no rendereco R2 na RAM o valor de R1
    mov R3, [R2]    ; Carrega o valor no rendereco R2 no R3
    jz R2           ; Salta condicionalmente para o endereço em R2 (nesse caso nao salta)
    mov R1, 255     ; Carrega o valor ff no R1
    add R1, R0      ; Carrega o valor de R0 + R1 no R1 (soma 00h)
    jz R1           ; Salta condicionalmente para o endereço em R1 (nesse caso salta para 0)
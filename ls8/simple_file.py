4   # SAVE [subroutine1 address] in reg 0
6   # subroutine1 at address 6
0
9   # CALL reg 0 (subroutine1)
0
2   # HALT
# -------------------------------
# subroutine1 (address 6)
4   # SAVE [subroutine2 address] in reg 0
14  # subroutine2 at address 14
0
9   # CALL reg 0 (subroutine2)
0
1   # PRINT_BEEJ
1   # PRINT_BEEJ
10  # RET
# -------------------------------
# subroutine2 (address 14)
1   # PRINT_BEEJ
1   # PRINT_BEEJ
1   # PRINT_BEEJ
10  # RET
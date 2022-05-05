#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) == 4):
        if not sys.argv[2][0] in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if (sys.argv[2][0] == '+'):
                fun = add(a, b)
            elif (sys.argv[2][0] == '-'):
                fun = sub(a, b)
            elif (sys.argv[2][0] == '*'):
                fun = mul(a, b)
            elif (sys.argv[2][0] == '/'):
                fun = div(a, b)
            print(f"{a} {sys.argv[2]} {b} = {fun}")
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

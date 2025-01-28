def get_token(char):
    return int(char) if char.isdigit() else char

def main():
    qF = [2, 4] # Final states
    qE = "MEEEC! Incorrect sequence"
    q = 0
    abc = [0, 1]

    print("Type a binary number that starts and ends with different digits")
    token = input("Typescript > ")
    len_token = len(token)

    for i in range(len_token):
        digit = get_token(token[i]) # actual digit
        is_in_the_end = True if i+1 == len_token else False # detects end of input

        if digit not in abc: return qE
        match q:
            case 0: # state q1
                if digit == 0:
                    q = 1
                else:
                    q = 3
            case 1:
                if digit == 1:
                    q = 2
            case 2:
                if digit == 0:
                    q = 1
                else:
                    if is_in_the_end:
                        return qF[0]
            case 3:
                if digit == 0:
                    q = 4
            case 4:
                if digit == 1:
                    q = 3
                else:
                    if is_in_the_end:
                        return qF[1]

        if is_in_the_end:
            return q if q in qF else qE

while True:
    qR = main()
    if qR in (2, 4):
        print("Valid sequence!")
    else:
        print(qR)


def generate_instructions(s):
    letters = ""
    tune = ""
    turn = ""

    for ch in s:
        if ch == "+":
            tune = "tighten"
        elif ch == "-":
            tune = "loosen"
        if ch.isnumeric():
            turn += ch
        if ch.isupper():
            if tune != "":
                print(letters + " " + tune + " "+ turn)
                letters = ""
                tune = ""
                turn = ""
            letters += ch

    print(letters + " " + tune + " " + turn)


command = input("")
generate_instructions(command)
# generate_instructions("AFB+8HC-4")
# print("----")
# generate_instructions("AFB+8SC-4H-2GDPE+9")
# print("----")
# generate_instructions("A+8H-4")
# print("----")
# generate_instructions("AFB+88HC-444")


s = "ABCDE"
s.isalpha() # return true if all characters are alphebet letter a-z(A-Z)
s.isupper() # return true if all the characters are upper case, numbers, symbolts and spaces are not checked

s = "THIS IS 2"
print(s.isupper())

s = "123"
print(s.isdigit()) # return true is all the characters are digits

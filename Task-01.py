def encryption(statement, Shift):
    New_Statement = ""
    for i in statement:
        if i.isalpha():
            if i.isupper():
                New_Statement += chr(((ord(i) - 65 + Shift) % 26) + 65)
            else:
                New_Statement += chr(((ord(i) - 97 + Shift) % 26) + 97)
        else:
            New_Statement += i
    print("Encrypted statement is " + New_Statement)
    return New_Statement

def decryption(statement, Shift):
    New_Statement = ""
    for i in statement:
        if i.isalpha():
            if i.isupper():
                New_Statement += chr(((ord(i) - 65 - Shift + 26) % 26) + 65)
            else:
                New_Statement += chr(((ord(i) - 97 - Shift + 26) % 26) + 97)
        else:
            New_Statement += i
    print("Decrypted statement is " + New_Statement)
    return New_Statement

statement = input("Enter your statement: ")
Shift = int(input("Enter the Shift value: "))

encrypted_statement = encryption(statement, Shift)
decryption(encrypted_statement, Shift)

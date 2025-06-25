py_logic = {"Integer":"A whole number without a decimal point.",
            "String":"A sentence or a sequence of characters.",
            "Float":"A number with a decimal point.",
            "Boolean":"To indicate if a statement true or false.",
            "NoneType":"Used for debugging purpose, to check if there's value in variables."}

Program_loop = True

print("Welcome to a mini dictionary!\n")

py_logic.update({"List":"A list of items."})

keys = list(py_logic.keys())
print(f"1. {keys[0]}\n2. {keys[1]}\n3. {keys[2]}\n4. {keys[3]}\n5. {keys[4]}\n6. {keys[5]}\n7. All Types\n")

# print("1. Integer\n2. String\n3. Float\n4. Boolean\n5. NoneType\n6. All Types\n")

while Program_loop:
    num = input("Please input the number to choose!\n")
    
    if num == '1':
        print(py_logic["Integer"])
        Program_loop = False
    elif num == '2':
        print(py_logic["String"])
        Program_loop = False
    elif num == '3':
        print(py_logic["Float"])
        Program_loop = False
    elif num == '4':
        print(py_logic["Boolean"])
        Program_loop = False
    elif num == '5':
        print(py_logic["NoneType"])
        Program_loop = False
    elif num == '6':
        print(py_logic["List"])
        Program_loop = False
    elif num == '7':
        print(py_logic)
        Program_loop = False
    else:
        print("Invalid Input!")

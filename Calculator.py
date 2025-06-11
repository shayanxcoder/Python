# Build A calculator

# Select Operation
# Print Instruction
print("Select an operation:")
# User input1(thier Choice)
choice = int(input("Press 1 for Add, Press 2 for Sub, Press 3 for Multiply and Press 4 for Div"))
# User input(Number 1 and number 2)

no1 = int(input("Enter the Number one:"))
no2 = int(input("Enter the Number 2:"))
# to do that operation on the provided number
if choice == 1:
    print(no1 + no2)
if choice == 2:
    print(no1 - no2)
if choice == 3:
    print(no1 * no2)
if choice == 4:
    print(no1 / no2)

# If user input 1 then do addition

Legnth = int(input("Enter the Legnth:"))
Width = int(input("Enter the Width:"))
Height = int(input("Enter the Height"))
def surfvol(l,b,h):
    volume = l*b*h
    area1 = 2*l*b
    area2 = 2*b*h
    area3 = 2*h*l
    area = area1 + area2 + area3
    return print(area,volume)

surfvol(Legnth, Width, Height)


print ("Hello I am a calculator ")
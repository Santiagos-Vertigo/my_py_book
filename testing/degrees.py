temp = input("Input the temperature youd like to convert? (e.g., 45F, 102F etc.) :")

dregree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == 'C':
    result = int(round((9 * dregree) / 5 + 32))
    o_convention = "Farenheit"
elif i_convention.upper() == 'F':
    result = int(round((dregree - 32) * 5 / 9))
    o_convention = "Celcius"
else:
    print("Input proper convention")
    quit()

print("The temperature in", o_convention, "is", result, "degrees.")
from random import randrange
num = randrange(-1, 37)
status = []

if 1 > num > -2:
    if num == 0:
        print("""
The spin result in 0...
Pay 0
        """)
    if num == -1:
        print("""
The spin result in 00...
Pay 00
        """)
else:
    if 10 >= num > 0:
        if num % 2 != 0:
            status = ['Red', 'Odd', '1 to 18']
        else:
            status = ['Black', 'Even', '1 to 18']
    elif 19 > num >= 11:
        if num % 2 != 0:
            status = ['Black', 'Odd', '1 to 18']
        else:
            status = ['Red', 'Even', '1 to 18']
    elif 28 >= num >= 19:
        if num % 2 != 0:
            status = ['Red', 'Odd', '19 to 36']
        else:
            status = ['Black', 'Even', '19 to 36']
    elif 37 > num > 28:
        if num % 2 != 0:
            status = ['Black', 'Odd', '19 to 36']
        else:
            status = ['Red', 'Even', '19 to 36']
    print(f'''
The spin resulted in {num}...
Pay {num}
Pay {status[0]}
Pay {status[1]}
Pay {status[2]}
    ''')
# Connor Ren 2020

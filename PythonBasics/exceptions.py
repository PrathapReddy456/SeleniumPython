ItemsinCart=0

if ItemsinCart !=2:
    pass
    #raise Exception("Didn't match")

assert(ItemsinCart !=2)


#Try Except Mechanism

    #Method 1: with Customized exception message
try:
    with open("filelog.txt", 'r') as reader:
        reader.read()
except:
    print("Failed with Try")

    #Method2: with System exception message

try:
    with open("filelog.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

# Finally

try:
    with open("filelog.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("It execute any cost")
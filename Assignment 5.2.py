largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num 
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print ("Maximum is", largest) 
    print ("Minimum is", smallest)
done(int(largest),int(smallest))

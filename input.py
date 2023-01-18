name = int(input("put a integer number: "))
name2 = float(input("put a float number: "))
print ("Total : ", name + name2) #adding int and float together



a,b,c = input("put 3 numbers here (using commas in between numbers) : ").split(",") #getting 3 numbers at once(using commas in between numbers)
print("Number of students : ", a)
print("Number of male students : ", b)
print("Number of female students : ", c)


d,e,f = input("put 3 numbers here : ").split() #getting 3 numbers using format(using space in between numbers)
print("value of d {} and value of e {} and value of f {}".format(d,e,f))




g = list(map(int, input("Enter multiple numbers : ").split())) #makes a list of input numbers(using space in between)
print("Marks of students in class : ", g)

h = [int(h) for h in input("Enter multiple numbers : ").split()] # makes a list of input numbers(using loop)
print("Entered numbers : ", h )


i, j, k = [int(x) for x in input("Put 3 numbers (using commas in between numbers): ").split(",")] #taking 3 values separately(using commas in between numbers)
print("value of i : ", i)
print("value of j : ", j)
print("value of k : ", k)

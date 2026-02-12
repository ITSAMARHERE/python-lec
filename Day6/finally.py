def func1():
  try:
        l = [1, 4 , 6 , 8]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
  except:
        print("Please enter a valid index")
        return 0
  finally:
        print("I am alwasys executed")

x = func1()
print(x)
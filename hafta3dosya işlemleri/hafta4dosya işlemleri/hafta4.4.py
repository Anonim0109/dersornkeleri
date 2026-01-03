for a in range(1,11):
    if a < 3 : continue
    if a == 7 : break
    print("\nBasamak:",a)
    for b in range(1,11):
        print(a,"x", b, "=", a*b)
        #print(f"{a} x {b} = {a*b}")
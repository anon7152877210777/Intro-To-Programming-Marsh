cat = 3
questions = 3
a = ["","",""]
for i in range(cat):
    catagoryname = str(input("Enter a category: "))
    for j in range(questions):
        a[j] = str(input("Enter something in that category: "))
    print(str(catagoryname)+": " + a[0] + " " + a[1] + " " + a[2])

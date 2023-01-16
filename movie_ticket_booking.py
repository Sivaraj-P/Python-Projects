import random
row=["A","B","C","D","E","F","G","H","I","J","K","L"]
theatre=["AGS CINEMAS","CINEPOLIS","PVR CINEMAS","INOX","JAZZ","IMAX"]
movies=["varisu","thunivu","vikram","avatar 2","kgf 3","vaadivasal"]
shows=["11.00 AM","3.00 PM","6.00 PM","9.OO PM"]
selected_seat=[]
list=[]

# theatre hall setup rows, column ,no of seats, different prices of seat

def theatre_hall():
    for i in row:
        col=[]
        for j in range(14):
            a=random.randint(0,1)
            if a==0:
                col.append("x")
            else:
                col.append("_")
        list.append(col)
    for i in range(1,15):
        print(i,end=" ")
        if i==2:
            print(end="\t\t")
        if i==12:
            print(end="\t\t")
    a=0      
    for i in list:
        if i==list[0]:
            print("\n\t\t\t BUDGET 60RS\n")
        for j in range(len(i)):
        
            print(i[j],end=" ")
            if j==1:
                print(end="\t\t")
            if j==11:
                print(end="\t\t")
            if j==13:
                print("  ",row[a],"\n")
                a=a+1
        if i==list[1]:
            print("\t\t\t PREMIUM 120RS\n")
        if i==list[9]:
            print("\n")
            print("\t\t\t BOX 160RS\n")

# payment ->select the available seats, no of tickets , total price for the selected seats

def Payment():
    price=0
    n=int(input("enter the no of tickets:"))
    for i in range(n):
        r=input("select the row:")
        c=int(input("seletc the column:"))
        if r.upper() in row and (c>0 and c<=14):
            if list[row.index(r.upper())][c-1] == "x":
                print("seat already occupied")
            else:
                if row.index(r.upper())>=0 and row.index(r.upper())<2:
                    price=price+60
                if row.index(r.upper())>=2 and row.index(r.upper())<=9:
                    price=price+120
                if row.index(r.upper())>9 and row.index(r.upper())<12:
                    price=price+160
                selected_seat.append(r.upper()+str(c))
        else:
            print("invalid seat")
    print("YOUR SEATS:",end="")
    for i in selected_seat:
        print(i,end=" ")
    print("\ntotal price",price)

# -> select the city , theatre , movie
while True:
    print("1. CHENNAI\n2. BANGALORE \n3. MUMBAI\n4. KOLKATA\n5. Exit The Page")
    city=int(input("select the city:"))
    if city>0 and city<=4:
        for i in range(len(theatre)):
            print(i+1, theatre[i])
        t=int(input("select the theatre:"))
        if t>0 and t<=6:
            for i in range(len(movies)):
                print(i+1, movies[i])
            m=int(input("select the movie:"))
            if m>0 and m<=6:
                theatre_hall()
                Payment()
            else:
                print("!!!!!\tinvalid movie\t!!!!!")
        else:
            print("!!!!!\tinvalid theatre\t!!!!!")
    elif city==5:
        break
    else:
        print("!!!!!\tinvalid city\t!!!!!")


#thank you
#sivaraj-p

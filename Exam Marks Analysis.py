print("Exam Marks Analysis")

d = {}
sub = ["Maths", "English", "Physics", "Chemistry", "Computer Science"]

print("You can perform the following operations:", "1. Add new student", "2. Display all data", "3. Calculate the class average", "4. Display the highest scoring student", "5. Display the lowest scoring student", "6. Analyse a particular student\'s marks", "7. Analyse a particular subject\'s marks", "8. Exit program", sep = "\n")
print()


#Defining all the required functions
def add():
    roll = int(input("Enter roll no: "))
    name = str(input("Enter name: "))
    print("Enter marks obtained in the respective subjects -")
    mat = str(input("Maths: "))
    eng = str(input("English: "))
    phy = str(input("Physics: "))
    chem = str(input("Chemistry: "))
    cs = str(input("Computer Science: "))
    
    t = (mat, eng, phy, chem, cs)
    l = [name, t]

    d[roll] = l

def display():
    for i in d:
        print(i, ":", d[i][0], ":", d[i][1])

def total(r):
    m = d[r][1]

    total = 0
    for i in m:
        total += i

    return total

def stu_perc(r):
    print(total(r) / 5)

def sub_perc(s):
    net = 0

    for i in d:
        net += d[i][1][s]

    print(net)

def average():
    comb = 0

    for i in d:
        comb += total(i)

    print(comb / (500 * len(d)))

a = int(input("Enter operation no.: "))

while a != 8:
    #Analysing user input
    if a == 1:
        add()
        
        print("\n\n")
        print("Following is your new data -")
        display()

    if a == 2:
        if d != {}:
            display()

        else:
            print("Not sufficient data")

    if a == 3:
        average()

    if a == 4:
        base = 0

        for i in d:
            if stu_perc(i) > base:
                base = i

        print(i, ":", d[i][0], ":", d[i][1], ":", "Score =", stu_perc(i))

    if a == 5:
        base = 501

        for i in d:
            if stu_perc(i) < base:
                base = i

        print(i, ":", d[i][0], ":", d[i][1], ":", "Score =", stu_perc(i))
        
    if a == 6:
        g = int(input("Enter student roll no: "))
        
        print("You can perform the following operations:", "1. Display marks", "2. Calculate percentage", "3. Display highest-scoring subject", "4. Display lowest-scoring subject", sep = "\n")
        print()

        b = int(input("Enter operation no.: "))
        
        if b == 1:
            print(d[g][1])
            
        if b == 2:
            stu_perc(g)
            
        if b == 3:
            high_ind = 0
            high = 0
            
            for i in len(d[g][1]):
                if d[g][1][i] > high:
                    high_ind = i
                    high = d[g][1][i]
                    
            print(sub[high_ind], ":", high)
            
        if b == 4:
            low_ind = 0
            low = 101
            
            for i in len(d[g][1]):
                if d[g][1][i] < low:
                    low_ind = i
                    low = d[g][1][i]
                    
            print(sub[low_ind], ":", low)
            
    if a == 7:
        print("Which subject marks do you want to analyse?", "1. Maths", "2. English", "3. Physics", "4. Chemistry", "5. Computer Science", sep = "\n")
        
        h = int(input("Enter subject no.: "))
        
        print("You can perform the following operations:", "1. Display marks of all students", "2. Calculate average score in the subject", "3. Display highest scoring student", "4. Display lowest scoring student", sep = "\n")
        
        c = int(input("Enter operation no.: "))
        
        if c == 1:
            for i in d:
                print(d[i][0], ":", d[i][1][h - 1])
                
        if c == 2:
            sub_tot = 0
            
            for i in d:
                sub_tot += d[i][1][h - 1]
                
            print (sub_tot)
            
        if c == 3:
            high_ind = 0
            high = 0
            
            for i in len(d):
                if d[i][1][h - 1] > high:
                    high_ind = i
                    high = d[i][1][h - 1]
                    
            print(d[high_ind][0], ":", high)
            
        if c == 4:
            low_ind = 0
            low = 100
                
            for i in len(d):
                if d[i][1][h - 1] < low:
                    low_ind = i
                    low = d[i][1][h - 1]
                        
            print(d[low_ind][0], ":", low)

    print("\n\n")
    input("Press Enter to continue...\n")
    
    print("You can perform the following operations:", "1. Add new student", "2. Display all data", "3. Calculate the class average", "4. Display the highest scoring student", "5. Display the lowest scoring student", "6. Analyse a particular student\'s marks", "7. Analyse a particular subject\'s marks", "8. Exit program", sep = "\n")
    print()

    a = int(input("Enter operation no.: "))
        
    
    
        
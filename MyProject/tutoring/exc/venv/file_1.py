f = open('data.csv','r')

while 1:
    line = f.readline()

    data = line.split(',')

    inch = data[3]
    cm = float(inch) * 2.54
    data[3] = str(cm)
    new_line = ''.join(data)



    if not line: break
    print(new_line)




f.close()
"Name", "Team", "Position", "Height(inches)", "Weight(lbs)", "Age"
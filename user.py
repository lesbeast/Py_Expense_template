from PyInquirer import prompt
user_questions = [
      {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    infos = prompt(user_questions)
    f = open("users.csv", "a")
    f.write(infos['name'] + "\n")
    f.close()

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("User Added !")
    return True

def parseCSV():
    f = open("expense_report.csv", "r")
    Lines = f.readlines()
    comptes = []
    for line in Lines:
        i = 0
        sumString = ""

        while(line[i] != ","):
            sumString += line[i]
            i+=1
        i+=1
        sum = int(sumString)
        while(line[i] != ","):
            sumString += line[i]
            i+=1
        while(line[i] != ","):
            i+=1
        i+=1
        spender =""
        while(line[i] != ","):
            spender+=line[i]
            i+=1
        i+=1
        listParticipants = []
        while(line[i] != "\n"):
            participant = ""
            while(line[i] != "\n" and line[i] != "-"):
                participant+=line[i]
                i+=1
            if(participant != spender):
                listParticipants.append(participant)
            if(line[i] == "\n"):
                break
            i+=1
        for participant in listParticipants:
            comptes.append({"spender": spender, "participant": participant, "sum": sum/(len(listParticipants)+ 1)})
        f.close()
    return comptes

def getUsers():
    f2 = open("users.csv", "r")
    Lines2 = f2.readlines()
    f2.close()
    users = []
    for line2 in Lines2:
        users.append(line2[:len(line2)-1])
    return users


def getDebt():


    comptes = parseCSV()
    users = getUsers()
    listUsers = []
    
    for compte in comptes:
        print(compte["participant"] + " owes " + str(compte["sum"]) + " to " + compte["spender"])


   


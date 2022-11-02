from PyInquirer import prompt,Separator

def getSpender(r):
    f = open("users.csv", "r")
    Lines = f.readlines()
    options = []
    for line in Lines:
        name = str(line)
        options.append({"name": name[:len(name)-1]})
    f.close()
    return options
    
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        'type': 'list',
        'message': 'New Expense - Spender:',
        'name': 'spender',
        'choices': getSpender,
    },
     {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'New Expense - participants:',
        'name': 'participants',
        'choices': getSpender,
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    f = open("expense_report.csv", "a")
    res = infos['amount'] +"," + infos['label'] + "," + infos['spender']+","
    for name in infos['participants']:
        res = res + name + "-"
    if(not infos['spender'] in infos['participants']):
        res = res + infos['spender'] + "-"

    res = res[:len(res)-1]

    print(res)
    f.write(res + "\n")
    f.close()

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True
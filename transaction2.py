beneficiary_list = []
dic = {}

balance = 10000

def add_beneficiary(name, id):
    if name not in dic:
        dic[name] = id
        beneficiary_list.append({name:id})
        return True
    return False

    

def fund_transfer(name, amount):
    global balance
    if name in dic:
        if balance > amount:
            balance -= amount
            return "Transaction successful"
        else:
            return "Insufficient balance"
    else:
        return "Beneficiary not found"


def remove_beneficiary(name):
    if name in dic:
        dic.pop(name)
        global beneficiary_list
        beneficiary_list=[b for b in beneficiary_list if name not in b]
        return "Beneficiary removed successfully"
    else:
        return "Beneficiary not found"

def view_beneficiary_list():
    return beneficiary_list


if __name__ == "__main__":
    add_beneficiary("Ankitha", "001")
    add_beneficiary("Ancy", "002")
    add_beneficiary("Abhi", "003")
    print(view_beneficiary_list())
    print(fund_transfer("Ankitha",5000))
    print(remove_beneficiary("Ancy"))
    print(view_beneficiary_list())





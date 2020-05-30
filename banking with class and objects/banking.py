class Account:
    def __init__(self):
        self._signatures = ["phurba","sunil","nishan","sanjib","nischal"]
        self._pins = ["1234","1232","1243","5654","4948"]
        self._amounts = [100000,20000,25000,300000,100000]
    def check_pin(self,pin):
        if pin in self._pins:
            return self._pins.index(pin)
        else:
            return -1

    def check_sig(self,signature):
        if signature in self._signatures:
            return self._signatures.index(signature)
        else:
            return -1

    def show_details(self, acc):
        print(f"your acoount signature is {self._signatures[acc]}.")
        print(f'your current balance is {self._amounts[acc]}')

class Transaction(Account):
    """inheritence test"""
    def make_transaction(self, acc ,option,amount):
        if option == "1":
            self._amounts[acc] = self._amounts[acc] + amount
        elif option == "2":
            if amount > self._amounts[acc]:
                return -1
            self._amounts[acc] = self._amounts[acc] - amount
        else:
            print("Invalid selection.")


t= Transaction()
print(t._signatures)
while True:
    signature = input("Enter your signature: ")
    if signature.lower() == "exit":
        break
    if t.check_sig(signature) >=0:
        acc = t.check_sig(signature)
        pin = (input("Enter your pin: "))
        pin_index = t.check_pin(pin)
        if pin_index == acc:
            print("You are successfully loged in.")
            option = input("Do you want to 1) Deposite 2) Withdraw 3)show details (1/2/3): ")
            if option == "3":
                t.show_details(acc)
            else:
                amount = int(input("Enter the amount: "))
                t.make_transaction(acc,option,amount)
                t.show_details(acc)


        else:
            print("Pin did not match.")
    else:
        print("signature does not exist.")
    print("To close the program type: exit")

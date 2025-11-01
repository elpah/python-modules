class Employees:
    def __init__(self, firstname, lastname)->None:
        self.firstname = firstname
        self.lastname = lastname

class Supervisors(Employees):
    def __init__(self, firstname, lastname, password):
        super().__init__(firstname, lastname)
        self.password = password

class Chefs(Employees):
    def leave_request(self,days):
        return f"May i take a leave for {str(days)} days?"

adrian = Supervisors("Adrian", "A",  "apple")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.firstname)
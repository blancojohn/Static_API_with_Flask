
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self,last_name):
        self.last_name= last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
"""     def __repr__(self):
        return f"<Family structure of: family: {self.last_name}>"
 """    
class Member():
    def __init__(self, id, first_name, last_name, age, lucky_numbers):
        self.id= id
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.lucky_numbers= lucky_numbers

    def  serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers
        }

    def __repr__(self):
        return f"<Member: id: {self.id} first_name: {self.first_name} last_name: {self.last_name} age: {self.age} lucky_numbers: {self.lucky_numbers}>"

 
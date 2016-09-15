
class ContactList(list):
    def __init__(self, *args):
        super().__init__(self, *args)

    def search(self, name):
        matches = []
        for contact in self:
            if name in contact.name:
                matches.append(contact)
        return matches

    def longest_name(self):
        longest = ''
        for contact in self:
            if len(contact.name) > len(longest):
                longest = contact.name
        if longest == '':
            return None
        else:
            return longest

        #print(max([contact.name for contact in self], key=len))


class Contact():

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts.clear()


class Supplier(Contact):

    all_orders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def order(self, placed_order):
        if self.email in Supplier.all_orders.keys():
            Supplier.all_orders[self.email].append(placed_order)
        else:
            Supplier.all_orders[self.email] = [placed_order]



instance = Contact('belacska gabor', 'bela@gmail.com')
instance2 = Contact('kata', 'kata@gmail.com')
"""print(Contact.all_contacts)
Contact.reset_contacts()
print(Contact.all_contacts)
instance = Contact('bela', 'bela@gmail.com')
instance2 = Supplier('kata', 'kata@gmail.com')
print(Contact.all_contacts[1].name)
instance2.order('kutya')
instance2.order('macska')
print(Supplier.all_orders)"""

Contact.all_contacts.longest_name()

class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self._account_numbers = []

    def add_account_number(self, account_number):
        if account_number not in self._account_numbers:
            self._account_numbers.append(account_number)

    def remove_account_number(self, account_number):
        if account_number in self._account_numbers:
            self._account_numbers.remove(account_number)

    @property
    def account_numbers(self):  # ✅ Added this property
        return self._account_numbers

    def display_details(self):
        print(f"Customer ID = {self.customer_id} "
              f"Name = {self.name} "
              f"Address = {self.address} "
              f"Number of Accounts: {len(self._account_numbers)}")

    def dict_details(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "address": self.address,
            "account_numbers": self._account_numbers
        }

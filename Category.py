class Category:

    # Placed this in here to see if the missing class variables cause the program to crash, they don't.
    # category1 = ""
    # category1_amount = 0
    # category2 = ""
    # category2_amount = 0
    # category3 = ""
    # category3_amount = 0
    # category4 = ""
    # category4_amount = 0
    # all_categories = {category1:category1_amount, category2:category2_amount, category3:category3_amount,
    #                  category4:category4_amount}

    # Constructor
    def __init__(self, category1="Food", category2="Car Expenses", category3="Clothing", category4="Entertainment",
                 category1_amount=300, category2_amount=400, category3_amount=300, category4_amount=300):
        self.category1 = category1
        self.category1_amount = category1_amount
        self.category2 = category2
        self.category2_amount = category2_amount
        self.category3 = category3
        self.category3_amount = category3_amount
        self.category4 = category4
        self.category4_amount = category4_amount

        self.all_categories = {category1:category1_amount, category2:category2_amount, category3:category3_amount,
                          category4:category4_amount}

    #Methods
    def deposit(self, category, amount):
        if category in self.all_categories:
            self.all_categories[category] += amount
            print(category + " balance was " + str(self.all_categories[category]-amount) + " and is now " + str(self.all_categories[category]))
        else:
            print("Category not found, please specify one of the following categories:")
            for key, value in self.all_categories:
                print(key, end=" ")


    def check_balance(self):
        #purpose of printing the dictionary's contents is to see how it changes with each function.
        print(self.all_categories)
        total = 0
        for values in self.all_categories:
            total += self.all_categories[values]
        print("Total budget balance is " + str(total))


    def withdraw(self, category, amount):
        if category in self.all_categories:
            self.all_categories[category] -= amount
            print(category + " balance was " + str(self.all_categories[category]+amount) + " and is now " + str(self.all_categories[category]))
        else:
            print(category + " not found, please specify one of the following categories:")
            for key in self.all_categories:
                print(key, end=" ")

    def transfer(self, cat_to_transfer_from, cat_to_transfer_to, amount):
        if (cat_to_transfer_to in self.all_categories) & (cat_to_transfer_from in self.all_categories):
            self.all_categories[cat_to_transfer_from] -= amount
            self.all_categories[cat_to_transfer_to] += amount
            print("Taking " + str(amount) + " from " + cat_to_transfer_from + " and adding to " + cat_to_transfer_to)
        else:
            print("Categories not found, please try again")

test = Category()
test.check_balance()
test.withdraw("Food", 100)
test.deposit("Food", 200)
test.check_balance()
test.transfer("Food", "Entertainment", 100)
test.check_balance()

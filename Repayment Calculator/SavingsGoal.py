import datetime


class SavingsGoal(object):

    def __init__(self, name, amount):
        self.SavingsName = name
        self.TotalPaymentAmount = amount
        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17
        validStartDate = False
        self.userStartDate = None

    def setTotalAmount(self, newAmount):
        self.TotalPaymentAmount = newAmount

    def setStartDate(self):
        monthsWithout31 = [2, 4, 6, 9, 11]
        userYear = None
        userMonth = None
        userDay = None

        # * Take the user's year, it can't be less than the current year
        user_input = input("What is the Year of the start date?\n")
        try:
            val = int(user_input)
            if len(user_input) != 4 or val < datetime.datetime.now().year:
                raise ValueError
            else:
                userYear = val
                print("User Year Captured (NOT Saved!)\n")
        except ValueError as error:
            print('Your value is not an acceptable year\nNo values were saved.')
            return 1

        # * Month
        user_input = input("What is the Month of the start date?\n")
        try:
            val = int(user_input)
            if val < 1 or val > 12:
                raise ValueError

            if (userYear == datetime.datetime.now().year and val <= datetime.datetime.now().month):
                raise ValueError
            else:
                userMonth = val
                print("User Month Captured (NOT Saved Yet!)\n")
        except ValueError as error:
            print('Your value is not an acceptable month')
            return 2

        # * Day
        user_input = input("What is the Day of the start date?\n")
        try:
            val = int(user_input)
            if val < 1 or val > 31:
                raise ValueError

            if val == 31 and userMonth in monthsWithout31:
                raise ValueError
            else:
                userDay = val
                print("User Day Captured (Saving Soon)\n")
        except ValueError as error:
            print('Your value is not an acceptable month\day combination')
            return 3

        self.userStartDate = datetime.datetime(userYear, userMonth, userDay)
        validStartDate = True
        print("User Start Date Saved!")
        return 0

    def getAmount(self):
        print(self.TotalPaymentAmount)
        return self.TotalPaymentAmount

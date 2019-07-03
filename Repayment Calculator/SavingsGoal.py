import datetime
import calendar


class SavingsGoal(object):

    def __init__(self, name, amount):
        self.SavingsName = name
        self.TotalPaymentAmount = amount
        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17
        self.Phase1_Payments = [0, 0, 0, 0, 0]
        self.Phase2_Payments = [0, 0, 0, 0, 0]
        self.Phase3_Payments = [0, 0, 0, 0, 0]
        self.Phase_Dates = [[],[],[]]
        self.validStartDate = False
        self.userStartDate = None
        self.ranStartOnce = False
        self.longTermGoal = False

    def start(self):
        Pass1 = True
        Pass2 = True
        user_input = ''
        downPaymentAmt = 0

        if self.validStartDate == False:
            print("validStartDate is False. Run (object).setStartDate")
            return 1
        else:
            print("----------------------------------------\nStart of start()")

        while Pass1:
            user_input = (
                input("\nWould you like to plan a down payment (y/N): "))

            if user_input != 'y' and user_input != 'N':
                print("Invalid Input\n")

            if user_input == 'y' or user_input == 'N':
                Pass1 = False
                if user_input == 'y':
                    self.DivyAllPhases()

                    for payment in self.Phase1_Payments[0:3]:
                        downPaymentAmt += payment

                    print("The downpayment amt is: " + str(downPaymentAmt) +
                          "\t(Due on: " + str(self.userStartDate.strftime("%x")) + str(")\n\n"))

                if user_input == 'N':
                    self.DivyAllPhases()
                    print("Alrighty, Moving on!\n\n")

        while Pass2:
            user_input = (
                input("Is this a long-term goal? 3+ Years to Complete? (y/N): "))

            if user_input != 'y' and user_input != 'N':
                print("Invalid Input\n")

            if user_input == 'y' or user_input == 'N':
                Pass2 = False
                if user_input == 'N':
                    print(
                        "I will create a 3-month, 6-month, 12-month, and 24-month plans!\n\n")

                if user_input == 'y':
                    self.longTermGoal = True
                    print("I will create a 3-year, 5-year, and 10-year plan\n\n")

            if self.longTermGoal == False:
                print("The User Start Date is: " +
                      str((self.userStartDate.strftime("%x"))) + "\n")
                self.breakdown(3)
                self.breakdown(6)
                self.breakdown(12)
                self.breakdown(24)
            else:
                pass

        print("\nEnd of start()\n----------------------------------------")
        self.ranStartOnce = True

    def breakdown(self, monthsToAdd):
        planEndDate = self.add_months(self.userStartDate, monthsToAdd)

        diff = planEndDate - self.userStartDate

        print("The {}-Month End Date is: ".format(monthsToAdd) +
              str(planEndDate.strftime("%x")) + " ({} days)".format(diff.days))

        totalDays = round(float(diff.days))
        daysPerPhase_Interval = round(float(totalDays/3))
        daysBetweenPayments_Interval = round(float(totalDays/15))

        print("\n\tPhases")
        print("\n\n\tPhase 1\tPhase 2\tPhase 3")

        self.addPhase1Dates(daysPerPhase_Interval)

        
        # ! YOU LEFT OFF HERE

    def addPhase1Dates(self, daysPerPhaseInterval):
        start = self.userStartDate
        end = start + datetime.timedelta(daysPerPhaseInterval)
        diff = end - start
        daysTillNextPayment = diff.days/5

        nextPaymentDate = start
        for paymentDueDate in range(0, 5):
            nextPaymentDate += datetime.timedelta(daysTillNextPayment)
            print("\t" + str(nextPaymentDate))

        # ! YOU LEFT OFF HERE
        return 0


    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def setStartDate(self):
        monthsWithout31 = [2, 4, 6, 9, 11]
        userYear = None
        userMonth = None
        userDay = None

        print(
            "\n----------------------------------------\nStart of setStartDate()\n\n")

        # * Take the user's year, it can't be less than the current year
        user_input = input("What is the Year of the start date?\n")
        try:
            val = int(user_input)
            if len(user_input) != 4 or val < datetime.datetime.now().year:
                raise ValueError
            else:
                userYear = val
                print("User Year Captured (NOT Saved!)\n")
        except (UnboundLocalError, ValueError) as error:
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
        except (UnboundLocalError, ValueError) as error:
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
        except (UnboundLocalError, ValueError) as error:
            print('Your value is not an acceptable month \ day combination')
            return 3

        self.userStartDate = datetime.date(userYear, userMonth, userDay)
        self.validStartDate = True
        print("User Start Date Saved!")
        print(
            "\nEnd of setStartDate() - SUCCESS\n----------------------------------------")

        return 0

    def DivyPhase1Amount(self):
        self.Phase1_Payments[0] = float(self.Phase1Tot_TotalPaymentAmount)*.2
        self.Phase1_Payments[1] = float(self.Phase1Tot_TotalPaymentAmount)*.2
        self.Phase1_Payments[2] = float(self.Phase1Tot_TotalPaymentAmount)*.2
        self.Phase1_Payments[3] = float(self.Phase1Tot_TotalPaymentAmount)*.15
        self.Phase1_Payments[4] = float(self.Phase1Tot_TotalPaymentAmount)*.25

    def DivyPhase2Amount(self):
        self.Phase2_Payments[0] = float(self.Phase2Tot_TotalPaymentAmount)*.10
        self.Phase2_Payments[1] = float(self.Phase2Tot_TotalPaymentAmount)*.15
        self.Phase2_Payments[2] = float(self.Phase2Tot_TotalPaymentAmount)*.25
        self.Phase2_Payments[3] = float(self.Phase2Tot_TotalPaymentAmount)*.30
        self.Phase2_Payments[4] = float(self.Phase2Tot_TotalPaymentAmount)*.20

    def DivyPhase3Amount(self):
        self.Phase3_Payments[0] = float(self.Phase3Tot_TotalPaymentAmount)*.30
        self.Phase3_Payments[1] = float(self.Phase3Tot_TotalPaymentAmount)*.25
        self.Phase3_Payments[2] = float(self.Phase3Tot_TotalPaymentAmount)*.20
        self.Phase3_Payments[3] = float(self.Phase3Tot_TotalPaymentAmount)*.15
        self.Phase3_Payments[4] = float(self.Phase3Tot_TotalPaymentAmount)*.10

    def DivyAllPhases(self):
        self.DivyPhase1Amount()
        self.DivyPhase2Amount()
        self.DivyPhase3Amount()

    def setTotalAmount(self, newAmount):
        print(
            "\n----------------------------------------\nStart of setTotalAmount()")

        if self.ranStartOnce == True:
            print("----------------------------------------\nstart() was ran at least once before after this, it will be rerun after this to account for the adjusted Total amount")

        self.TotalPaymentAmount = newAmount
        self.reCalibrateAmounts()
        self.DivyAllPhases()

        print(
            "\nEnd of setTotalAmount() - SUCCESS - New Amount: " + str(self.TotalPaymentAmount) + "\n----------------------------------------")

        if self.ranStartOnce == True:
            print("Rerunning start() for you")
            self.start()

    def reCalibrateAmounts(self):
        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

    def getAmount(self):
        return self.TotalPaymentAmount

import datetime
import calendar
from decimal import *

class SavingsGoal(object):

    def __init__(self, name, amount):
        getcontext().prec=2
        self.SavingsName = name
        self.TotalPaymentAmount = Decimal(amount)
        self.userStartDate = None
        self.Phase1Tot_TotalPaymentAmount = None  # self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = None  # self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = None  # self.TotalPaymentAmount*.17
        self.Phase1_Payments = [0, 0, 0, 0, 0]
        self.Phase2_Payments = [0, 0, 0, 0, 0]
        self.Phase3_Payments = [0, 0, 0, 0, 0]
        self.Phase_Dates = [[], [], []]
        self.userStartDate = None
        self.ranStartOnce = False
        self.longTermGoal = False

    def start(self):
        validStartDate = False
        user_input = ''
        downPaymentAmt = 0


        if self.ranStartOnce == False:
            if not(validStartDate):
                self.setStartDate()
                self.DivyAllPhases()
            else:
                print("----------------------------------------\nStart of start()")

            while True:
                user_input = (
                    input("\nWould you like to plan a down payment (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")

                if user_input == 'y':
                    for payment in self.Phase1_Payments[0:3]:
                        downPaymentAmt += payment
                    print(f'The downpayment amt is: {downPaymentAmt}\t(Due on: {self.userStartDate.strftime("%x")}\n\n')
                    break
                elif user_input == 'N':
                    print("Alrighty, Moving on!\n")
                    break;

            while True:
                user_input = (
                    input("Is this a long-term goal? 3+ Years to Complete? (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")

                if user_input == 'N':
                    print(
                        "I will create a 3-month, 6-month, 12-month, and 24-month plans!\n\n")
                elif user_input == 'y':
                    self.longTermGoal = True
                    print("I will create a 3-year, 5-year, and 10-year plan\n\n")

                # * This is assuming that the goal is short term. User answers was N
                if self.longTermGoal == False:
                    print("The User Start Date is: " +
                          str((self.userStartDate.strftime("%x"))) + "\n")

                    self.breakdown(3)
                    self.breakdown(6)
                    self.breakdown(12)
                    self.breakdown(24)
                    break;
                elif self.longTermGoal == True:
                    break;

           
        self.ranStartOnce = True
        print("\nEnd of start()\n----------------------------------------")

        return 0

    def breakdown(self, monthsToAdd):
        planEndDate = self.add_months(self.userStartDate, monthsToAdd)

        diff = planEndDate - self.userStartDate

        print("The {}-Month End Date is: ".format(monthsToAdd) +
              str(planEndDate.strftime("%x")) + " ({} days)\n".format(diff.days))

        totalDays = round(float(diff.days))
        daysPerPhase_Interval = round(float(totalDays/3))
        daysBetweenPayments_Interval = round(float(totalDays/15))

        print("Format: Phase 1 Dates\t-\tPhase 2 Dates\t-\tPhase 3 Dates")

        self.phaseDatesPreview(daysPerPhase_Interval)

    def phaseDatesPreview(self, daysPerPhaseInterval):
        paymentPlanPreviewArray = []

        start = self.userStartDate
        end = start + datetime.timedelta(daysPerPhaseInterval)
        diff = end - start
        daysTillNextPayment = diff.days/5

        nextPaymentDate = start
        for paymentDueDate in range(0, 15):
            nextPaymentDate += datetime.timedelta(daysTillNextPayment)
            paymentPlanPreviewArray.append(nextPaymentDate)

        for element in range(0,5):
            element2 = element+5
            element3 = element+10
            print(f"\t{paymentPlanPreviewArray[element]} (${self.Phase1_Payments[element]})\t|\t{paymentPlanPreviewArray[element2]} (${self.Phase2_Payments[element]})\t|\t{paymentPlanPreviewArray[element3]} (${self.Phase3_Payments[element]})")

        print("")
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
        getcontext().prec=2
        self.Phase1_Payments[0] = (self.Phase1Tot_TotalPaymentAmount)*Decimal(.20)
        self.Phase1_Payments[1] = (self.Phase1Tot_TotalPaymentAmount)*Decimal(.20)
        self.Phase1_Payments[2] = (self.Phase1Tot_TotalPaymentAmount)*Decimal(.20)
        self.Phase1_Payments[3] = (self.Phase1Tot_TotalPaymentAmount)*Decimal(.15)
        self.Phase1_Payments[4] = (self.Phase1Tot_TotalPaymentAmount)*Decimal(.25)

    def DivyPhase2Amount(self):
        getcontext().prec=2
        self.Phase2_Payments[0] = (self.Phase2Tot_TotalPaymentAmount)*Decimal(.10)
        self.Phase2_Payments[1] = (self.Phase2Tot_TotalPaymentAmount)*Decimal(.15)
        self.Phase2_Payments[2] = (self.Phase2Tot_TotalPaymentAmount)*Decimal(.25)
        self.Phase2_Payments[3] = (self.Phase2Tot_TotalPaymentAmount)*Decimal(.30)
        self.Phase2_Payments[4] = (self.Phase2Tot_TotalPaymentAmount)*Decimal(.20)

    def DivyPhase3Amount(self):
        getcontext().prec=2
        self.Phase3_Payments[0] = (self.Phase3Tot_TotalPaymentAmount)*Decimal(.30)
        self.Phase3_Payments[1] = (self.Phase3Tot_TotalPaymentAmount)*Decimal(.25)
        self.Phase3_Payments[2] = (self.Phase3Tot_TotalPaymentAmount)*Decimal(.20)
        self.Phase3_Payments[3] = (self.Phase3Tot_TotalPaymentAmount)*Decimal(.15)
        self.Phase3_Payments[4] = (self.Phase3Tot_TotalPaymentAmount)*Decimal(.10)

    def DivyAllPhases(self):
        if self.Phase1Tot_TotalPaymentAmount == None:
            self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*Decimal(.33)
            self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*Decimal(.50)
            self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*Decimal(.17)

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

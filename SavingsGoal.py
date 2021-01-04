import datetime
import calendar
from decimal import Decimal
import itertools



"""
Instead of choices_A, B, C, D, being 'None',
init a payment plan class (struct) that holds [int] years, [int total payments]. [2 dim. array ]
"""

class PaymentPlant(object): 
    def __init__(self,years,totalPayments): 
        self.years = []
        self.totalPayments = []


class Observer(object): 
    def __init__(self,SavingsGoal): 
        self.years = []
        self.totalPayments = []



class SavingsGoal(object):

    def __init__(self, name, amount):
        """
        Initilization Method - asks user for name and amount, then init-s the other data structures need by the object, all initialized to {None} or {0}
        
        Arguments:
            name {string} -- The name of the SavingsGoal, initialized with the object
            amount {int} -- The total amount of money to be saved up
        """
        self.SavingsName = name
        self.TotalPaymentAmount = amount
        self.DownPaymentAmount = None
        self.userStartDate = None
        self.paymentPlan = [[None, None, None, None, None],
                            [None, None, None, None, None],
                            [None, None, None, None, None]]

        self.Phase1Tot_TotalPaymentAmount = None 
        self.Phase2Tot_TotalPaymentAmount = None  
        self.Phase3Tot_TotalPaymentAmount = None  
        self.Phase_Payments =  [[0,0,0,0,0], 
                                [0,0,0,0,0], 
                                [0,0,0,0,0]]

        self.Phase_Dates = [[0,0,0,0,0], 
                            [0,0,0,0,0], 
                            [0,0,0,0,0]]
        self.userStartDate = None
        self.ranStartOnce = False
        self.longTermGoal = False

        self.plan_choice = 'A'
        self.plan = []
        self.long_term_breakdown = {'A':36,'B':60,'C':120} 
        self.short_term_breakdown = {'A':3,'B':6,'C':12,'D':24} 

    def start(self):
        validStartDate = False
        user_input = ''
        downPaymentAmt = 0
        choice_A = None
        choice_B = None
        choice_C = None
        choice_D = None
        user_choice_letter = None


        if self.ranStartOnce == False:
            if not(validStartDate):
                return_val = self.setStartDate()
                while return_val != 0:
                    return_val = self.setStartDate()
                self.divyAllPhases()
            else:
                print("----------------------------------------\nStart of start()")

            while True:
                user_input = (
                    input("\nWould you like to plan a down payment (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")

                if user_input == 'y':
                    for amount in range(0,3):
                        downPaymentAmt += self.Phase_Payments[0][amount]
                    self.DownPaymentAmount = downPaymentAmt
                    print(f'The down payment amt is: ${downPaymentAmt}\t(Due on: {self.userStartDate.strftime("%x")})\n\n')
                    break
                elif user_input == 'N':
                    print("Alrighty, Moving on!\n")
                    break

            while True:
                pass_loop = False

                user_input = (
                    input("Is this a long-term goal? 3+ Years to Complete? (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")
                    continue
                elif user_input == 'y' or user_input == 'N':
                    pass_loop = True
                
                if pass_loop == False:
                    continue


                if user_input == 'N':
                    print(
                        "I will create a (A) 3-month, (B) 6-month, (C) 12-month, and (D) 24-month plans!\n\n")
                elif user_input == 'y':
                    self.longTermGoal = True
                    print("I will create a (A) 3-year, (B) 5-year, and (C) 10-year plan\n\n")

                # * This is assuming that the goal is short term. User answers was N
                if self.longTermGoal == False:
                    print("The User Start Date is: " +
                        str((self.userStartDate.strftime("%x"))))
                    print(f"The User Goal Amount is: ${self.TotalPaymentAmount}\n")

                    while True:
                        user_choice_letter = input("Which plan would you like? (A) : 3 mo, (B) : 6 mo, (C) : 12 mo, (D) : 24 mo\n")

                        if user_choice_letter != 'A' and user_choice_letter != 'B' and user_choice_letter != 'C' and user_choice_letter != 'D':
                            print("Invalid Input\n")
                            continue
                        else:
                            print(f"Thank you! You've selected {user_choice_letter}")
                            break;

                    self.payment_plan_choice(user_choice_letter)
                    self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
                    break
                elif self.longTermGoal == True:
                    print("The User Start Date is: " + str((self.userStartDate.strftime("%x"))))
                    print(f"The User Goal Amount is: ${self.TotalPaymentAmount}\n")

                    while True:
                        user_choice_letter = input("Which plan would you like? (A) : 3 year, (B) : 5 year, (C) : 10 year\n")

                        if user_choice_letter != 'A' and user_choice_letter != 'B' and user_choice_letter != 'C':
                            print("Invalid Input\n")
                            continue
                        else:
                            print(f"Thank you! You've selected {user_choice_letter}")
                            break;

                    self.payment_plan_choice(user_choice_letter)
                    self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
                    break
        else:
            self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
            

        self.ranStartOnce = True
        print("\nEnd of start()\n----------------------------------------")
        return 0


    def construct_payment_plan(self, Phase_Dates, Phase_Payments):

        print("Constructing payment plan...")
        for i, element in itertools.product(range(0,3),range(0,5)): 
            self.paymentPlan[i][element] = (self.Phase_Dates[i][element], Phase_Payments[i][element])
        print("Payment plan construction finished! \n")

        
        return 0


    def payment_plan_choice(self,user_choice_letter):


        plan_options = {}
        
        if self.longTermGoal == True: 
            plan_options = self.long_term_breakdown
        else: 
            plan_options = self.short_term_breakdown

        phase_ranges = [0,5,10,15]

        self.plan = self.breakdown(plan_options[user_choice_letter])
        
        i = 0; 
        while i < 3: 
        
            for element in range(phase_ranges[i],phase_ranges[i+1]): 
                temp = self.plan[element]
                self.Phase_Dates[i][element - phase_ranges[i]] = temp 
            i += 1;
        
        self.plan_choice = user_choice_letter        
        
        return 0



    def breakdown(self, monthsToAdd):

        planEndDate = self.add_months(self.userStartDate, monthsToAdd)
        diff = planEndDate - self.userStartDate
        return_array = []

        if monthsToAdd > 30:
            monthsToAdd = int(monthsToAdd/12)
            print("The {}-Year End Date is: ".format(monthsToAdd) +
                str(planEndDate.strftime("%x")) + " ({} months)\n".format(int(diff.days/30)))
        else:
            print("The {}-Month End Date is: ".format(monthsToAdd) +
                str(planEndDate.strftime("%x")) + " ({} days)\n".format(int(diff.days)))

        totalDays = round(float(diff.days))
        daysPerPhase_Interval = round(float(totalDays/3))
        daysBetweenPayments_Interval = round(float(totalDays/15))

        print("Format: Phase 1 Dates\t\t-\t\tPhase 2 Dates\t\t-\tPhase 3 Dates")

        return_array = self.phaseDatesPreview(totalDays)
        return return_array



    def phaseDatesPreview(self, totalDays):
        paymentPlanPreviewArray = []

        start = self.userStartDate
        end = start + datetime.timedelta(totalDays)
        diff = end - start
        daysTillNextPayment = diff.days/15

        nextPaymentDate = start
        for paymentDueDate in range(0, 15):
            nextPaymentDate += datetime.timedelta(daysTillNextPayment)
            paymentPlanPreviewArray.append(nextPaymentDate)

        for element in range(0,5):
            print(f"\t{paymentPlanPreviewArray[element]} (${self.Phase_Payments[0][element]})\t\t|\t{paymentPlanPreviewArray[element+5]} (${self.Phase_Payments[1][element]})\t|\t{paymentPlanPreviewArray[element+10]} (${self.Phase_Payments[2][element]})")
            

        print("")
        return paymentPlanPreviewArray

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
        userYear = user_input
        
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

    def divyPhase1Amount(self):
        for element in range(0,5):
            if element != 3 and element != 4:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
            elif element == 3:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            else:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
        return

    def divyPhase2Amount(self):
        for element in range(0,5):
            if element == 0:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.10)
            elif element == 1:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            elif element == 2:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
            elif element == 3:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.30)
            elif element == 4:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
        return

    def divyPhase3Amount(self):

        for element in range(0,5):
            if element == 0:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.30)
            elif element == 1:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
            elif element == 2:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
            elif element == 3:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            elif element == 4:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.10)
        return

    def divyAllPhases(self):
        if self.Phase1Tot_TotalPaymentAmount == None:
            self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
            self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
            self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        self.divyPhase1Amount()
        self.divyPhase2Amount()
        self.divyPhase3Amount()
        return

    def setNewTotalAmount(self, newAmount):
        print(
            "\n----------------------------------------\nStart of setTotalAmount()")

        self.TotalPaymentAmount = newAmount
        self.reCalibrateAmounts()

        print(
            "\nEnd of setTotalAmount() - SUCCESS - New Amount: " + str(self.TotalPaymentAmount) + "\n----------------------------------------")
        return

    def reCalibrateAmounts(self):
        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        self.divyAllPhases()
        self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
        return

    def getAmount(self):
        return self.TotalPaymentAmount

    def getName(self):
        return self.SavingsName

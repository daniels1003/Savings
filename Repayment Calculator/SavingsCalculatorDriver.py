import datetime


class SavingsGoal:

    def __init__(self):
        SavingsName = "Tesla"
        TotalPaymentAmount = 0
        Phase1Tot_TotalPaymentAmount = 0
        Phase2Tot_TotalPaymentAmount = 0
        Phase3Tot_TotalPaymentAmount = 0

    def run(self):

        Phase1_Payments = []
        Phase2_Payments = []
        Phase3_Payments = []

        self.TotalPaymentAmount = 500.00
        # try:
        #     self.TotalPaymentAmount = float(self.TotalPaymentAmount)
        #     print("Input number value is: ", self.TotalPaymentAmount)
        # except ValueError:
        #     print("That's not an int!")
        #     print("No.. input string is not an Integer. It's a string")

        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        Phase1_Payments.append(float(self.Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(self.Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(self.Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(self.Phase1Tot_TotalPaymentAmount)*.15)
        Phase1_Payments.append(float(self.Phase1Tot_TotalPaymentAmount)*.25)

        Phase2_Payments.append(float(self.Phase2Tot_TotalPaymentAmount)*.10)
        Phase2_Payments.append(float(self.Phase2Tot_TotalPaymentAmount)*.15)
        Phase2_Payments.append(float(self.Phase2Tot_TotalPaymentAmount)*.25)
        Phase2_Payments.append(float(self.Phase2Tot_TotalPaymentAmount)*.30)
        Phase2_Payments.append(float(self.Phase2Tot_TotalPaymentAmount)*.20)

        Phase3_Payments.append(float(self.Phase3Tot_TotalPaymentAmount)*.30)
        Phase3_Payments.append(float(self.Phase3Tot_TotalPaymentAmount)*.25)
        Phase3_Payments.append(float(self.Phase3Tot_TotalPaymentAmount)*.20)
        Phase3_Payments.append(float(self.Phase3Tot_TotalPaymentAmount)*.15)
        Phase3_Payments.append(float(self.Phase3Tot_TotalPaymentAmount)*.10)

        # sum_payments = 0

        # for payment in Phase1_Payments[0:3]:
        #     sum_payments += payment
        #     print(sum_payments)

        #  TODO: Take the Start and End Date from the user and divide the days between the two dates into 3 phase increments with 15 payments. So divide the total amount of days by 3, and divide the total amount of days by 15

        # August 25, 2018 - Start Date of Loan Repayment

        date_now = datetime.datetime.now()
        mininmumStart_date = date_now + datetime.timedelta(days=92)
        print("Now:" + str(date_now))
        print("Minimum: " + str(mininmumStart_date))

        userYear_date = 0
        userMonth_date = 0
        userDay_date = 0

    #    try:
    #         userYear_date = int(input("Enter Year: "))
    #     except (UnboundLocalError, ValueError) as e:
    #         print("Invalid Input, Error: %s" % e)

    #     try:
    #         userMonth_date = int(input("Enter Month: "))
    #     except (UnboundLocalError, ValueError) as e:
    #         print("Invalid Input, Error: %s" % e)

    #     try:
    #         userDay_date = int(input("Enter Day: "))
    #     except (UnboundLocalError, ValueError) as e:
    #         print("Invalid Input, Error: %s" % e)

        # Testing Purposes
        userStart_date = datetime.datetime(
            2019, 8, 25)

        if mininmumStart_date < date_now:  # less than means "in the past", this asks, does the minimum start date come before the NOW date? result: false
            print("True")
        else:
            print("False")

        # diff = userStart_date - date_now
        # if diff.days < 91:
        #     print(
        #         "You must select a date more than 3 Months (91 days) Away\nYours is: %s" % diff.days)

        # diff = start_date - datetime.datetime.now()
        # print(
        #     "There are %s total days between now and when you plan to begin" % diff.days)
        # print(str(diff.days/3) + " days per phase")


Tesla = SavingsGoal()
Tesla.run()

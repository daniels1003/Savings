class SavingsGoal:

    def __init__(self):
        SavingsName = "Tesla"
        TotalPaymentAmount = 50000
        Phase1_TotPaymentAmount = 0
        Phase2_TotPaymentAmount = 0
        Phase3_TotPaymentAmount = 0

    def run(self):

        Phase1_Payments = []
        Phase2_Payments = []
        Phase3_Payments = []

        self.TotalPaymentAmount = input("Amt: ")
        try:
            self.TotalPaymentAmount = float(self.TotalPaymentAmount)
            print("Input number value is: ", self.TotalPaymentAmount)
        except ValueError:
            print("That's not an int!")
            print("No.. input string is not an Integer. It's a string")

        Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        Phase1_Payments.append(float(Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(Phase1Tot_TotalPaymentAmount)*.2)
        Phase1_Payments.append(float(Phase1Tot_TotalPaymentAmount)*.15)
        Phase1_Payments.append(float(Phase1Tot_TotalPaymentAmount)*.25)

        Phase2_Payments.append(float(Phase2Tot_TotalPaymentAmount)*.10)
        Phase2_Payments.append(float(Phase2Tot_TotalPaymentAmount)*.15)
        Phase2_Payments.append(float(Phase2Tot_TotalPaymentAmount)*.25)
        Phase2_Payments.append(float(Phase2Tot_TotalPaymentAmount)*.30)
        Phase2_Payments.append(float(Phase2Tot_TotalPaymentAmount)*.20)

        Phase3_Payments.append(float(Phase3Tot_TotalPaymentAmount)*.30)
        Phase3_Payments.append(float(Phase3Tot_TotalPaymentAmount)*.25)
        Phase3_Payments.append(float(Phase3Tot_TotalPaymentAmount)*.20)
        Phase3_Payments.append(float(Phase3Tot_TotalPaymentAmount)*.15)
        Phase3_Payments.append(float(Phase3Tot_TotalPaymentAmount)*.10)

        sum_payments = 0

        for payment in Phase1_Payments[0:3]:
            sum_payments += payment
            print(sum_payments)

        #  TODO: Take the Start and End Date from the user and divide the days between the two dates into 3 phase increments with 15 payments. So divide the total amount of days by 3, and divide the total amount of days by 15
        exit


Tesla = SavingsGoal()
Tesla.run()

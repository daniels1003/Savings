import datetime


class SavingsGoal:

    def __init__(self):
        SavingsName = "Tesla"
        TotalPaymentAmount = 0
        Phase1Tot_TotalPaymentAmount = 0
        Phase2Tot_TotalPaymentAmount = 0
        Phase3Tot_TotalPaymentAmount = 0

   def setPaymentAmount(self, TotalPaymentAmount):
        self.TotalPaymentAmount = TotalPaymentAmount

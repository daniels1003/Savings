from SavingsGoal import SavingsGoal

Tesla = SavingsGoal("Tesla", 50000)
Tesla.setTotalAmount(100)
Tesla.setStartDate()
Tesla.start()


#     Phase1_Dates = []
#     Phase2_Dates = []
#     Phase3_Dates = []

#     #  TODO: Take the Start and End Date from the user and divide the days between the two dates into 3 phase increments with 15 payments. So divide the total amount of days by 3, and divide the total amount of days by 15

# date_now = datetime.datetime.now()
#  print("Today's Date is: " + str(date_now.strftime("%A" + " " + "%x")))

#  mininmumStart_date = date_now + datetime.timedelta(days=92)
#  print("Minimum Payment Plan Start Date: " +
#        str(mininmumStart_date.strftime("%x")))

#  # Testing Purposes
#  userStart_date = datetime.datetime(2019, 9, 25)
#  userEnd_date = datetime.datetime(2026, 10, 26)

#     print("The User Start Date is: " + str(userStart_date.strftime("%x")))
#     print("The User End Date is: " + str(userEnd_date.strftime("%x")))

#         # less than means "in the past", this asks, does the minimum start date come before the NOW date? result: false
#     if userStart_date < mininmumStart_date:
#         print("Sorry, your user start date is invalid!")
#     else:
#         print("Acceptable user start date!")

#     Tot_RepaymentDays = userEnd_date - userStart_date

#     DaysPerPhase_RepaymentDays = round(float(Tot_RepaymentDays.days/3))
#     DaysBetweenPayments_RepaymentDays = (round(float(Tot_RepaymentDays.days/15)))

#     if int(DaysPerPhase_RepaymentDays)%2 != 0:
#         round(float(DaysPerPhase_RepaymentDays))

#     print("Amount of Days between Start & End: "+ str(Tot_RepaymentDays.days))
#     print("Initial Days per Phase = " + str(DaysPerPhase_RepaymentDays))

#     print("Initial Days between Phase Payments = " + str(DaysBetweenPayments_RepaymentDays))

#     # * Phase Ranges (Display the date ranges)
#     Phase1End_date = userStart_date + datetime.timedelta(DaysPerPhase_RepaymentDays)
#     Phase2End_date = Phase1End_date + datetime.timedelta(DaysPerPhase_RepaymentDays)
#     Phase3End_date = Phase2End_date + datetime.timedelta(DaysPerPhase_RepaymentDays)

#     print("\nThe User Start Date is: " + str(userStart_date.strftime("%x")))
#     print("Phase 1 Ends " + str(Phase1End_date.strftime("%x")))
#     print("Phase 2 Ends " + str(Phase2End_date.strftime("%x")))
#     print("Phase 3 Ends " + str(Phase3End_date.strftime("%x")))
#     print("The End Date is: " + str(userEnd_date.strftime("%x")))

#     # if userEnd_date < Phase3End_date:
#     #     print("\tThe User's End Date conflicts with the payment schedule: Rescheduling End Date")
#     #     print("\tThe User End Date was: " + str(userEnd_date.strftime("%x")))
#     #     print("\tPhase 3 was scheduled to end: " + str(Phase3End_date.strftime("%x")))
#     #     userEnd_date = Phase3End_date
#     #     userEnd_date += datetime.timedelta(7)
#     #     print("The New End Date is: " + str(userEnd_date.strftime("%x")))

#     # * Phase 1 Payment Date Ranges

#     print("\n\nBreakdown!\nPhase 1:")

# # TODO: Create a breakdown of when payments are due including the dates

#     # diff = userStart_date - date_now
#     # if diff.days < 91:
#     #     print(
#     #         "You must select a date more than 3 Months (91 days) Away\nYours is: %s" % diff.days)

#     # diff = start_date - datetime.datetime.now()
#     # print(
#     #     "There are %s total days between now and when you plan to begin" % diff.days)
#     # print(str(diff.days/3) + " days per phase")

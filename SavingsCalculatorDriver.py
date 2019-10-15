from SavingsGoal import SavingsGoal


def main():
    Car = SavingsGoal("Accord", 8000)
    Car.start()
    Car.setNewTotalAmount(100)
    print(str(Car.getAmount()))

    exit


if __name__ == "__main__":
    main()

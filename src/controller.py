from src import calculateBMI


class Controller:

    def __init__(self):
        weight = self.getWeightFromUser()
        height = self.getHeightFromUser()
        calculator = calculateBMI.CalculateBMI()
        bmi = calculator.calculateBMI(weight, height)
        self.printBodyWeightAssessment(calculator, bmi)
        highest_correct_weight, lowest_correct_weight = calculator.findCorrectWeigth(height)
        self.printCorrectWeight(height, highest_correct_weight, lowest_correct_weight)

    def getWeightFromUser(self):
        return input("Podaj swoją wagę [w kg]: ").replace(',', '.')

    def getHeightFromUser(self):
        return input("Podaj swój wzrost [w cm]: ").replace(',', '.')

    def printBodyWeightAssessment(self, calculator, bmi):
        if calculator.lowest_index <= bmi < calculator.highest_index:
            print("waga prawidłowa")
        elif bmi < calculator.lowest_index:
            print("niedowaga")
        else:
            print("nadwaga")

    def printCorrectWeight(self, height, highest_correct_weight, lowest_correct_weight):
        print("Dla podanego wzrostu (" + height + " cm) prawidłowa waga wynosi pomiędzy: " + lowest_correct_weight
              + " a " + highest_correct_weight + " kg.")

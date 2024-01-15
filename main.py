class Calc():

    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.total_investment = 0

    def income(self):
        rent = int(input('Add rental income: '))
        laundry = int(input('Add monthly laundry income: '))
        storage = int(input('Add storage income: '))
        misc = int(input('add misc income: '))
        
        self.monthly_income = rent + laundry + storage + misc
        

    def expenses(self):
        tax = int(input("Monthly taxes: "))
        insurance = int(input("Monthly insurance: "))
        utilities = int(input("Total monthly ulitilites: "))
        hoa = int(input("Monthly HOA price: "))
        lawn = int(input("Monthly lawn/snow care: "))
        vacancy = int(input("Monthly money set aside for vacancy: "))
        repairs = int(input("Monthly money set aside for repairs: "))
        capex = int(input("Monthly money set aside for large repairs: "))
        property_management = int(input("Monthly property management price: "))
        mortgage = int(input("Monthly mortgage price: "))

        self.monthly_expenses = tax + insurance + utilities + hoa + lawn + vacancy+ repairs + capex + property_management + mortgage
         

    def cash_flow(self):
        self.monthly_cash_flow = self.monthly_income - self.monthly_expenses

    def cash_on_cash(self):
        down_payment = int(input('Down payment amount: '))
        closing = int(input('Closing cost amount: '))
        rehab = int(input('Rehab budget: '))
        misc = int(input('Misc/other costs: '))
        self.total_investments = down_payment + closing + rehab + misc

        self.annual_cash_flow = self.monthly_cash_flow * 12
        self.cash_cash_roi = (self.annual_cash_flow / self.total_investments) * 100

        return f'Your total ROI is: {self.cash_cash_roi}'
    
def run():
    new_roi = Calc()
    while True:
        print("\nFirst we are gonna ask a few question's about possible monthly income. Please enter all values in whole numbers.\n")
        new_roi.income()
        print(f"\nYour monthly income is [${new_roi.monthly_income}]")
        print("\nNext We're gonna ask a few questions about your monthly exspenses. Please enter all values in whole numbers\n")
        new_roi.expenses()
        print(f"\nYour total monthly expenses are: [${new_roi.monthly_expenses}]\n")
        new_roi.cash_flow()
        print(f"Your monthly cash flow is: [${new_roi.monthly_cash_flow}]\n")
        new_roi.cash_on_cash()
        print(f"\nYour total ROI is: [{round(new_roi.cash_cash_roi, 2)}%] ")

        break

run()
        
"""
         -- CODING CHALLENGE * HOURS WORKED --
# Multiply the hours/ week by weeks worked and print total hours worked

hrs/week:[22, 17, 27, 40, 45] weeks: [48, 50, 42, 46, 43]

output: 'Total hours 1056,850,1134,1840,1935'

#Advanced: Print hours worked and pay for name of each person

name, pay/hour in silver pieces:
['John,1', 'Eric,1.5', 'Terry,2', 'Michael,4', 'Graham,2']

Output:'John made 1056 Silver in 1056 hours.'
  	   'Eric made 1275 Silver in 850 hours.'
       'Terry made 2268 silver in 1134 hours.'....etc
"""


def main():
    hours_per_week = [22, 17, 27, 40, 45]
    weeks = [48, 50, 42, 46, 43]

    persons_raw = ['John,1', 'Eric,1.5', 'Terry,2', 'Michael,4', 'Graham,2']


    emps = [Employee(*name_salary(raw), weeks, hours)
        for hours, weeks, raw in zip(hours_per_week, weeks, persons_raw)
    ]

    #Part1
    print(f"Total hours {','.join(map(str,[emp.total_hours() for emp in emps]))}")

    #Part2:
    for emp in emps:
        print(emp.payment_info())


class Employee:
    def __init__(self, name, pay, weeks, hours):
        self.name = name
        self.pay = pay
        self.weeks = weeks
        self.hours = hours

    def total_hours(self):
        return self.hours * self.weeks

    def income(self):
        return round(self.pay * self.total_hours())

    def payment_info(self):
        return f"{self.name} made {self.income()} Silver in {self.total_hours()} hours"


def name_salary(s):
    name, salary = s.split(',')
    return name, float(salary)


if __name__ == '__main__':
    main()

#Kassahun Workie CIS261 Course Project Phase 3
class Employee:
    def __init__(self, name, from_date, to_date, hours_worked, hourly_rate, tax_rate):
        self.name = name
        self.from_date = from_date
        self.to_date = to_date
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate

def WriteEmployeeInformation(employee):
    with open("employeeinfo.txt", "a") as file:
        file.write('{}|{}|{}|{}|{}|{}\n'.format(employee.from_date, employee.to_date, employee.name, employee.hours_worked, employee.hourly_rate, employee.tax_rate))

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList, EmpTotals):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    for emp in EmpDetailList:
        fromdate = emp.from_date
        todate = emp.to_date
        empname = emp.name
        hours = emp.hours_worked
        hourlyrate = emp.hourly_rate
        taxrate = emp.tax_rate

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}",
              f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")

def GetFromDate():
    valid = False
    fromdate = ""
    while not valid:
        fromdate = input("Enter From Date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True
    return fromdate

def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    condition = True
    if fromdate.upper() == 'ALL':
        condition = False
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            EmpDetailList.append(Employee(employee[2], employee[0], employee[1], float(employee[3]), float(employee[4]), float(employee[5])))
        else:
            if fromdate == employee[0]:
                EmpDetailList.append(Employee(employee[2], employee[0], employee[1], float(employee[3]), float(employee[4]), float(employee[5])))
    return EmpDetailList

def main():
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetEmpName()
        if empname.upper() == "END":
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        emp = Employee(empname, fromdate, todate, hours, hourlyrate, taxrate)
        WriteEmployeeInformation(emp)
        print()
        print()

    fromdate = GetFromDate()
    EmpDetailList = ReadEmployeeInformation(fromdate)
    print()
    printinfo(EmpDetailList, EmpTotals)
    print()
    PrintTotals(EmpTotals)

    # Display subset of employees based on a specific from date
    fromdate_subset = input("Enter a specific 'from date' to display a subset of employees: ")
    EmpDetailList_subset = ReadEmployeeInformation(fromdate_subset)
    print()
    print("Subset of Employees Based on Specific From Date:")
    printinfo(EmpDetailList_subset, EmpTotals)
    print()
    PrintTotals(EmpTotals)

if __name__ == "__main__":
    main()


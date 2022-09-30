import EmployeeClass as e
import PayrollDeductionClass as d


emp1 = e.employee('Jimmy Smith','58475','Information Systems','Developer',6800)

transaction1 = d.deduction('food court','8/14/2022',22.50,'39119')
transaction2 = d.deduction('gift contribution','8/12/2022',25.00,'58475')
transaction3 = d.deduction('food court','8/17/2022',15.25,'21547')
transaction4 = d.deduction('vending machine','8/22/2022',3.00,'58475')
transaction5 = d.deduction('vending machine','8/5/2022',2.75,'58475')

net_pay = emp1.get_salary() - transaction2.get_amt() - transaction4.get_amt() - transaction5.get_amt()

print('*** Employee Pay ***')
print('Name:', emp1.get_name())
print('Department:',emp1.get_department())
print('Gross Pay:', emp1.get_salary())
print('Net Pay:', net_pay)

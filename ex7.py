print("Enter your annual salary:")
annual_salary=float(input())
print("Enter the percent of your salary to save, as a decimal: ")
portion_saved=float(input())
print("Enter the cost of your dream home:")
total_cost=float(input())
m=0
portion_deposit=total_cost/10*2
current_savings=0
r=0.04
total_cost=total_cost-portion_deposit
while(current_savings!=total_cost):
    portion_saved=annual_salary/12/10
    current_savings=current_savings+portion_saved+current_savings*r/12
    m=m+1
print("Number of months:"+m)

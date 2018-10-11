annual_salary=float(input("Enter your annual salary:"))
m=1
current_savings=0
portion_deposit=0.25
m_salary=annual_salary/12
r=0.04
semi_annual_raise=0.07
total_cost=1000000
money_needed=total_cost*portion_deposit
epsilon=0.1
number_guesses=0
low=0
high=1
guess=(high+low)/2.0
while abs(current_savings-money_needed)>=epsilon:
    current_savings=0
    m=1
    while(m<=36):
        current_savings+=m_salary*guess
        current_savings+=current_savings*r/12
        if(m%6==0):
            annual_salary*=semi_annual_raise
        m+=1
    if(current_savings<money_needed):
     low=guess
    else:
         high=guess
    guess=(high+low)/2.0
    number_guesses+=1
if(guess>1):
    print("not enough")
else:
    print("Best savings rate:"+str(guess))
    print("Steps in bisection search:"+str(number_guesses))

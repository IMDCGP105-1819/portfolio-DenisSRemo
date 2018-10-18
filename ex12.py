def hotel_cost(nights):
    return nights*70
def plane_ticket_cost(city,class):
    if city==NewYork:
        return 2000*class
    else:
        if city==Auckland:
            return 790*class
        else:
            if city==Venice:
                return 154*class
            else:
                if city==Glasgow:
                    return 65*class
def rental_car(days):
    if days>3 and days<7:
        return days*30-30
    else:
        if days>7:
            return days*30-50
        else:
            return days*30
def total_cost(city,days):
    nights=int(input())
    class=float(input())
   
    
    x=hotel_cost(nights)
    y=plane_ticket_cost(city,class)
    z=rental_car(days)
    return x+y+z
days=int(input())

 city=str(input())
 sum=total_cost(city,days)
Cities = {
    "Paris":{
        "Return_flight":200,
        "Hotel_per_day":20,
        "weekly_car_rental":200
    }, 
    "London":{
        "Return_flight":250,
        "Hotel_per_day":30,
        "weekly_car_rental":120
    },
    "Dubai":{
        "Return_flight":370,
        "Hotel_per_day":15,
        "weekly_car_rental":80
    },
    "Mumbai":{
        "Return_flight":450,
        "Hotel_per_day":10,
        "weekly_car_rental":70
    }
}

for keys,values in Cities.items():
    print(f"{keys}:{values}")

# Answer the following questions using the data above:

# 1. If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?

import math

def total_cost(city,duration):
    values= Cities[city]
    return (values["Return_flight"]+values["Hotel_per_day"]*duration+values["weekly_car_rental"]*math.ceil(duration/7))

def minimum_cost():
    total_costt={}
    duration=7
    for i in Cities.keys():
        total_costt[i] = total_cost(i,duration)
    
    print(total_costt)

    minimum_city=None
    minimum_value=math.inf

    for i in total_costt:
        if total_costt[i]<minimum_value:
            minimum_value=total_costt[i]
            minimum_city=i
    
    print(f"To spend least amount of money in 1week trip, you should visit {minimum_city} for just ${total_costt[minimum_city]}")

minimum_cost()

# 2. How does the answer to the previous question change if you change the duration of the trip to 4 days, 10 days or 2 weeks?

def minimum_cost1():
    total_cost1={}
    duration=[4,10,12]

    for k in duration:
        total_cost1[k]={}
        for i in Cities.keys():
            total_cost1[k][i] = total_cost(i,k)
    
    for k in duration:
        print(f"----for {k} days:---")
        for i in total_cost1[k]:
            print(f"{i}:{total_cost1[k][i]}")
            minimum_city=None
            minimum_value=math.inf
            if total_cost1[k][i]<minimum_value:
                minimum_value=total_cost1[k][i]
                minimum_city=i
        print(f"To spend least amount of money in {k} days trip, you should visit {minimum_city} for just ${total_cost1[k][minimum_city]}")

minimum_cost1()

# 3. If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip? 
# Which city should you visit if you want to minimize the duration?
# 4. How does the answer to the previous question change if your budget is $600, $2000 or $1500 ?
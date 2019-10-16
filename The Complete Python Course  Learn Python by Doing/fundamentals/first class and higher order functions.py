operations = {
  "total": lambda seq : sum(seq),
  "top": lambda seq : max(seq),
  "avg": lambda seq :sum(seq)/len(seq)
}

listofcars = [

  {
    "name" : "mercides",
    "year" : 2004,
    "prices":(300,600,900)
  },
   {
    "name" : "corolla",
    "year" : 2007,
    "prices":(500,800.900)

  },
   {
    "name" : "tida",
    "year" : 2011,
    "prices":(600,300,800)

  }

]
  
name = input("enter your  choice of car  :  ")
for car in listofcars:
  if name == car["name"]:
    theprices = car["prices"]



operation = input(f"enter operation you like to applay on your {name} => (total) for sum of all prices or (top) for max price or (avg) for avarage price  ")
result = operations[operation](theprices)
print(result)
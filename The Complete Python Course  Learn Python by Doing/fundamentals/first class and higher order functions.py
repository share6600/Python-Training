thisdict = {
  "total": lambda seq : sum(seq),
  "top": lambda seq : max(seq),
  "average": lambda seq :sum(seq)/len(seq)
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



operation = input("enter operation you like total of all available or max price or average")
result = thisdict[operation](theprices)
print(result)
#code that print out the LastName of the second employee to the dictionary below.

d = {
  "employee":[{"firstName" : "John", "lastName" : "Doe"},
              {"firstName" : "Anna", "lastName" : "Smith"},
              {"firstName" : "Peter", "lastName" : "Jones"}],

"owners":[{"firstname": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]
           }

lastName = d["employee"][1]["lastName"]
print(f" The last Name of the second employee is: {lastName}")

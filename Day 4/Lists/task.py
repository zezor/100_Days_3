# worKing with lists
fruits = ["Cherry", "Apple", "Pear"]
print(fruits)
print(fruits[0])

states_of_america = ["Delaware", "Pennsylvania",
                     "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina",
                     "New Hampshire", "Virginia",
                     "New York", "North Carolina",
                     "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee",
                     "Ohio", "Louisiana",
                     "Indiana", "Mississippi",
                     "Illinois", "Alabama",
                     "Maine", "Missouri",
                     "Arkansas", "Michigan",
                     "Florida", "Texas",
                     "Iowa", "Wisconsin",
                     "California", "Minnesota",
                     "Oregon", "Kansas",
                     "West Virginia",
                     "Nevada", "Nebraska",
                     "Colorado", "North Dakota",
                     "South Dakota", "Montana",
                     "Washington", "Idaho",
                     "Wyoming", "Utah",
                     "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]
states_of_america[-1] = "Ghana"
print(states_of_america)

states_of_america.append("Kumerica")
print(states_of_america)

#adding another list
states_of_america.extend(["Accra", "Koforidua", "Kumasi"])
print(states_of_america)
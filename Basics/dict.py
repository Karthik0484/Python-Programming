trip = {
   "123456": {"trip_id": "123456","pick_up": "Hosur","Drop": "Banglore","Status": "Active"},
   "654321": {"trip_id":"654321","pick_up":"Electronic City","Drop":"Infosys","Status":"Completed"},
   "987654": {"trip_id":"987654","pick_up":"PG","Drop":"Qspiders","Status":"Inprogress"},

}


for trips,desc in trip.items():
    print(trips)
    print(desc["pick_up"],"-->",desc["Drop"])

'''

# Accessing Dictionary Values
print(trip["Drop"])
print(trip.get("Statu"))

# Updating Dictionary Values
trip["Drop"]= "QSpiders"
print("After Updating:",trip)

trip["Driver"] = "Alice"
print("Adding new Keys:",trip)

# Deleting a key-value pair
del trip["Driver"]
print("After Deleting:",trip)

print(trip.keys())
print(trip.values())

# Looping through
for key,value in trip.items():
    print(f"{key} : {value}")



print(trip.update({"Status":"Completed"}))
print(trip)

print(trip["pick_up"][2])

for pick_up in trip["pick_up"]:
    print(pick_up)
'''
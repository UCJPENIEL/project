expenses = [
{"date": "2026-09-11",
"category": "food",
"description": "lunch",
"amount": 3500},
 
 {"date": "2026-09-12",
  "category": "transportation",
  "description": "bus fare",
  "amount": 1500},
 
 {"date": "2026-09-13",
  "category": "bills",
  "description": "internet subscription",
  "amount": 25000}
 ]

total_expenses = sum(expense["amount"] for expense in expenses)
for expense in expenses:
    print(expense)
print(f"Total expenses: {total_expenses}")

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
print(category_totals) 

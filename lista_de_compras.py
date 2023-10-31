import csv

# Initialize an empty list to store the shopping items
shopping_list = []

# Function to add items to the shopping list
def add_item():
    while True:
        item = input("Add an item or quit (Enter Q): ")
        if item.lower() == 'q':
            break
        shopping_list.append(item)

# Call the function to add items to the shopping list
add_item()

# Specify the file name and open it for appending
with open('lista_compras.csv', 'a', newline='') as csvfile:
    append = csv.writer(csvfile)
    
    # Append the data (shopping list) to the CSV file
    append.writerow(shopping_list)

print("Shopping list has been saved.\n")


# Read and print all the items in the list
with open('lista_compras.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    position = 1  # Initialize position so we can keep track
    for row in reader:
        print(f"Current items in position {position} in the list are:")
        for item in row:
            print(item)
        position += 1
    if position == 1:
        print("The shopping list is empty.")
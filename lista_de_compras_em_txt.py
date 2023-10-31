# Open our .txt file and make it just append the new array, we do not want to override

with open('lista_compras_v2.txt', 'a') as file:
    # Initialize an empty list to store the array
    lista_de_compras = []

    # Function to add items to the array
    def add_item():
        while True:
            item = input("Add an item or quit (Enter Q): ")
            if item.lower() == 'q':
                break
            lista_de_compras.append(item)
            # Append the item to the text file
            file.write(item + '\n')

    # Call the function to add items to the array and the .txt file
    add_item()

# Read and print the contents of the text file
with open('lista_compras_v2.txt', 'r') as file:
    content = file.read()
    if content:
        print("Current items in the array are:")
        print(content)
    else:
        print("The array is empty.")
#

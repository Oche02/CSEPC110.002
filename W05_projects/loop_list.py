new_clients = ""
client = []

while new_clients != "exit":
    new_clients = input("Enter a new client name (or type 'exit' to finish): ")
    if new_clients != "exit":
        client.append(new_clients)

print()
print("Here is the list of clients you entered:")
for clients in sorted(client):
    print(f"--- {clients.title()}")
print("Thank you for using the client list program!")

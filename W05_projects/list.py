clients = []

clients.append("Augustine")
clients.append("Hamza")
clients.append("General")
clients.append("Moses")
clients.append("Adams")

new_clients = input("Enter a new client name: ")
clients.append(new_clients)

for client in sorted(clients):
    print(client)

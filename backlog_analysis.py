import csv
import matplotlib.pyplot as plt

file_name = r"C:\Users\Karla Alvarez\Desktop\python backlog\test_tickets.csv.txt"

status_counts = {'Open': 0, 'In Progress': 0, 'Resolved': 0, 'Closed': 0}

# Open the CSV file and read its contents
with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Skip the header row (Ticket_ID, Status, etc.)
    headers = next(reader)

    for row in reader:
        status = row[1]
        if status in status_counts:
            status_counts[status] += 1

print("--- Backlog Analysis ---")
for status, count in status_counts.items():
    print(f"{status}: {count}")

statuses = list(status_counts.keys())
counts = list(status_counts.values())
plt.bar(statuses, counts, color=['blue', 'orange', 'green', 'red'])

plt.title('Ticket Backlog Distribution')
plt.xlabel('Ticket Status')
plt.ylabel('Number of Tickets')

plt.show()
visitors = []

while True:
    print("\n=== Barangay Visitor Log ===")

    # Ask for visitor information
    name = input("Enter visitor name: ")
    purpose = input("Enter purpose of visit: ")

    visitor = {
        "name": name,
        "purpose": purpose
    }

    visitors.append(visitor)

    choice = input("Add another visitor? (yes/no): ").strip().lower()

    if choice != "yes":
        break

print("\n===== RECORDED VISITORS =====")

for number, visitor in enumerate(visitors, start=1):
    print(f"{number}. Name: {visitor['name']}")
    print(f"   Purpose: {visitor['purpose']}")

print(f"\nTotal Visitors Recorded: {len(visitors)}")
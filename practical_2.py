practical=2
Qno.2.1.1
numbers = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            num = int(input("Integer: "))
            numbers.append(num)
            print(f"List after adding: {numbers}")
        except ValueError:
            print("Invalid input")

    elif choice == "2":
        if len(numbers) == 0:
            print("List is empty")
        else:
            try:
                num = int(input("Integer: "))
                if num in numbers:
                    numbers.remove(num)
                    print(f"List after removing: {numbers}")
                else:
                    print("Element not found")
            except ValueError:
                print("Invalid input")

    elif choice == "3":
        if len(numbers) == 0:
            print("List is empty")
        else:
            print(f"{numbers}")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

Qno.2.1.2
students = {
    1: 'Amit',
    2: 'Riya',
    3: 'Kiran',
    4: 'Neha',
    5: 'Arjun',
    6: 'Pooja',
    7: 'Rahul',
    8: 'Sneha',
    9: 'Vikram',
    10: 'Anjali'
}


print("Original Dictionary:", students)


key_insert = int(input())
value_insert = input()

students.update({key_insert: value_insert})
print("After Insertion:", students)


key_update = int(input())
value_update = input()

if key_update in students:
    students.update({key_update: value_update})

print("After Update:", students)


key_delete = int(input())

students.pop(key_delete, None)

print("After Deletion:", students)

print("Traversing Dictionary:")
for key, value in students.items():
    print(key, ":", value)

Qno.2.2.1
arr = list(map(int, input().split()))

key = int(input())

found = False
for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        found = True
        break

if not found:
    print("Not found")

Qno.2.2.2
heights = list(map(int, input().split()))
tallest = max(heights)
print(tallest)

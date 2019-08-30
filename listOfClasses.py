number_of_classes = int(input("How many classes are you taking this semester?: "))
class_list = []

while number_of_classes > 0:
    class_name = input("Enter you class name: ")
    class_list.append(class_name)
    number_of_classes -= 1

print("The classes you are taking are:")
for item in class_list:
    print(item)
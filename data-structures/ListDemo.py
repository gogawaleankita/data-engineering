import random

print("### Create a list of the first 20 positive integers. Print the list. ###")

list1 = [num for num in range(1, 21)]

print(list1)

print("### Print the first, middle, and last elements of the list created in Assignment 1 ###")

print(f"FirstElement: {list1[0]} ,MiddleElement: {list1[int(len(list1) / 2)]},,MiddleElement: {list1[-1]}")

print("### Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list "
      "created ",
      "in Assignment 1####")

print(f"the first five elements {list1[0:5]}")
print(f"the last five elements {list1[-6:]}")
print(f"the elements from index 5 to 15 of the list created in Assignment 1 {list1[5:15]}")

print("### Create a new list containing the squares of the first 10 positive integers using a list comprehension. "
      "Print the new list ###")

square = [i ** 2 for i in range(1, 11)]
print(square)

print("### Create a new list containing only the even numbers from the list created in Assignment 1 using a list "
      "comprehension. Print the new list. ###")

evenSquare = [i for i in square if i % 2 == 0]
print(evenSquare)

print("### Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from "
      "the list and print the modified list### ")

randList = [random.randint(1, i) for i in range(1, 100)]

print(randList)
print(f"Ascending => {sorted(randList)}")
print(f"Descending => {sorted(randList,reverse=True)}")

print("### Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the "
      "second row and third column### ")

nestedList = [[i for i in range(3)] for i in range(3) ]
for i in nestedList:
    print(i)
print(nestedList[1][2])

print("### Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. "
      "Sort the list of dictionaries by the 'score' in descending order and print the sorted list.### ")

studentList = [{'name': f'aab{i}','score':  random.randint(24,100)} for i in enumerate(range(1,10))]

studentList.f
print(studentList)




# print("### Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.### ")
# print("### Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.### ")
# print("### Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.### ")
# print("### Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.### ")
# print("### Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.### ")
# print("### Write a function that rotates a list by n positions. Print the original and rotated lists.### ")
# print("### Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.### ")

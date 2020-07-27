'''
This is a program that takes input on a book code, book's cost, the number of current
books on hand, the class enrollment, whether the book is required or recommended, and
has or has not been used in the past. Then the program will display all this
information, whether on not more books need to be ordered and how much that will cost,
and the store's expected profit.
Author: Jacob Roberson
Course: ITM313
'''
bookCode = ""
bookPrice = 0
bookStock = 0
classSize = 0
bookStatus = ""
bookUsage = ""
bookOrder = 0
bookCost = 0
storeProfit = 0

print("Welcome the Book Information System.\nPlease enter the information as it is "
      "requested.")
bookCode = input("Please enter the book code: ")
bookPrice = eval(input("Please enter the book's single copy cost: "))
bookStock = int(input("Please enter the current number of volumes on hand: "))
classSize = int(input("Please enter the prospective class enrollment: "))
bookStatus = input("Please enter whether the book is required or recommended: ")
bookUsage = input("Has this book been used in the past? (Enter 'Yes' or 'No'): ")

bookOrder = (classSize - bookStock)
bookCost = (bookOrder * bookPrice)
storeProfit = ((classSize * bookPrice) * .2)

print("\nBook Code:", bookCode, "\nPrice per Book: %.2f" % (bookPrice), "\nBooks in "
      "Stock: ", bookStock, "\nProspective Class Enrollment: ", classSize, "\nRequired"
      " or Recomended: ", bookStatus, "\nHas this book been used in the past: ",
      bookUsage)
if (bookStock >= classSize):
    print("Books needed to be ordered: None\nCost of Book Order: N/A\nStore Profit: "
          "$%.2f" % (storeProfit))
else:
    print("Books needed to be ordered: ", bookOrder, "\nCost of Book Order: $%.2f" %
    (bookCost), "\nStore Profit: $%.2f" % (storeProfit))

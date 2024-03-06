from user_input import get_selection, SelectionFromNumber
from time import time

fruits = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "pineapple", "mango", "kiwi", "pear",
          "cherry", "blueberry", "lemon", "lime", "peach", "plum", "raspberry", "blackberry", "pomegranate", "avocado"]
print(f"{fruits=}")
print(len(fruits))

start = time()
sel = get_selection(fruits)
end = time()
print(f"{sel=} time:{end-start}")

start = time()
sel = SelectionFromNumber(fruits)
sel.prompt()
sel.prompt_process()
sel.make_selection()
end = time()
print(f"{sel.selection=} time:{end-start}")

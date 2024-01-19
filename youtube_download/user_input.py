from utility import *


def mode_select(modes: dict) -> any:

    question = f"\nPlease select mode (1 - {len(modes)})"
    for i, name in enumerate(modes):
        question += f"\n({i + 1}) {name}"

    question += "\n(-1) Quit\n>"

    while True:

        try:
            mode = int(input(question))

            if mode == -1:
                quit()

            elif mode >= 1 and mode <= len(modes):
                return list(modes)[mode-1]

        except ValueError:
            print("\nMode not found. Please try again")


def selection_single(text, number_of_items, selection, array):
    n = int(text)

    if check_num_range(n, 1, number_of_items):
        i = n-1
        if array[i] not in selection:
            selection.append(array[i])


def selection_range(text, number_of_items, selection, array):
    start, end = text.split("-")

    try:

        start = int(start)
        end = int(end)

        if start < end and check_num_range(start, 1, number_of_items) and check_num_range(end, 1, number_of_items):
            selection.extend(
                [elem for elem in array[start-1:end] if elem not in selection])

    except ValueError:
        # add a statment here
        pass


def get_selection(array) -> list:
    selected_indexs = []
    number_of_items = len(array)
    selection = []
    answer = get_input("Enter selection (1-10 5)",
                       default="all").lower().strip()

    if answer == "all":
        return array

    answer = answer.split()

    # print(answer)

    for text in answer:

        if len(text.split("-")) == 2:
            selection_range(text, number_of_items, selection, array)

        elif text.isdigit():

            selection_single(text, number_of_items, selection, array)

    return selection


def get_input(question, default=None):

    if default is not None:
        question += f". Default is {str(default)}."

    question = "\n" + question + "\n>"
    while True:

        answer = input(question)
        if answer:
            return answer

        if default is not None:
            return default


def get_num(question, default=None):

    while True:
        answer = get_input(question, default)
        if answer.isdigit():
            return answer
        else:
            print("Enter a positve integer")


def get_confirm(question, default=None):

    question += " [y/n]"

    while True:
        answer = get_input(question, default)

        if answer.lower().strip() in ["yes", "y"]:
            return True

        elif answer.lower().strip() in ["no", "n"]:
            return False

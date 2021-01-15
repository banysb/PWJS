import os

def tree(filepath):
    print("\n" + filepath)
    print(os.listdir(filepath))
    previous_filepath = os.path.dirname(filepath)
    if previous_filepath != filepath:
        tree(previous_filepath)

filepath = "C:/Users/Dell/PycharmProjects"
tree(filepath)
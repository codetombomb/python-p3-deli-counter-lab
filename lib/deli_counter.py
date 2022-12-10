def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        string = "The line is currently:"
        for idx, name in enumerate(list):
            string += f" {idx + 1}. {name}"
        print(string)

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {len(list)} in line.")

def now_serving(list):
    if len(list) == 0:
         print("There is nobody waiting to be served!")
    else:
        removed = list[0]
        list.remove(list[0])
        print(f"Currently serving {removed}.")

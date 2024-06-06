todo_list = []

def add_todo_item(item):
    todo_list.append(item)
    return f"Added '{item}' to your to-do list."

def get_todo_list():
    if not todo_list:
        return "Your to-do list is empty."
    return "Your to-do list:\n" + "\n".join(f"- {item}" for item in todo_list)

def remove_todo_item(item):
    if item in todo_list:
        todo_list.remove(item)
        return f"Removed '{item}' from your to-do list."
    else:
        return f"'{item}' is not in your to-do list."

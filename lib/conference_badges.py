def badge_maker(name):
    return(f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_message = []
    for name in names:
        badge_message.append(f"Hello, my name is {name}.")
    return badge_message

def assign_rooms(names):
    room_message = []
    for i, name in enumerate(names):
        room_message.append(f"Hello, {name}! You'll be assigned to room {i + 1}!")
    return room_message

def printer(names):
    badge_creator = batch_badge_creator(names)
    room_message = assign_rooms(names)

    for message in badge_creator:
        print(message)

    for message in room_message:
        print(message)

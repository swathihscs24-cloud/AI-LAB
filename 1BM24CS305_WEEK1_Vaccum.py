def simple_reflex_agent(location, status):

    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"


environment = {"A": "Dirty", "B": "Dirty"}
loc = "A"

print("--- Simple Reflex Agent ---")
for step in range(4):
    status = environment[loc]
    action = simple_reflex_agent(loc, status)
    print(f"Location: {loc}, Status: {status} -> Action: {action}")


    if action == "Suck":
        environment[loc] = "Clean"
    elif action == "Right":
        loc = "B"
    elif action == "Left":
        loc = "A"

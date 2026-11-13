
import re

def parse(expr):
    name, args = expr.split("(", 1)
    args = args.rstrip(")")
    return name.strip(), [x.strip() for x in args.split(",")]


def is_variable(x):
    return x.islower() and x not in ["john", "riya", "apple", "mango"]


def occurs_check(var, term, subs):
    while term in subs:
        term = subs[term]
    return var == term


def unify(x, y, subs):
    if x == y:
        return True

    if is_variable(x):
        if occurs_check(x, y, subs):
            return False
        subs[x] = y
        return True

    if is_variable(y):
        if occurs_check(y, x, subs):
            return False
        subs[y] = x
        return True

    return False


def main():
    print("UNIFICATION IN FIRST ORDER LOGIC")

    e1 = input("Enter first expression: ")
    e2 = input("Enter second expression: ")

    p1, a1 = parse(e1)
    p2, a2 = parse(e2)

    if p1 != p2 or len(a1) != len(a2):
        print("Unification Failed!")
        return

    subs = {}

    for x, y in zip(a1, a2):
        if not unify(x, y, subs):
            print("Unification Failed!")
            return

    print("\nUnification Successful!")
    print("Most General Unifier (MGU):")

    for x, y in subs.items():
        print(x, "=", y)


main()

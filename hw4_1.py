# x: int = int(input("pizza pieces: "))
# pizza_pieces_for_a_friends: int = x // 4
# the_undivided_pizza_pieces: int = x % 4
#
# print(f"pizza pieces for a friends {pizza_pieces_for_a_friends}")
#
# if x % 4 != 0:
#     print(f"the undivided pieces of pizza {the_undivided_pizza_pieces}")


x: int = int(input("pizza pieces: "))
f: int = int(input("danny's friends: "))
pizza_pieces_for_a_friends: int = x // f
the_undivided_pizza_pieces: int = x % f

print(f"pizza pieces for a friends {pizza_pieces_for_a_friends}")

if x % f != 0:
    print(f"the undivided pieces of pizza {the_undivided_pizza_pieces}")

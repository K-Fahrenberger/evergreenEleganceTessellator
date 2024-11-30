# Trees per row
X_REPEAT = 5
# Rows of trees
Y_REPEAT = 8

for y in range(Y_REPEAT):
    # Top of the tree
    for x in range(X_REPEAT):
        print("   ^   ", end="")
    print()
    for x in range(X_REPEAT):
        print("  ^^^  ", end="")
    print()
    for x in range(X_REPEAT):
        print(" ^^^^^ ", end="")
    print()
    for x in range(X_REPEAT):
        print("^^^^^^^", end="")
    print()
    # Trunk of the tree
    for x in range(X_REPEAT):
        print("   |   ", end="")
    print()
    for x in range(X_REPEAT):
        print("   |   ", end="")
    print()
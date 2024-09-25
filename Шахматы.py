def rotate_left(triple):
    return (triple[1], triple[2], triple[0])
def rotate_right(triple):
    return (triple[2], triple[0], triple[1])

triple=("A","B","C")
print(rotate_left(triple))

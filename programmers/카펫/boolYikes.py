# The carpet conundrum
# What kinda alien mind remembers the number of tiles anyway?
# Leo is a computer vision AI. RESOLVED
def solution(brown, yellow):

    # Super high-tech footage calculator for the given x, y configuration 😮
    def config(x, y):
        return x * 2 + y * 2
    # On a sidenote, lambda functions don't have tracebacks built in.
    
    # border: solid brown 1px 😛
    # i == height for the yellow stuff
    for i in range(1, yellow+1):
        
        # No raggedy incomplete row!
        if yellow % i == 0:

            # Blocks divided by rows
            div = yellow // i
            # Had to draw pictures to figure this out
            if config(div, i) == brown - 4:
                return [div + 2, i + 2] if div > i else [i + 2, div + 2]

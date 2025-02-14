def solution(name):

    # name = list(name)
    l_target = len(name)
    moves = 0

    ### Vertical, Letter-selection moves
    for letter in name:
        
        # Which is closer, 'A' or 'Z'?
        dist_a = ord(letter) - ord('A')
        dist_z = 26 - (ord(letter) - ord('A')) # inverted
        
        # Move as much as the shorter one
        moves += min(dist_a, dist_z)

    ### Horizontal, cursor moves
    # Init moves for comparison
    min_moves = l_target - 1 # the maximum

    # Life is loop 😫
    # The split point 'i' to the right. (default right movement amount)
    for i in range(l_target):
        next_idx = i + 1
        
        # Find the next non-'A' position == Skip consecutive 'A's
        while next_idx < l_target and name[next_idx] == 'A':
            next_idx += 1

        #                 R Back       L
        right_then_left = i + i + l_target - next_idx

        # You can't wrap around to the right from the last letter (according to the restraints)
        # i.e., from 'Z' to 'A' to the right
        # This prolly is a pitfall of this problem?
        #                        L              BACK  R
        left_then_right = (l_target - next_idx) * 2 + i

        # Update min_moves
        min_moves = min(min_moves, right_then_left, left_then_right)

    return moves + min_moves

    ### The struggle 😇😛😭🤪😵😬🤮
    # letters = [chr(alph_ordinal) for alph_ordinal in range(65, 91)]
    # l_letters = len(letters)
    # middle = len(letters) // 2
    
    # init_name = ["A"] * l_target
    # if name == init_name:
        # return 0

    # Settle for a letter once in any position, otherwise you waste a move.
    # For an initial input index 'position'...
    # ...and the cursor movement as 'direction':
    # def sweet_home_alabama(position, direction, curr_name=["A"] * l_target, moves_record=0): # why don't it reset?
    # def sweet_home_alabama(position, curr_name=init_name.copy(), moves_record=0):
    #     print(f"position: {position}, curr: {curr_name} and {moves_record} moves...", end=" ")

    #     # Always starts from 'A' -> distance is always positive and absolute...
    #     # ...which is a load off
    #     distance = ord(name[position]) - ord(curr_name[position])

    #     # Go up(next letter) if the target is on the right to the middle
    #     print(f"dist: {distance},", end=" ")
    #     if distance > middle:
    #         curr_name[position] = letters[-(l_letters % distance)]
    #         moves_record += min(distance, 26-distance)
    #     else:
    #         curr_name[position] = letters[distance]
    #         moves_record += distance

    #     print(f"modified: {curr_name}, {moves_record} moves.")

    #     # Target reached
    #     if curr_name == name:
    #         print(f"done. this record: {moves_record}")
    #         # Subtract the last move before returning
    #         return moves_record

    #     # For directions
    #     left, right = 1, 1

    #     # , search for consecutive, complete letters to the left,
    #     # while curr_name[(position - left) % l_target] == name[(position - left) % l_target] and left < l_target:
    #     #     left += 1
        
    #     # # and to the right from this position,
    #     # while curr_name[(position + right) % l_target] == name[(position + right) % l_target] and right < l_target:
    #     #     right += 1

    #     # Skip matching 'A's
    #     while name[(position - left) % l_target] == "A" and left < l_target:
    #         left += 1
    #     while name[(position + right) % l_target] == "A" and right < l_target:
    #         right += 1

    #     # et choisir
    #     if left < right:
    #         return sweet_home_alabama((position - left) % l_target, curr_name, moves_record + left)
    #     else:
    #         return sweet_home_alabama((position + right) % l_target, curr_name, moves_record + right)
    
    # return sweet_home_alabama(0, curr_name=init_name.copy(), moves_record=0)

    #     # To move cursor is to manipulate the index(position). 🤮
    #     # No going back(you settle for a letter per move) -> one direction 🎶
    #     # Move only once for economy
    #     return sweet_home_alabama(position+direction, direction, curr_name, moves_record+1)

    # moves = []
    # for direction in [-1, 1]:
    #     # Start position == always the first letter
    #     moves.append(sweet_home_alabama(0, direction, curr_name=init_name.copy(), moves_record=0))
    # return min(moves)
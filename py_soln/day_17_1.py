ans = sum(list(range(1,74)))
print("Answer {}".format(ans))

min_y = -74
max_y = -54

min_x = 281
max_x = 311

#lower triangle number in x range is n = 24 -> 300
# lowest triangle number in y range

x_range = list(range(0,2000))

y_range = list(range(-75,75))

highest_y = ans


def is_valid(v_x, v_y):
    pos_y = 0
    pos_x = 0
    while pos_y <= highest_y and pos_y > 10*min_y and pos_x <= 10*max_x:
        #print(pos_x, pos_y)
        if pos_y >= min_y and pos_y <= max_y and pos_x >= min_x and pos_x <= max_x:
            return True
        pos_y += v_y
        pos_x += v_x
        if v_x > 0:
            v_x -= 1
        v_y -= 1
    return False

valid_vel = []
for x in x_range:
    for y in y_range:
        if is_valid(x,y):
            print(x,y)
            valid_vel.append((x,y))

print("Part 2 Answer {}".format(len(valid_vel)))


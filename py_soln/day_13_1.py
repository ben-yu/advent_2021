import copy
import sys

with open('../inputs/day_13_input.txt') as f:
    lines = f.readlines()

    coords = {}
    for l in lines:
        if len(l.strip()) == 0:
            print(coords)
            continue

        if len(l) > 4 and l[:4] == 'fold':
            res = l.strip().split(' along ')
            res = res[1].split('=')
            #print(res)
            direction = res[0]
            dir_val = int(res[1])
            new_paper = copy.deepcopy(coords)
            if direction == 'y':
                for x,y in coords:
                    if y > dir_val:
                        new_y = dir_val - (y - dir_val)
                        print((x,new_y,x,y))
                        new_paper[x,new_y] = True
                        del new_paper[x,y]
                total = 0
                print('-----')
                for k in new_paper:
                    if new_paper[k]:
                        total += 1
                print("Answer: {}".format(total))
                sys.exit()

            elif direction == 'x':
                for x,y in coords:
                    if x > dir_val:
                        new_x = dir_val - (x - dir_val)
                        new_paper[new_x,y] = True
                        del new_paper[x,y]
                total = 0
                print('-----')
                for k in new_paper:
                    if new_paper[k]:
                        total += 1
                print("Answer: {}".format(total))
                sys.exit()


            coords = new_paper
            print(coords)

        else:

            res = l.strip().split(',')
            #print(res)
            x = int(res[0])
            y = int(res[1])

            coords[(x,y)] = True

    total = 0
    print('-----')
    print(coords)
    for k in coords:
        if coords[k]:
            print(k)
            total += 1

    print("Answer: {}".format(total))

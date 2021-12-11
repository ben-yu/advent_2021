import numpy as np
import scipy.signal
import sys

with open('../inputs/day_11_input.txt') as f:
    lines = f.readlines()

    grid = []
    for l in lines:
        row = []
        for c in list(l.strip()):
            row.append(int(c))
        grid.append(row)

    grid = np.array(grid).astype(float)

    steps = 500
    diag_kernel = np.array([[1,0,1], [0,0,0], [1,0,1]])
    horiz_kernel = np.array([[0,1,0], [1,0,1], [0,1,0]])


    flash_count = 0
    flash_mask = np.where(grid > 9, 1, 0)

    for i in range(steps):
        # all increment by 1
        grid += 1
        new_flash_mask = np.where(grid > 9, 1, 0)

        # Keep flashes propogating until theres no more flashes
        while (new_flash_mask != flash_mask).any():
            # count flashes
            flash_count += np.sum(np.where(new_flash_mask > 0, 1, 0))
            horiz_mask = scipy.signal.convolve2d(new_flash_mask, horiz_kernel, mode='same')
            diag_mask = scipy.signal.convolve2d(new_flash_mask, diag_kernel, mode='same')
            sum_mask = horiz_mask + diag_mask
            # add flash amount
            grid = grid + sum_mask

            flash_mask = new_flash_mask
            # remove octopus that have already flashed
            grid = np.where(flash_mask > 0, -100, grid)
            # find next wave that flash triggered
            new_flash_mask = np.where(grid > 9, 1, 0)


        grid = np.where(grid < 0, 0, grid)
        # Part 2
        if np.sum(grid) == 0:
            print("Simul Flash: {}".format(i+1))
            sys.exit()

        print("After Step {}".format(i+1))
        print(grid)
        print('----------')

    print(flash_count)




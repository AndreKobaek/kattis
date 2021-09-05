from sys import stdin

input = stdin.readlines()
input = [x[:-1].split(" ") for x in input]
info = list()
for i in input:
    info += [int(x) for x in i]


def check_and_remove_drop_outs(positions, velocity, length):
    to_del = []
    for i, x in enumerate(positions):
        if x <= 0:
            to_del.append(i)
        else:
            break
    for i, x in enumerate(positions[::-1]):
        if x >= length:
            to_del.append(i)
        else:
            break
    for i in sorted(to_del, reverse=True):
        del positions[i]
        del velocity[i]

    return positions, velocity


def update_velocities(velocity, collisions):
    for i in collisions:
        velocity[i] = -1 * velocity[i]
        velocity[i + 1] = -1 * velocity[i + 1]
    return velocity


def time_for_next_collision(positions, velocities):
    time = 1_000_001
    collisions = []
    for i in range(len(velocities) - 1):
        if velocities[i] > velocities[i + 1]:
            dist_coll = (positions[i + 1] - positions[i]) / 2
            if dist_coll < time:
                time = dist_coll
                collisions = [i]
            elif dist_coll == time:
                collisions.append(i)
    return time, collisions


def no_more_collisions(velocity):
    for i in range(len(velocity) - 1):
        if velocity[i] > velocity[i + 1]:
            return False
    return True


def last_ant_out(positions, velocities, length):
    time_to_exit = [x if v < 0 else length - x for x, v in zip(positions, velocities)]
    return max(time_to_exit)


counter = 1
for i in range(info[0]):
    length = info[counter]
    counter += 2
    number_of_ants = info[counter - 1]
    positions = sorted(info[counter: counter + number_of_ants])
    counter += number_of_ants
    center = length / 2
    # best case
    position_from_center = [x - center for x in positions]
    slowest_best_ant = center - min([abs(x) for x in position_from_center])

    # worst case

    time = max(max([length - x for x in positions]), max(positions))

    # Apparently the above holds true and solves the problem with in the time limit,
    # which the code below didn't. But it was a much more comprehensive and interesting solution.

    # sim_positions = positions.copy()
    
    # sim_velocities = [-x/abs(x) for x in position_from_center]
    # time, collisions = time_for_next_collision(sim_positions, sim_velocities)
    # delta_time = time

    # while len(sim_positions) > 0:
    #     sim_positions = [x + y * delta_time for x, y in zip(sim_positions, sim_velocities)]
    #     sim_velocities = update_velocities(sim_velocities, collisions)
    #     sim_positions, sim_velocities = check_and_remove_drop_outs(sim_positions, sim_velocities, length)
    #     if len(sim_positions) == 0:
    #         break
  
    #     if no_more_collisions(sim_velocities):
    #         time += last_ant_out(sim_positions, sim_velocities, length)
    #         break

    #     delta_time, collisions = time_for_next_collision(sim_positions, sim_velocities)

    #     time += delta_time

    print(int(slowest_best_ant), int(time))

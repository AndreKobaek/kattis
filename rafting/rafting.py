from sys import stdin


def line_from_points(x, y):
    if x[0] == y[0]:
        return [x[0]]
    else:
        a = (y[1] - x[1]) / (y[0] - x[0])
        b = (y[0] * x[1] - x[0] * y[1]) / (y[0] - x[0])
        return [a, b]


def dist_to_line(line, z):
    if len(line) == 1:
        return abs(line[0] - z[0])
    else:
        return abs(line[0] * z[0] + line[1] - z[1]) / ((line[0] ** 2 + 1) ** 0.5)


def find_projection(line, x: int, y: int):
    if len(line) == 1:
        return [line[0], y]
    if line[0] == 0:
        return [x, line[1]]
    b = x / line[0] + y
    x_coord = (line[1] - b) / ((-line[0] ** -1) - line[0])
    y_coord = line[0] * x_coord + line[1]
    return [x_coord, y_coord]


def distance_to_point(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def within_points(x1: int, y1: int, x2: int, y2: int, point) -> bool:
    return min(x1, x2) <= point[0] and max(x1, x2) >= point[0] and min(y1, y2) <= point[1] and max(y1, y2) >= point[1]


def compare_polygons(inner, outer, min_distance) -> float:
    for i in range(0, len(inner) - 1):
        for j in range(0, len(outer)):
            min_distance = min(min_distance, distance_to_point(inner[i][0], inner[i][1], outer[j][0], outer[j][1]))
            line = line_from_points(inner[i], inner[i + 1])
            dist = dist_to_line(line, outer[j])
            if dist == min(dist, min_distance):
                point_on_line = find_projection(line, outer[j][0], outer[j][1])
                if within_points(inner[i][0], inner[i][1], inner[i + 1][0], inner[i + 1][1], point_on_line):
                    min_distance = dist
            #check line from end to start point
            if i == len(inner) - 2:
                min_distance = min(min_distance, distance_to_point(inner[i + 1][0], inner[i + 1][1], outer[j][0], outer[j][1]))
                line = line_from_points(inner[i + 1], inner[0])
                dist = dist_to_line(line, outer[j])
                if dist == min(dist, min_distance):
                    point_on_line = find_projection(line, outer[j][0], outer[j][1])
                    if within_points(inner[i + 1][0], inner[i + 1][1], inner[0][0], inner[0][1], point_on_line):
                        min_distance = dist
    return min_distance


for _ in range(int(stdin.readline())):
    min_distance = float('inf')
    polygons = [[] for _ in range(2)]
    for k in range(2):
        for j in range(int(stdin.readline())):
            polygons[k].append([int(x) for x in stdin.readline().split()])
    dist = min(compare_polygons(polygons[0], polygons[1], min_distance), compare_polygons(polygons[1], polygons[0], min_distance))
    print("{:.8}".format(dist/2.0))

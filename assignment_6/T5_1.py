import sys
import math


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    case_num = 0
    while idx < len(data):
        n = int(data[idx])
        d = int(data[idx + 1])
        idx += 2
        case_num += 1

        if n == 0 and d == 0:
            break

        islands = []
        max_y = 0
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx + 1])
            islands.append((x, y))
            if y > max_y:
                max_y = y
            idx += 2

        if max_y > d:
            print(f"Case {case_num}: -1")
            continue

        ranges = []
        for x, y in islands:
            offset = math.sqrt(d * d - y * y)
            ranges.append((x - offset, x + offset))

        # 通过.sort()使临近区间在一起，方便了后续邻两项间的判断
        ranges.sort(key=lambda item: item[1])

        ans = 1
        last_radar_pos = ranges[0][1]

        for i in range(1, n):
            l, r = ranges[i]
            if l > last_radar_pos:
                ans += 1
                last_radar_pos = r
        print(f"Case {case_num}: {ans}")


if __name__ == "__main__":
    main()

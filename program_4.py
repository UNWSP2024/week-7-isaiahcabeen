def distance(coord1, coord2):
    return ((coord2[0] - coord1[0]) ** 2 +
            (coord2[1] - coord1[1]) ** 2 +
            (coord2[2] - coord1[2]) ** 2) ** 0.5
def main():
    while True:
        try:
            x1, y1, z1 = map(float, input("Enter the first point as x1 y1 z1 (ex. 19 59 39): ").split())
            coord1 = (x1, y1, z1)

            x2, y2, z2 = map(float, input("Enter the second point as x2 y2 z2: ").split())
            coord2 = (x2, y2, z2)

            dist = distance(coord1, coord2)

            print(f"The distance between the points {coord1} and {coord2} is: {dist:.2f}")
            break

        except ValueError:
            print("Invalid input. Please enter three numbers for each point.")

if __name__ == '__main__':
    main()

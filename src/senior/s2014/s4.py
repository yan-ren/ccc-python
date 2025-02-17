"""
CCC 2014 Senior 4: Tinted Glass Window

NOTE: This solution is verified with CCC online grader with full marks,
however if testing on dmoj, two tests will fail with TLE

The problem requires calculating the total area of a window that has a tint level
equal to or exceeding a specified threshold. The window is composed of multiple
rectangular tinted panels, each contributing to the overall tint level in their
covered area. Overlapping panels have additive tint effects.

Approach:
1. Line Sweeping: This technique involves "sweeping" a vertical line from left to
   right across the window. As the sweep line encounters the left and right edges
   of rectangles, it updates the tint levels of affected horizontal segments.

2. Axis Compression: Since the problem deals with discrete rectangles, we compress
   the y-axis into horizontal segments formed by the top and bottom edges of these
   rectangles. This reduces the problem space and simplifies calculations.

3. Vertical and Horizontal Segments:
   - Vertical Lines: Represented by the left and right edges of rectangles. Each
     vertical line is associated with the y-coordinates it spans and a tint factor
     (positive for entering/left edges, negative for exiting/right edges).
   - Horizontal Segments: Formed by compressing the y-axis using the top and bottom
     edges of all rectangles. These segments represent distinct vertical slices of
     the window.

4. Calculating the Area:
   - As we sweep across the window, we update the tint levels of horizontal segments
     affected by the current vertical line.
   - After updating tint levels, we calculate the area of segments with a tint level
     at or above the threshold. This is done by multiplying the height of each
     qualifying segment by the width of the current column (the distance between the
     current vertical line and the next).

5. Result: The sum of areas calculated for each column of segments gives the total
   area of the window with the desired tint level.

Key Concepts:
- Line Sweeping: Efficiently processes geometric information by moving through the
  space in a systematic manner.
- Axis Compression: Reduces the complexity of geometric problems by minimizing the
  number of segments or points to consider.
- Event Sorting: By sorting vertical lines (events), we ensure that updates and
  calculations are performed in the correct order.
"""

N = int(input())
T = int(input())

vertical_lines = []
temp_horizontal_segments = set()

for _ in range(N):
    x1, y1, x2, y2, t = map(int, input().split())
    vertical_lines.append((x1, y1, y2, t))  # Incoming side
    vertical_lines.append((x2, y1, y2, -t))  # Outgoing side, with negative tint factor
    temp_horizontal_segments.add(y1)
    temp_horizontal_segments.add(y2)

horizontal_segments = sorted(temp_horizontal_segments)
vertical_lines.sort()  # Sort vertical lines by their x-coordinate

y_coord_to_line_num = {y: i for i, y in enumerate(horizontal_segments)}

compressed_yaxis = [0] * (len(horizontal_segments) - 1)

good_area = 0

for i in range(len(vertical_lines) - 1):
    x, y1, y2, t = vertical_lines[i]
    # Update all horizontal segments that it affects
    for j in range(y_coord_to_line_num[y1], y_coord_to_line_num[y2]):
        compressed_yaxis[j] += t
    # For each horizontal block
    for j in range(len(compressed_yaxis)):
        # If the tint factor is high enough
        if compressed_yaxis[j] >= T:
            # Add the area, height * width
            good_area += abs(horizontal_segments[j] - horizontal_segments[j + 1]) * abs(x - vertical_lines[i + 1][0])

print(good_area)

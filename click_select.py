import os.path
import cv2

SELECTION_COLOUR = (222, 0, 222)
WINDOW_NAME = "Select regions with a mouse"

x = 0
path = "./files/selection" + str(x) + ".png"
while os.path.exists(path):
    x = x+1
    path = "./files/selection" + str(x) + ".png"

OUTPUT_FILE = path


def click_select(event, x, y, flags, data):
    image, points = data
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        cv2.rectangle(image, points[-2], points[-1], SELECTION_COLOUR, 2)
        cv2.imshow(WINDOW_NAME, image)


def show_mouse_select(image_filename):
    orig = cv2.imread(image_filename)
    image = orig.copy()
    cv2.namedWindow(WINDOW_NAME)

    points = []
    cv2.setMouseCallback(WINDOW_NAME, click_select, (image, points))

    while True:
        cv2.imshow(WINDOW_NAME, image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break       # press q to exit

    # Output points and save image
    if len(points) > 1:
        print("Points:")
        for i in range(0, len(points), 2):
            a, b = points[i], points[i+1]
            s = str((min(a, b), max(a, b)))
            s = s.replace('(', '')
            s = s.replace(')', '')
            print('<area class="area" shape="rect" coords="', s,
                  '" alt="placeholder" onclick="openInfo(\'Standrohr\')">')

        cv2.imwrite(OUTPUT_FILE, image)
        print("Saved to:", OUTPUT_FILE)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    from sys import argv
    show_mouse_select(argv[1])

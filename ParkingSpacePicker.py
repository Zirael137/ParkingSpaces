import cv2
import pickle #нужен для того, чтобы сохранить позиции парковочных мест

try: # если файл такой есть, то забираем его данные в posList, если же такого файла нет, то создаем новый posList.
    # это нужно для того, чтобы при каждом новом запуске сразу же загружались прошлая версия выделений.
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
width, height = 107, 48


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    # чтобы сохранять то, что нарисовали wb - read and write    dump - сваливать
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f) # сваливаем posList в файл f

while True:
    img = cv2.imread('carParkImg.png')  # считываем изображени
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick) # первым аргументом передаем название изображения, по которому клацаем,
    # а вторым параметром передаем функцию, которая будет вызываться, когда мы кликаем по чему-либо
    cv2.waitKey(1)
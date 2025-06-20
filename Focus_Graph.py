import matplotlib.pyplot as pt


def focus_graph():
    file = open("Focus.txt", "r")
    content = file.read()
    file.close()

    content = content.split(",")
    x1 = []
    for i in range(0,len(content)):
        content[i] = float(content[i])
        x1.append(i)

    print(content)
    y1 = content

    pt.plot(x1, y1, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=5)
    pt.title('Focus Graph')
    pt.xlabel('Days')
    pt.ylabel('Focus Time (in hours)')
    pt.show()
    pt.grid()
import cv2
class minRect():
    def __init__(self,idx,rotbox):
        self.idx = idx
        self.center = (int(rotbox[0][0]),int(rotbox[0][1]))
        points = cv2.boxPoints(rotbox)
        width,height = rotbox[1]
        if width < height:
            if rotbox[2] == -90:
                angle = 90
            else:
                angle = -rotbox[2] + 90
        else:
            if rotbox[2] == -90:
                angle = 0
            else:
                angle = -rotbox[2]
        self.points = points
        self.width = min(width,height)
        self.length = max(width,height)
        self.angle = angle
        self.area = self.width * self.length
        self.rotbox = rotbox


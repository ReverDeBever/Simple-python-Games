import pyxel

class App:
    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0

        self.cubeX = 10
        self.cubeY = 10
        self.cubeSize = 30
        self.cubeVX = 0
        self.cubeVY = 0
        self.cubePrevX = self.cubeX
        self.cubePrevY = self.cubeY


        self.dragOffsetX = 0
        self.dragOffsetY = 0
        self.dragging = False

        pyxel.init(160, 120, fps=120)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.mouseX = pyxel.mouse_x
        self.mouseY = pyxel.mouse_y

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.cubeX <= self.mouseX <= self.cubeX + self.cubeSize and self.cubeY <= self.mouseY <= self.cubeY + self.cubeSize:
                self.dragging = True
                self.dragOffsetX = self.mouseX - self.cubeX
                self.dragOffsetY = self.mouseY - self.cubeY

        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.dragging = False

        if self.dragging:
            self.cubeX = self.mouseX - self.dragOffsetX
            self.cubeY = self.mouseY - self.dragOffsetY

        dx = self.cubeX - self.cubePrevX
        dy = self.cubeY - self.cubePrevY
        dt = 1 / 120
        self.cubeVX = dx / dt
        self.cubeVY = dy / dt

        self.cubePrevX = self.cubeX
        self.cubePrevY = self.cubeY

    def draw(self):
        pyxel.cls(1)
        pyxel.rect(self.cubeX, self.cubeY, self.cubeSize, self.cubeSize, 8)
        pyxel.text(5, 5, f"Velocity: ({self.cubeVX:.1f}, {self.cubeVY:.1f})", 7)

App()

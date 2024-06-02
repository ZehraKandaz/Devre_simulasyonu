import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QGraphicsTextItem, QGraphicsRectItem, QLineEdit, QGraphicsEllipseItem, QMenu, QAction, QMessageBox, QGraphicsSceneContextMenuEvent
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QPointF

class CircuitElement(QGraphicsPixmapItem):
    def __init__(self, pixmap, label):
        super().__init__(pixmap)
        self.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.setFlag(QGraphicsPixmapItem.ItemIsSelectable)
        self.label = label
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.PointingHandCursor)
        
    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        contextMenu = QMenu()
        showLabelAction = QAction("Label", contextMenu)
        showLabelAction.triggered.connect(self.showName)
        contextMenu.addAction(showLabelAction)

        showConnectionsAction = QAction("Connections", contextMenu)
        showConnectionsAction.triggered.connect(self.showConnections)
        contextMenu.addAction(showConnectionsAction)

        contextMenu.exec_(event.screenPos())

    def showName(self):
        QMessageBox.information(None, "Label", f"Label: {self.label}")
    
    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 2")

class ANDGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = self.input1 and self.input2
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class ORGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = self.input1 or self.input2
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class NANDGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = not (self.input1 and self.input2)
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class NORGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = not (self.input1 or self.input2)
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class XORGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = self.input1 != self.input2
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class XNORGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input1 = None
        self.input2 = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input1 is not None and self.input2 is not None:
            self.output = self.input1 == self.input2
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))

class NOTGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInput(self, input_value):
        self.input = input_value
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input is not None:
            self.output = not self.input
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))
    
    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 1")

class BufferGate(CircuitElement):
    def __init__(self, pixmap, label):
        super().__init__(pixmap, label)
        self.input = None
        self.output = None
        self.output_box = None
        self.led = None

    def setInput(self, input_value):
        self.input = input_value
        self.updateOutput()

    def setLED(self, led):
        self.led = led

    def updateOutput(self):
        if self.input is not None:
            self.output = self.input
            if self.output_box:
                self.output_box.setValue(self.output)
            if self.led:
                self.led.setState(self.output)

    def showOutput(self):
        if self.output_box:
            self.output_box.setText(str(int(self.output)))
    
    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 1")


class InputBox(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        self.setBrush(Qt.white)

        self.text_item = QGraphicsTextItem("0", self)
        self.text_item.setDefaultTextColor(Qt.black)
        self.text_item.setPos(x + 5, y + 5)

    def mouseDoubleClickEvent(self, event):
        self.editText()

    def editText(self):
        self.text_edit = QLineEdit()
        self.text_edit.setText(self.text_item.toPlainText())
        self.text_edit.setGeometry(self.scene().views()[0].mapToGlobal(self.pos().toPoint()).x() + 5,
                                   self.scene().views()[0].mapToGlobal(self.pos().toPoint()).y() + 5,
                                   30, 20)
        self.text_edit.editingFinished.connect(self.finishEditing)
        self.scene().views()[0].parentWidget().layout().addWidget(self.text_edit)
        self.text_edit.show()
        self.text_edit.setFocus()

    def finishEditing(self):
        new_text = self.text_edit.text()
        if new_text in ['0', '1']:
            self.text_item.setPlainText(new_text)
        self.text_edit.deleteLater()
        self.text_edit = None

    def getValue(self):
        return int(self.text_item.toPlainText())
    
    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        contextMenu = QMenu()
        showLabelAction = QAction("Label", contextMenu)
        showLabelAction.triggered.connect(self.showName)
        contextMenu.addAction(showLabelAction)

        showConnectionsAction = QAction("Connections", contextMenu)
        showConnectionsAction.triggered.connect(self.showConnections)
        contextMenu.addAction(showConnectionsAction)

        contextMenu.exec_(event.screenPos())

    def showName(self):
        QMessageBox.information(None, "Label", "Label: Giris Kutusu")

    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 1")

class OutputBox(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        self.setBrush(Qt.yellow)

        self.text_item = QGraphicsTextItem("Output", self)
        self.text_item.setDefaultTextColor(Qt.black)
        self.text_item.setPos(x + 5, y + 5)

    def setText(self, text):
        self.text_item.setPlainText(text)

    def setValue(self, value):
        self.value = value

    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        contextMenu = QMenu()
        showLabelAction = QAction("Label", contextMenu)
        showLabelAction.triggered.connect(self.showName)
        contextMenu.addAction(showLabelAction)

        showConnectionsAction = QAction("Connections", contextMenu)
        showConnectionsAction.triggered.connect(self.showConnections)
        contextMenu.addAction(showConnectionsAction)

        contextMenu.exec_(event.screenPos())

    def showName(self):
        QMessageBox.information(None, "Label", "Label: Cikis Kutusu")

    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 1")

class LED(QGraphicsEllipseItem):
    def __init__(self, x, y, diameter):
        super().__init__(x, y, diameter, diameter)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setBrush(Qt.red)
        self.state = False

    def setState(self, state):
        self.state = state
        if state:
            self.setBrush(Qt.green)
        else:
            self.setBrush(Qt.red)
        
    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        contextMenu = QMenu()
        showLabelAction = QAction("Label", contextMenu)
        showLabelAction.triggered.connect(self.showName)
        contextMenu.addAction(showLabelAction)

        showConnectionsAction = QAction("Connections", contextMenu)
        showConnectionsAction.triggered.connect(self.showConnections)
        contextMenu.addAction(showConnectionsAction)

        showColorAction = QAction("Color", contextMenu)
        showColorAction.triggered.connect(self.showColor)
        contextMenu.addAction(showColorAction)

        contextMenu.exec_(event.screenPos())

    def showName(self):
        QMessageBox.information(None, "Label", "Label: LED")
    
    def showConnections(self):
        QMessageBox.information(None, "Connections", "Connections: 1")

    def showColor(self):
        if self.state:
            QMessageBox.information(None, "Color", "Color: Green")
        else:
            QMessageBox.information(None, "Color", "Color: Red")

class CircuitSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Circuit Simulator'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()
        self.led = None

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()

        button_layout = QHBoxLayout()

        # Devre tuvali
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        elements = [
            ('AND', 'andGate.png'),
            ('BUFFER', 'buffer.png'),
            ('NAND', 'nandGate.png'),
            ('NOR', 'norGate.png'),
            ('NOT', 'notGate.png'),
            ('OR', 'orGate.png'),
            ('XNOR', 'xnorGate.png'),
            ('XOR', 'xorGate.png'),
            ('Giris Kutusu', 'girisKutusu.png'),
            ('Cikis Kutusu', 'cikisKutusu.png'),
            ('LED', 'LED.png'),
            ('Cizgi Cizme', 'cizgiCizme.png'),
            ('Baglanti Dugumu', 'baglantiDugumu.png'),
            ('Calistir', 'calistir.png'),
            ('Reset', 'reset.png'),
            ('Durdur', 'durdur.png')
        ]

        for label, icon_path in elements:
            button = QPushButton(label, self)
            button.setIcon(QIcon(icon_path))
            if label == 'Calistir':
                button.clicked.connect(self.runSimulation)
            elif label == 'Reset':
                button.clicked.connect(self.reset)
            else:
                button.clicked.connect(lambda checked, l=label, ip=icon_path: self.addElement(l, ip))
            button_layout.addWidget(button)

        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.show()

    def addElement(self, label, icon_path):
        if label == 'Giris Kutusu':
            element = InputBox(0, 0, 30, 30)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'Cikis Kutusu':
            element = OutputBox(0, 0, 60, 30)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'LED':
            self.led = LED(0, 0, 30)
            self.scene.addItem(self.led)
            self.led.setPos(QPointF(0, 0))
        elif label == 'AND':
            pixmap = QPixmap(icon_path)
            element = ANDGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'OR':
            pixmap = QPixmap(icon_path)
            element = ORGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'NAND':
            pixmap = QPixmap(icon_path)
            element = NANDGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'NOR':
            pixmap = QPixmap(icon_path)
            element = NORGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'XOR':
            pixmap = QPixmap(icon_path)
            element = XORGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))

        elif label == 'XNOR':
            pixmap = QPixmap(icon_path)
            element = XNORGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))

        elif label == 'NOT':
            pixmap = QPixmap(icon_path)
            element = NOTGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))
        elif label == 'BUFFER':
            pixmap = QPixmap(icon_path)
            element = BufferGate(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))


        else:
            pixmap = QPixmap(icon_path)
            element = CircuitElement(pixmap, label)
            self.scene.addItem(element)
            element.setPos(QPointF(0, 0))

    def reset(self):
        self.scene.clear()
        self.led = None

    def runSimulation(self):
        input_boxes = [item for item in self.scene.items() if isinstance(item, InputBox)]
        and_gates = [item for item in self.scene.items() if isinstance(item, ANDGate)]
        output_boxes = [item for item in self.scene.items() if isinstance(item, OutputBox)]
        or_gates = [item for item in self.scene.items() if isinstance(item, ORGate)]
        nand_gates = [item for item in self.scene.items() if isinstance(item, NANDGate)]
        nor_gates = [item for item in self.scene.items() if isinstance(item, NORGate)]
        xor_gates = [item for item in self.scene.items() if isinstance(item, XORGate)]
        xnor_gates = [item for item in self.scene.items() if isinstance(item, XNORGate)]
        not_gates = [item for item in self.scene.items() if isinstance(item, NOTGate)]
        buffer_gates = [item for item in self.scene.items() if isinstance(item, BufferGate)]

        if len(input_boxes) >= 2 and len(and_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            and_gate = and_gates[0]
            and_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                and_gate.output_box = output_boxes[0]
            if self.led:
                and_gate.setLED(self.led)
            and_gate.showOutput()

        if len(input_boxes) >= 2 and len(or_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            or_gate = or_gates[0]
            or_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                or_gate.output_box = output_boxes[0]
            if self.led:
                or_gate.setLED(self.led)
            or_gate.showOutput()

        if len(input_boxes) >= 2 and len(nand_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            nand_gate = nand_gates[0]
            nand_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                nand_gate.output_box = output_boxes[0]
            if self.led:
                nand_gate.setLED(self.led)
            nand_gate.showOutput()

        if len(input_boxes) >= 2 and len(nor_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            nor_gate = nor_gates[0]
            nor_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                nor_gate.output_box = output_boxes[0]
            if self.led:
                nor_gate.setLED(self.led)
            nor_gate.showOutput()

        if len(input_boxes) >= 2 and len(xor_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            xor_gate = xor_gates[0]
            xor_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                xor_gate.output_box = output_boxes[0]
            if self.led:
                xor_gate.setLED(self.led)
            xor_gate.showOutput()

        if len(input_boxes) >= 2 and len(xnor_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            input2 = bool(input_boxes[1].getValue())
            xnor_gate = xnor_gates[0]
            xnor_gate.setInputs(input1, input2)
            if len(output_boxes) >= 1:
                xnor_gate.output_box = output_boxes[0]
            if self.led:
                xnor_gate.setLED(self.led)
            xnor_gate.showOutput()

        if len(input_boxes) >= 1 and len(not_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            not_gate = not_gates[0]
            not_gate.setInput(input1)
            if len(output_boxes) >= 1:
                not_gate.output_box = output_boxes[0]
            if self.led:
                not_gate.setLED(self.led)
            not_gate.showOutput()

        if len(input_boxes) >= 1 and len(buffer_gates) >= 1:
            input1 = bool(input_boxes[0].getValue())
            buffer_gate = buffer_gates[0]
            buffer_gate.setInput(input1)
            if len(output_boxes) >= 1:
                buffer_gate.output_box = output_boxes[0]
            if self.led:
                buffer_gate.setLED(self.led)
            buffer_gate.showOutput()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircuitSimulator()
    sys.exit(app.exec_())

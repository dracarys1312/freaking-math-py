import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QComboBox, QWidget, QHBoxLayout, QLabel, QLineEdit, QFormLayout

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)


class LayoutExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width.
        QWidget.__init__(self)
        self.setWindowTitle('Basic Calculator')
        self.setMinimumWidth(400)

        # Create the QVBoxLayout that lays out the whole form
        self.layout = QVBoxLayout()

        # Create the form layout that manages the labeled controls
        self.form_layout = QFormLayout()

        # self.salutations = ['Ahoy',
        #                     'Good day',
        #                     'Hello',
        #                     'Heyo',
        #                     'Hi',
        #                     'Salutations',
        #                     'Wassup',
        #                     'Yo']
        #
        # # Create and fill the combo box to choose the salutation
        # self.salutation = QComboBox(self)
        # self.salutation.addItems(self.salutations)
        # # Add it to the form layout with a label
        # self.form_layout.addRow('&Salutation:', self.salutation)

        # Create the entry control to specify a
        # num2 and set its placeholder text
        self.num1 = QLineEdit(self)

        # Add it to the form layout with a label
        self.form_layout.addRow('&Number 1:', self.num1)

        self.num2 = QLineEdit(self)

        # Add it to the form layout with a label
        self.form_layout.addRow('&Number 2:', self.num2)

        # Create and add the label to show the greeting text
        self.result = QLabel('', self)
        self.form_layout.addRow('Result:', self.result)

        # Cdd the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)

        # Create a horizontal box layout to hold the button
        self.button_box = QHBoxLayout()

        # Add stretch to push the button to the far right
        self.button_box.addStretch(1)

        # Create the build button with its caption
        self.build_button = QPushButton('&Calculate', self)

        # Connect the button's clicked signal to show_greeting
        self.build_button.clicked.connect(self.show_add)

        # Add it to the button box
        self.button_box.addWidget(self.build_button)

        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)

    def show_add(self):
        self.result.setText('%s + %s' %
                              (self.num1.text(),
                               self.num2.text()))

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()


# Create an instance of the application window and run it
app = LayoutExample()
app.run()
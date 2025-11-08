"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.5"
__credits__ = "Mark Batac"

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem

from PySide6.QtCore import Slot

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()      

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
   
    @Slot()
    def __on_add_contact(self):
        """Slot that handles the Add Contact button click event."""
        name = self.contact_name_input.text()
        phone = self.phone_input.text()

        # Validate input (both fields must be filled)
        if len(name.strip()) == 0 or len(phone.strip()) == 0:
            self.status_label.setText("Please enter a contact name and phone number.")
            return

        # Determine the new row position at the end of the table
        row_position = self.contact_table.rowCount()
        self.contact_table.insertRow(row_position)

        # Add name and phone as items in the new row
        self.contact_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.contact_table.setItem(row_position, 1, QTableWidgetItem(phone))

        # Provide success feedback
        self.status_label.setText(f"Added contact: {name}")
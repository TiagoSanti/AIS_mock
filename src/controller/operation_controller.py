from src.view.operation_viewer import Ui_OperationMetadataViewer
from PySide6.QtWidgets import QMainWindow
from src.service.operation_service import OperationService
from src.service.operator_service import OperatorService
from src.model.operation import Operation
from PySide6.QtWidgets import QMainWindow, QFrame, QTableWidgetItem, QHeaderView, QSizePolicy
from src.view.form_metadata import Ui_dynamic_form_metadata
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os
import sys


class OperationController(QMainWindow, Ui_OperationMetadataViewer):
    def __init__(self):
        super(OperationController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Operations")
        self.operation_service = OperationService()
        self.load_operations()
        self.get_operation_values()
        self.imagel_label.setPixmap(self.set_image())
        self.new_operationbtn.clicked.connect(self.new_operation)
        self.edit_operationbtn.clicked.connect(self.edit_operation)
        self.static_dropdown.currentIndexChanged.connect(
            self.populate_static_table)
        self.static_dropdown.currentIndexChanged.connect(
            self.populate_dynamic_table)
        self.delete_btn.clicked.connect(self.delete_operation)
        self.btn_add_dynamic.clicked.connect(self.add_dynamic_field)
        self.btn_remove_dynamic.clicked.connect(self.remove_dynamic_field)
        self.discard_changes_btn.clicked.connect(
            self.discard_return_to_pre_changes)

    def set_image(self):
        pixmap = QPixmap("./src/view/resources/images/operation.png")
        if not pixmap.isNull():
            return pixmap.scaled(210, 210, aspectMode=Qt.KeepAspectRatio)

    def new_operation(self):
        self.new_operation_form = QFrame()
        self.ui_new = Ui_dynamic_form_metadata()
        self.ui_new.setupUi(self.new_operation_form)
        self.new_operation_form.show()
        self.populate_new_operation_fields()
        self.ui_new.btn_add_dynamic.hide()
        self.ui_new.btn_save_changes.text = "Create Operation"
        self.ui_new.btn_save_changes.clicked.connect(self.create_new_operation)
        self.ui_new.btn_discard.clicked.connect(self.new_operation_form.close)

    def get_operation_path(self):
        return os.path.join(os.getcwd(), "operations")

    def populate_new_operation_fields(self):
        self.ui_new.add_text_line_edit("Name", "OperationName")
        self.ui_new.add_static_label("Folder Path", self.get_operation_path())
        self.ui_new.add_text_combobox("Operator", self.get_operator_names())

    def get_operator_names(self):
        operator_service = OperatorService()
        operators = operator_service.get_metadata_values("name")
        return operators

    def turn_Operator_name_into_id(self, operator_name):
        operator_service = OperatorService()
        operator = operator_service.get_by_metadatas({"name": operator_name})
        for operator in operator:
            return operator["_id"]

    def create_new_operation(self):
        input_values = self.ui_new.get_input_values()
        operation_complete_path = os.path.join(
            self.get_operation_path(), input_values[0])
        operator_id = self.turn_Operator_name_into_id(input_values[2])
        operation = Operation(
            name=input_values[0], folder_path=operation_complete_path, operator_id=operator_id, metadata={})
        self.operation_service.create_document(operation)
        self.load_operations()
        self.static_dropdown.setCurrentText(input_values[0])
        self.new_operation_form.close()

    def edit_operation(self):
        self.edit_operation_form = QFrame()
        self.ui_edit = Ui_dynamic_form_metadata()
        self.ui_edit.setupUi(self.edit_operation_form)
        self.edit_operation_form.show()
        self.populate_edit_operation_fields()
        self.ui_edit.btn_add_dynamic.hide()
        self.ui_edit.btn_save_changes.clicked.connect(self.save_changes)
        self.ui_edit.btn_discard.clicked.connect(
            self.edit_operation_form.close)

    def populate_edit_operation_fields(self):
        operator_service = OperatorService()
        static_dict = self.get_static_dict()
        dynamic_dict = self.get_dynamic_dict()
        operator_name = operator_service.get_by_id(
            static_dict["operator_id"])["name"]
        static_dict["operator_id"] = operator_name + \
            " (ID: " + static_dict["operator_id"] + ")"
        for key, value in static_dict.items():
            self.ui_edit.add_static_label(str(key), str(value))
        for key, value in dynamic_dict.items():
            self.ui_edit.add_text_line_edit(str(key), str(value))

    def save_changes(self):
        operation = self.get_operation_values()
        edited_dict = self.ui_edit.get_edit_dict()
        for key, value in edited_dict.items():
            operation["metadata"][key] = value
        self.operation_service.update_document(operation["_id"], operation)
        self.load_operations()
        self.static_dropdown.setCurrentText(operation["name"])
        self.edit_operation_form.close()

    def load_operations(self):
        operations = self.operation_service.get_metadata_values("name")
        self.static_dropdown.clear()
        self.static_dropdown.addItems(operations)
        self.static_dropdown.setCurrentIndex(0)
        self.static_dropdown.setCurrentText("Select Operation")
        self.populate_static_table()
        self.populate_dynamic_table()

    def get_operation_values(self):
        operation_name = self.static_dropdown.currentText()
        operationscursor = self.operation_service.get_by_metadatas(
            {"name": operation_name})
        for operation in operationscursor:
            return dict(operation)
        return {"name": "Example Operation", "folder_path": "/path/to/example", "operator_id": "example_operator_id", "metadata": {"example_key": "example_value"}}

    def get_static_dict(self):
        operation = self.get_operation_values()
        operation.pop("metadata", None)
        return operation

    def get_dynamic_dict(self):
        operation = self.get_operation_values()
        metadata = operation["metadata"]
        return metadata

    def populate_static_table(self):
        operation = self.get_static_dict()
        self.static_table.setRowCount(len(operation))
        self.static_table.setColumnCount(2)
        self.static_table.setHorizontalHeaderLabels(["Key", "Value"])
        self.static_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, (key, value) in enumerate(operation.items()):
            self.static_table.setItem(i, 0, QTableWidgetItem(key))
            self.static_table.setItem(i, 1, QTableWidgetItem(str(value)))
        self.static_table.resizeColumnsToContents()
        self.static_table.resizeRowsToContents()
        self.static_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.static_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def populate_dynamic_table(self):
        operation = self.get_operation_values()
        if "metadata" in operation:
            metadata = operation["metadata"]
            self.dynamic_table.setRowCount(len(metadata))
            self.dynamic_table.setColumnCount(2)
            self.dynamic_table.setHorizontalHeaderLabels(["Key", "Value"])
            self.dynamic_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            for i, (key, value) in enumerate(metadata.items()):
                self.dynamic_table.setItem(i, 0, QTableWidgetItem(key))
                self.dynamic_table.setItem(i, 1, QTableWidgetItem(value))
            self.static_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.static_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.dynamic_table.clear()
            self.dynamic_table.setHorizontalHeaderLabels(["Key", "Value"])
            self.dynamic_table.setRowCount(0)
            self.dynamic_table.setColumnCount(0)
            self.dynamic_table.setHorizontalHeaderLabels(["Key", "Value"])
            self.static_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.static_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def delete_operation(self):
        operation = self.get_static_dict()
        self.operation_service.delete_document(operation["_id"])
        self.load_operations()
        self.static_dropdown.setCurrentText("Select Operation")

    def add_dynamic_field(self):
        self.new_dynamic_field = QFrame()
        self.ui_new_dynamic = Ui_dynamic_form_metadata()
        self.ui_new_dynamic.setupUi(self.new_dynamic_field)
        self.new_dynamic_field.show()
        self.new_dynamic_field.setWindowTitle("Add Dynamic Fields")
        self.ui_new_dynamic.btn_save_changes.text = "Add Field"
        self.ui_new_dynamic.set_metadata_values(
            OperationService().get_all_metadata_dict_keys())
        self.ui_new_dynamic.add_editable_combobox_text()
        self.ui_new_dynamic.btn_save_changes.clicked.connect(
            self.save_dynamic_field)
        self.ui_new_dynamic.btn_discard.clicked.connect(
            self.new_dynamic_field.close)

    def dynamic_fields_pre_changes(self):
        operation = self.get_operation_values()
        metadata = operation["metadata"]
        return metadata

    def save_dynamic_field(self):
        operation = self.get_operation_values()
        metadata = operation["metadata"]
        input_values = self.ui_new_dynamic.transform_input_values_metadata_to_dict()
        for key, value in input_values.items():
            metadata[key] = value
        self.operation_service.update_document(operation["_id"], operation)
        self.populate_dynamic_table()

    def remove_dynamic_field(self):
        operation = self.get_operation_values()
        metadata = operation["metadata"]
        selected_rows = self.dynamic_table.selectionModel().selectedRows()
        for row in selected_rows:
            key = self.dynamic_table.item(row.row(), 0).text()
            metadata.pop(key)
        self.operation_service.update_document(operation["_id"], operation)
        self.populate_dynamic_table()

    def discard_return_to_pre_changes(self):
        self.load_operations()
        self.static_dropdown.setCurrentText(self.static_dropdown.currentText())
        self.populate_static_table()
        self.populate_dynamic_table()
        self.close()

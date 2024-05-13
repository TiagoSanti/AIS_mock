import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from PySide6.QtCore import QCoreApplication, Qt
from src.view.start_deploy_window import Ui_start_deploy_window
from src.service.operation_service import OperationService
from src.service.deployment_service import DeploymentService
from src.service.operator_service import OperatorService
from src.controller.operation_controller import OperationController
from src.controller.operations_view_window_controller import start_operation_window
from src.view.operation_views_window import Ui_MainWindow
from src.model.deployment import Deployment
from bson import ObjectId
from datetime import datetime
import datetime


class DeployController(QMainWindow, Ui_start_deploy_window):
    def __init__(self):
        super(DeployController, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Online Evidence Grabber")
        self.operation_service = OperationService()
        self.deployment_service = DeploymentService()
        self.operator_service = OperatorService()
        self.load_operations()
        self.load_operators()
        self.operationPlus_btn.clicked.connect(self.create_operation)
        self.bnt_Start_Deploy.clicked.connect(self.start_deployment)
        self.personnaPlus_btn.clicked.connect(self.open_operation_views_window)

    def load_operations(self):
        operations = self.operation_service.get_metadata_values("name")
        self.operation_drop.addItems(operations)

    def load_operators(self):
        operators = self.operator_service.get_metadata_values("name")
        self.operator_drop.addItems(operators)

    def get_operation_values(self):
        operation_name = self.operation_drop.currentText()
        operationscursor = self.operation_service.get_by_metadatas(
            {"name": operation_name})
        for operation in operationscursor:
            return dict(operation)

    def get_operator_values(self):
        operator_name = self.operator_drop.currentText()
        operatorscursor = self.operator_service.get_by_metadatas(
            {"name": operator_name})
        for operator in operatorscursor:
            return dict(operator)

    def start_deployment(self):
        operation = self.get_operation_values()
        operator = self.get_operator_values()
        self.create_deploy_path()

        deployment = Deployment(
            title=self.generate_title(),
            operation_id=operation["_id"],
            hash_list="hash_list",
            hash_list_hash="hash_list_hash",
            is_closed=False,
            record_path=self.create_deploy_path(),
            agent_name=self.operator_drop.currentText(),
            metadata={"operator_id": operator["_id"]}
        )
        DeploymentService().create_document(deployment)

    def create_deploy_path(self):
        operation = self.get_operation_values()
        deploy_title = self.generate_title()
        path = f"{operation['folder_path']}/{deploy_title}/evidences/"
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def generate_title(self):
        return f"{self.operator_drop.currentText()}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

    def create_operation(self):
        self.operation_controller = OperationController()
        self.operation_controller.show()
        self.operation_controller.savechanges_btn.clicked.connect(
            self.refresh_ui)

    def refresh_ui(self):
        self.operation_controller.close()
        self.operation_drop.clear()
        self.load_operations()
        self.operation_controller = None

    def open_operation_views_window(self):
        self.operation_views_window = start_operation_window()
        self.operation_views_window.show()

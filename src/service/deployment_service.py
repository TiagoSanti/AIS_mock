from src.service.base_service import BaseService

class DeploymentService(BaseService):
    def __init__(self):
        super().__init__(collection_name='deployments')
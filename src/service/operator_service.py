from src.service.base_service import BaseService

class OperatorService(BaseService):
    def __init__(self) -> None:
        super().__init__(collection_name="operators")
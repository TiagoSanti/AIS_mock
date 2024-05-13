from src.service.base_service import BaseService

class BookmarkService(BaseService):
    def __init__(self):
        super().__init__(collection_name='bookmarks')

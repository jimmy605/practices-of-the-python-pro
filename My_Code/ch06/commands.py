import sys 
from data_base import DataBaseManager
from datetime import datetime

db = DataBaseManager('bookmarks.db')

class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null'
        })
    
class AddBookmarkCommand:
    def execute(self, data):
        data['data_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmarks added!'

class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by
    
    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()

class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted!'

class QuitCommand:
    def execute(self):
        sys.exit()
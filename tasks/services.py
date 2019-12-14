class TaskService(object):
    def delete_item(self, item_id):
        return item_id

    def add_item(self, item_obj):
        return {'id': item_obj.id, 'description': item_obj.description, 'name': item_obj.name}

    def update_item(self, item_id):
        return item_id

    def get_item(self, item_id):
        return item_id
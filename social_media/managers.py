from django.db import models

class ItemManager(models.Manager):
    def get_items_by_type(self, item_type):
        return self.filter(type=item_type)
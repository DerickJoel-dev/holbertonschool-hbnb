#!/usr/bin/python3

class InMemoryRepository:
    def __init__(self):
        self.storage = {}

    def add(self, obj):
        """Adds an object to the storage."""
        self.storage[obj.id] = obj
        print(f"DEBUG: Added object with ID {obj.id}")

    def get_all(self):
        """Returns all objects stored."""
        print("DEBUG: get_all() called, storage:", self.storage)
        return list(self.storage.values())

    def get(self, obj_id):
        """Retrieves an object by its ID."""
        return self.storage.get(obj_id)

    def update(self, obj_id, obj):
        """Updates an existing object in the storage."""
        if obj_id in self.storage:
            self.storage[obj_id] = obj
            print(f"DEBUG: Updated object with ID {obj_id}")
            return obj
        return None

    def delete(self, obj_id):
        """Deletes an object from the storage if it exists."""
        if obj_id in self.storage:
            del self.storage[obj_id]
            print(f"DEBUG: Deleted object with ID {obj_id}")
            return True
        print(f"DEBUG: Object with ID {obj_id} not found")
        return False

# Create global repository instances
user_repo = InMemoryRepository()
amenity_repo = InMemoryRepository()
place_repo = InMemoryRepository()
review_repo = InMemoryRepository()
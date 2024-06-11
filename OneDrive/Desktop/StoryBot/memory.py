from typing import Optional


class LongTermMemory:
    """
    Class to handle long-term memory for the StoryBot.
    """

    def __init__(self, name: str, system: Optional[str] = None):
        self.name = name
        self.system = system
        self.memory = []

    def insert(self, item):
        """
        Insert an item into the long-term memory.
        """
        self.memory.append(item)

    def retrieve(self):
        """
        Retrieve all items from long-term memory.
        """
        return self.memory

    def clear(self):
        """
        Clear the long-term memory.
        """
        self.memory = []

"""
My node file
"""


class Node:
    """
    My Node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


    def get_data(self):
        """
        Returns data
        """
        return self.data

    def get_next(self):
        """
        Gets next node
        """
        return self.next

    def set_data(self, newdata):
        """
        Sets current nodes data
        """
        self.data = newdata

    def set_next(self, newnext):
        """
        Sets next node
        """
        self.next = newnext

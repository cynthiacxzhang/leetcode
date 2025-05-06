# Design Hash Map

class MyHashMap(object):

    # Note: no collision handling for this solution
    # - how should we implement separate chaining? open addressing?

    def __init__(self):
        self.map = [-1] * 1000001  # Supports keys from 0 to 1,000,000
        # since keys are always 0 and above, -1 indicates no value at that position
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value # inserts value at spot "key" in the array
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.map[key]    # gets the value at position "key"
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.map[key] = -1      # sets the value at position "key" back to -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
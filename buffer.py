from collections import deque


class Buffer :
    def __init__(self,capacity,iterable=None):
        """
        Initialises Buffer with capacity and iterable
        
        Parameters:
        capacity (int) : The maximum number of items to allocate
        iterable (iterable) : iterable to initialise buffer with


        Returns:
        None 
        """
        if capacity <=0 :
            raise ValueError('capacity must be positive')
        self._capacity = capacity
        self._buffer = deque(maxlen=self._capacity)

        if iterable :
            if len(iterable) > capacity :
                raise ValueError ('iterable must be less than or equal than capacity')
            
            for item in iterable:
                self._buffer.append(item)

    def __len__(self):
        """
        Returns the number of items in the buffer
        """
        return len(self._buffer)
    
    def __getitem__(self,key:int):
        """
        Return the item based on the specified key
        
        Parameters:
        key (int) : The index of the item to return
        
        Returns:
        item (int or float) : The item at the specified index
        """
        return self._buffer[key]
    
    def add(self,item):
        """
        Add an item to the buffer
        
        Parameters:
        item (int or float) : The item to add to the buffer
        
        Returns:
        item (int or float) : The item at the specified index
        """
        if not isinstance(item, (int,float)):
            raise TypeError('item must be int or float')
        self._buffer.append(item)
     
    def __repr__(self) -> str:
        """
        Returns a string representation of the buffer
        """
        return ' '.join(map(str, self._buffer))
    
    def __str__(self) -> str:
        """
        Returns a string representation of the buffer
        """
        return repr(self)
    
    @property
    def capacity(self):
        """
        Returns the capacity of the buffer
        """
        return self._capacity
    
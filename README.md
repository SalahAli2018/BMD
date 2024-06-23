# buffer class

The Buffer class has this functions:  
    `add`: To add an item to the buffer.    
    `capacity`: To get the capacity (the max size of items).

# Use this class 
```python
from buffer import Buffer

buffer = Buffer(3, [1, 2, 3])
print(buffer)  # Output: 1 2 3
buffer.add(4)
print(buffer)  # Output: 2 3 4
```    

# Run the test
Run this command 
```bash 
python -m unittest discover -s .
```

expected results 
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

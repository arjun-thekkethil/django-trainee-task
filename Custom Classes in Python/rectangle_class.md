# Custom Class - Rectangle Iterator

## Task Description:
Create a `Rectangle` class with:
1. Constructor requires `length: int` and `width: int`
2. The class is **iterable**
3. Iteration yields:
   - First: `{'length': <value>}`
   - Then: `{'width': <value>}`

---

## Implementation:

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # For iteration state

    def __iter__(self):
        self._index = 0  # Reset iteration on new loop
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration

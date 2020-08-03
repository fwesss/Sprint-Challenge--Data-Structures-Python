from typing import List


class RingBuffer:
    def __init__(self, capacity: int = 1) -> None:
        self._storage = []
        self._size = 0
        self._capacity = capacity
        self._oldest = 0

    @property
    def storage(self) -> List[str]:
        return self._storage

    @property
    def size(self) -> int:
        return len(self._storage)

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def oldest(self) -> int:
        return self._oldest

    @oldest.setter
    def oldest(self, value) -> None:
        self._oldest = (self._oldest + value) % self.capacity

    def append(self, item: str) -> None:
        if self.size == self.capacity:
            self.storage[self.oldest] = item
            self.oldest = 1
        else:
            self.storage.append(item)

    def get(self):
        return self.storage

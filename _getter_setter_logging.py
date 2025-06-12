"""Test module for setter, getter and logging"""

import logging

logging.basicConfig(level=logging.INFO)


class Test:
    """Test class with setter, getter and logging"""

    def __init__(self) -> None:
        self._a = 0

    @property
    def a(self) -> int:
        """a getter"""
        logging.info(" READ:  a = %d", self._a)
        return self._a

    @a.setter
    def a(self, value: int) -> None:
        """a setter"""
        logging.info(" WRITE: a = %d", self._a)
        self._a = value


if __name__ == "__main__":
    t = Test()
    t.a = 5
    print(t.a)

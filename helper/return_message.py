#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

class ReturnMessage:
    def __init__(self, valid: bool):
        self.valid: bool = valid
        self.entry: None = None


class ReturnMessageNone(ReturnMessage):
    def __init__(self, valid: bool):
        super().__init__(valid)
        self.entry: None = None


class ReturnMessageStr(ReturnMessage):
    def __init__(self, entry: str, valid: bool):
        super().__init__(valid)
        self.entry: str = entry


class ReturnMessageInt(ReturnMessage):
    def __init__(self, entry: int, valid: bool):
        super().__init__(valid)
        self.entry = entry


class ReturnMessageTuple(ReturnMessage):
    def __init__(self, entry: tuple, valid: bool):
        super().__init__(valid)
        self.entry: tuple = entry


class ReturnMessageList(ReturnMessage):
    def __init__(self, entry: list, valid: bool):
        super().__init__(valid)
        self.entry: list = entry

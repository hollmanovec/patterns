class StringBuilder():
    def __init__(self, str=""):
        self.__strings = [str]

    def append(self, new_str):
        self.__strings.append(new_str)

        return self

    def build(self):
        result = ""
        for str in self.__strings:
            result += str

        return result
class ListWorker:
    def __init__(self, *args):
        self.arg_list = list(args)

    def getStrings(self):
        return [i for i in self.arg_list if type(i) == str]

    def getNumbers(self):
        return [i for i in self.arg_list if type(i) == int or type(i) == float]

    def getOther(self):
        return [i for i in self.arg_list if type(i) != int and type(i) != float and type(i) != str]
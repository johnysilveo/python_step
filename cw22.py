def add(*args,**kwargs):
    result = 0
    for elem in list(args) + list(kwargs.values()):
        if type(elem) == int or type(elem) == bool or type(elem) == float:
            result += elem
        else:
            try:
                result += float(elem)
                continue
            except (ValueError,TypeError):
                pass

    return result




class Calculate:
    def add(*args, **kwargs):
        result = 0
        for elem in list(args) + list(kwargs.values()):
            if type(elem) == int or type(elem) == bool or type(elem) == float:
                result += elem
            else:
                try:
                    result += float(elem)
                    continue
                except (ValueError, TypeError):
                    pass

        return result

    def subtract(self,a,b):
        return a - b

    def mult(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b
    def exp(self,a,b):
        return a ** b

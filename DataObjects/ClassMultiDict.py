class MultiDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            if isinstance(self[key], list):
                val = self[key]
                if isinstance(value, list):
                    val = val + value
                else:
                    val.append(value)
            else:
                if isinstance(value, list):
                    val = [self[key]] + value
                else:
                    val = [self[key], value]
        else:
            if isinstance(value, list):
                val = value
            else:
                val = [value]

        super().__setitem__(key, val)

import enum
from typing import List

class TransitionClassificationEnum(enum.Enum):

    invalid = 0
    access_miss = 1
    access_hit = 2

    evict_miss = 3
    evict_hit = 4

    remote_miss = 5
    remote_hit = 6
    data_ack = 7


class TransitionClassificationFunc:

    def __init__(self):
        self.access_class = TransitionClassificationEnum.invalid

    def gen_classification(self, general_access: List[str]) -> TransitionClassificationEnum:
        if not self.access_class == TransitionClassificationEnum.invalid:
            return self.access_class
        return self.classification_function(general_access)

    def classification_function(self, general_access: List[str]) -> TransitionClassificationEnum:
        startstateid = self.getstartstate().getstatename()
        finalstateid = self.getfinalstate().getstatename()

        if self.getaccess() and not self.getinmsg():
            if [access for access in general_access if self.getaccess() == access]:
                if not self.getoutmsg():  # startstateid == finalstateid or
                    self.access_class = TransitionClassificationEnum.access_hit
                else:
                    self.access_class = TransitionClassificationEnum.access_miss
            else:
                if startstateid == finalstateid:
                    self.access_class = TransitionClassificationEnum.evict_hit
                else:
                    self.access_class = TransitionClassificationEnum.evict_miss
        else:
            if self.getoutmsg():
                self.access_class = TransitionClassificationEnum.remote_miss
            elif not self.getoutmsg() and self.getinmsg():
                self.access_class = TransitionClassificationEnum.data_ack
            else:
                assert False, "State could not be classified"

        return self.access_class

    def get_classification(self) -> TransitionClassificationEnum:
        return self.access_class

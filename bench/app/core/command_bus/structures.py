# -*- coding: utf-8 -*-


class Command(object):

    def __eq__(self, o: object) -> bool:
        if isinstance(self, o.__class__):
            return self.__dict__ == o.__dict__
        return False

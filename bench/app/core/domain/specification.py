# -*- coding: utf-8 -*-


class Specification(object):

    def is_satisfied_by(self, obj: object) -> bool:
        raise NotImplementedError()

# -*- coding: utf-8 -*-

from typing import Dict


class Presenter(object):

    @staticmethod
    def from_object(obj: object) -> Dict:
        raise NotImplementedError()

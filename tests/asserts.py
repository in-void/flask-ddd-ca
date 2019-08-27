# -*- coding: utf-8 -*-

from uuid import UUID


def is_uuid(uuid_string: str) -> bool:

    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return val.hex == uuid_string.replace('-', '')

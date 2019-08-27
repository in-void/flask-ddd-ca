# -*- coding: utf-8 -*-

import json

from tests.asserts import is_uuid

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def test_post(client):
    # when
    data = {
        'subject_url': 'http://www.wp.pl',
        'competitors_urls': ['http://www.google.pl', 'http://www.onet.pl']
    }

    response = client.post('/api/benchmark', data=json.dumps(data), headers=headers)

    # then
    assert True is is_uuid(response.json.get('id'))
    assert 'subject_url' in response.json
    assert 'subject_load_time' in response.json
    assert 'competitors' in response.json
    assert response.status_code == 201
    assert response.mimetype == 'application/json'

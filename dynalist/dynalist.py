"""
"""
import json
import requests
import os
import codecs

class Dynalist():

    def __init__(self, file_id, token=None):
        """
        If `token` is not provided, :any:`_auth()` will attempt
        to use ``os.environ['DYNALIST_TOKEN']``
        """
        self._auth(token)

        self._doc(file_id)
        self._file()

    def _auth(self, token):
        env_token = os.environ.get('DYNALIST_TOKEN', None)

        if token:
            self.TOKEN = token
        elif env_token:
            self.TOKEN = env_token
        else:
            raise KeyError('Token not found. Pass token as a kwarg \
                            or set an env var DYNALIST_TOKEN with your key')

    def _doc(self, file_id):
        res = requests.post(
            'https://dynalist.io/api/v1/doc/read',
            json={'token': self.TOKEN, 'file_id': file_id})

        nodes = res.json()['nodes']

        self.file_id = file_id
        self.doc = nodes

        self.doc_dict = {n['id']:n for n in nodes}

    def _file(self):
        _info = {'title': self.doc_dict['root']['content']}
        self.file = _info

    def to_json(self, file_name=None):
        if not file_name:
            file_name = self.file['title']

        if '.json' not in file_name:
            file_name += '.json'

        with codecs.open(file_name, 'w', encoding='utf8') as f:
            json.dump(self.doc, f, ensure_ascii=False, indent=4)

    def get_node(self, node_id='root'):
        return self.doc_dict.get(node_id, {})

    def get_node_link(self, node_id):
        node = self.get_node(node_id)
        _url = 'https://dynalist.io/d/'+self.file_id+'#z=' + node['id']

        return '[{}]({})'.format(node['content'],_url)


    def get_children(self, node_id='root'):
        node = self.doc_dict.get(node_id)
        _children = node.get('children',[])
        return [self.doc_dict[_child] for _child in _children]

    def search(self, keyword):
        return [n for n in self.doc if keyword in n['content'] or n['note']]
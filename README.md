# Dynalist
[![LICENSE](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)
[![PyPI version](https://badge.fury.io/py/dynalist.svg)](https://badge.fury.io/py/dynalist)
[![docs](https://readthedocs.org/projects/dynalist/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/dynalist/badge/?version=latest&style=flat-square)

Unofficial Dynalist API Written in Python.

## Installing

```
pip install dynalist
```

## Documentation

### Usage Example

Below are some of the methods available in the wrapper.

```
dynalist = Dynalist('your_file_id')

dynalist.file  # file info

dynalist.doc  # document

dynalist.get_node(node_id='root')

dynalist.get_children(node_id='root')

dynalist.to_json()

```

## License
[MIT](https://opensource.org/licenses/MIT)

## Requires
* requests

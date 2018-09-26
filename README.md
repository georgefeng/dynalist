# Dynalist

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

_generated = {}


def __getattr__(name):
    if name in _generated:
        return _generated[name]
    else:
        raise AttributeError(f'generated lookup failure. No name {name!r}')

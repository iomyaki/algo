def flatten_dict(dct, prefix=""):
    for key, value in dct.items():
        new_prefix = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            yield from flatten_dict(value, prefix=new_prefix)
        else:
            yield new_prefix, value


test_dct = {"a": 1, "b": {"c": 2, "d": 3}}
print(list(flatten_dict(test_dct)))

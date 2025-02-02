def stringify_plain(value):
    if value is True:
        result = 'true'
    elif value is None:
        result = 'null'
    elif value is False:
        result = 'false'
    elif isinstance(value, int):
        result = value
    else:
        result = f"'{value}'"
    return result


def gen_diff_plain(value, lvl=''):
    res = ''
    for el, val in value.items():
        match val[0]:
            case 'nested':
                res += gen_diff_plain(val[1], lvl + f'{el}.') + '\n'
            case 'added':
                if isinstance(val[1], dict):
                    res += (f"Property '{lvl + el}'"
                            f" was added with value: [complex value]") + '\n'
                else:
                    res += (f"Property '{lvl + el}'"
                            f" was added with value:"
                            f" {stringify_plain(val[1])}") + '\n'
            case 'removed':
                res += f"Property '{lvl + el}' was removed" + '\n'
            case 'changed':
                if isinstance(val[1], dict):
                    res += (f"Property '{lvl + el}'"
                            f" was updated. From [complex value]"
                            f" to {stringify_plain(val[2])}") + '\n'
                elif isinstance(val[2], dict):
                    res += (f"Property '{lvl + el}'"
                            f" was updated. From {stringify_plain(val[1])}"
                            f" to [complex value]") + '\n'
                else:
                    res += (f"Property '{lvl + el}'"
                            f" was updated. From {stringify_plain(val[1])}"
                            f" to {stringify_plain(val[2])}") + '\n'
    return res.strip()

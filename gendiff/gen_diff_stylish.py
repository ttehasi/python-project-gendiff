def stringify(value, lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{'    ' * lvl}{el}: '
            result += stringify(val, lvl + 1) + '\n'
        result += '    ' * (lvl - 1) + '}'
    else:
        if value is True:
            result = 'true'
        elif value is None:
            result = 'null'
        elif value is False:
            result = 'false'
        else:
            result = str(value)
    return result


def gen_diff_stylish(value, lvl=1):
    res = ''
    if isinstance(value, dict):
        res += '{\n'
        for el, val in value.items():
            match val[0]:
                case 'nested':
                    res += f'{'    ' * lvl}{el}: '
                    res += gen_diff_stylish(val[1], lvl + 1) + '\n'
                case 'unchanged':
                    res += (f'{'    ' * lvl}{el}:'
                            f' {stringify(val[1], lvl=lvl + 1)}') + '\n'
                case 'added':
                    res += (f'{'    ' * (lvl - 1) + '  + '}{el}:'
                            f' {stringify(val[1], lvl=lvl + 1)}') + '\n'
                case 'removed':
                    res += (f'{'    ' * (lvl - 1) + '  - '}{el}:'
                            f' {stringify(val[1], lvl=lvl + 1)}') + '\n'
                case 'changed':
                    res += (f'{'    ' * (lvl - 1) + '  - '}{el}:'
                            f' {stringify(val[1], lvl=lvl + 1)}') + '\n'
                    res += (f'{'    ' * (lvl - 1) + '  + '}{el}:'
                            f' {stringify(val[2], lvl=lvl + 1)}') + '\n'
        res += '    ' * (lvl - 1) + '}'
    return res

import re


class EmptyMatchedException(Exception):
    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source

    def __str__(self):
        return '일치 결과가 없습니다.'


def search_pattern(pattern, source):
    m = re.search(pattern, source)
    if m:
        return m
    raise EmptyMatchedException(pattern, source)


try:
    pattern = 'Man'
    string = 'Lux, the Lady of Luminocity'

    search_pattern(pattern, string)
except Exception as e:
    print(e)


print('------------------------------------------')


try:
    pattern = r'(L\w+)'
    string = 'Lux, the Lady of Luminocity'

    m_list = re.finditer(pattern, string)
    result_list = [m.group() for m in m_list]
except Exception as e:
    print(e)
else:
    print(result_list)
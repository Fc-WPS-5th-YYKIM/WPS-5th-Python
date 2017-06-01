import re


class Node:

    """
    HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """
    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'

    # r : 패턴영역 '' 사이의 \는 이스케이프 표시자가 아닌 문자 그대로의 의미로 사용하겠다는 표시
    # <{tag}.*?> : <와 특정태그로 시작하며 .(모든문자가)*?>(> 처음 나오기 전까지 찾는다) 즉, '<태그로 시작하며 모든 문자가 첫 >가 나올때 까지 찾는다'을 의미
    # \s* : 앞에 공백, 탭, 줄바꿈을 포함한다.
    # [.\w\W] : .(줄바꿈이외의 모든 문자)가 [](오거나 - [] 사이의 패턴간의 관계는 or ) \w (문자, 숫자)가 오거나 \W (문자, 숫자 이외의 것)이 올 수 있다
    # \s* : 앞에 공백, 탭, 줄바꿈을 포함한다.
    # </{tag}> : </특정태그> 형식의 문자까지 출력

    _pattern_tag_content = r'<[^!]*?>([.\w\W]*)</.*?>'

    # <[^!]*?> : <로 시작하며 !를 제외한 모든 문자를 첫 >가 나올때 까지 찾는다
    # [.\w\W]* : 숫자나 문자나 그 외 모든 것이 몇 번 반복 되든 선택
    # </.*?> : </와 .(모든단어) *?> (첫번째 > 가 나올 때 까지 찾는다

    _pattern_tag_class = r'class=[\'\"]([.\w\W]*)[\'\"]'
    #_pattern_tag_class = r'^\s*<.*?class=[\'\"](.*?)[\'\"]'

    def __init__(self, source):
    # init 메소드 ( 초기화 메소드 )를 생성하며 매개변수는 source를 갖는다
        self.source = source
        # 매개변수로 받은 source의 값을 Node 자신(self)의 속성을 생성하여 저장한다

    def __str__(self):
    # 문자열 표현을 리턴하는 특수 메소드 __str__를 생성한다
        return '{}\n{}'.format(
            super().__str__(),
            self.source
        )
        # 부모 객체의 __str__ 메소드에 리턴 되는 값을 {} 매치 하고 \n 줄바꿈 후
        # Node 자신의 source 속성을 {} 매치한 문자열을 리턴 한다

    def find_tag(self, tag):
    # tag를 매개변수로 갖는 인스턴스 메소드 find_tag를 생성한다

        """
        주어진 tag 문자열, 또는 문자열의 리스트 반환
        :param tag: 검색을 원하는 태그. ex)'div'
        :param source: 태그를 검색할 전체 문자열
        :return: 검색 결과가 1개일 경우에는 tag문자열로 만든 Node객체, 2개 이상 일 경우에는 tag문자열로 만든 Node의 리스트
        """
        pattern = re.compile(self._pattern_tag_base.format(tag=tag))
        # re.compile(정규표현식) : 정규표현식을 컴파일하여 패턴객체를 리턴한다.

        m_list = re.finditer(pattern, self.source)
        # Node의 source 에서 pattern과 일치 하는 결과를 담은 이터레이터 객체를 반환한다
        # 이터레이터 ( 반복 가능한 객체 ) ex) list

        if m_list:
        # m_list가 비어있는지 아닌지 체크 한 후 비어있지 않으면 if 구문 내의 로직 수행
            return_list = [Node(m.group()) for m in m_list]
            # m_list에 저장된 문자열을 불러와 리스트에 담는다.
            return return_list if len(return_list) > 1 else return_list[0]
            # return_list의 크기가 1을 초과 할 경우 return_list 그대로 리스트를 리턴하고, 그렇지 않을 경우 return_list[0]에 저장된 문자열 한개만 리턴 한다
        return None
        # m_list가 비어있다면 None을 리턴 한다.

    @property
    def content(self):
        """
        Node인스턴스의 내용을 리턴
        :return: Node(태그)내부의 내용 문자열을 리턴
        """
        pattern = re.compile(self._pattern_tag_content)
        # re.compile(정규표현식) : 정규표현식을 컴파일하여 패턴객체를 리턴한다.

        m = re.search(pattern, self.source.strip())
        # 좌우 공백을 제거한 Node의 source 에서 pattern과 일치 하는 결과를 찾는다

        if m:
        # 찾은 데이터가 있는 경우 if문 내의 로직 수행
            return m.group(1).strip()
            # 좌우 공백을 제거 한 값을 리턴
        return None
        # 데이터가 없을 경우 None 리턴

    @property
    def class_(self):
        """
        해당 Node가 가진 class속성의 value를 리턴 (문자열)
        :return: 
        """
        pattern = re.compile(self._pattern_tag_class)
        # re.compile(정규표현식) : 정규표현식을 컴파일하여 패턴객체를 리턴한다.

        m_list = re.finditer(pattern,self.source)
        # Node의 source 에서 pattern과 일치 하는 결과를 담은 이터레이터 객체를 반환한다
        # 이터레이터 ( 반복 가능한 객체 ) ex) list

        if m_list:
        # m_list가 비어있는지 아닌지 체크 한 후 비어있지 않으면 if 구문 내의 로직 수행
            return_list = [ m.group(1) for m in m_list ]
            # m_list에 저장된 문자열을 불러와 리스트에 담는다.
            return return_list if len(return_list) > 1 else return_list[0]
            # return_list의 크기가 1을 초과 할 경우 return_list 그대로 리스트를 리턴하고, 그렇지 않을 경우 return_list[0]에 저장된 문자열 한개만 리턴 한다
        return None
        # 데이터가 없을 경우 None 리턴


with open('example.html') as f:
# example.html 파일을 오픈하며 이하 별칭은 f로 하고, with의 범주를 벗어나면 자동 close한다
    html = Node(f.read())
    # html변수에 파일 f의 내용을 읽어 들인 후 저장 한다.

node_div = html.find_tag('div')
# div 태그의 내용을 추출
node_p_list = node_div.find_tag('p')
# p 태그의 내용을 추출
for node_p in node_p_list:
# 반복문을 수행하며 node_p_list 리스트 객체에 들어있는 데이터를 node_p 변수에 담는다
    print(node_p.content)
    # node_p에 담긴 데이터를 content property를 통해 변환하여 출력 한다.

node_class = html.class_
# html에서 클래스 명을 추출하는 property를 호출
print(node_class)
# 저장된 클래스 명을 출력

# pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
#
#
# def find_tag(tag, source):
#     """
#     주어진 tag 문자열, 또는 문자열의 리스트 반환
#     :param tag: 검색을 원하는 태그. ex)'div'
#     :param source: 태그를 검색할 전체 문자열
#     :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
#     """
#     pattern = re.compile(pattern_tag_base.format(tag=tag))
#     m_list = re.finditer(pattern, source)
#     if m_list:
#         return_list = [m.group() for m in m_list]
#         return return_list if len(return_list) > 1 else return_list[0]
#     return None
#
#
# # pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'
# pattern_tag_content = r'<.*?>([.\w\W]*)</.*?>'
#
#
# def get_tag_content(tag_string):
#     """
#     tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
#     :param tag_string: <tag>내용</tag>형태의 문자열
#     :return: 위 형태에서 '내용'부분
#     """
#     pattern = re.compile(pattern_tag_content)
#     m = re.search(pattern, tag_string.strip())
#     if m:
#         return m.group(1)
#     return None
#
#
# # html문자열 변수에서 'div'태그의 내용을 찾아 반환하는 함수 실행
# div = find_tag('div', html)
# p_list = find_tag('p', div)
# print(p_list)
# for p in p_list:
#     print(get_tag_content(p))
#
#
# # 원리
# pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
# m = re.search(pattern_div, html)
# div = m.group(1)
#
# pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
# m_list = re.finditer(pattern_p, div)

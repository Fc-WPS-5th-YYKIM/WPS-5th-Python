class Email:

    def __init__(self, sender, receiver, title, content):
        self.__sender = sender
        self.__receiver = receiver
        self.title = title
        self.__content = content

    def write_email(self):
        print('[ 메 일 정 보 ]\n보내는 사람 : {}\n받는 사람 : {}\n제 목 : {}\n내 용 : {}\n'.format(
            self.__sender, self.__receiver, self.title, self.__content
        ))

    @property
    def sender(self):
        return self.__sender

    @property
    def receiver(self):
        return self.__receiver

    @property
    def get_content(self):
        return self.__content

    @get_content.setter
    def set_content(self, content):
        self.__content = content
from mycroft import MycroftSkill, intent_file_handler


class Cinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cinder.intent')
    def handle_cinder(self, message):
        self.speak_dialog('cinder')


def create_skill():
    return Cinder()


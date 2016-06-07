from ansiblelint import AnsibleLintRule

class TaskNoLocalAction(AnsibleLintRule):
    id = 'E304'
    shortdesc = 'Do not use local_action. use delegate_to: localhost instead'
    description = ''
    tags = ['task']

    def match(self, file, text):
        if 'local_action' in text:
            return True
        return False

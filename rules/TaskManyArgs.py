from ansiblelint import AnsibleLintRule

class TaskManyArgs(AnsibleLintRule):
    id = 'E303'
    shortdesc = 'Use ":" YAML format when arguments are over 4'
    description = ''
    tags = ['task']

    def match(self, file, text):
        count = 0
        for action in text.split(" "):
            if "=" in action:
                count += 1

        if count > 4:
            return True

        return False

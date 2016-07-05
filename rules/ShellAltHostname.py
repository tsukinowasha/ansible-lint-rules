from ansiblelint import AnsibleLintRule

class ShellAltHostname(AnsibleLintRule):
    id = 'E503'
    shortdesc = 'Use hostname module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if ('hostname' in task['action']['__ansible_arguments__'] and
            'register' not in task):
            return True
        return False

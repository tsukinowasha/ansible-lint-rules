from ansiblelint import AnsibleLintRule

class ShellAltHostname(AnsibleLintRule):
    id = 'E503'
    shortdesc = 'Use hostname module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if ('hostname' in task['action']['module_arguments'] and
            'register' not in task):
            return True
        return False

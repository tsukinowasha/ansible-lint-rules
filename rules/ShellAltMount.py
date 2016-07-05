from ansiblelint import AnsibleLintRule

class ShellAltMount(AnsibleLintRule):
    id = 'E504'
    shortdesc = 'Use mount module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if ('mount' in task['action']['__ansible_arguments__'] and
            'register' not in task):
            return True
        return False

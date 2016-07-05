from ansiblelint import AnsibleLintRule

class ShellAltUnarchive(AnsibleLintRule):
    id = 'E510'
    shortdesc = 'Use unarchive module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        args = task['action']['__ansible_arguments__']
        if 'unzip' in args:
            return True
        if 'tar' in args and 'xf' in args:
            return True
        return False

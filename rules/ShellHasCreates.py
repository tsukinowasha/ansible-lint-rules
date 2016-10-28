from ansiblelint import AnsibleLintRule

class ShellHasCreates(AnsibleLintRule):
    id = 'E511'
    shortdesc = 'Shell/command module must contain creates or removes'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'creates' in task['action'] or 'removes' in task['action']:
            return False
        if 'register' in task:
            return False
        return True

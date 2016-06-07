from ansiblelint import AnsibleLintRule

class ShellAltChown(AnsibleLintRule):
    id = 'E502'
    shortdesc = 'Use chown module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'chown' in task['action']['module_arguments']:
            return True
        return False

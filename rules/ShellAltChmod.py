from ansiblelint import AnsibleLintRule

class ShellAltChmod(AnsibleLintRule):
    id = 'E501'
    shortdesc = 'Use chmod module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'chmod' in task['action']['__ansible_arguments__']:
            return True
        return False

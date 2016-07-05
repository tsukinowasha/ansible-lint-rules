from ansiblelint import AnsibleLintRule

class ShellAltRpm(AnsibleLintRule):
    id = 'E506'
    shortdesc = 'Use yum module with file path'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'rpm' in task['action']['__ansible_arguments__']:
            return True
        return False

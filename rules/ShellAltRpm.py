from ansiblelint import AnsibleLintRule

class ShellAltRpm(AnsibleLintRule):
    id = 'E506'
    shortdesc = 'Use yum module with file path'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'rpm' in task['action']['module_arguments']:
            return True
        return False

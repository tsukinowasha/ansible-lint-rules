from ansiblelint import AnsibleLintRule

class ShellAltChmod(AnsibleLintRule):
    id = 'E501'
    shortdesc = 'Use chmod module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'chmod' in task['action']['module_arguments']:
            return True
        return False

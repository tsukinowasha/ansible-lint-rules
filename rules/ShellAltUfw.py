from ansiblelint import AnsibleLintRule

class ShellAltUfw(AnsibleLintRule):
    id = 'E509'
    shortdesc = 'Use ufw module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'ufw' in task['action']['module_arguments']:
            return True
        return False

from ansiblelint import AnsibleLintRule

class ShellAltUfw(AnsibleLintRule):
    id = 'E509'
    shortdesc = 'Use ufw module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'ufw' in task['action']['__ansible_arguments__']:
            return True
        return False

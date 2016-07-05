from ansiblelint import AnsibleLintRule

class ShellAltNmcli(AnsibleLintRule):
    id = 'E505'
    shortdesc = 'Use nmcli module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'nmcli' in task['action']['__ansible_arguments__']:
            return True
        return False

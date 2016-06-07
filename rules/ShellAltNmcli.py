from ansiblelint import AnsibleLintRule

class ShellAltNmcli(AnsibleLintRule):
    id = 'E505'
    shortdesc = 'Use nmcli module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'nmcli' in task['action']['module_arguments']:
            return True
        return False

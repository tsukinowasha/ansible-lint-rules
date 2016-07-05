from ansiblelint import AnsibleLintRule

class ShellAltSysctl(AnsibleLintRule):
    id = 'E508'
    shortdesc = 'Use sysctl module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if ('sysctl' in task['action']['__ansible_arguments__'] and
            'register' not in task):
            return True
        return False

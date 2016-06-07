from ansiblelint import AnsibleLintRule

class ShellAltSysctl(AnsibleLintRule):
    id = 'E508'
    shortdesc = 'Use sysctl module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if ('sysctl' in task['action']['module_arguments'] and
            'register' not in task):
            return True
        return False

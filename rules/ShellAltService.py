from ansiblelint import AnsibleLintRule

class ShellAltService(AnsibleLintRule):
    id = 'E507'
    shortdesc = 'Use service module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        args = task['action']['module_arguments']

        if 'service' in args:
            return True
        if 'systemctl' in args:
            return True
        if '/etc/rc.d/init.d/' in args:
            return True
        return False

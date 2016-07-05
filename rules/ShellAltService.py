from ansiblelint import AnsibleLintRule

class ShellAltService(AnsibleLintRule):
    id = 'E507'
    shortdesc = 'Use service module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        args = task['action']['__ansible_arguments__']

        if 'service' in args:
            return True
        if 'systemctl' in args:
            return True
        if '/etc/rc.d/init.d/' in args:
            return True
        return False

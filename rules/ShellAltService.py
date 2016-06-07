from ansiblelint import AnsibleLintRule

class ShellAltService(AnsibleLintRule):
    id = 'E507'
    shortdesc = 'Use service module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'service' in task['action']['module_arguments']:
            return True
        if '/etc/rc.d/init.d/' in task['action']['module_arguments']:
            return True
        return False

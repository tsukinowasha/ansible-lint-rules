from ansiblelint import AnsibleLintRule

class ShellAltFile(AnsibleLintRule):
    id = 'E512'
    shortdesc = 'Use file module instead of mkdir, ln -s and so on'
    description = ''
    tags = ['shell']
    alt_commands = ["ln -s", "mkdir"]

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        for c in self.alt_commands:
            if c in task['action']['module_arguments']:
                self.shortdesc += " ({})".format(c)
                return True
        return False

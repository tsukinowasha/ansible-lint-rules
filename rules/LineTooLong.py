from ansiblelint import AnsibleLintRule


class LineTooLong(AnsibleLintRule):
    id = 'E602'
    shortdesc = 'Line too long'
    description = 'Line too long'
    tags = ['formatting']

    def match(self, file, line):
        if len(line) > 80:
            self.shortdesc += " ({} characters)".format(len(line))
            return True
        return False

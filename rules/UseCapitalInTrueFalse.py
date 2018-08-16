from ansiblelint import AnsibleLintRule

import re

class UseCapitalInTrueFalse(AnsibleLintRule):
    id = 'E604'
    shortdesc = 'True/False should be started from capitalized letter'
    description = ''
    tags = ['formatting']

    compiled = re.compile(r'\:\s(true|false)$')

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False

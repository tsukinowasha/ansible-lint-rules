from ansiblelint import AnsibleLintRule

import re

class UseTrueFalseInsteadYesNo(AnsibleLintRule):
    id = 'E603'
    shortdesc = 'Use True/False instead of yes/no'
    description = ''
    tags = ['formatting']

    compiled = re.compile(r'\:\s(yes|no)$', re.IGNORECASE)

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False

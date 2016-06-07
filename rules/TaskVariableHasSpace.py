from ansiblelint import AnsibleLintRule

import re

class TaskVariableHasSpace(AnsibleLintRule):
    id = 'E305'
    shortdesc = 'Variable should has space "{{ foo }}"'
    description = ''
    tags = ['task']

    compiled = re.compile(ur'{{(\w*)}}')

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            return True
        return False



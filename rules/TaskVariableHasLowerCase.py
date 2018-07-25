from ansiblelint import AnsibleLintRule

import re

class TaskVariableHasLowerCase(AnsibleLintRule):
    id = 'E306'
    shortdesc = 'Variable should be lowercase "{{ foo }}"'
    description = ''
    tags = ['task']

    compiled = re.compile(r'{{(\s?\w*\s?)}}')

    def match(self, file, text):
        m = self.compiled.search(text)
        if m:
            if any(c.isupper() for c in m.group(0)):
                return True
        return False

from ansiblelint import AnsibleLintRule

import os

class PlaybookExtention(AnsibleLintRule):
    id = 'E101'
    shortdesc = 'playbook should has ".yml" extention'
    description = ''
    tags = ['playbook']
    done = []  # already noticed path list

    def match(self, file, text):
        if file['type'] != 'playbook':
            return False

        path = file['path']
        ext = os.path.splitext(path)
        if ext[1] != ".yml" and path not in self.done:
            self.done.append(path)
            return True
        return False



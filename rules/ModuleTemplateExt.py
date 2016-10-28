from ansiblelint import AnsibleLintRule
import os

class ModuleTemplateExt(AnsibleLintRule):
    id = 'E402'
    shortdesc = "Template files should have the extension '.j2' "
    description = ''
    tags = ['module']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] != 'template':
            return False
        ext = os.path.splitext(task['action']['src'])
        if ext[1] != ".j2":
            return True
        return False

from ansiblelint import AnsibleLintRule

# FIXME: how to get include task?
class TaskIncludeShouldHaveTags(AnsibleLintRule):
    id = 'E302'
    shortdesc = 'Include should have tags'
    description = ''
    tags = ['task']

    def matchplay(self, file, play):
        ret = []

        if isinstance(play, dict) and 'tasks' in play:
            for item in play['tasks']:
                if 'include' in item and 'tags' not in item:
                    ret.append((file, self.shortdesc))
        return ret

# Copyright (c) 2018 EPAM SYSTEMS INC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from ansiblelint import AnsibleLintRule


class MetaShouldHaveGithubBranch(AnsibleLintRule):
    """Ansible Lint Rule - Meta Should Have GitHub branch specified"""

    id = "E706"
    shortdesc = "Meta information should have a valid github_branch value"
    description = "Checking that github_branch field is valid"
    tags = ['meta']

    def matchplay(self, ansible_file, play):
        """Check rule for meta"""

        if "galaxy_info" not in play:
            return False

        github_branch = play["galaxy_info"].get("github_branch", None)

        if not github_branch:
            return (
                "github_branch is undefined or empty",
                self.shortdesc
            )

        return False

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


class MetaShouldHaveAnsibleVersion(AnsibleLintRule):
    """Ansible Lint Rule - Meta Should Have Ansible Version"""

    id = "E702"
    shortdesc = "Meta information should have a valid Ansible Version value"
    description = "Checking that min_ansible_version field is set correctly"
    tags = ['meta']

    def matchplay(self, ansible_file, play):
        """Check rule for meta"""

        if "galaxy_info" not in play:
            return False

        min_ansible_version = play["galaxy_info"].get("min_ansible_version", None)

        if not min_ansible_version:
            return (
                "min_ansible_version is undefined or empty",
                self.shortdesc
            )
        elif str(min_ansible_version) == "1.2":
            return (
                "Define min_ansible_version, instead of default placeholder",
                self.shortdesc
            )
        elif len(str(min_ansible_version).split(".")) < 2:
            return (
                "Define valid min_ansible_version (with major and minor values specified)",
                self.shortdesc
            )

        return False

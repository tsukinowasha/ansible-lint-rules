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


class MetaShouldHaveLicense(AnsibleLintRule):
    """Ansible Lint Rule - Meta Should Have Correct License set"""

    id = "E708"
    shortdesc = "Meta information should have a valid license value"
    description = "Checking that license field is valid"
    tags = ['meta']

    def matchplay(self, ansible_file, play):
        """Check rule for meta"""

        if "galaxy_info" not in play:
            return False

        license = play["galaxy_info"].get("license", None)

        if not license:
            return (
                "license is empty or undefined",
                self.shortdesc
            )
        elif license == 'license (GPLv2, CC-BY, etc)':
            return (
                "Define license, instead of default placeholder",
                self.shortdesc
            )
        elif license not in ['BSD', 'MIT', 'GPLv2', 'GPLv3', 'Apache', 'CC-BY']:
            return (
                "Correct licence type should be set. Values allowed: 'BSD', 'MIT', 'GPLv2', 'GPLv3', 'Apache', 'CC-BY'",
                self.shortdesc
            )

        return False

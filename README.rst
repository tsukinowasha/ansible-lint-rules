====================================
Rules for ansible-lint |travisstatus|
====================================
.. |travisstatus| image:: https://travis-ci.org/lean-delivery/ansible-lint-rules.svg?branch=master
    :target: https://travis-ci.org/lean-delivery/ansible-lint-rules

This is a rule set for `ansible-lint <https://github.com/willthames/ansible-lint>`_ .

How to use
----------------

1. Install `ansible-lint` (ex: `pip install ansible-lint`)
2. Copy or `git clone` on your ansible playbook repository with `rules` name
3. Run ansible lint with `-r rules` flag (ex: `ansible-lint -r rules <your playbook file>`)


Rules
=========

+------------+----------------------------------------------------------------------+
|code        |sample message                                                        |
+============+======================================================================+
|**E3**      |*Task*                                                                |
+------------+----------------------------------------------------------------------+
|E302        |Include should has tags                                               |
+------------+----------------------------------------------------------------------+
|E303        |Use ":" YAML syntax when arguments are over 4                         |
+------------+----------------------------------------------------------------------+
|E306        |Variable should be lowercase "{{ foo }}"                              |
+------------+----------------------------------------------------------------------+
|**E4**      |*Module*                                                              |
+------------+----------------------------------------------------------------------+
|E402        |Template file should has '.j2' extension                              |
+------------+----------------------------------------------------------------------+
|**E6**      |*Formatting*                                                          |
+------------+----------------------------------------------------------------------+
|E603        |Use True/False instead of yes/no                                      |
+------------+----------------------------------------------------------------------+
|E604        |True/False should be started from capitalized letter                  |
+------------+----------------------------------------------------------------------+
|**E7**      |*Metadata*                                                            |
+------------+----------------------------------------------------------------------+
|E704        |Incorrect Dependencies in meta                                        |
+------------+----------------------------------------------------------------------+
|E706        |Absent Role name in meta                                              |
+------------+----------------------------------------------------------------------+
|E707        |Incorrect Issue tracker in meta                                       |
+------------+----------------------------------------------------------------------+


Why so many shell module lint?
---------------------------------------------------------

Because user may want to use a command to correct use. Since we separete these rule, user can disable specific rule easily.

If you can manage playbook your self, consider set `skip_ansible_lint` tag.

Original repo
--------------------------------------------------------
`tsukinowasha/ansible-lint-rules <https://github.com/tsukinowasha/ansible-lint-rules>`_

These rules are used in the `Tsukinowa Inc. <http://tsukinowa.jp>`_ , but anyone can use with the license (MIT).



License
==============

MIT License (same as ansible-lint)

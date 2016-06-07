.PHONY: test

test:
	ansible-lint -r rules tests/*.yml

list_tags:
	ansible-lint -r rules -T

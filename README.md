# Apply Recursive Permissions

Uses a breadth-first approach to apply a permission to a file or directory

## Incoming Message

Recognizes a message such as:

```json
{
    "uri": "agave://data-tacc-cloud/good_news/free_tacos",
    "username": "taco",
    "permission": "READ"
}```

## Return

Returns a `True` on success and `False` or Exception on failure.

## Develop and Test

All tests run local to the container. so you no need to manage Python deps.

```shell

make container
make tests-local
make tests-reactor
make deploy
make after
```

Tests are implemeted in Pytest, with support for coverage and flake8.

## Get an interactive shell

```make shell
bash tests/run_container_tests.sh bash
[INFO] Working directory: /Users/taco/src/SD2/apply-recursive-pems-reactor
[INFO] Not running under continous integration
root@5164a75ac9ee:/mnt/ephemeral-01# more /etc/reactors-VERSION
TACC.cloud Reactors
Language: python3
Version: 0.5.5
```

This is super userfule for debugging tricky siutations.

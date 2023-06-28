# Tests for OURCHIVE

!! unit tests live in the app repo @ [ourchive]()

this repo is solely for feature and end to end/userflow tests.

## repo structure

```
api-tests/
framework/
LICENSE
Pipfile
pytest.ini
README.md
requirements.txt
setup.py
ui-tests/
```

[framework](/framework) is where functionality that might be used in either ui and/or api tests lives

[api-tests](/api-tests) is where api-only tests live -- ourchive does not currently have a public api, and until it does (see [roadmap!](https://ourchive-admin-docs.stopthatimp.net/roadmap/)) there probably won't be any api tests in here.

[ui-tests](/ui-tests) is where selenium based ui tests live.


## how to run tests

### locally

### pipeline


## local dev set up
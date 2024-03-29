# matter-exceptions

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Background

The matter-exceptions library in Python is a comprehensive package that allows developers to create and customize different types of exceptions. This library includes three major categories of exceptions, namely API exceptions, detailed exceptions, and FastAPI exceptions, that can be tailored to specific use cases.

API exceptions are designed to provide clear and concise error messages for clients accessing an API. With this library, developers can easily create and customize API exceptions that contain relevant error messages, HTTP status codes, and detailed descriptions of what went wrong. These API exceptions can also include payloads, which can be forwarded to error tracking systems for debugging and analysis purposes.

Detailed exceptions, on the other hand, are designed for internal use by developers. These exceptions can be used to catch specific errors and provide detailed information about what went wrong. Developers can easily create and customize detailed exceptions with this library, including payloads that can be sent to error tracking systems to aid in debugging.

FastAPI exceptions are designed specifically for use with the FastAPI framework. With this library, developers can create and customize FastAPI exceptions that are easy to use and integrate seamlessly with FastAPI applications. These exceptions can also contain payloads, which can be forwarded to error tracking systems for analysis and debugging purposes.

Overall, the matter-exceptions library in Python is a powerful tool that allows developers to create and customize exceptions that provide clear, concise, and detailed error messages. With the ability to include payloads, these exceptions can be used to aid in debugging and error tracking, ensuring that developers can quickly and effectively resolve any issues that arise in their applications.


## Installation

Basic:
```console
pip install matter-exceptions
```

With FastAPI Support:
```console
pip install matter-exceptions[fastapi]
```

With Sentry Support:
```console
pip install matter-exceptions[sentry]
```

With FastAPI and Sentry Support:
```console
pip install matter-exceptions[fastapi,sentry]
```


## Getting Started
Raise an API Exception:
```python
from matter_exceptions.exceptions.api import ConflictError
raise ConflictError(description="test", detail="any payloads, including dicts or objects")
```

Raise a Fast API Exception:
```python
from matter_exceptions.exceptions.fastapi import NotFoundError
raise NotFoundError(description="test")
```

Raise a Detailed Exception:
```python
from matter_exceptions.exceptions.general import AuthenticationFailedError
raise AuthenticationFailedError(description="test")
```


## Contributing

Make sure you have all supported python versions installed in your machine:

* 3.10
* 3.11

### Install hatch in your system

```https://hatch.pypa.io/latest/install/```

### Create the environment

```console
hatch env create
```

Do your changes...

### Run the tests

```console
hatch run test
```

The command above will run the tests against all supported python versions
installed in your machine. For testing in other operating system you may use the
configured CI in github. 

### Bump a new version

In general, you just need to execute:

```console
hatch version
```

This command will update the minor version. i.e.:
No breaking changes and new feature has been added

We are using [semantic version](https://semver.org/), if you are doing a bug fix:

```console
hatch version fix
```

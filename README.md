## Development

### One-time install

Make sure to install the Githooks using the following command:

```bash
docker-compose up --build githooks
```

This will check the code quality before every commit. When errors occur during a commit, inspect the errors using the following command:

```bash
docker-compose run --rm webapp make check
```

### Conventions

The NumPy docstring format is used.
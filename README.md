## Development

### One-time install

Make sure to install the Githooks using the following command:

```bash
docker-compose up --build githooks
```

This will install Github hooks which check the code quality before every commit. When errors occur during a commit, inspect the errors using the following command:

```bash
docker-compose run --rm webapp make check
```

### Conventions

The NumPy docstring format is used.

### Build and push Docker image

In order to build and push the Docker image, run the following command:

```bash
make build push
```
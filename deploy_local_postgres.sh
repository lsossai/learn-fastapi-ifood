# Create docker volume for persistent storage
docker volume create postgres_storage

# Deploy postgres
docker run -d --name postgres -p 5432:5432 \
    -v postgres_storage:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=1234 \
    postgres
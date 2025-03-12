<div style='text-align:center; color: #00B050'>
<h1 style="font-size: 16pt">Author: Madhurima Rawat</h1>
<h2 style="font-size: 14pt">Cloud Databases and Data Management</h2>

<h3 style="font-size: 12pt">This experiment covers setting up and managing cloud-based relational databases using PostgreSQL, Docker, and LocalStack. It provides hands-on experience with database management in a simulated cloud environment. The setup replicates real-world cloud database operations using containerized solutions.

This document provides a comprehensive breakdown of all commands, inputs, outputs, and their explanations, ensuring a clear understanding of each step in the workflow.</h3>

</div>

---

## **1. Creating an RDS Instance Using LocalStack**

### **Command:**

```sh
aws rds create-db-instance --db-instance-identifier mydb \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --master-username admin \
  --master-user-password password \
  --allocated-storage 20 \
  --endpoint-url=http://localhost:4566
```

### **Error Output:**

```sh
Could not connect to the endpoint URL: "http://localhost:4566/"
```

```sh
An error occurred (InternalFailure) when calling the CreateDBInstance operation:
API for service 'rds' not yet implemented or pro feature - please check
https://docs.localstack.cloud/references/coverage/ for further information
```

### **Explanation:**

- The command attempts to create an **RDS instance** in **LocalStack**.
- `--endpoint-url=http://localhost:4566` → Uses LocalStack instead of AWS.
- **Errors indicate**:
  - LocalStack is either not running or misconfigured.
  - RDS API might not be fully implemented in the **free** version of LocalStack.

### **Output Breakdown:**

- **`Could not connect to the endpoint URL`** → LocalStack might not be running or accessible.
- **`InternalFailure` error** → The RDS API might require LocalStack Pro for full functionality.
- **Possible Fixes**:
  - Ensure LocalStack is running:
    ```sh
    docker run --rm -d --name localstack_main -p 4566:4566 localstack/localstack
    ```
  - Check service coverage:  
    [LocalStack RDS Coverage](https://docs.localstack.cloud/references/coverage/)

---

## **2. Starting a PostgreSQL Container**

### **Command:**

```sh
docker start my-postgres
```

```sh
docker start postgres
```

### **Error Output:**

```sh
Error response from daemon: No such container: my-postgres
Error: failed to start containers: my-postgres
```

```sh
Error response from daemon: No such container: postgres
Error: failed to start containers: postgres
```

### **Explanation:**

- The **containers do not exist** under the specified names.
- Verify running containers with:
  ```sh
  docker ps -a
  ```
- If needed, create a new container:
  ```sh
  docker run --name my-postgres -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydb \
    -p 5432:5432 -d postgres:15
  ```

### **Output Breakdown:**

- **`No such container: my-postgres`** → The container was never created or was removed.
- **`failed to start containers`** → The container name does not match any existing instances.
- **Possible Fixes**:
  - Check existing containers: `docker ps -a`
  - Create and start a new PostgreSQL container using `docker run` (above).

---

## **3. Listing Available Docker Images**

### **Command:**

```sh
docker images
```

### **Output:**

```markdown
| REPOSITORY            | TAG    | IMAGE ID     | CREATED      | SIZE   |
| --------------------- | ------ | ------------ | ------------ | ------ |
| my-flask-app          | latest | f5feae0ac7a4 | 6 hours ago  | 139MB  |
| flask-app             | latest | ae4054c49614 | 7 hours ago  | 139MB  |
| hackvortex-backend    | latest | 14e63c26d40b | 21 hours ago | 1.05GB |
| postgres              | 15     | e45d3f5ec589 | 7 days ago   | 430MB  |
| localstack/localstack | latest | b686f3948f42 | 6 weeks ago  | 1.18GB |
| python                | 3.9    | 9f98746e2033 | 3 months ago | 999MB  |
| nginx                 | latest | b52e0b094bc0 | 4 weeks ago  | 192MB  |
```

### **Explanation:**

- Displays **available images** in the local Docker environment.
- PostgreSQL (`postgres:15`) is available.
- LocalStack (`localstack/localstack`) is present but needs verification (`docker ps -a`).

### **Output Breakdown:**

- **`postgres:15` is listed** → The image exists but the container may not be running.
- **`localstack/localstack` exists** → LocalStack is installed but may need to be started.
- **Possible Fixes**:
  - Start PostgreSQL if not running:
    ```sh
    docker run --name my-postgres -e POSTGRES_USER=admin \
      -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydb \
      -p 5432:5432 -d postgres:15
    ```
  - Ensure LocalStack is running:
    ```sh
    docker start localstack_main
    ```

---

## **4. Starting a PostgreSQL Container**

### **Command:**

```sh
C:\Users\rawat>docker start postgres
```

### **Explanation:**

This command attempts to start a container named `postgres` that was previously created but is currently stopped. However, an error occurs.

### **Error Output:**

```sh
Error response from daemon: No such container: postgres
Error: failed to start containers: postgres
```

### **Cause:**

The error indicates that no container with the name `postgres` exists. This could be due to:

- The container never being created.
- The container being removed.
- A typo in the container name.

---

## **5. Listing All Containers**

### **Command:**

```sh
C:\Users\rawat>docker ps -a
```

### **Explanation:**

The `docker ps -a` command lists all containers, including those that have stopped. This helps verify whether the `postgres` container exists.

### **Output:**

| CONTAINER ID | IMAGE                 | COMMAND                | CREATED       | STATUS                     | PORTS                                                                  | NAMES           |
| ------------ | --------------------- | ---------------------- | ------------- | -------------------------- | ---------------------------------------------------------------------- | --------------- |
| a10c5a71f625 | localstack/localstack | "docker-entrypoint.sh" | 2 minutes ago | Up 2 minutes (healthy)     | 127.0.0.1:4510-4560->4510-4560/tcp, 127.0.0.1:4566->4566/tcp, 5678/tcp | localstack-main |
| 7f0fa023ac4f | 3a669f02efff          | "python app.py"        | 7 hours ago   | Exited (255) 5 minutes ago | 8080/tcp, 0.0.0.0:5002->5000/tcp                                       | backend2        |
| 9ff472da8892 | 3a669f02efff          | "python app.py"        | 7 hours ago   | Exited (255) 5 minutes ago | 8080/tcp, 0.0.0.0:5001->5000/tcp                                       | backend1        |

Since the `postgres` container is missing, it must be created before running it.

---

## **6. Running a PostgreSQL Container**

### **Command:**

```bash
C:\Users\rawat>docker run --name my-postgres -e
POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -e
POSTGRES_DB=mydb -p 5432:5432 -d postgres:15
```

### **Explanation:**

This command creates and starts a new PostgreSQL container named `my-postgres` with:

- `POSTGRES_USER=admin`: Defines the database user as `admin`.
- `POSTGRES_PASSWORD=password`: Sets the password for the user.
- `POSTGRES_DB=mydb`: Creates a database named `mydb`.
- `-p 5432:5432`: Maps the container's port 5432 to the host's port 5432.
- `-d`: Runs the container in detached mode.

### **Error Output:**

```sh
docker: Error response from daemon: driver failed
programming external connectivity on endpoint my-postgres
(feae7f0fb87909bde1853a7ddefa49bb518f11250e54304f7510968
f7a88cca1): Bind for 0.0.0.0:5432 failed: port is already allocated.
```

### **Cause:**

The error occurs because port 5432 on the host machine is already in use by another process or container.

---

## **7. Resolving Port Conflict and Running PostgreSQL on a Different Port**

### **Command:**

```sh
C:\Users\rawat>docker run --name my-new-postgres -e
POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -e
POSTGRES_DB=mydb -p 5433:5432 -d postgres:15
```

### **Explanation:**

- Changes the host port to `5433` while keeping the container's internal port as `5432`.
- Ensures there is no conflict with existing processes using port `5432`.

### **Output:**

```sh
b2efdca3c6f0af6cf4154fce236f0b66b5efba0f4f9e14972c94b3e0a5afa9de
```

This confirms that the container was created and started successfully.

---

## **8. Verifying Running Containers**

### **Command:**

```sh
C:\Users\rawat>docker ps
```

### **Explanation:**

Lists only running containers to confirm PostgreSQL is active.

### **Output:**

| CONTAINER ID | IMAGE                 | COMMAND                | CREATED        | STATUS                 | PORTS                                                                  | NAMES           |
| ------------ | --------------------- | ---------------------- | -------------- | ---------------------- | ---------------------------------------------------------------------- | --------------- |
| b2efdca3c6f0 | postgres:15           | "docker-entrypoint.s…" | 42 seconds ago | Up 41 seconds          | 0.0.0.0:5433->5432/tcp                                                 | my-new-postgres |
| a10c5a71f625 | localstack/localstack | "docker-entrypoint.sh" | 3 minutes ago  | Up 3 minutes (healthy) | 127.0.0.1:4510-4560->4510-4560/tcp, 127.0.0.1:4566->4566/tcp, 5678/tcp | localstack-main |

The `my-new-postgres` container is running successfully.

---

## **9. Connecting to PostgreSQL and Performing SQL Operations**

### **Command:**

```sh
C:\Users\rawat>docker exec -it my-new-postgres psql -U admin -d mydb
```

### **Explanation:**

- `docker exec -it`: Runs a command inside a running container.
- `my-new-postgres`: Specifies the container name.
- `psql -U admin -d mydb`: Connects to the PostgreSQL database `mydb` as the user `admin`.

### **Output:**

```sh
psql (15.12 (Debian 15.12-1.pgdg120+1))
Type "help" for help.
```

---

## **10. Performing SQL Queries**

### **Creating a Table and Inserting Data:**

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
INSERT INTO students (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com');
```

### **Explanation:**

- `CREATE TABLE students`: Creates a table with `id`, `name`, and `email` columns.
- `INSERT INTO students`: Adds three records.

### **Selecting Data:**

```sql
SELECT * FROM students;
```

### **Updating Data:**

```sql
UPDATE students SET email = 'bob.smith@example.com'
WHERE name = 'Bob Smith';
```

### **Deleting Data:**

```sql
DELETE FROM students WHERE name = 'Charlie Brown';
```

### **Exiting PostgreSQL:**

```sql
\q
```

# Dockerized PyTorch App with Debugging Support

This project demonstrates a simple PyTorch application containerized with Docker, featuring both production and debugging configurations.

## Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── debug-docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```

## Setup

1. Ensure you have Docker and Docker Compose installed on your system.
2. Clone this repository to your local machine.

## Running in Production Mode

To run the application in production mode:

```bash
docker-compose up --build
```

This will start the server on port 8000. You can access it by navigating to `http://localhost:8000` in your web browser or using curl:

```bash
curl http://localhost:8000
```

## Debugging the Application

To debug the application, we use a separate Docker Compose file that enables remote debugging capabilities.

### Starting the Debug Container

1. Start the debug container:

   ```bash
   docker-compose -f debug-docker-compose.yml up --build
   ```

2. The container will start and wait for a debugger to attach.

### Setting Up VS Code for Debugging

1. Install the Python extension in VS Code.

2. Create or update `.vscode/launch.json` with the following configuration:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: Remote Attach",
               "type": "python",
               "request": "attach",
               "connect": {
                   "host": "localhost",
                   "port": 5678
               },
               "pathMappings": [
                   {
                       "localRoot": "${workspaceFolder}",
                       "remoteRoot": "/app"
                   }
               ]
           }
       ]
   }
   ```

3. Set breakpoints in `app.py` as needed.

4. Go to the Run and Debug view in VS Code, select "Python: Remote Attach", and start debugging.

5. Once the debugger is attached, the server will start running.

### Testing the Debugger

1. With the debug container running and the VS Code debugger attached, open a new terminal and make an HTTP request:

   ```bash
   curl http://localhost:8000
   ```

2. The execution should pause at your breakpoint in VS Code, allowing you to step through the code, inspect variables, etc.

3. When you let the code continue running, you'll see the JSON response in your terminal where you ran curl.

## Modifying the Application

The main application logic is in `app.py`. You can modify this file to change the PyTorch operations or add new functionality. Remember to rebuild your Docker container after making changes:

```bash
docker-compose up --build
```

or for the debug version:

```bash
docker-compose -f debug-docker-compose.yml up --build
```

## Requirements

The application uses:

- Python 3.9
- PyTorch 2.2.1
- debugpy 1.8.0

You can update these in the `requirements.txt` file if needed.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements.

## License

[Specify your license here]

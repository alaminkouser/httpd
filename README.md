# HTTPD - Lightweight Web Server with CGI Support

A minimal web server implementation using BusyBox httpd with CGI scripting
support. This project demonstrates how to create a lightweight,
resource-efficient web server that can run in constrained environments where
BusyBox is available.

## Why This Project?

This project uses BusyBox httpd as the web server, which is one of the lightest
HTTP servers with scripting support. It can be deployed anywhere BusyBox runs
and uses minimal system resources, making it ideal for:

- Embedded systems
- Containerized applications
- Development environments
- Resource-constrained environments
- Quick prototyping

## Project Structure

```
httpd/
├── README.md              # This documentation
├── httpd.conf            # Server configuration file
└── home/                 # Web root directory
    ├── index.cgi         # Main CGI script (Hello World)
    ├── favicon.ico       # Website favicon
    ├── cgi-bin/          # CGI scripts directory
    │   └── index.cgi     # CGI router/dispatcher
    ├── deno/             # Deno-based CGI example
    │   └── index.cgi     # Deno script fetching external content
    └── top/              # System monitoring example
        └── index.cgi     # System top command output
```

## Requirements

- **BusyBox** with httpd support
- **Shell access** for CGI scripts
- **Deno** (optional, for the Deno CGI example)

## Configuration

### httpd.conf

The server configuration file contains:

- **Authentication**: Basic auth for `/admin` path with MD5 hashed password
- **MIME types**: Configuration for `.ico` files as `image/x-icon`

### CGI Scripts

The project includes several CGI examples:

1. **Main index.cgi** (`/home/index.cgi`): Simple "Hello World" script
2. **CGI Router** (`/home/cgi-bin/index.cgi`): Dispatches requests to
   appropriate CGI scripts
3. **Deno CGI** (`/home/deno/index.cgi`): Demonstrates Deno integration for
   fetching external content
4. **System Monitor** (`/home/top/index.cgi`): Shows system resource usage via
   `top` command

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd httpd
   ```

2. **Set proper permissions**:
   ```bash
   chmod 700 ./home/cgi-bin/index.cgi
   chmod 700 ./home/*.cgi
   chmod 700 ./home/*/*.cgi
   ```

3. **Verify BusyBox httpd support**:
   ```bash
   busybox httpd --help
   ```

## Usage

### Development Mode

Run the server in foreground with verbose logging:

```bash
busybox httpd -f -p 8080 -h "home" -vvv
```

- `-f`: Run in foreground
- `-p 8080`: Listen on port 8080
- `-h "home"`: Use "home" as document root
- `-vvv`: Maximum verbosity for debugging

### Production Mode

Run the server in background, bound to localhost:

```bash
busybox httpd -f -p 127.0.0.1:80 -h "home"
```

- `-p 127.0.0.1:80`: Listen on localhost port 80
- `-h "home"`: Use "home" as document root

### HTTPS Configuration

For production HTTPS deployment, use external tools like:

- **nginx** as reverse proxy
- **stunnel** for SSL termination
- **Let's Encrypt** for SSL certificates

## API Endpoints

| Endpoint       | Description             | Content Type            |
| -------------- | ----------------------- | ----------------------- |
| `/`            | Main page (Hello World) | text/plain              |
| `/admin/`      | Protected admin area    | Requires authentication |
| `/deno/`       | Deno CGI example        | text/html               |
| `/top/`        | System monitoring       | text/stream             |
| `/favicon.ico` | Website icon            | image/x-icon            |

## CGI Script Details

### Main Index Script

- **Location**: `/home/index.cgi`
- **Purpose**: Simple greeting page
- **Output**: "Hello World!" in plain text

### CGI Router

- **Location**: `/home/cgi-bin/index.cgi`
- **Purpose**: Routes requests to appropriate CGI scripts
- **Features**:
  - Path-based routing
  - 404 error handling
  - Status logging

### Deno Integration

- **Location**: `/home/deno/index.cgi`
- **Purpose**: Demonstrates Deno CGI capabilities
- **Features**:
  - Fetches content from external URLs
  - Network access with `--allow-net` permission
  - HTML content output

### System Monitor

- **Location**: `/home/top/index.cgi`
- **Purpose**: Real-time system resource monitoring
- **Features**:
  - Live system statistics
  - Streaming output format
  - Non-interactive top command

## Security Considerations

- **Authentication**: Basic auth configured for admin paths
- **File Permissions**: CGI scripts have restricted permissions
- **Network Binding**: Production mode binds to localhost only
- **Input Validation**: CGI scripts should validate all inputs

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure CGI scripts are executable
   ```bash
   chmod +x ./home/*.cgi
   ```

2. **Port Already in Use**: Change the port number
   ```bash
   busybox httpd -f -p 8081 -h "home"
   ```

3. **CGI Scripts Not Executing**: Check script shebang and permissions
   ```bash
   ls -la ./home/*.cgi
   ```

### Debugging

- Use `-vvv` flag for verbose logging
- Check system logs for error messages
- Verify CGI script syntax and permissions
- Test CGI scripts directly from command line

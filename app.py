import torch
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

def run_torch_operation():
    print(f"PyTorch version: {torch.__version__}")
    
    # Using newer PyTorch features
    x = torch.rand(5, 3, device='cpu')
    print("Random tensor:")
    print(x)
    
    # Using torch.jit for a simple operation
    @torch.jit.script
    def matrix_multiply(a, b):
        return torch.mm(a, b.t())
    
    y = matrix_multiply(x, x)
    print("Matrix multiplication result:")
    print(y)
    
    # Using torch.nn.functional for a more complex operation
    import torch.nn.functional as F
    z = F.relu(y)
    print("ReLU activation:")
    print(z)
    
    return {
        "random_tensor": x.tolist(),
        "matrix_multiplication": y.tolist(),
        "relu_activation": z.tolist()
    }

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        result = run_torch_operation()
        self.wfile.write(json.dumps(result).encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        # For debugging, just run the torch operation
        run_torch_operation()
        breakpoint()
    else:
        # For production, run the server
        run_server()
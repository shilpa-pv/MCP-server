from fastmcp import FastMCP
from fastmcp.transports.websocket import WebSocketServerTransport

app = FastMCP("demo")

@app.tool()
def ping():
    return "pong"

if __name__ == "__main__":
    transport = WebSocketServerTransport("localhost", 8080)
    app.run(transport)
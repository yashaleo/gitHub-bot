import os
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def main(request):
    return web.Response(status=200, text="Hello, world!")

# ✅ App setup moved outside the if block
app = web.Application()
app.add_routes(routes)

def run():
    port = int(os.environ.get("PORT", 5000))  # Heroku sets PORT
    web.run_app(app, port=port)

if __name__ == "__main__":
    run()

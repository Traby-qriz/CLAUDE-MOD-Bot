# File: features/auto_view_status.py

async def auto_view_status(client):
    @client.on_status_update()
    async def view_status(status):
        await status.view()
        print(f"Viewed status from {status.author}")
from app import app
import config

app.config.from_object(config)
app.run()

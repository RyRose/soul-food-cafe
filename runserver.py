import config
from app import app

app.config.from_object(config)

def main():
    app.run()

if __name__ == "__main__":
    main()

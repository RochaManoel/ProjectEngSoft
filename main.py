from model.server import Server

if __name__ == "__main__":
    serverAutoShop = Server('Auto Shop','0.0.0.0', 8000)
    serverAutoShop.start()
    
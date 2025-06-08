import os
import dotenv

dotenv.load_dotenv()


BOT_TOKEN = os.getenv('TOKEN')
ID_ADMIN = os.getenv('ID_ADMIN')
import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "22367430"))
    API_HASH = os.environ.get("API_HASH", "cd790f2f9ba414c2e7fd9d15a1f8a069")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5850969684:AAG6sMeY-YdYS6IGaFKbRW8H-LydJW8tMTQ") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "5710099312")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://afiqsam:afiqsam@cluster0.0wb1c.mongodb.net/afiqsam?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","afiqsam")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'TG_Files_Forward')
    SESSION = os.environ.get("SESSION", "BQB36cR6UPcN-1IPeBIh7MmUYFiiVS1zryJXvc5KiOGy8XRxTxAy2UipfkamBVTcE4fstZo-24MoxipHHiBCTCP6DdbePQ4XTy3xomZlIyWBYd4C_zqCAiwjfQQgGWTtxQ5V-aCwVA5GCjKPsUmgASz98G6REqNfQSVL6mi6BlXq-BJ9-2e_OtiR3RL_tGg4KG4678A8fXIpobQPcvBHdY0MWVwCIYuylXERPBb0WEX0blZWoDBgpa6SnR-6xIyUIOHIYTp_sz0zycqPSmxREkZu-Jp-L2-AZ02J4xgtPbH6C4U7lXhDRJ3Bq7LQqsnhxfnM79Xl5yEU-62rVun3CiYDAAAAAVRZM3AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001892469460"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

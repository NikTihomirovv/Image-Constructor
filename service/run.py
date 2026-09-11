import sys
import uvicorn
from config_loader import config

if __name__ == "__main__":
    sys.setrecursionlimit(config.RECURSION_LIMIT)
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
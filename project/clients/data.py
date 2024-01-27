import requests
import asyncio
import json
import multiprocessing
import enum

from check import Client

if __name__ == "__main__":
    
    c = Client(10, 2)
    c.run()
    # c.run_multiple(100)
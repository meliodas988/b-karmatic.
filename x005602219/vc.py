#///////imports\\\\\\\\#
import discord
import random
import json
from discord.ext import commands
import asyncio
import time
import requests
import os
from os import sys
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from datetime import datetime
from itertools import cycle
import aiohttp
from aiohttp import request
import math
import traceback
import praw
from webserver import keep_alive
from discord.utils import get
import youtube_dl



class Vc(commands.Cog):
    
    def __init__(self, client):

        self.client=client








def setup(client):
    client.add_cog(Vc(client))
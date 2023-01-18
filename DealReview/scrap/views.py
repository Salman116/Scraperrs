from django.shortcuts import render
import os
import pandas as pd

path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)


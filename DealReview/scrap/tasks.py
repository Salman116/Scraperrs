from __future__ import absolute_import, unicode_literals
from celery import shared_task
from scrap.codes.amli import amli
from scrap.codes.assetliving import assetliving
from scrap.codes.camden import camden
from scrap.codes.gables import gables
from scrap.codes.greystar import greystar
from scrap.codes.lincolnapts import lincolnapts
from scrap.codes.maac import maac
from scrap.codes.paycomonline import paycomonline
from scrap.codes.pinnade import pinnade
from scrap.codes.weidner import weidner
import os
import pandas as pd

path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)


@shared_task(name = "scrapper_runner")
def scrapper_runner_function(*args, **kwargs):
    amli_jobs = amli()
    df = pd.DataFrame.from_records(amli_jobs)
    df.to_csv(f"{path}/amli.csv")
    print("Updated Amli")
    
    assetliving_jobs = assetliving()
    df = pd.DataFrame.from_records(assetliving_jobs)
    df.to_csv(f"{path}/assetliving.csv")
    print("Updated AssetLiving")
    
    camden_jobs = camden()
    df = pd.DataFrame.from_records(camden_jobs)
    df.to_csv(f"{path}/camden.csv")
    print("Updated Camden")
     
    gables_jobs = gables()
    df = pd.DataFrame.from_records(gables_jobs)
    df.to_csv(f"{path}/gables.csv")
    print("Updated Gables")
    
    greystar_jobs = greystar()
    df = pd.DataFrame.from_records(greystar_jobs)
    df.to_csv(f"{path}/greystar.csv")
    print("Updated Greystar")
    
    lincolnapts_jobs = lincolnapts()
    df = pd.DataFrame.from_records(lincolnapts_jobs)
    df.to_csv(f"{path}/lincolnapts.csv")
    print("Updated Gincolnapts")
    
    maac_jobs = maac()
    df = pd.DataFrame.from_records(maac_jobs)
    df.to_csv(f"{path}/maac.csv")
    print("Updated Maac")
    
    paycomonline_jobs = paycomonline()
    df = pd.DataFrame.from_records(paycomonline_jobs)
    df.to_csv(f"{path}/paycomonline.csv")
    print("Updated Paycomonline")
    
    pinnade_jobs = pinnade()
    df = pd.DataFrame.from_records(pinnade_jobs)
    df.to_csv(f"{path}/pinnade.csv")
    print("Updated Pinnade")
    
    weidner_jobs = weidner()
    df = pd.DataFrame.from_records(weidner_jobs)
    df.to_csv(f"{path}/weidner.csv")
    print("Updated Weidner")
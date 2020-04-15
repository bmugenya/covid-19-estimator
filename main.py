from fastapi import FastAPI,Request,Form
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.estimator import *

class COVID19(BaseModel):
    name : str = "Africa"
    avgAge : float = 19.7
    avgDailyIncomeInUSD: int = 5
    avgDailyIncomePopulation: float =  0.71
    periodType : str ="days"
    timeToElapse :int = 58
    reportedCases : int = 674
    population: int = 66622705
    totalHospitalBeds: int = 1380614


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

report = COVID19()

@app.get("/api/v1/on-covid-19")
async def review(request:Request):
    data = {
    'data' : {
    'region' : {
       'name' : report.name,
        'avgAge' : report.avgAge,
        'avgDailyIncomeInUSD': report.avgDailyIncomeInUSD,
        'avgDailyIncomePopulation':  report.avgDailyIncomePopulation
    },
        'periodType' : report.periodType,
        'timeToElapse' : report.timeToElapse,
        'reportedCases': report.reportedCases,
        'population':  report.population,
        'totalHospitalBeds': report.totalHospitalBeds
    }
    }

    result = estimator(data['data'])
    return templates.TemplateResponse("index.html", {'request':request,'data':data['data'],'impact':result['impact'],'sever':result['severeImpact']})

@app.post("/api/v1/on-covid-19")
async def addReport(request:Request,
                     population = Form("population"),
                    timeToElapse = Form('timeToElapse'),
                    reportedCases = Form('reportedCases'),
                    totalHospitalBeds = Form('totalHospitalBeds'),
                    periodType  = Form('periodType')
                    ):
    data = {
        'data' : {
            'region' : {
               'name' : report.name,
                'avgAge' : report.avgAge,
                'avgDailyIncomeInUSD': report.avgDailyIncomeInUSD,
                'avgDailyIncomePopulation':  report.avgDailyIncomePopulation
            },
                'periodType' : periodType,
                'timeToElapse' : int(timeToElapse),
                'reportedCases': int(reportedCases),
                'population':  int(population),
                'totalHospitalBeds': int(totalHospitalBeds)
            }
    }

    result = estimator(data['data'])
    return templates.TemplateResponse("index.html",  {'request':request,'data':data['data'],'impact':result['impact'],'sever':result['severeImpact']})






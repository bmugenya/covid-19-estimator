from fastapi import FastAPI
from pydantic import BaseModel
from estimator import *

class COVID19(BaseModel):
    name : str = "Africa"
    avgAge : float = 19.7
    avgDailyIncomeInUSD: int =5
    avgDailyIncomePopulation: float =  0.71
    periodType : str ="days"
    timeToElapse :int = 58
    reportedCases : int = 674
    population: int = 66622705
    totalHospitalBeds: int = 1380614


app = FastAPI()


@app.post("/api/v1/on-covid-19")
async def review(report:COVID19):
    data = {
       'name' : report.name,
        'avgAge' : report.avgAge,
        'avgDailyIncomeInUSD': report.avgDailyIncomeInUSD,
        'avgDailyIncomePopulation':  report.avgDailyIncomePopulation,
        'periodType' : report.periodType,
        'timeToElapse' : report.timeToElapse,
        'reportedCases': report.reportedCases,
        'population':  report.population,
        'totalHospitalBeds': report.totalHospitalBeds
    }


    result = estimator(report.reportedCases,report.totalHospitalBeds)
    return data,result


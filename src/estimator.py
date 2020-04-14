def estimator(data):
    name = data['region']['name']
    avgAge= data['region']['avgAge']
    avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
    periodtype = data['periodType']
    timeToElapse = data['timeToElapse']
    population = data['population']
    reportedCases = data['reportedCases']
    totalHospitalbeds = data['totalHospitalBeds']

    impactt = impact(reportedCases, periodtype,avgDailyIncomePopulation,population)
    severe = severeImpact(reportedCases,periodtype,totalHospitalbeds,avgDailyIncomePopulation,population)
    return {"data":data,"impact":impactt,"severeImpact":severe}



def duration(periodtype):
    if periodtype == 'days':
      days =  1
    elif periodtype == 'weeks':
      days = 7
    elif periodtype == 'months':
      days = 30
    return days


def impact(reportedCases, periodtype,avgDailyIncomePopulation,population):
    currentlyInfected = reportedCases * 10
    factor = duration(periodtype) // 3
    infectionsByRequestedTime = currentlyInfected * (2**factor)
    region = (currentlyInfected / population) * 100

    return  {
        "currentlyInfected" :  currentlyInfected,
        "infectionsByRequestedTime" : infectionsByRequestedTime,
         "dollarsInFlight": (infectionsByRequestedTime * region ) * avgDailyIncomePopulation *  duration(periodtype)

}

def severeImpact(reportedCases,periodtype,totalHospitalbeds,avgDailyIncomePopulation,population):
    currentlyInfected = reportedCases * 50
    factor = duration(periodtype) // 3
    infectionsByRequestedTime = currentlyInfected * (2**factor)
    severCasesByRequestedTime = infectionsByRequestedTime * (15 / 100)
    totalHospitalbeds = totalHospitalbeds * (35 / 100)
    region = (currentlyInfected / population) * 100

    return  {
        "currentlyInfected" : currentlyInfected,
        "severCasesByRequestedTime"  : int(severCasesByRequestedTime),
        "hospitalBedsByRequestedTime" : int(totalHospitalbeds - severCasesByRequestedTime),
        "casesForICUByRequestedTime": int(infectionsByRequestedTime * (5 / 100)),
        "casesForVentilatorsByRequestedTime": int(infectionsByRequestedTime * (2 / 100)),
        "dollarsInFlight": (infectionsByRequestedTime * region ) * avgDailyIncomePopulation *  duration(periodtype)
    }






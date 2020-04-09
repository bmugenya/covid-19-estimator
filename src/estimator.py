def impact(reportedCases):
    currentlyInfected = reportedCases * 10
    infectionsByRequestedTime = currentlyInfected * (2**10)

    impact =  {
        "currentlyInfected" :  currentlyInfected,
        "infectionsByRequestedTime" : infectionsByRequestedTime,
       "dollarsInFlight ": (infectionsByRequestedTime * 0.65 ) * 1.5 * 30

    }
    return impact

def serverImpact(reportedCases,totalHospitalbeds):

    severeImpact = reportedCases * 50
    infectionsByRequestedTime = severeImpact  * (2**10)

    sever =  {
        "severeImpact" : severeImpact,
        "severCasesByRequestedTime"  : infectionsByRequestedTime * (100 / 15),
        "hospitalBedsByRequestedTime" : totalHospitalbeds * (95 / 35),
        "casesForICUByRequestedTime": infectionsByRequestedTime * (100 / 5),
        "casesForVentilatorsByRequestedTime": infectionsByRequestedTime * (100 / 2),
        "dollarsInFlight": (infectionsByRequestedTime * 0.65 ) * 1.5 * 30
    }

    return sever


def estimator(reportedCases,totalHospitalbeds):
    impactt = impact(reportedCases)
    sever = serverImpact(reportedCases,totalHospitalbeds)
    return impactt,sever

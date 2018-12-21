const fs = require('fs')

var util = require('util')

var jsonfile = require('./xml_2018_12_17.json')

var airlineInfo = jsonfile["FareInterface"]["Output"]["Result"]["FlightShopResult"]["AvJourneys"]["AvJourney"]["AvOpt"]
var psinfo = jsonfile["FareInterface"]["Output"]["Result"]["FlightShopResult"]["PSn"]["PS"]

airlineDict = {}
pslist = []

for (i in airlineInfo) {
    airlineDict[airlineInfo[i]['Flt']["airline"] + airlineInfo[i]['Flt']['fltNo']] = airlineInfo[i]['Flt']
}

for (i in psinfo) {
    routsinfo = psinfo[i]['Routs']
    if (util.isArray(routsinfo)) {
        for (subitem in routsinfo) {
            var temp = routsinfo[subitem]["Rout"]
            if ('codeshare' in airlineDict[temp['carr'] + temp['fltNo']]) {
                temp['codeshare'] = airlineDict[temp['carr'] + temp['fltNo']]['codeshare']['airline'] + airlineDict[temp['carr'] + temp['fltNo']]['codeshare']['fltno']
            }
            temp['yFareAmount'] = psinfo[i]['FCs']['FC']['YFares']['yFareAmount']
            pslist.push(temp)
        }
    } else {
        var temp = routsinfo["Rout"]
        if ('codeshare' in airlineDict[temp['carr'] + temp['fltNo']]) {
            temp['codeshare'] = airlineDict[temp['carr'] + temp['fltNo']]['codeshare']['airline'] + airlineDict[temp['carr'] + temp['fltNo']]['codeshare']['fltno']
        }
        temp['yFareAmount'] = psinfo[i]['FCs']['FC']['YFares']['yFareAmount']
        pslist.push(temp)
    }
}

fs.appendFileSync('./csv_2018_12_17.csv', 'carr,fltNo,bkClass,OI,departureDate,departureTime,arrivalDate,arrivalTime,departureAirport,arrivalAirport,codeshare,yFareAmount\n')
for (i in pslist) {
    // console.log(pslist[i])
    fs.appendFileSync('./csv_2018_12_17.csv', pslist[i]['carr'] + ',' + pslist[i]['fltNo'] + ',' + pslist[i]['bkClass'] + ',' + pslist[i]['OI'] + ',' + pslist[i]['departureDate'] + ',' + pslist[i]['departureTime'] + ',' + pslist[i]['arrivalDate'] + ',' + pslist[i]['arrivalTime'] + ',' + pslist[i]['departureAirport'] + ',' + pslist[i]['arrivalAirport'] + ',' + pslist[i]['codeshare'] + ',' + pslist[i]['yFareAmount'] + '\n')
}

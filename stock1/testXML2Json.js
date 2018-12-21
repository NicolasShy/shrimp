const parseString = require('xml2js').parseString
const fs = require('fs')

// 把xml字段转化为json
let xml2Json = (xml) => {
	return new Promise((resolve, reject) => {
		parseString(xml, {
			explicitArray: false
		}, function (error, result) {
			if (error) {
				reject(error)
			} else {
				resolve(result)
			}
		})
	})
}


xml2Json(fs.readFileSync('./xml_2018_12_17.xml')).then(result => {
    console.log(JSON.stringify(result))
    fs.appendFileSync('./xml_2018_12_17.json', JSON.stringify(result))
})
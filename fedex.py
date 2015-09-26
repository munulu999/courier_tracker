import requests
import json

class crawler:
	def fedex_crawler(self,tracking_id):
		headers = {}
		url = "https://www.fedex.com/trackingCal/track"

		headers = {'Referer': "https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber="+str(tracking_id)+"&cntry_code=us"}
		headers['User-Agent']= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36"
		headers['Accept'] = "*/*"
		headers['Accept-Encoding'] = "gzip, deflate"
		headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
		headers['DNT'] = "1"
		
		payload = {'data' : json.dumps({"TrackPackagesRequest":{"appType":"WTRK","uniqueKey":"","processingParameters":{},"trackingInfoList":[{"trackNumberInfo":{"trackingNumber":"618571001700","trackingQualifier":"","trackingCarrier":""}}]}})}
		payload['action'] = "trackpackages"
		payload['locale'] = "en_US"
		payload['version'] = "1"
		payload['format'] = "json"
		client = requests.session()
		data = client.post(url, headers= headers, data = payload)
		
		if (data.status_code==200):
			data = data.json()
			data = data['TrackPackagesResponse']
			if data['successful']==True:
				data = data['packageList']
				for package in data:
					print (package['trackingNbr'])
					print (package['trackingCarrierDesc'])
					print (package['shipperCntryCD'])
					print (package['recipientCity'])
					print (package['recipientCntryCD'])
					print (package['keyStatus'])
					print (package['shipDt'])
					print (package['pickupDt'])
					print (package['displayTotalWgt'])
					print (package['serviceDesc'])
					print (package['specialHandlingServicesList'])

					for event in package['scanEventList']:
						print (event['date'])
						print (event['time'])
						print (event['gmtOffset'])
						print (event['status'])
						print (event['statusCD'])
						print (event['scanLocation'])
						print (event['scanDetails'])
						print (event['rtrnShprTrkNbr'])
						print (event['isException'])
						print (event['isDelException'])
						print (event['isClearanceDelay'])
						print (event['isDelivered'])


					

					print (package['originCity'])
					print (package['originStateCD'])
					print (package['originZip'])
					print (package['originCntryCD'])
					print (package['destLocationCity'])
					print (package['destLocationStateCD'])
					print (package['destLocationZip'])
					print (package['destLocationCntryCD'])
			




def main():
	craw = crawler()
	craw.fedex_crawler(618568856172)


main()
import requests



def ob_havo(shahar):
	url = "https://yahoo-weather5.p.rapidapi.com/weather"
	querystring = {"location": f"{shahar}", "format": "json", "u": "c"}
	headers = {
		"X-RapidAPI-Key": "49ef7ea530mshb0e75622c84a9d2p16b7cfjsn8a8797a5ba72",
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	temperatura = response.json()["current_observation"]["condition"]["temperature"]
	qchiq = response.json()["current_observation"]["astronomy"]["sunrise"]
	qbot = response.json()["current_observation"]["astronomy"]["sunset"]
	min = response.json()['forecasts'][0]["low"]
	max = response.json()['forecasts'][0]["high"]
	text = response.json()['forecasts'][0]["text"]
	day = response.json()['forecasts'][0]["day"]
	addres = response.json()["location"]['city']
	addres1 = response.json()["location"]['country']


	if day == 'Thu':
		kun = 'Payshanba'
	elif day == 'Fri':
		kun = 'Juma'
	elif day == 'Sat':
		kun = 'Shanba'
	elif day == 'Sun':
		kun = 'Yakshanba'
	elif day == 'Mon':
		kun = 'Dushanba'
	elif day == 'Tue':
		kun = 'Seshanba'
	elif day == 'Wed':
		kun = 'Chorshanba'

	return f"Bugun: {kun} \n Havo: {text} \n🌡Harorat: {max}°...{min}° \n🌡Hozir: {temperatura} °c \n" \
		   f"⏱ Quyosh chiqishi: {qchiq} \n⏱ Quyosh botishi: {qbot} \n\n 👉 @Ob_havoKbot \n\n📍 city: {addres} | country: {addres1}"


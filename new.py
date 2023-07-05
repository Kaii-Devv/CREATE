"""
SC FREEE DI BUAT OLEH TAMSIS
"""


import requests,re,bs4,os,time,random
from bs4 import BeautifulSoup as parse
from bs4 import BeautifulSoup as par
from fake_email import Email
sess=requests.Session()
nama='tamsis+rob'
pw="muhamad123"
while True:
	try:
		ua="Mozilla/5.0 (Linux; Android "+str(random.randrange(4,6))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
		ses=requests.Session()
		buat=Email().Mail()
		nomer=buat["mail"]
		
#		nomer=input("nomer acak : ")

		print("email akun : "+nomer)
		login=ses.get("https://free.facebook.com/reg")
		lsd=re.search('name="lsd" value="(.*?)"',str(login.text)).group(1)
		jazo=re.search('name="jazoest" value="(.*?)"',str(login.text)).group(1)
		inta=re.search('name="reg_instance" value="(.*?)"',str(login.text)).group(1)
		impres=re.search('name="reg_impression_id" value="(.*?)"',str(login.text)).group(1)
		data=f"lsd={lsd}&jazoest={jazo}&ccp=2&reg_instance={inta}&submission_request=true&helper=&reg_impression_id={impres}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names[]=firstname&field_names[]=reg_email__&field_names[]=sex&field_names[]=birthday_wrapper&field_names[]=reg_passwd__&firstname={nama}&reg_email__={nomer}&sex=2&custom_gender=male&did_use_age=false&birthday_day={random.randrange(1,28)}&birthday_month={random.randrange(1,13)}&birthday_year={random.randrange(1970,2000)}&age_step_input=&reg_passwd__={pw}&submit=Daftar"
		koki = (";").join([ "%s=%s" % (key, value) for key, value in login.cookies.get_dict().items() ])
		koki+=';m_pixel_ratio=2.625;wd=412x756'
		head={
    "Host": "m.facebook.com",
    "content-length": str(len(data)),
    "cache-control": "max-age=0",
    "viewport-width": "980",
    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-platform-version": '"9.0.0"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
    "sec-ch-prefers-color-scheme": "light",
    "upgrade-insecure-requests": "1",
    "origin": "https://mbasic.facebook.com",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://mbasic.facebook.com/reg/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		gas=ses.post("https://m.facebook.com/reg/submit/",data=data,headers=head,cookies={"cookie":koki})
		kon=ses.get("https://m.facebook.com")
		if "checkpoint" in str(kon.url):
			print("gagal create akun,coba pancing ubah email menggunalan nomer tlpn acak")
			continue
		else:pass
		print("BERHASIL BUAT AKUN")
		para=parse(kon.text,"html.parser")
		data2={}
		for gg in para("input"):
			if None in {gg.get("name")}:pass
			else:data2.update({gg.get("name"):gg.get("value")})
		link=para.find("form",{"method":"post"}).get("action")
		time.sleep(10)
		while True:
			print("\rMenunggu kode.....",end="\r")
			mess=Email(buat["session"]).inbox()
			if mess:
				c=mess['topic'].split(' ')[0].replace("FB-","")
				data2.update({"c":c})
				break
		heads={
    "Host": "m.facebook.com",
    "content-length": str(len(str(data2))),
    "cache-control": "max-age=0",
    "viewport-width": "980",
    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-platform-version": '"9.0.0"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
    "sec-ch-prefers-color-scheme": "light",
    "upgrade-insecure-requests": "1",
    "origin": "https://m.facebook.com",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": kon.url,
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		yes=ses.post("https://m.facebook.com"+link,headers=heads,data=data2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		print("COOKIES : "+coki+';m_pixel_ratio=2.625;wd=412x756')		
		open("coki.txt","a").write(coki+";m_pixel_ratio=2.625;wd=412x756\n")
		login=ses.get("https://mbasic.facebook.com")
		pars=par(login.text,"html.parser")
		for gg in pars.find_all("a",href=True):
			if "Tidak, Terima Kasih" in gg.text:
				gas=ses.get("https://mbasic.facebook.com"+gg["href"].replace("https://mbasic.facebook.com",""))
				gass=par(gas.text,"html.parser")
				link=gass.find("form",{"method":"post"})
				data={}
				for lan in gass("input"):
					data.update({lan.get("name"):lan.get("value")})
				head={
    "Host": "mbasic.facebook.com",
    "content-length": str(len(str(data))),
    "cache-control": "max-age=0",
    "viewport-width": "980",
    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-platform-version": '"9.0.0"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
    "sec-ch-prefers-color-scheme": "light",
    "upgrade-insecure-requests": "1",
    "origin": "https://mbasic.facebook.com",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": gas.url,
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				ses.post("https://mbasic.facebook.com"+link.get("action").replace("https://mbasic.facebook.com",""),headers=head,data=data)
		cari=ses.get("https://mbasic.facebook.com")
		lanj=par(cari.text,"html.parser")
		for gg in lanj.find_all("a",href=True):
			if "Selanjutnya"in gg.text:
				lan=ses.get("https://mbasic.facebook.com"+gg["href"].replace("https://mbasic.facebook.com",""))
				pas=par(lan.text,"html.parser")
				for gc in pas.find_all("a",href=True):
					if "Selanjutnya"in gg.text:
						la=ses.get("https://mbasic.facebook.com"+gc["href"].replace("https://mbasic.facebook.com",""))

	#UNTUK CREATE TOKEN
	
#		data={};data2={}
#		link=ses.post('https://graph.facebook.com/v16.0/device/login/', data={'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e', 'scope': ''}).json()
#		kode,user = link['code'],link['user_code']
#		vers = parse(ses.get(f'https://mbasic.facebook.com/device').content, 'html.parser')
#		item = ['fb_dtsg','jazoest','qr']
#		for x in vers.find_all('input'):
#			if x.get('name') in item:
#				aset = {x.get('name'):x.get('value')}
#				data.update(aset)
#		data.update({'user_code':user})
#		meta = parse(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data).text, 'html.parser')
#		xzxz  = meta.find('form',{'method':'post'})
#		for x in xzxz('input',{'value':True}):
#			try:
#				if x['name'] == '__CANCEL__' : pass
#				else:
#					data2.update({x['name']:x['value']})
#			except Exception as e:pass
#		ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2)
#		token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e').json()['access_token']
#		print("TOKEN: "+str(token))
		try:
			fol=["100066790856758"]
			fl=0
			for user in fol:
				for response in par(ses.get(f'https://mbasic.facebook.com/'+user).text,'html.parser').find_all('a',href=True):
					if '/a/subscribe.php?' in response.get('href'):x=ses.get('https://mbasic.facebook.com{}'.format(response['href'])).text;fl+=1
		except:time.sleep(20)
		print(f"berhasil follow {fl} akun")
		try:
			res=ses.get("https://mbasic.facebook.com/100066790856758/posts/pfbid0WFjmrCzgunSKzicfqxYRMUdqJx6pUZztVeMJ2rKo7KsPHdTs1yLgpzoQTW8VqvZbl/?app=fbl")
			log=par(res.text,"html.parser")
			link="https://mbasic.facebook.com"+log.find("form",{"method":"post"}).get("action")
			data={}
			for z in log.find_all("a",href=True):
				if z.text in ["Suka","Like"]:
					if "/a/like.php?" in z.get("href"):ses.get("https://mbasic.facebook.com"+z["href"].replace("https://mbasic.facebook.com",""));print("berhasil like")
					else:pass
				else:continue
			kom=random.choice(["Bang+tamsis+ganteng+banget","Hai+bang"])
			data={}
			res=ses.get("https://mbasic.facebook.com/pfbid02Zw9XjkxUDfi1JEwZ6t2q598vrUpgUCvgbqpnW84Ba5GfV27Wtz6XjcbSsZ8uKBqhl")
			log=par(res.text,"html.parser")
			link="https://mbasic.facebook.com"+log.find("form",{"method":"post"}).get("action")
			heado={"Host": "mbasic.facebook.com","content-length": "111","cache-control": "max-age=0","viewport-width": "980","sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"sec-ch-ua-platform-version": '"9.0.0"',"sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',"sec-ch-prefers-color-scheme": "light","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer":str(res.url),"accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			for date in log("input"):data.update({date.get("name"):date.get("value")})
			ko=0
			for i in range(10):ses.post(link,headers=heado,data="fb_dtsg="+data["fb_dtsg"]+"&jazoest="+data["jazoest"]+"&comment_text="+kom);ko+=1
		except:time.sleep(10)
		print(f"berhasil kirim {ko} komen")
		try:
			log=ses.get("https://mbasic.facebook.com/profile/basic/intro/bio/")
			dita={}
			login=par(log.text,"html.parser")
			for dat in login("input"):
				if dat.get("name") in ["fb_dtsg","jazoest"]:
					dita.update({dat.get("name"):dat.get("value")})
			dita.update({"bio":"Akun Ini di buat oleh bot TamsisSlebew"})
			heado.update({"referer": log.url})
			ses.post("https://mbasic.facebook.com/profile/intro/bio/save/",headers=heado,data=dita)
		except:pass
		print("berhasil ubah bio")
		kir=par(ses.get("https://www.facebook.com/milah.hujaemah").text,"html.parser")
		kikir=0
		for x in kir.find_all("a",href=True):
			try:
				if "/a/friends" in str(x["href"]):
					ses.get("https://mbasic.facebook.com"+x["href"])
					kikir+=1
			except:time.sleep(10)
		print(f"berhasil add {kikir} teman")
	except requests.exceptions.ConnectionError:time.sleep(31)
	except Exception as e:
		if 'permalink' in str(e):
			continue
		else:
			print("gagal kirim bot")
			continue
#

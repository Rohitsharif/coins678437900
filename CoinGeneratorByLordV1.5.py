PasswordForAllEmails="rohit101"
community_Link="http://aminoapps.com/invite/7SVTQ52EFR"
import os, time, random, hmac, base64;from hashlib import sha1
try:import requests,json;from json_minify import json_minify;from colorama import Style,Fore;from pyfiglet import figlet_format;from flask import Flask;from threading import Thread
except:os.system("pip install requests json-minify colorama flask pyfiglet");print("RestartTheScript")
A = "\033[1;91m"  ;E = "\033[1;92m";H = "\033[1;93m";L = "\033[1;95m";X = '\033[2;36m';M = "\033[1;94m";B = "\033[1;90m";C = "\033[1;97m";select = input(f"1-accounts.json\n2-emails.txt\nselect:")
app = Flask('')
@app.route('/')
def home():
	return 'Im in!'
def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000))
def keep_alive():
	t = Thread(target=run)
	t.start()
class Main:
	def __init__(self):
		self.time = self.time();self.device = self.device();self.api = "https://service.narvii.com/api/v1";self.headers = {"NDCDEVICEID": self.device, "SMDEVICEID": "b89d9a00-f78e-46a3-bd54-6507d68b343c", "Accept-Language": "en-EN", "Content-Type": "application/json; charset=utf-8", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)", "Host": "service.narvii.com", "Accept-Encoding": "gzip", "Connection": "keep_alive"};self.comId =int(self.comId(community_Link)['linkInfoV2']['extensions']['community']['ndcId']);self.sid = None
	def time(self):
		hour=time.strftime("%H", time.gmtime()); minute=time.strftime("%M", time.gmtime());
		UTC={"GMT0":'+0', "GMT1":'+60', "GMT2":'+120', "GMT3":'+180', "GMT4":'+240', "GMT5":'+300', "GMT6":'+360', "GMT7":'+420', "GMT8":'+480', "GMT9":'+540', "GMT10":'+600', "GMT11":'+660', "GMT12":'+720', "GMT13":'+780', "GMT-1":'-60', "GMT-2":'-120', "GMT-3":'-180',"GMT-4":'-240', "GMT-5":'-300', "GMT-6":'-360', "GMT-7":'-420', "GMT-8":'-480', "GMT-9":'-540', "GMT-10":'-600', "GMT-11":'-660'}; Hour = [hour, minute]
		if Hour[0]=="00":tz=UTC["GMT-1"];return int(tz)
		if Hour[0]=="01":tz=UTC["GMT-2"];return int(tz)
		if Hour[0]=="02":tz=UTC["GMT-3"];return int(tz)
		if Hour[0]=="03":tz=UTC["GMT-4"];return int(tz)
		if Hour[0]=="04":tz=UTC["GMT-5"];return int(tz)
		if Hour[0]=="05":tz=UTC["GMT-6"];return int(tz)
		if Hour[0]=="06":tz=UTC["GMT-7"];return int(tz)
		if Hour[0]=="07":tz=UTC["GMT-8"];return int(tz)
		if Hour[0]=="08":tz=UTC["GMT-9"];return int(tz)
		if Hour[0]=="09":tz=UTC["GMT-10"];return int(tz)
		if Hour[0]=="10":tz=UTC["GMT13"];return int(tz)
		if Hour[0]=="11":tz=UTC["GMT12"];return int(tz)
		if Hour[0]=="12":tz=UTC["GMT11"];return int(tz)
		if Hour[0]=="13":tz=UTC["GMT10"];return int(tz)
		if Hour[0]=="14":tz=UTC["GMT9"];return int(tz)
		if Hour[0]=="15":tz=UTC["GMT8"];return int(tz)
		if Hour[0]=="16":tz=UTC["GMT7"];return int(tz)
		if Hour[0]=="17":tz=UTC["GMT6"];return int(tz)
		if Hour[0]=="18":tz=UTC["GMT5"];return int(tz)
		if Hour[0]=="19":tz=UTC["GMT4"];return int(tz)
		if Hour[0]=="20":tz=UTC["GMT3"];return int(tz)
		if Hour[0]=="21":tz=UTC["GMT2"];return int(tz)
		if Hour[0]=="22":tz=UTC["GMT1"];return int(tz)
		if Hour[0]=="23":tz=UTC["GMT0"];return int(tz)
	def sig(self, data):
		return base64.b64encode(bytes.fromhex("42") + hmac.new(bytes.fromhex("F8E7A61AC3F725941E3AC7CAE2D688BE97F30B93"), data.encode("utf-8"), sha1).digest()).decode("utf-8")
	def device(self):
		identifier = os.urandom(20)
		return ("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()
	def log(self, email: str, password: str):
		print(self.device)
		data = json.dumps({"email": email, "secret": f"0 {password}", "deviceID": self.device, "clientType": 100, "action": "normal", "timestamp": (int(time.time() * 1000))})
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/g/s/auth/login", data = data, headers = self.headers)
		try:self.sid = request.json()["sid"]
		except:pass
		return request.json()
	def comId(self, community_Link):
		return requests.get(f'{self.api}/g/s/link-resolution?q={community_Link}',headers = self.headers).json()
	def join(self, comId: int):
		data = json.dumps({"timestamp": int(time.time()*1000)})
		self.headers["NDC-MSG-SIG"] = self.sig(data=data)
		request = requests.post(f"{self.api}/x{comId}/s/community/join?sid={self.sid}", data = data, headers = self.headers)
		return request.json()
	def check_in(self, comId: int, timezone: int):
		data = json.dumps({"timezone": timezone, "timestamp": int(time.time() * 1000)})
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/x{comId}/s/check-in/lottery?sid={self.sid}", data = data, headers = self.headers)
		return request.json()
	def send_time(self, comId: int, start: int = None, end: int = None, timers: list = None, timezone: int=None ):
		data = {"userActiveTimeChunkList": [{"start": start, "end": end}], "timestamp": int(time.time() * 1000), "optInAdsFlags": 2147483647, "timezone": timezone}
		if timers: data["userActiveTimeChunkList"] = timers
		data = json_minify(json.dumps(data))
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/x{comId}/s/community/stats/user-active-time?sid={self.sid}", data = data, headers = self.headers)
		return request.json()
class Run:
	def __init__(self):
		self.client = Main()
		self.comId = self.client.comId
	def run(self, email: str, password :  str):
		try:
			print(f'{X}[Login]{A}[{email}]{C}[{self.client.log(email,password)["api:message"]}]')
			print(f'{L}[join_community]{C}[{self.client.join(comId=self.comId)["api:message"]}]')
			print(f'{E}[Check_In]{C}[{self.client.check_in(comId=self.comId,timezone=self.client.time)["api:message"]}]')
			for i in range(24):
				print(f'{A}[GeneratorCoin]{X}[{i+1} Times]{C}[{self.client.send_time(comId = self.comId, timers = [{"start": int(time.time()), "end": int(time.time()) + 180}for i in range(20)],timezone=self.client.time)["api:message"]}]')
				time.sleep(12)
		except Exception as e:print(e);pass
	def main(self):
		os.system("clear")
		print(f'{X}{figlet_format("CoinGeneratorBy Lord", font="doom", width=70)}')
		if select=="1":
			accs = json.load(open("accounts.json"))
			for acc in accs:
				email = acc["email"]
				password = acc["password"]
				self.client.device = acc["device"]
				self.client.headers["NDCDEVICEID"] = self.client.device
				self.run(email,password)
		if select=="2":
			password = PasswordForAllEmails
			emails = open("emails.txt")
			for email in emails:
				email = email.strip()
				self.run(email,password)
if __name__=='__main__':
	while True:
		keep_alive()
		Run().main()
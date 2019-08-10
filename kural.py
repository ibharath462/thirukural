import csv
import json

with open ('detail.json',"rb") as f:
	detailsJSON = json.load(f);

detailPaal = detailsJSON[0].get('section').get("detail");

def getDesc(paaal,kCount) :
	adhigaramName = "";
	eyalName = "";
	eyalArray = detailPaal[paaal].get("chapterGroup").get("detail");
	for eyal in eyalArray:
		eyalName = str(eyal.get('name'));
		adhigaramArray = eyal.get('chapters').get("detail");
		for adhigaram in adhigaramArray:
			aStart = adhigaram.get("start");
			aEnd = adhigaram.get("end");
			if kCount >= aStart and kCount <= aEnd:
				adhigaramName = str(adhigaram.get("name"));
				return eyalName + "-" + adhigaramName;

with open ('thirukkural.json',"rb") as f:
	data = json.load(f);

json_new = [];
paal = 0;

for kural in data['kural']:
	no = int(kural.get('Number'));
	#Paal separation
	if no <= 380 :
		kural.update({"paal":"அறத்துப்பால்"});
		paal = 0;
	elif no > 380 and no <= 1080 :
		kural.update({"paal":"பொருட்பால்"});
		paal = 1;
	else :
		kural.update({"paal":"காமத்துப்பால்"});
		paal = 2;
	result = getDesc(paal,no);
	eyal = result.rsplit('-',1)[0];
	adhigaram = result.rsplit('-',1)[1];
	kural.update({"iyal":str(eyal)})
	kural.update({"agaradhi":str(adhigaram)})
	kural.update({"amma":""})
	json_new.append(kural);

with open('updated.json', 'w') as update_json:
    json.dump(json_new, update_json)
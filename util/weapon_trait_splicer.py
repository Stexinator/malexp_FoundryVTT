import csv
import re

advanceRegEx = re.compile(r"([\d]) Advance[s]? in ([\w]*)(\(([\w -–,]*)\))?(,| and| or)?")
talentRegEx = re.compile(r"([\w ’]*)(\([\w ]*\))? Talent")


with open("src_w_rules.csv", encoding="utf-8", newline='') as csvfile:
  dictreader = csv.DictReader(csvfile)
  is_first = True
  for row in dictreader:
    # foreach row
    col_names = dictreader.fieldnames
    for row in dictreader:
      for col in col_names:
        if(not col == "Prerequisites"):
          continue
        advanceReqMatch = advanceRegEx.findall(row[col])
        talentMatches = talentRegEx.findall(row[col])
        rules = ""
        skill_req = []
        spec_req = []
        talent_req = []
        for m in advanceReqMatch:
          if(not m[0]):
            continue
          if(not m[2]):
            skill_req.append("this.actor.system.skills.{}.advances >= {}".format(m[1].lower(), m[0]))
          else:
            spec_req.append(r'(this.actor.itemTypes["specialisation"].find(i => i.name == "{}" && i.system.skill == "{}")?.system?.advances >= {})'.format(m[3], m[1].lower(), m[0]))
        for m in talentMatches:
          if(not m[0]):
            continue
          talent_req.append('this.actor.itemTypes["talent"].find(i => i.name == "{}")'.format(m[0].strip()+m[1].strip()))
        #print("SkillReq: {} || SpecReq: {} || TalentReq: {}".format(skill_req, spec_req, talent_req))
        if(not skill_req and not spec_req and not talent_req):
          print()
        else:
          print('return ' + " && ".join(skill_req + spec_req + talent_req))
import re
import json
import sys
# 0:attack, 1:trojan, 2:http


def getFileName(flag):
    if flag == 0:
        return 'nznids_attack.rules'
    elif flag ==1:
        return 'nznids_trojan.rules'
    elif flag ==2:
        return 'trojanRule/http.json'
    elif flag ==3:
        return 'trojanRule/tcp.json'
    elif flag == 4:
        return 'all.rules'
    else:
        return 'trojanRule/' + flag + '.json'
        print("Print 0/1")


def loadRuleFile(inFileName):
    with open(inFileName, 'r') as f:
        data = json.load(f)
    return data


def readAllRuleFile(inFileName):
    with open(inFileName, 'r') as f:
        data = f.readlines()
    return data



def writeRule(prt, newDict, outFileName):
    # fileName = ''
    # filePath = getFilePath(flag)
    # if flag == 1:
    #     # fileName = "./" + filePath + 'total/' + prt + ".json"
    #     fileName = "./" + filePath + prt + ".json"
    #
    # elif flag ==2:
    #     fileName = "./jcqTojan.json"
    # else:
    #     fileName = "./" + filePath + flag + "/" + prt + ".json"

    with open(outFileName, "w") as f:
        json.dump(newDict, f)


def jcq2All(inFileName, outFilename):
    data = loadRuleFile(inFileName)
    with open(outFilename, 'w') as allRule:
        for item in data:
            ruleString = item['rule'].\
                replace("classtype-danger", "classtype").\
                replace("tid", "sid")
            # replace('msg:\\\"', 'msg:\"').\
            # replace('\\\";', '\";').\
            # replace('content:\\\"', 'content:\"').\
            allRule.write(ruleString + "\n")


def all2Jcq(inFileName, outFilename):
    data = readAllRuleFile(inFileName)
    fileName = "./jcqTrojan.rules"
    result = []
    for item in data:
        risk = 1
        store_pcap = 0
        msg = re.search('\(msg:"(.*?)";', item).group(1)
        rule = item.replace("classtype", "classtype-danger").replace("; tid:", "; sid:").rstrip()
        trojan_id = 0
        os = ""
        rule_id = 0
        desc = ""
        line = {"risk": risk,
                "store_pcap": store_pcap,
                "trojan_name": msg,
                "rule": rule,
                "trojan_id": trojan_id,
                "os": os,
                "rule_id": rule_id,
                "desc": desc
                }
        result.append(line)
    print(type(result))
    writeRule('', result, outFilename)


if __name__ == "__main__":
    params = sys.argv
    print('''example1 : python ruleFormat.py toZnids txtStyleFilePath jsonStyleFilePath \nexample2 : python ruleFormat.py fromZnids jsonStyleFilePath txtStyleFilePath''')
    if params[1].lower() == 'toznids':
        all2Jcq(params[2], params[3])
        print('You have completed the conversion from  txtStyleFile to jsonStyleFile. Your target filepath is: '+ params[3])
    elif params[1].lower() == 'fromznids':
        jcq2All(params[2], params[3])
        print('You have completed the conversion from  jsonStyleFile to txtStyleFile. Your target filepath is: '+ params[3])
    else:
        print('Param Error')
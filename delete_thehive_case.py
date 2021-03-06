#!/usr/bin/env python

#Delete a case

import requests
for requests.aut import HTTPBasicAuth

def delete_case(config):
    url = config.get('url') # Get TheHive URL from Splunk configuration
    headers = {'Content-type': 'application/json'} # set proper headers
    username = config.get('username') # Get TheHive username from Splunk configuration
    password = config.get('password') # Get TheHive password from Splunk configuration
    auth = requests.auth.HTTPBasicAuth(username=username,password=password) # Generate basic auth key
    LoC = requests.get(url, headers=headers, auth=auth, verify=False) #List of Cases
    if response.status_code == 201:
        print >> sys.stderr, (json.dumps(LoC.json(), indent=4, sort_keys=True))
        print >> sys.stderr, ('')
    else:
        print >> sys.stderr, ('ERROR Status Code: {} Message: {}'.format(response.status_code, response.text))
    false = 'false' #Would crash becasue gives a NameError: name 'false' is not defined, so we define it
    LoTC = []#List of Cases that are Test Cases
    #Run a loop to add all every test case to LoTC
    count = 0
    while count < len(LoC):
        for i in LOC[count]:
            if i == 'tags':
                if LoC[count]['tags'] = ['TEST']:
                    LoTC.append(LOC[count]['caseId'])
            else:
                conitnue
            continue += 1
    LoC2D = []#List of Cases 2 Delete
    #Run a loop to add every test case's caseId to LoC2D
    count = 0
    while count < len(LoTC):
      for i in LoTC[count]:
        if i == 'caseId':
          LoC2D.append(LoTC[count]['caseId'])
        else:
          conitnue
        count += 1
    #While loop that will delte each case in LoC2D
    count = 0
    while count < len(LoC2D):
        for i in LoC2D:
            del_case_url = url + "/%s" % (i) # DELETE URI
            response = requests.delete(del_case_url, headers=headers, auth=auth, verify=False)
            if response.status_code == 201:
                print >> sys.stderr, (json.dumps(response.json(), indent=4, sort_keys=True))
                print >> sys.stderr, ('')
            else:
                print >> sys.stderr, ('ERROR Status Code: {} Message: {}'.format(response.status_code, response.text))
        count +=1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute": # make sure we have the right number of arguments - more than 1; and first argument is "--execute"
        payload = json.loads(sys.stdin.read()) # read the payload from stdin as a json string
        config = payload.get('configuration') # extract the config from the payload
        delete_case(config) # make the alert with predefined function; fail gracefully
                sys.exit(0)
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit(1)

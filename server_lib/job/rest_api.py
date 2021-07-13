
import requests
import constants

def callRestAPI(api):

    print (">> callRestAPI")

    resp = requests.get(constants.REST_URL + api)

    print ("<< callRestAPI")

    if resp.status_code != 200:
        # This means something went wrong.
        #raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        return(1)
    #for todo_item in resp.json():
    #    print('{} {}'.format(todo_item['id'], todo_item['summary'])
    else:
        return(0)

    
def add_to_tray_moving(tray_id, src, dst):

    url = constants.REST_URL
    myobj = {'tray_id': tray_id, 'source_location_id': src, 'destination_location_id': dst }
    x = requests.post(url, data = myobj)
    


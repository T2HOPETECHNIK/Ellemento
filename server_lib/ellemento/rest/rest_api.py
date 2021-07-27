
import requests
import constants

def callRestAPI(api):

    if (constants.NO_REST):
        return constants.ERROR_NONE

    print (">> callRestAPI")

    resp = requests.get(constants.REST_URL + api)

    print ("<< callRestAPI")

    if resp.status_code != 200:
        # This means something went wrong.
        #raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        return constants.ERROR_REST_FAIL
    #for todo_item in resp.json():
    #    print('{} {}'.format(todo_item['id'], todo_item['summary'])
    else:
        return constants.ERROR_NONE

    
def add_to_tray_moving(tray_id, src, dst):

    if (constants.NO_REST):
        return constants.ERROR_NONE

    # To do ...
    url = constants.REST_URL
    myobj = {'tray_id': tray_id, 'source_location_id': src, 'destination_location_id': dst }
    x = requests.post(url, data = myobj)

    return constants.ERROR_NONE
    


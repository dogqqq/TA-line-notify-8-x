import requests
import json

def lineNotifyMessage(token, msg):
  headers = {
      "Authorization": "Bearer " + token, 
      "Content-Type" : "application/x-www-form-urlencoded"
  }

  payload = {'message': msg}
  r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
  return r.status_code

# encoding = utf-8

def process_event(helper, *args, **kwargs):
    
    notify_token = helper.get_param("notify_token")
    #helper.log_info("notify_token={}".format(notify_token))

    message_kind = helper.get_param("message_kind")
    #helper.log_info("message_kind={}".format(message_kind))

    fields = helper.get_param("fields")
    
    fielddata = fields.split(",")
    
    fielddata = [ field.strip() for field in fielddata ]
    
    events = helper.get_events()
    msg = ""
    
    for event in events:
        
        if message_kind == 'custom':
            #msg .= event.get("_raw")
            msg = event.get("_raw")
        else:
            for field in fielddata:
                # msg .= event.get(field)
                msg += "\n" + field + "=" + event.get(field) 
                print(msg)
        lineNotifyMessage(notify_token, msg)
    return 0
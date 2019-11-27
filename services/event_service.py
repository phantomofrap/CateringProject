from models.event_model import Event, EventSchema
from datetime import datetime, date
def create_event(data):

    new_event = Event(
        title=data['title'],
        menu_choice=data['menu_choice'],
        event_date=data['event_date'],
        created_at=datetime.utcnow(),
        last_modified=datetime.utcnow(),
        client_id=data['client_id']
    )
    try:
        new_event.save()
        message = {"Message": "Event was saved successfully"}
        return message, 200
        
    except Exception as e:
        return str(e), 400
event_schema = EventSchema()

def fetch_one_event(event_id):
    x = Event.get_one_event(event_id)
    event_posts = event_schema.dump(x)
    return event_posts

def fetch_events():
    x = Event.get_all_events()
    event_posts = event_schema.dump(x, many=True)
    return event_posts

def edit_event(event_id, data):
    x = Event.get_one_event(event_id)
    updated = x.update(x, data)
    new_event = event_schema.dump(updated)
    return new_event

def delete_event(event):
    x = Event.get_one_event(event['id'])
    return x.delete()
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# POST/ events-Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code

    data = request.get_json()
    #Input validation: check if request body exists and title is present
    if not data or "title" not in data or not data ["title"].strip():
       return jsonify({"error": "Title is required"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element

    #Auto-generate next id using the current maximum ID in events
    next_id = max([e.id for e in events], default=0) + 1
    new_event = Event(next_id, data["title"].strip())
    #Append the new to the the in-memory list
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    #Return the newly created event as JSON with 201 Created status
    return jsonify(new_event.to_dict()), 201

    
# TODO: Task 1 - Define the Problem
# PATCH/ events/<id>-Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

    # TODO: Task 2 - Design and Develop the Code
    #Parse incoming JSON payload
    data = request.get_json()

    # TODO: Task 3 - Implement the Loop and Process Each Element

    #Find the target event by iterating over the events list
    event = next((e for e in events if e.id == event_id), None)
    #Return 404 if the event does not exist
    if not event:
        return jsonify({"error": "Event not found"}), 404
    #Update event title if provided in the payload
    if data and "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        event.title = data["title"].strip()

    # TODO: Task 4 - Return and Handle Results
    #Return updated event details with 200 OK
    return jsonify(event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# DELETE/ events/<id>-Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    global events

    #Check if target event exists before deletion
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    #Filter out the event matching the event_id from the list
    events = [e for e in events if e.id != event_id]

    # TODO: Task 4 - Return and Handle Results
    #Return 204 no content indicating successfull deletion with an empty response body.
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)

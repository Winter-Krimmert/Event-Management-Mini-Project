#!/usr/bin/env python3

# Dictionary to store events with event ID as the key
events = {}

def print_event_schedule():
    print("\nEvent Schedule:")
    for event_id, event in events.items():
        print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}, Participant Limit: {event['participant_limit']}")
        print(f"Participants: {event['participants']}")
        print(f"Waitlist: {event['waitlist']}")
        

def add_event():
    event_id = len(events) + 1
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    time = input("Enter event time (HH:MM): ")
    location = input("Enter event location: ")
    participant_limit = int(input("Enter participant limit: "))
    events[event_id] = {
        'name': name,
        'date': date,
        'time': time,
        'location': location,
        'participant_limit': participant_limit,
        'participants': {},
        'waitlist': []
    }
    print(f"Event {name} added with ID {event_id}.")

def remove_event(event_id):
    if event_id in events:
        del events[event_id]
        print(f"Event ID {event_id} has been removed.")
    else:
        print(f"No event found with ID {event_id}.")

def search_events(keyword):
    results = []
    for event_id, event in events.items():
        if keyword.lower() in event['name'].lower() or keyword in event['date'] or keyword.lower() in event['location'].lower():
            results.append((event_id, event))
    return results

def remove_participant(event_id, participant_id):
    if event_id in events and participant_id in events[event_id]['participants']:
        del events[event_id]['participants'][participant_id]
        print(f"Participant ID {participant_id} has been removed from event ID {event_id}.")
        # Move participant from waitlist to participants if waitlist is not empty
        if events[event_id]['waitlist']:
            next_participant = events[event_id]['waitlist'].pop(0)
            events[event_id]['participants'][next_participant['participant_id']] = {
                'name': next_participant['name'],
                'contact_info': next_participant['contact_info']
            }
            print(f"Participant {next_participant['name']} moved from waitlist to event.")
    else:
        print(f"No participant found with ID {participant_id} for event ID {event_id}.")

def add_participant(event_id):
    if event_id not in events:
        print(f"No event found with ID {event_id}.")
        return
    participant_id = len(events[event_id]['participants']) + 101
    name = input("Enter participant name: ")
    contact_info = input("Enter participant contact info: ")
    if len(events[event_id]['participants']) < events[event_id]['participant_limit']:
        events[event_id]['participants'][participant_id] = {
            'name': name,
            'contact_info': contact_info
        }
        print(f"Participant {name} added to event {events[event_id]['name']}.")
    else:
        events[event_id]['waitlist'].append({
            'participant_id': participant_id,
            'name': name,
            'contact_info': contact_info
        })
        print(f"Participant {name} added to waitlist for event {events[event_id]['name']}.")

def sort_events():
    sorted_events = sorted(events.items(), key=lambda item: item[1]['date'])
    return sorted_events

def binary_search_events(events, target_date):
    left, right = 0, len(events) - 1
    while left <= right:
        mid = (left + right) // 2
        if events[mid][1]['date'] == target_date:
            return events[mid]
        elif events[mid][1]['date'] < target_date:
            left = mid + 1
        else:
            right = mid - 1
    return None

def display_participant_details(event_id):
    if event_id in events:
        print(f"Participants for Event ID {event_id}:")
        for participant_id, details in events[event_id]['participants'].items():
            print(f"Participant ID: {participant_id}, Name: {details['name']}, Contact: {details['contact_info']}")
    else:
        print(f"No event found with ID {event_id}.")
        
def print_event_schedule():
    print("\nEvent Schedule:")
    sorted_events = sort_events()
    for event_id, event in sorted_events:
        print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}, Participant Limit: {event['participant_limit']}")
        print(f"Participants: {event['participants']}")
        print(f"Waitlist: {event['waitlist']}")

def search_events(keyword):
    results = []
    if keyword.count('-') == 2:
        sorted_events = sort_events()
        event = binary_search_events(sorted_events, keyword)
        if event:
            results.append(event)
    else:
        for event_id, event in events.items():
            if keyword.lower() in event['name'].lower() or keyword.lower() in event['location'].lower():
                results.append((event_id, event))
    return results

def generate_report():
    with open("event_report.txt", "w") as file:
        for event_id, event in events.items():
            file.write(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}, Participant Limit: {event['participant_limit']}\n")
            file.write("Participants:\n")
            for participant_id, details in event['participants'].items():
                file.write(f"  Participant ID: {participant_id}, Name: {details['name']}, Contact: {details['contact_info']}\n")
            file.write("Waitlist:\n")
            for waitlisted in event['waitlist']:
                file.write(f"  Participant ID: {waitlisted['participant_id']}, Name: {waitlisted['name']}, Contact: {waitlisted['contact_info']}\n")
            file.write("\n")
    print("Report generated: event_report.txt")


def main():
    while True:
        print("\nEvent Management System")
        print("1. Add Event")
        print("2. Add Participant to Event")
        print("3. View Event Schedule")
        print("4. Remove Event")
        print("5. Remove Participant from Event")
        print("6. Search Events")
        print("7. Display Participant Details")
        print("8. Generate Event Report")
        print("9. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_event()
        elif choice == '2':
            event_id = int(input("Enter event ID to add participant: "))
            add_participant(event_id)
        elif choice == '3':
            print_event_schedule()
        elif choice == '4':
            event_id = int(input("Enter event ID to remove: "))
            remove_event(event_id)
        elif choice == '5':
            event_id = int(input("Enter event ID to remove participant from: "))
            participant_id = int(input("Enter participant ID to remove: "))
            remove_participant(event_id, participant_id)
        elif choice == '6':
            keyword = input("Enter name, date, or location to search: ")
            results = search_events(keyword)
            for event_id, event in results:
                print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}, Participant Limit: {event['participant_limit']}")
        elif choice == '7':
            event_id = int(input("Enter event ID to display participant details: "))
            display_participant_details(event_id)
        elif choice == '8':
            generate_report()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

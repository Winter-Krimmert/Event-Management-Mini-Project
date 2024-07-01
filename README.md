# Event Management System

Welcome to the Event Management System! This project aims to provide a dynamic and interactive way to manage events, including creation, registration, scheduling, and participant management.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Project Overview

Our goal is to develop a system that allows users to create and manage events, register participants, and view event schedules. The system ensures efficient event handling with features like participant limit enforcement and waitlist management.

## Features

- **Event Creation and Management**
  - Add, remove, and search for events by name, date, or location.
  - Store information about events, including event ID, name, date, time, location, and participant limit.

- **Participant Management**
  - Register participants for events, ensuring participant limit is not exceeded.
  - Remove participants from events and manage waitlists.
  - Display participant details for each event.

- **Scheduling**
  - Display a schedule of all events.
  - Implement a waitlist system using a queue for events that reach participant capacity.
  - Automatically move participants from waitlist when space becomes available.

- **Data Structures and Algorithms**
  - Use dictionaries to store event information and participants.
  - Implement binary search for efficient event searching.
  - Sort events in chronological order for display.

- **Additional Features**
  - Generate a report of all events and participants.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/event-management-system.git
    ```

2. Navigate to the project directory:

    ```sh
    cd event-management-system
    ```

3. (Optional) Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install any required packages (if applicable):

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```sh
    python3 command_line_prompt.py
    ```

2. Follow the on-screen prompts to interact with the Event Management System:
    - Add new events.
    - Register participants.
    - View the event schedule.
    - Remove events or participants.
    - Search for events by keyword.
    - Display participant details for specific events.
    - Generate a report of all events and participants.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

Thank you for using the Event Management System! We hope it helps you efficiently manage your events and participants.

https://github.com/Winter-Krimmert/Event-Management-Mini-Project.git
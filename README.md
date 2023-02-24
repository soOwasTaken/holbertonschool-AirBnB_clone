
![App Screenshot](https://i.imgur.com/7IGhjHd.gif)


# AirBnB clone - The console

The idea of this project was to create a Python console to import value to json, so we can use them later on using SQL. It has the possibility to create, update, overwrite, delete and so on. It will be usefull later for the full fonctionnal website.


## Features

- Documented commands (type help <topic>)
- Will create a json file if it doesn't exist.
- Save changes automatically
- Commands : Update, create, destroy, quit, show, all


## Installation

```bash
  git clone https://github.com/MathieuMorel62/holbertonschool-AirBnB_clone.git
  cd holbertonschool-AirBnB_clone
```
    

and then to use this command interpreter

```bash
  ./console.py
```

you should see the prompt running like this, and now you are able to write and use it as much as you want.

```bash
  (hbtn)
```

## Classes

● BaseModel (Init Class (ID))

● Amenity (attribute : name)

● City (attribute: state_id, name)

● Place (attribute: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guests, price_by_night, latitude, longitude, amenity_ids)

● Review (attribute: place_id, user_id, text)

● State (attribute: name)

● User (attribute: email, password, first_name, last_name)


## Commands

| Command     | Description                                                                                                            | Usage                  | Exemple   | Output |
|-------------|------------------------------------------------------------------------------------------------------------------------|--------------------------|----------|-------|
| `create`        | Create a new instance                                                                                          | create <classes>       | create BaseModel        |  49faff9a-6318-451f-87b6-910505c55907 |
| `show`        | Prints the string representation of an instance based on the class name and id | show <classes> <id>                                                                                         | show BaseModel 49faff9a-6318-451f-87b6-910505c55907 | [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49f.."}|
| `destroy`        | Deletes an instance based on the class name and id (save it to json so be carefull)                                                                                   | destroy <classes> <id>            | destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907         | No Output
| `all`        | Prints all string representation of all instances based or not on the class name                                                                                      | all <classes>          | all BaseModel        | ["[BaseModel] (2dd6e...|
| `update`        | Updates an instance based on the class name and id by adding or updating attribute                                                                                            | update <classes> <id> <attribute> <"value">          | update BaseModel 1234-12.. email "email@email.com"        | No output|
| `exit`        | Quit the prompt                                                                                            | quit         |         | No ouput, just close!





## Authors

- [@MathieuMorel62](https://github.com/MathieuMorel62/)
- [@soOwasTaken](https://github.com/soOwasTaken)



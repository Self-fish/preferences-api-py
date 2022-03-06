# Preferences API
The purpose of this API is able to provide a way to handle lights and water temperature preferences by storing them on a mongo-db data base as follows:
```json
{
  "_id":{
    "$oid":"6206a995528df91ea56b00cf"
  },
  "creationDate":{
    "$numberLong":"1611690385066"
  },
  "updatedDate":{
    "$numberLong":"1611690385066"
  },
  "lightsPreferences":{
    "mode":"AUTOMATIC",
    "range":{
      "starting":"14:00",
      "finishing":"23:59"
    }
  },
  "waterPreferences":{
    "mode":"AUTOMATIC",
    "value":{
      "$numberInt":"24"
    }
  },
  "deviceId":"sf-000000009df9b724"
}
```

At the moment, the API expose just a few endpoints: GET to retrieve the preferences and PUT to update them.

## Data base connection
In order to connect with your mongodb, you need to define a *db_connection.ini* file with the following format

```text
[CREDENTIALS]
user = user
password = password

[DATABASE]
name = database-name
```

and it's used as follows:

```python
def __connect_to_database(self):
  config = configparser.ConfigParser()
  config.read(CREDENTIALS_FILE)
  db_user = config[CREDENTIALS_SECTION][USER]
  db_password = config[CREDENTIALS_SECTION][PASSWORD]
  db_name = config[DATA_BASE_SECTION][NAME]
  return "mongodb+srv://" + db_user + ":" + db_password + "@cluster0.ryrnh.mongodb.net/" + \
    db_name + "?retryWrites=true&w=majority"
```

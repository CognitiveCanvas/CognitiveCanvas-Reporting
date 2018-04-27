# User Table

| Field | Description  |
| ------| ------------ |
|email | String Primary Key|
|FirstName | String|
|LastName | String|
|Type| String|
|isLogin | boolean|
|MapsCreated | [MapID Foreign Key]|
|MapsAccessed | [MapID Foreign Key]|
|MapsWithPermission | [MapID Foreign Key]|


# User Login Table 

| Field | Description  |
| ------| ------------ |
| Email | Foreign Key |
| Login | [Date] |
| logout | [Date] |


# Maps Table 

| Field | Description  |
| ------| ------------ |
| MapWebstrateID | String Primary Key |
| Owner | String Foreign Key |
| Permission | [String Foreign Key] |
| Topic/Title | String  |
| Created | Date |
| Modified | Date |
| Screen | Shot |
| Versions | [V- Tag] |


# Content Table

| Field | Description  |
| ------| ------------ |
| ContentID | Number |
| Title | String |
| URL | String |
| Type | String |

# Keyword Table

| Field | Description  |
| ------| ------------ |
| Keyword | String |
| URL_IDS | [Number] |


# Action Table

| Field | Description  |
| ------| ------------ |
| Timestamp | Date Primary Key |
| User | String Primary Key |
| Event | {One of Keyboard, Mouse, Touchscreen} |
| Type | {One of Created, Modified, Deleted, Moved} |



<!-- How to gather resources? --> 

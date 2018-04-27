# Node  

| Field | Description  |
| ------| ------------ |
| NodeID | Integer Primary Key |
| Creator | String Foreign Key |
| Label | String |
| Shape | String |
| Color | String |
| Size | String |
| Created | Date |
| LocationX | Integer |
| LocationY | Integer |

# Edge  

| Field | Description  |
| ------| ------------ |
| EdgeID | Integer Primary Key |
| Creator | String Foreign Key |
| Node 1 | Integer Foreign Key |
| Node 2 | Integer Foreign Key |
| Label | String |
| Created | Date |
| Type | {One of Double Arrowed, Single Arrowed, none } |

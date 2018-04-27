# Node  

| NodeID | Integer Primary Key |
| Creator | String Foreign Key |
| Label | String |
| Shape | String |
| Color | String |
| Size | String |
| OutgoingEdges | [EdgeIDs Integer] |
| IncomingEdges | [EdgeIDs Integer] |
| Created | Date |
| LocationX | Integer |
| LocationY | Integer |

# Edge  

| EdgeID | Integer Primary Key |
| Creator | String Foreign Key |
| Label | String |
| Created | Date |
| Type | {One of Double Arrowed, Single Arrowed, none } |

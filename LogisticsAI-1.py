import random
import time
choices=[
"Policy would need to be reviewed.",
"Jim Deyo has the most recent experience in this area.",
"Karen Cushing may have a record of this.",
"Scott Reed may have the most experience in this area.",
"Kathy DeSchuiteneer worked on this most recently",
"This would be an AE Engineering technical question.",
"Scott Reed worked on this most recently",
"John McFarland could probably find out for you.",
"Kathy DeSchuiteneer has the most recent experience in this area",
"Brent Scott is resposable for resource allocation and policy"
]
while True:
    input("Logistics AI provisioning query:")
    for i in range(0,3):
        print("Scanning Tracker DB...")
        time.sleep(1)
    print(random.choice(choices))

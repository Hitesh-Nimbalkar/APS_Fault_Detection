## Problem statement.
   ## Data: Sensor Data

### Problem statement :

The system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.


|True class | Positive | Negative | |
| ----------- | ----------- |   |  |
|<b>Predicted class</b>||| |
| Positive      |   -       | cost_1  |    |
| Negative   | cost_2        |  | |


Cost 1 = 10 and Cost 2 = 500



## Project_Overview 


### Training Pipeline 
![Training_Pipeline](https://user-images.githubusercontent.com/109200332/225400692-4b1f7725-d9aa-402c-af47-f2bead839adf.png)


![Sensor ](https://user-images.githubusercontent.com/109200332/225382868-ded182fe-e0ca-4f0e-9298-2036273f3d9c.png)

## Data Ingestion 
![Data_Ingestion_Complete](https://user-images.githubusercontent.com/109200332/225345768-06535df9-3cea-4f39-87c9-a7583468f68f.png)


## Data Validation 


![Data_Validation_complete](https://user-images.githubusercontent.com/109200332/225347020-f798fb8a-7466-4d7d-b8e9-65b1529ce8d5.png)


## Data Transformation 

![Data_Transformation_Complete](https://user-images.githubusercontent.com/109200332/225348759-36ce36c4-53e9-415c-9037-e77dccfee53c.png)


## Model trainer 
![Model_Trainer](https://user-images.githubusercontent.com/109200332/225368082-5010e0dd-5f4b-47de-869c-06a599ac0f21.png)



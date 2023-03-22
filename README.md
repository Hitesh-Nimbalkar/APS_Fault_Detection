
   ## Data: Sensor Data

### Problem statement :

The system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

     Predicted class |      True class       |
                     |    pos    |    neg    |
     -----------------------------------------
      pos            |     -     |  Cost_1   |
     -----------------------------------------
      neg            |  Cost_2   |     -     |
     -----------------------------------------


Cost 1 = 10 and Cost 2 = 500


- The total cost of a prediction model the sum of `Cost_1` multiplied by the number of Instances with type 1 failure and `Cost_2` with the number of instances with type 2 failure, resulting in a `Total_cost`. In this case `Cost_1` refers to the cost that an unnessecary check needs to be done by an mechanic at an workshop, while `Cost_2` refer to the cost of missing a faulty truck, which may cause a breakdown. 
- `Total_cost = Cost_1 * No_Instances + Cost_2 * No_Instances.`

- From the above problem statement we could observe that, we have to reduce false positives and false negatives. More importantly we have to **reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives.**


## Tech Stack Used
  1. Python
  2. Flask
  3. Machine learning algorithms
  4. Docker
  5. MongoDB



## Project_Overview 


### Training Pipeline 

![Training_Pipeline](https://user-images.githubusercontent.com/109200332/225405968-6941f370-edbd-4557-9f5a-678970de893b.png)



![Sensor ](https://user-images.githubusercontent.com/109200332/225382868-ded182fe-e0ca-4f0e-9298-2036273f3d9c.png)

## Data Ingestion 
![Data_Ingestion_Complete](https://user-images.githubusercontent.com/109200332/225345768-06535df9-3cea-4f39-87c9-a7583468f68f.png)


## Data Validation 


![Data_Validation_complete](https://user-images.githubusercontent.com/109200332/225347020-f798fb8a-7466-4d7d-b8e9-65b1529ce8d5.png)


## Data Transformation 

![Data_Transformation_Complete](https://user-images.githubusercontent.com/109200332/225348759-36ce36c4-53e9-415c-9037-e77dccfee53c.png)


## Model trainer 
![Model_Trainer](https://user-images.githubusercontent.com/109200332/225368082-5010e0dd-5f4b-47de-869c-06a599ac0f21.png)

## Model Evaluation

![Model Evaluation](https://user-images.githubusercontent.com/109200332/225520543-9b7a529e-d4be-48ec-855d-989b148028ca.png)




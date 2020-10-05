# Multi Aget System approach to simulate COVID-19 spreading

Epidemic of COVID-19 has a significant impact on people's lifestyle all over the world. It has paralyzed economic situation of many countries and lowered the sense of security of whole societies. One of possible solutions to fight against this pandemic reality, that the governments can undertake, is to impose several social restrictions. In this study, we propose a Agent-Based model, which we will use to evaluate the influence of those restrictions on the COVID-19 spreading. The model is based on previous research regarding social contacts between people in four age groups (Child, Young, Adult, Old), the impact of disease on people in different ages. We also will perform a list of experiments with different behavioral scenarios. We believe, that this approach will give a clear view on which restrictions are helpful to deal with epidemic, and what are the consequences of not following the suggested limitations.

## Model design

The method we decided upon for simulating the transmission of a virus is the SEIR model. In this model each agent can be either susceptible to receiving the virus (S), be exposed to it (E), infected with corona (I) or removed from the simulation (R). We decided that, due to the recent findings that a human can contract the COVID-19 more than once, those who recover from the virus return to be susceptible. On theother hand, those who are removed from the simulation represent those who passed away. The agents in the model represent individuals that belong to one of four different categories: Children, Young Adults, Adults and Old. 

### Parameters of the model 


   Parameter  | Value 
   ------------- | ------------- 
   Transition to "Infected"  | 1−exp (1/dL)  
   P(child’s death)  | 1/10647
   P(young's death) | 7/33345
   P(adult's death) | 194/40833
   P(old's death) | 6191/32056
   dL (incubation period) | 6 days
   Infection period | 7 days
   P(infection) per exposure | 0,1


Parameters are fixed and based on available research regarding COVID-19 epidemic.
## How to start a simulation

- Make sure you have Python 3.7.6 installed
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt`
- `python launchModel.py`

## Output of the program

At the end of simulation, program prints statistics of each age group as well as of the whole population of agents. Moreover, it draws a bunch of graphs which might be useful for the further analysis. Example output plots are presented below:

<p align="center">
  <img src="example_plots.PNG" width="1000" title="hover text">
</p>

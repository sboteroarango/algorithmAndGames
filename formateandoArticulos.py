texto = """Evaluation of the Uniformity of Protective Coatings on Concrete Structure Surfaces Based on Cluster Analysis,Liu,2021*

Development of a Reference-Free Indirect Bridge Displacement Sensing System,Won,2021. *

A Multichannel Strain Measurement Technique for Nanomodified Smart Cement-Based Sensors in Reinforced Concrete Structures,Meoni,2021*

Multi-Sensors Geophysical Monitoring for Reinforced Concrete Engineering Structures: A Laboratory Test, Capozzoli,2021*

An Innovative Smart Concrete Anchorage with Self-Stress Sensing Capacity of Prestressing Stress of PS Tendon,Lee,2021. *

Performance of Linear Mixed Models to Assess the Effect of Sustained Loading and Variable Temperature on Concrete Beams Strengthened with NSM-FRP,Perera,2021.*

Fiber Optic Sensors Embedded in Textile-Reinforced Concrete for Smart Structural Health Monitoring: A Review,Alwis,2021*

New Hydraulic Sensor for Distributed and Automated Displacement Measurements with Temperature Compensation System,Bednarski,2021*

Effect of the Geometrical Constraints to the Wenner Four-Point Electrical Resistivity Test of Reinforced Concrete Slabs,Robles,2021. *

Unmanned Aerial Vehicles (UAVs) for Physical Progress Monitoring of Construction,Jacob-Loyola,2021*

On the Use of Embedded Fiber Optic Sensors for Measuring Early-Age Strains in Concrete,Silva,2021.* 

Optimum PZT Patch Size for Corrosion Detection in Reinforced Concrete Using the Electromechanical Impedance Technique,Hire,2021*

Study of a Long-Gauge FBG Strain Sensor with Enhanced Sensitivity and Its Application in Structural Monitoring,Yang,2021.*

Cement-Based Piezoelectric Ceramic Composites for Sensing Elements: A Comprehensive State-of-the-Art Review,Ding,2021*

Stainless Steel Voltammetric Sensor to Monitor Variations in Oxygen and Humidity Availability in Reinforcement Concrete Structures,Martínez-Ibernón,2021.* 

Development of a Numerical Model to Predict the Dielectric Properties of Heterogeneous Asphalt Concrete,Cao,2021.*

An Embedded-Sensor Approach for Concrete Resistivity Measurement in On-Site Corrosion Monitoring: Cell Constants Determination,Ramón,2021.*

Smart Node Networks Orchestration: A New E2E Approach for Analysis and Design for Agile 4.0 Implementation,Bertoli,2021.*

Shape-Sensing of Beam Elements Undergoing Material Nonlinearities,Savino,2021.*

Piezoelectric Sensor-Embedded Smart Rock for Damage Monitoring in a Prestressed Anchorage Zone,Pham,2021.*

Structural Health Monitoring Based on Acoustic Emissions: Validation on a Prestressed Concrete Bridge Tested to Failure,Tonelli,2020.*

Electrical Resistivity Measurements of Reinforced Concrete Slabs with Delamination Defects,Robles,2020.*

Wireless Sensing of Concrete Setting Process,González-López,2020.*

Measuring Three-Dimensional Temperature Distributions in Steel–Concrete Composite Slabs Subjected to Fire Using Distributed Fiber Optic Sensors,Bao,2020.*

Smart Sensing Using Electromagnetic Waves for Inspection of Defects in Rock Bolts,Yu,2020.*

Securing MQTT by Blockchain-Based OTP Authentication,Buccafurri,2020.*

Non-Contact, Non-Destructive Testing in Various Industrial Sectors with Terahertz Technology,Tao,2020.*

Acoustic Inspection of Concrete Structures Using Active Weak Supervision and Visual Information,Louhi_Kasahara,2020.*

Smart RFID Sensors Embedded in Building Structures for Early Damage Detection and Long-Term Monitoring,Strangfeld,2019.*

Research on RPLS soft-measuring project realization of cement clinker f-CaO,C.Wan,2016.*

A comparative study of black-box models for cement quality prediction using input-output measurements of a closed circuit grinding,Minchala-Avila,2016.*

Virtual Sensing f-CaO Content of Cement Clinker Based on Incremental Deep Dynamic Features Extracting and Transferring Model,L. Yao,2021*

Prediction of the Cement Grate Cooler Pressure in the Cooling Process Based on a Multi-Model Fusion Neural Network,Y. Geng,2020.*

Study on target optimization method of cement raw material ingredients,X.Lu,2018*

Analysis of Ca in cement using laser-induced breakdown spectroscopy,Z.Guo,2017* 

Application of the Static and Dynamic Models in Predicting the Future Strength of Portland Cements, D. C._Tsamatsoulis,2014* 

Highly efficient burning of clinker using flame analysis and NMPC,D.Schmidt,2007* 

Prediction of Compressive Strength of Green Concrete with Admixtures Using Neural Networks,P.Singh,2020* 

PREDICTION OF CONCRETE STRENGTH WITH DATA MINING METHODS USING ARTIFICIAL BEE COLONY AS FEATURE SELECTOR,M. Kaya-Keles,2018* 

Relation of resonant frequency and appropriate linear predictive order for evaluating concrete strength by quality factor,R.Toh,2012
"""
texto = texto.split("*")

for i in range(len(texto)):
    texto[i] = texto[i].replace("\n","",-1)
    texto[i] = texto[i].replace(" ","_",-1)
texto.sort()
texto[23] = "Smart_Node_Networks_Orchestration:_A_New_EE_Approach_for_Analysis_and_Design_for_Agile_Implementation,Bertoli,2021." 
texto[15] = "Non-Contact_Non-Destructive_Testing_in_Various_Industrial_Sectors_with_Terahertz_Technology,Tao,2020."
#hasta aqui es el orden establecido
años = []
for articulo in texto:
    for letra in articulo:
        if letra.isnumeric():
            años.append(letra)
años = "".join(años)
print(años)
añosOrganizados = []
for i in range(0,len(años),4):
    añosOrganizados.append(años[i:i+4])
titulos = []
autores = []
for articulo in texto:
    primeraComa = articulo.find(",")
    titulos.append(articulo[0:primeraComa])
    segundaComa = articulo.find(",",primeraComa+1)
    autores.append(articulo[primeraComa+1:segundaComa])

titulos[15]="Non-Contact,_Non-Destructive_Testing_in_Various_Industrial_Sectors_with_Terahertz_Technology"
titulos[23] ="Smart_Node_Networks_Orchestration:_A_New_E2E_Approach_for_Analysis_and_Design_for_Agile_4.0"
print(añosOrganizados)
#2021, Cobaleda_et_al., Titulo_del_articulo (1)
for año,autor,titulo in zip(añosOrganizados,autores,titulos):
    print(f"{año}, {autor}_et_al., {titulo}")
    print()



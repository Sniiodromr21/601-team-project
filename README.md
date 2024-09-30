# 601-project
## Definition of the project
The mission of our project is to utilize graph databases and graph neural networks (GNN) to develop an easy-to-use diagnostic tool for Alzheimer's disease. By integrating the medical data obtainable, we aim to offer healthcare professionals deeper insights into disease progression, early diagnosis, and personalized treatment strategies. Our objective is to enhance patient outcomes and support the global battle against Alzheimer's disease through advanced technology.

## User Stories
As a family member of a potential Alzheimer’s patient, I want an easy-to-use application that allows me to perform an initial assessment at home using cognitive tests and symptom checklists, so that I can detect early signs of Alzheimer’s and seek professional medical advice if necessary.

As a data scientist, I want to explore large-scale Alzheimer’s datasets using graph neural networks, allowing me to discover new relationships and predictors of Alzheimer’s progression.

As a neurologist, I want a system that can quickly integrate various patient data, including MRI scans, genetic tests, and cognitive assessments, so that I can make more informed diagnoses of Alzheimer’s disease.

## Citations of Papers
[Alzheimer's disease](https://www.sciencedirect.com/science/article/pii/S0140673610613499)  
[ADiag: Graph Neural Network Based Diagnosis of Alzheimer’s Disease](https://ar5iv.labs.arxiv.org/html/2101.02870)  
[A comparative study of GNN and MLP based machine learning for the
diagnosis of Alzheimer’s Disease involving data synthesis](https://www.sciencedirect.com/science/article/pii/S0893608023006020?via%3Dihub)  
New Perspectives of Alzheimer Disease Diagnosis – the Most Popular and Future Methods

## Literature review of the topic with references 
 Diagnostic Approaches to Alzheimer’s Disease (AD):  
### 1.Clinical Diagnosis:  
 Alzheimer’s disease is typically diagnosed based on clinical assessments, patient history, and cognitive testing. The NINCDS-ADRDA criteria are commonly used, achieving more than 80% accuracy in distinguishing Alzheimer’s from non-demented individuals, but less accurate in differentiating AD from other types of dementia.
### 2.Neuroimaging Techniques:  
 CT and MRI: These are used to rule out other conditions that may cause cognitive impairment, such as tumors or vascular issues. MRI is especially used for detecting medial temporal lobe atrophy.  
 Volumetric Imaging & 3D Mapping: Emerging techniques like volumetric imaging and hippocampal mapping are showing promise for early diagnosis, especially to track disease progression.  
### 3.Positron Emission Tomography (PET):  
 PET with fluorodeoxyglucose (FDG-PET) has shown sensitivity and specificity for detecting AD, especially by identifying reduced glucose metabolism in temporal and parietal regions. PET can also be used with Pittsburgh compound B (PIB) to visualize amyloid plaques.  
### 4.Single-Photon Emission Computed Tomography (SPECT):  
 SPECT can measure blood flow and has been used to differentiate Alzheimer’s from other dementias like frontotemporal dementia. However, it shows lower accuracy compared to PET imaging.  
### 5.Cerebrospinal Fluid (CSF) Biomarkers:  
 CSF biomarkers such as low Aβ1-42 and high total tau or hyperphosphorylated tau are indicative of AD and can differentiate AD from other dementias with good sensitivity and specificity. Combination of these biomarkers in panels is improving diagnostic accuracy, especially for early diagnosis.  
### 6.Genetic Testing:  
 APOE ε4 allele is a strong risk factor for Alzheimer’s and is associated with increased amyloid burden. Other genetic mutations such as PSEN1, PSEN2, and APP have been implicated, though they are rare in late-onset Alzheimer’s.  
### 7.Other Emerging Biomarkers:  
 Various novel biomarkers, including those related to inflammation and oxidative stress, are under investigation to further improve the diagnostic process.  


 In this project we use database systems with the help of AI in imaging, hence our main focus is to learn a level of expert knowledge in how different imaging techniques can be used to diagnose AD, hence we expand on the Neuroimaging Techniques.  
 MRI is one of the most widely used imaging techniques in AD diagnosis due to its ability to provide detailed structural images of the brain without radiation exposure. It can detect specific atrophies and changes in brain volume associated with AD, particularly in the medial temporal lobe and hippocampus.
### •Medial Temporal Lobe Atrophy:  
 The medial temporal lobe (including the hippocampus, entorhinal cortex, and amygdala) is one of the first regions to show atrophy in AD. MRI is sensitive to these changes and can identify patients with early-stage AD.  
 Quantitative Imaging: Volumetric techniques measure hippocampal and overall brain atrophy. Studies have shown that MRI-based measures of hippocampal volume have a high sensitivity and specificity (greater than 85%) for diagnosing AD. Volumetric and 3D mapping of the hippocampus are emerging as important tools for identifying patients with mild cognitive impairment (MCI) who are at risk of progressing to AD.
### •Cortical Thickness Measurement:  
 A reduction in cortical thickness in specific brain areas such as the posterior cingulate cortex and parietal cortex is associated with AD. Measuring cortical thinning is an emerging diagnostic tool that could complement other imaging methods in AD diagnosis.  
### •Longitudinal Imaging:  
 MRI is also used in longitudinal studies to monitor brain atrophy over time, helping to distinguish AD from normal aging. Serial scans can reveal the progressive loss of brain tissue, which is qualitatively and quantitatively different from normal aging.  

 From the GPT analysis I acknowledged all the different methods of diagnosing AD, and chose to use 3D mapping techniques to continue on the project. In the next sprint we plan to check for existing databases that we can access and investigate further in how the data can be used, with existing studies in the data collected.   

References:
1.	Ballard, C., Gauthier, S., Corbett, A., Brayne, C., Aarsland, D., & Jones, E. (2011). Alzheimer’s disease. The Lancet, 377(9770), 1019-1031.
https://www.sciencedirect.com/science/article/pii/S0140673610613499

2.	Subramonian, A. (2021). ADiag: Graph Neural Network Based Diagnosis of Alzheimer’s Disease. A comparative study of GNN and MLP based machine learning for the diagnosis of Alzheimer’s Disease involving data synthesis. 
arXiv preprint arXiv:2101.02870. 
https://ar5iv.labs.arxiv.org/html/2101.02870


  

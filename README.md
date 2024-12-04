# 601-team project
## Definition of the project
The mission of our project is to utilize  AI models like graph neural networks and convolutional neural networks to develop an easy-to-use diagnostic tool for Alzheimer's disease. By integrating the medical data obtainable, we aim to offer healthcare professionals deeper insights into disease progression, early diagnosis, and personalized treatment strategies. Our objective is to enhance patient outcomes and support the global battle against Alzheimer's disease through advanced technology.

## User Stories
As a family member of a potential Alzheimer’s patient, I want an easy-to-use application that allows me to perform an initial assessment at home using cognitive tests and symptom checklists, so that I can detect early signs of Alzheimer’s and seek professional medical advice if necessary.

As a data scientist, I want to explore large-scale Alzheimer’s datasets using graph neural networks, allowing me to discover new relationships and predictors of Alzheimer’s progression.

As a neurologist, I want a system that can quickly integrate various patient data, including MRI scans, genetic tests, and cognitive assessments, so that I can make more informed diagnoses of Alzheimer’s disease.

## Approaches to Detect AD
Given the significant and growing impact of Alzheimer’s Disease (AD), it is crucial to focus on enhancing early detection and diagnosis to mitigate its effects. Detecting AD early not only provides an opportunity for timely intervention but also allows patients to benefit from emerging treatments and lifestyle modifications that may slow the disease's progression. To effectively diagnose AD, researchers and clinicians employ a variety of approaches, each targeting different aspects of the disease's pathology. These approaches can be categorized into cognitive assessments, neuroimaging techniques, fluid biomarkers, genetic testing, and advanced artificial intelligence (AI) methods. Here are the primary approaches currently used to detect AD:

### 1. Cognitive and Neuropsychological Testing
Cognitive decline is one of the earliest and most apparent symptoms of AD. Neuropsychological tests are widely used as the first line of assessment to identify deficits in memory, executive function, language, and other cognitive abilities. Commonly used tests include the Mini-Mental State Examination (MMSE) and the Montreal Cognitive Assessment (MoCA), which provide a quick screening for cognitive impairment. More comprehensive neuropsychological batteries evaluate specific cognitive domains to distinguish between normal aging, mild cognitive impairment (MCI), and early AD. These tests are easy to administer and cost-effective, making them a practical approach for primary care settings, although they may not detect AD at its preclinical stages.

### 2. Neuroimaging Techniques
Neuroimaging provides a direct window into the structural and functional changes in the brain associated with AD. Advances in imaging techniques have revolutionized the ability to detect AD early and differentiate it from other dementias.  
Magnetic Resonance Imaging (MRI): MRI is a commonly used tool to assess structural changes in the brain. In AD, key regions such as the hippocampus and medial temporal lobes show significant atrophy, which can be detected even in the early stages of the disease. MRI is particularly useful for monitoring disease progression and ruling out other causes of cognitive impairment, such as vascular dementia or tumors.  
Positron Emission Tomography (PET): PET imaging is used to detect the buildup of amyloid-beta plaques and tau tangles, the hallmark pathological features of AD. Amyloid PET imaging, using tracers like Pittsburgh Compound B (PiB), allows for the visualization of amyloid deposits in the brain. Tau PET imaging similarly detects tau tangles, providing insight into the extent of neurodegeneration.  
Functional MRI (fMRI) and FDG-PET: These techniques assess brain function by measuring changes in blood flow (fMRI) or glucose metabolism (FDG-PET). Functional imaging can reveal patterns of disrupted brain activity or hypometabolism in areas typically affected by AD, such as the parietal and temporal lobes, even before significant structural damage occurs.

### 3. Cerebrospinal Fluid (CSF) Biomarkers
Biochemical markers found in cerebrospinal fluid (CSF) offer a highly sensitive method for detecting AD pathology. A lumbar puncture can be used to collect CSF samples, which are then analyzed for specific biomarkers:  
Amyloid-beta (Aβ42): Reduced levels of Aβ42 in CSF reflect amyloid plaque deposition in the brain, a core feature of AD pathology.  
Total Tau (T-tau) and Phosphorylated Tau (P-tau): Elevated levels of tau proteins in CSF are associated with neurofibrillary tangles and neuronal damage. The ratio of Aβ42 to tau in CSF is a key diagnostic marker for distinguishing AD from other dementias.  
These biomarkers provide highly accurate diagnostic information and can detect AD pathology even before cognitive symptoms emerge, making them a critical tool for early detection.

### 4. Blood-Based Biomarkers
While CSF biomarkers are highly informative, lumbar punctures are invasive and not practical for routine screening. Recent advances in blood-based biomarkers offer a less invasive and more accessible method for detecting AD.  
Plasma Amyloid and Tau: Research has shown that blood tests can detect changes in amyloid-beta and tau protein levels, which correlate with their CSF counterparts and neuroimaging findings.  
Neurofilament Light (NfL): Elevated NfL levels in the blood reflect neuronal injury and are being explored as a marker for AD progression.  
Blood-based biomarkers are rapidly advancing and could revolutionize the screening and diagnosis of AD in primary care settings, making early detection more feasible on a large scale.  

### 5. Genetic Testing
Genetic factors play a significant role in AD risk, especially for early-onset cases. Genetic testing can identify individuals with a higher risk of developing AD, particularly those with familial Alzheimer’s Disease.  
APOE ε4 Allele: The presence of the APOE ε4 allele is the most significant genetic risk factor for late-onset AD. Individuals with one or two copies of this allele have a higher likelihood of developing AD, though it is not deterministic.  
PSEN1, PSEN2, and APP Mutations: Mutations in these genes are associated with early-onset familial AD, a rare form of the disease that typically manifests before the age of 65.  
Genetic testing is useful for identifying individuals at risk and is often used in combination with other diagnostic approaches. However, it is important to note that not all individuals with genetic risk factors will develop AD.  

### 6. Artificial Intelligence and Machine Learning
With the advent of big data and machine learning, artificial intelligence (AI) is increasingly being applied to AD detection. AI algorithms can analyze large datasets, including neuroimaging scans, biomarker levels, and genetic data, to identify patterns that may indicate early AD.  
Deep Learning Models: These models are trained on imaging and clinical data to predict the likelihood of AD development. AI can detect subtle changes in brain structure and function that may not be visible to the human eye, offering earlier and more precise diagnoses.  
Multimodal Approaches: AI can combine data from multiple sources (e.g., imaging, biomarkers, cognitive tests) to create a comprehensive profile of an individual’s risk, improving diagnostic accuracy.  

### 7. Olfactory Testing
A growing body of evidence suggests that olfactory dysfunction may be an early indicator of AD. The olfactory bulb is one of the first brain regions to be affected by amyloid-beta and tau accumulation. Testing an individual's ability to recognize and differentiate smells may provide an early, non-invasive clue to AD onset, though this method is still under investigation and not widely adopted.  

We are planning to look at the Artificial Intelligence and Machine Learning Method and the Neuroimaging method at a start, and investigate in the direction of how these two methods can contribute to a high CCR of Alzheimer’s Disease.


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

Sprint 2 update:

Job completed: 
    Successful discovery of a new database to research and develop, request to new databases.
    Research and decided the direction of study, MRI neuroimaging.
Work to do: 
    Research on the databases, find out what the parameters do, and contact professors that know about the content.


  

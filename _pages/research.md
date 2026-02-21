---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

## Research Statement

My research lies at the intersection of **robust machine learning, uncertainty-aware modeling, and interpretable and trustworthy AI**. I develop theoretically grounded learning frameworks that remain reliable under **noise, outliers, class imbalance, and distributional shift**, with the overarching goal of enabling trustworthy machine learning in high-stakes clinical and biomedical settings.

My early work focused on the design of **robust loss functions *(e.g., RoBoSS loss, Wave loss, Guardian loss, HawkEye loss)* and adaptive weighting mechanisms *(e.g., RAPID weighting scheme)*** for support vector machines, randomized neural networks, and kernel-based learning models. In particular, I introduced strategies for jointly addressing noise, outliers, and class imbalance through bounded loss formulations and data-adaptive weighting schemes, enabling stable learning under imperfect real-world data conditions. These contributions established theoretically grounded frameworks for robust learning and were validated across diverse benchmarks and biomedical prediction tasks, resulting in publications in leading venues such as **IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)**, **Pattern Recognition**, **Neural Networks**, and **Applied Soft Computing**.

I further investigated the statistical structure of feature dependencies in tabular data and proposed **copula-based weight initialization for randomized neural networks**, enabling dependency-aware hidden representations and improved generalization. This work addresses a long-standing limitation of randomized neural networks, i.e., the use of fully random, fixed input-to-hidden weights that ignore data distribution and feature relationships. By introducing statistically aligned, dependency-aware initialization, the proposed framework closes this foundational gap and transforms randomized neural networks from purely random feature models into data-informed learning systems. This work was accepted at the **International Conference on Artificial Intelligence and Statistics (AISTATS)**.

Through this line of research, I identified a fundamental limitation of conventional learning systems: their reliance on deterministic point predictions with limited uncertainty characterization and weak density-level interpretability. Such models provide accurate predictions but lack calibrated uncertainty and probabilistic structure, which restricts their reliability and clinical trustworthiness in high-stakes biomedical decision-making.

Motivated by this gap, my recent research has shifted toward **probabilistic and density-aware neural learning frameworks** that integrate statistical modeling with neural architectures to provide uncertainty quantification and interpretable predictive structure. In parallel, I investigate **statistical modeling of feature dependencies via copula theory** to capture structured relationships among biomedical variables and to enable dependency-aware probabilistic inference in machine learning systems.

Overall, my research vision is to bridge **statistical learning theory, probabilistic modeling, and neural network methods** to develop machine learning frameworks that are **robust, interpretable, and uncertainty-aware *by design***—moving beyond point prediction toward trustworthy, distribution-aware learning systems suitable for deployment in biomedical and scientific domains.

---

## Core Research Themes

- Robust Machine Learning
- Loss Function Design and Robust Optimization  
- Randomized Neural Networks and Kernel Methods    
- Uncertainty-Aware Learning  
- Interpretable and Trustworthy AI  
- Statistical Machine Learning  
- Copula-Based Dependency Modeling  
- Probabilistic Neural Networks  
- Tabular Machine Learning  
- Biomedical and Clinical AI  

---

## Methodological Contributions

My research develops learning frameworks to improve **stability, robustness, and generalization** in machine learning systems. Key methodological contributions include:

- Robust loss function design for learning under noise, outliers, and class imbalance  
- Adaptive and data-driven weighting mechanisms for imbalance- and difficulty-aware learning  
- Stable randomized neural networks via spectral regulation and structured initialization  
- Copula-based statistical modeling to capture feature dependencies in learning systems  
- Uncertainty-aware learning frameworks for reliable and calibrated prediction  
- Hierarchical probabilistic neural networks for robust and interpretable prediction  

These methodological advances have been validated across diverse benchmark datasets and biomedical learning scenarios, demonstrating consistent improvements in robustness, stability, and predictive reliability.

---

## Application Focus

My methodological research is motivated by high-stakes real-world domains where learning systems must operate reliably under uncertainty and imperfect data. I focus particularly on **tabular biomedical and clinical data**, where noise, missingness, class imbalance, and complex feature dependencies pose major challenges for conventional machine learning models.

Key application areas include:

- Biomedical and healthcare data analysis  
- Disease diagnosis and prognosis modeling  
- Clinical decision-support systems  
- Dependency-aware modeling of biomedical variables   

---

## Future Research Vision

State-of-the-art machine learning and deep learning models achieve strong predictive performance, yet most operate as **black-box predictors** that provide point estimates with limited interpretability and weakly characterized uncertainty. In high-stakes domains such as healthcare and biomedical decision-making, this lack of transparency and calibrated uncertainty significantly limits practitioner trust and real-world deployment.

Existing research often addresses this limitation through *post-hoc* interpretability methods or auxiliary uncertainty modules layered onto complex models. While useful, these approaches typically introduce explanations or uncertainty estimates external to the core learning mechanism, leaving interpretability and uncertainty as secondary properties rather than intrinsic characteristics of the model.

My research vision is to move beyond this paradigm by developing learning systems that are **probabilistic, interpretable, and uncertainty-aware *by design***. The foundational modeling framework for this direction is the **Probabilistic Neural Network (PNN)**, which provides a principled density-based and probabilistic learning formulation with inherent interpretability.

My goal is to transform classical PNNs into a new generation of **robust, statistically aligned, and hierarchical probabilistic neural models** that integrate:

- robustness to noise, outliers, and class imbalance  
- statistically grounded dependency modeling (e.g., copula-based structure)  
- hierarchical and probabilistic representations  
- calibrated predictive uncertainty  
- interpretable density-level decision mechanisms  

Through this direction, I aim to unify **robust learning theory, probabilistic modeling, and neural architectures** within a single coherent framework. The long-term objective is to establish robust probabilistic neural learning systems that retain the transparency and uncertainty-awareness of classical statistical models while achieving the predictive power of modern machine learning—thereby enabling trustworthy deployment in biomedical and scientific applications.


---

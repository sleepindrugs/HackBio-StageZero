### **Single Cell, Big Data**

|By Team Valine 

### **1\. Introduction** 

The advent of high-throughput sequencing technologies has revolutionized molecular biology, fundamentally transforming our ability to study the dynamic landscape of an organism's genetic activity \[1\]. At the heart of this transformation is RNA sequencing (RNA-seq), a powerful genomic approach developed around 2008 (1-4) that allows for the detection and quantitative analysis of all RNA molecules (the transcriptome) within a biological sample \[2\]. Unlike previous methods such as microarrays or Sanger sequencing, RNA-seq offers unprecedented precision and breadth, enabling the discovery of novel transcripts, alternative splicing patterns, and a comprehensive view of gene expression dynamics that was previously impossible \[3\]. 

### **Big Data: Definition and the Four Vs** 

The term Big Data Analytics (BDA) refers to the use of computational methods, algorithms, and technologies that collect, process, and interpret massive and complex datasets to reveal patterns, correlations, and actionable insights \[4,5\].  BDA employs statistical and computational techniques such as clustering, regression, and predictive modeling, applied to large-scale datasets using tools like Hadoop, Spark, and NoSQL databases \[4,5\]. 

The nature of big data is defined by the five Vs:  
 • Volume: The sheer magnitude of data—ranging from terabytes to zettabytes—generated continuously \[4,5\].  
 • Variety: The heterogeneity of data, including structured, unstructured, and semi-structured formats \[4\].  
 • Velocity: The high speed at which data is generated and processed, enabling both batch and real-time analysis\[4,5\].  
 • Veracity: The reliability, accuracy, and trustworthiness of the data \[4\].  
 • Value: The actionable insights derived from data that create business or scientific impact \[4,5\]. 

This matches the characteristics of data produced by omics field. The analysis of these datasets are required to reveal interrelationships among biomolecules \[6,7\]. Subramanian et al. \[6\] emphasized that combining data across multiple molecular layers enhances understanding of disease mechanisms, enables precise patient stratification, and supports biomarker discovery. 

Big data omics analysis leverages a diverse ecosystem of tools to manage large-scale datasets including cloud computing frameworks, Machine learning and Deep learning. These offer predictive modeling and pattern recognition analysis \[7, 8, 9\]. 

### **2\. Bulk RNA Sequencing**

Bulk RNA sequencing (bulk RNA-seq) is a widely used transcriptomic technique that measures the average gene expression across a mixed population of cells derived from a tissue or cell sample. It defines the transcriptome profile by quantifying RNA molecules extracted from the entire sample without discriminating between different cell types within that population\[10\]. A review by Hegenbarth et al. (2022) discusses how bulk RNA-seq captures averaged gene expression profiles from tissue samples, covering gene expression changes in cardiac tissues but noting that it masks cellular heterogeneity intrinsic to complex tissues \[11\]. This means that since RNA is isolated from a heterogeneous mixture of cells, the resulting data reflect an aggregate signal representing the dominant cell types and states, masking individual cell variability. This averaging approach is suitable for investigating overall molecular changes and gene expression patterns within tissues or complex cell populations. Therefore, this approach is used to identify different sample conditions \[10\].

Workflow \-

The traditional bulk RNA-seq workflow as described by Wang et al. (2020) for clinical oncology includes covering sample harvesting, RNA isolation, library construction (poly-A selection or rRNA depletion), sequencing on Illumina platforms, followed by computational alignment and gene expression quantification. This study also emphasized quality control metrics such as RNA integrity number (RIN) for high-quality data \[10\].

Different Application \- 

Wang et al. (2020) applied bulk RNA sequencing to myeloproliferative neoplasm patient samples and healthy controls. They identified significant transcriptional alterations in immune response genes and mutation-associated expression changes, enabling discovery of disease-related expression profiles that differentiate patient from control samples, with clear clinical implications for prognosis and therapy \[11, 10\]. Barretto et al. (2025) used bulk RNA sequencing on 53 different neuron types from the *Caenorhabditis elegans* nervous system. They generated transcriptome profiles that offered high sensitivity and specificity for neuron-type-specific gene expression, including non-polyadenylated transcripts. This dataset provided detailed expression patterns at the neuronal population level and complemented existing single-cell data by detecting lowly expressed genes missed by scRNA-seq \[12\]. Li et al. (2021) review demonstrates bulk RNA-seq in cancer biology, focusing on gene expression differences between tumor and non-tumor tissue. They identified differentially expressed genes involved in tumorigenesis pathways, signaling processes, and immune escape mechanisms, highlighting molecular drivers of cancer progression uncovered by bulk transcriptome profiling \[13\]. The FoundationOne Heme RNA-seq panel, described by Li et al. (2021), uses bulk RNA sequencing to detect gene fusions, mutations, and expression signatures used clinically as biomarkers for cancer diagnosis, prognosis, and therapy selection. The panel has widespread adoption in clinical labs, demonstrating bulk RNA-seq utility in biomarker-driven precision oncology \[13\]. The *C. elegans* neuron bulk RNA-seq dataset by Barretto et al. (2025) represents a foundational transcriptomic resource detailing neuronal gene expression in an important model organism. It enables advanced research linking gene expression to neuron function, structure, and connectivity, providing a rich resource for neuroscience and developmental biology communities.

Limitation \-

The study by Wang et al. (2020) shows that bulk RNA-seq remains cost-effective for large clinical cohorts and provides a robust overview of the transcriptome that supports downstream biomarker panel development without the high computational and financial burden of single-cell sequencing. But it does not resolve cellular heterogeneity as it provides no spatial information within tissues as explained by Hegenbarth et al. (2022).  

This is where single cell RNA closes the gap for the limitations of Bulk RNA sequencing. 

### **3\. Single Cell RNA Sequencing** 

Single-cell RNA sequencing is an advanced approach for the transcriptomic analysis where the RNA molecules from a single cell of the population are isolated and sequenced using the next generation sequencing techniques. This will enable the researchers to visualize and analyze the critical functionalities and behaviors of the cell at molecular level and to differentiate between the cells of the same population. The transcriptome of a cell can reveal the state and identity of that cell in the given condition and time since RNA acts as cell’s regulatory molecules, messengers and essential component in housekeeping genes \[14\].The pioneering techniques to analyze transcriptomes at single cell level were relied on Fluorescent microscopic techniques which limited to only few genes \[14\]. The emergence of Single-cell RNA sequencing was after the advancement made in probe dependent single-cell qPCR where the gene expression analysis is performed on single-cell \[15\]. The transcriptomes developed by scRNA sequencing were first published by *Tang et al* in 2009\. The probe independent scRNA sequencing involves the following stages starting with isolation single cells, cell lysis, conversion of scRNA to cDNA by reverse transcription, bar-coding of DNA, Library preparation \- amplification of cDNA through PCR, sequencing and data analysis\[15\]. 

 *Why is scRNA sequencing better than other techniques?*

By far, to study and analyze the single-cell gene expression qRT- PCR is preferred, but it has some limitations like confinement to specific set of genes chosen by the experimentalists while microarray enables the transcriptome profiling, the requirement of probes and huge starting amounts of RNA make it very expensive. Therefore, scRNA sequencing best replaces the pioneering techniques to study transcriptomes at the single-cell level.

Applications

**Oncogenic analysis**: The application of scRNA sequencing in tumor has revealed the existence of transcriptional heterogeneity in cancer cells, for example, in melanoma the scRNA sequencing of CD45+ and CD45- cells is having different T cell exhaustion programs, a significant finding that is helpful for proper immunotherapy treatments \[16\]. Gu et al., \[17\] demonstrated that malignant epithelial cells exhibit transcriptional plasticity and interact dynamically with immune and fibroblast cells, shaping the immunosuppressive TME \[20\]. 

**Immune cell analysis**: Cells having the same genetic content but shows differential gene expression when assessed through scRNA sequencing. When the different population of dendritic cells is taken for scRNA sequencing and analyzed the expression levels of transcripts in individual cells of both populations, it is evident that the expression of housekeeping genes is higher in one subset compared to the other. This finding is also validated by SMART sequencing and RNA FISH techniques \[16\].

**Embryogenic development**: scRNA sequencing becomes crucial when the biological material available for analysis is very limited such as during embryogenic development. The whole genome expression analysis of the embryonic cells has provided valuable insights about the development of embryos after fertilization and allows researchers to predict further events in developmental embryos \[14\].

**Stem cell differentiation:** Differentiation of stem cells form the basis of organ development and it starts from a single cell; hence analysis of stem cells at single cell level will help to follow the trajectory of molecular markers at different stages of organ development. In the development of murine lung, previously unknown lineage specific markers in different subsets have been identified. Similarly, the development of skeletal muscles from primary myoblasts have shown the requirement of eight transcriptional factors to promote the expression of more than 1000 genes during the development \[15\]. 

### **4\. Comparison: Bulk RNA-seq vs Single Cell RNA-seq**

Bulk RNA sequencing: The conventional bulk RNA sequencing is the replacement of microarray technique in the late 2000s before the advancement of scRNA technique. Bulk sequencing of RNA is profiling the transcriptomes from the bulk population of cells; it will give the measurement of average transcript of the population \[16\]. Therefore,  bulk RNA sequencing (bulk RNA-seq) is the result of homogenic data. Homogeneity refers to datasets that assume all cells within a population behave similarly, producing an averaged signal  (Haque et al., 2017\) \[18\]. It fails to provide subtle and biologically significant differences between cells of the same population \[14\]. The bulk sequencing will not be able to detect the precise characterization of the subsets population of the cells with respect to its microenvironment \[17\].

scRNA sequencing: To understand the differential gene expression between the cells and genetic heterogeneity at transcriptome level, scRNA sequencing is the promising approach \[14,17\].  Choi and Kim (2019) explained that this heterogenic data shows the complexity of biological systems and is influenced by differences in development, environmental response, and stochastic gene expression \[17, 19\] It can give additional and different dimensionalities to the complete genome profile of a cell than bulk sequencing \[17\]. The sample collection for bulk sequencing can be done on tissues while scRNA requires viable cellular suspension and for scRNA the analysis must be completed within a few days of sample collection since the viability of samples may get affected. The cost involved in scRNA is huge compared to bulk sequencing due to the requirement of good quality RNA \[17, 20\]. 

### **11\. Future Directions: Spatial & Multi-Omics Approaches**

The improvement in bulk rna sequencing involves integrated bulk and single-cell RNA-seq data as seen by Barrett et al. (2025) on 53 *C. elegans* neuron types. This integration improved gene detection accuracy by combining high sensitivity of bulk RNA-seq with single-cell specificity, refining transcriptional profiles and reducing false positives from contamination in scRNA-seq data. Xu et al. (2025) applied Scissor, a machine learning-based algorithm, to integrate single-cell and bulk RNA-seq data to identify survival-associated cellular states in glioblastoma. This approach inferred cell type composition and clinical relevance from bulk transcriptomes guided by single-cell references \[21\]. Though not explicitly a single study, the 2025 review by Barrett et al. emphasizes that recent long-read RNA sequencing approaches applied to bulk samples enhance detection of alternative splicing, isoform diversity, and allele-specific expression, crucial for comprehensive transcriptome characterization. Zhang et al. (2025) constructed a prognostic model integrating bulk RNA-seq, scRNA-seq, and clinical data in hepatocellular carcinoma. Using machine learning, they linked T cell marker gene expression from single-cell data with clinical bulk RNA profiles to predict patient outcomes, showing computational annotation and integration \[22\].

### **12\. Conclusion**

Big data and its different analysis methods are crucial for advancement of modern medicine. The predictive models help manage and unlock deeper insights into cell, gene, protein, and metabolite behaviour, identity and disease at both bulk and single level. The future lies in integrating multi-omics and computational power to decode life.

**References** 

1\. Mortazavi A, Williams BA, McCue K, Schaeffer L, Wold B. Mapping and quantifying mammalian transcriptomes by RNA-Seq. Nat Methods. 2008;5(7):621-8.

2\. Cloonan N, Forrest AR, Kolle G, Gardiner BB, Faulkner GJ, Brown MK, et al. Stem cell transcriptome profiling via massive-scale mRNA sequencing. Nat Methods. 2008;5(7):613-9.

3\. Wang Z, Gerstein M, Snyder M. RNA-Seq: a revolutionary tool for transcriptomics. Nature reviews genetics. 2009 Jan;10(1):57-63.

4\.       What Is Big Data Analytics? Definition, Benefits, and More \[Internet\]. Coursera. 2023\. Available from: [https://www.coursera.org/in/articles/big-data-analytics](https://www.coursera.org/in/articles/big-data-analytics)

5\. Arena F, Pau G. An Overview of Big Data Analysis. Bull Electr Eng Inform. 2020;9(4):1646–53.

6\.  Subramanian I, Verma S, Kumar S, Jere A, Anamika K. Multi-omics Data Integration, Interpretation, and Its Application. Bioinformatics and Biology Insights. 2020;14:1–24.

7\.  Kaur P, Singh A, Chana I. Computational Techniques and Tools for Omics Data Analysis: State-of-the-Art, Challenges, and Future Directions. Arch Comput Methods Eng. 2021;28(7):4485–502.

8\.      Koppad S, Annappa B, Gkoutos GV, Acharjee A. Cloud Computing Enabled Big Multi-Omics Data Analytics. Bioinformatics and Biology Insights. 2021;15:1–16.

9\. Arjmand B, Hamidpour SK, Tayanloo-Beik A, Goodarzi P, Aghayan HR, Adibi H, et al. Review of Multi-Omics Data Integration Approaches and Tools in Translational Research. Front Genet. 2022;13:824451.

10\.  Wang Y, Mashock M, Tong Z, Mu X, Chen H, Zhou X, et al. Changing Technologies of RNA Sequencing and Their Applications in Clinical Oncology. Front Oncol. 2020;10:447.

11\. Hegenbarth J-C, Lezzoche G, De Windt LJ, Stoll M. Perspectives on Bulk-Tissue RNA Sequencing and Single-Cell RNA Sequencing for Cardiac Transcriptomics. Frontiers in Molecular Medicine. 2022;Volume 2 \- 2022\.

12\. Barrett A, Varol E, Weinreb A, Taylor SR, McWhirter RM, Cros C, et al. Integrating bulk and single cell RNA-seq refines transcriptomic profiles of individual C. elegans neurons. eLife Sciences Publications, Ltd; 2025\.

13\.     Li X, Wang C-Y. From bulk, single-cell to spatial RNA sequencing. International Journal of Oral Science. 2021;13(1):36.

14\. Kolodziejczyk AA, Kim JK, Svensson V, Marioni JC, Teichmann SA. The technology and biology of single-cell RNA sequencing. Molecular cell. 2015 May 21;58(4):610-20.

15\. Saliba AE, Westermann AJ, Gorski SA, Vogel J. Single-cell RNA-seq: advances and future challenges. Nucleic acids research. 2014 Aug 18;42(14):8845-60.

16\. Kashima, Y., Sakamoto, Y., Kaneko, K. *et al.* Single-cell sequencing techniques from individual to multiomics analyses. *Exp Mol Med* **52**, 1419–1427 (2020).

17\. Gu Y, Zhang Z, Peter Ten Dijke. Harnessing epithelial-mesenchymal plasticity to boost cancer immunotherapy. Cellular & Molecular Immunology/Cellular & molecular immunology. 2023 Feb 24;20(4):318–40.

18\. Haque A, Engel J, Teichmann SA, Lönnberg T. A practical guide to single-cell RNA-sequencing for biomedical research and clinical applications. Genome medicine. 2017 Aug 18;9(1):75.

19\. Choi YH, Kim JK. Dissecting cellular heterogeneity using single-cell RNA sequencing. Molecules and cells. 2019 Mar 1;42(3):189-99.

20\. Kuksin M, Morel D, Aglave M, Danlos FX, Marabelle A, Zinovyev A, Gautheret D, Verlingue L. Applications of single-cell and bulk RNA sequencing in onco-immunology. European journal of cancer. 2021 May 1;149:193-210.

21\.  Xu Z, Xi B, Huang J, Zhang L, Cui S, Wang X, et al. Integration of Single-Cell RNA and Bulk RNA Sequencing Reveals Cellular Heterogeneity and Identifies Survival-Associated Regulatory Networks in Glioblastoma. IET Syst Biol. 2025;19(1):e70025.

22.Zhang Y, Zhang H, Liu L. Integration of single-cell and bulk RNA sequencing identifies and validates T cell-related prognostic model in hepatocellular carcinoma. PLOS ONE. 2025;20(5):e0322706.


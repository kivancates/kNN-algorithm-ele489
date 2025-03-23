# k-NN Wine Dataset Classifier  

 The **Wine dataset** is used in this research to test a **k-Nearest Neighbors (k-NN)** classifier that was created from scratch.  It compares accuracy for a range of {k` values and assesses several distance metrics (Euclidean, Manhattan, and Chebyshev).  

 ## Project Organization  
 **`knn.py`**: a custom implementation of k-NN.  
 **`analysis.ipynb`** - Jupyter Notebook containing results, visualization, and dataset analysis.  
 The project description and setup instructions can be found in **`README.md`**.  

 ## Dataset  
 The **Wine dataset**, which includes **178 wine samples** with **13 chemical properties**, was sourced from **scikit-learn**.  It divides wines into **three classes** according to their chemical makeup.  

 **Features:** - Magnesium, ash, alcohol, malic acid, etc.  
 The target classes are wine kinds `1, 2, 3`.  

 ## Results
 As a result of testing 3 different distance finding methods and different **k** values, it was determined that the most suitable distance finding method for this data set was the **Euclidean Distance** method and the most suitable **k** value for this method was determined to be **7**. These tests are given in detail in the report and it is also explained which feature is more effective in classification.


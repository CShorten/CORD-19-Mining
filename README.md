# CORD-19-Mining
Thanks for checking out this CORD-19 Mining Repository!

This repository contains some notebooks for processing the CORD-19 dataset, hosted on Kaggle!
<br /><br />
<h2> Major Notebooks </h2>
<table>
  <tr>
  <th><a href = "https://github.com/CShorten/CORD-19-Mining/blob/main/How_Papers_Are_Stored.ipynb"> How Papers Are Stored </a></th>
    <th> This notebook illustrates the JSON structure of each paper in the dataset </th>
  </tr>
  <tr>
    <th><a href = "https://github.com/CShorten/CORD-19-Mining/blob/main/Contrastive_Learning.ipynb"> Contrastive Learning </a>
    </th>
    <th style = "color:red;"> This notebook loads the sequences and labels stored in a DataFrame, tokenizes them, and feeds it to siamese transformers for similarity loss </th>
</table>
  
<h2> Utilities to Data Preprocessing </h2>
<table>
   <tr>
     <th><a href = "https://github.com/CShorten/CORD-19-Mining/blob/main/Pdf_Json_Chunker.ipynb">Splitting up the pdf_json folder </a></th>
     <th> This notebook splits up the pdf_json folder to make smaller files to load into colab </th>
  </tr>
  <tr>
     <th><a href = "https://github.com/CShorten/CORD-19-Mining/blob/main/Atomic_Unit_Construction.ipynb">Truncating Body Texts, Assigning Class Labels for each Paper </a></th>
    <th> This notebook loops through the papers in the pdf_json folder, processes each body text for sequence inputs to the contrastive learning network, and it assigns a class label corresponding to paper membership </th>
  </tr>
  
  </table>

<div align="left">
  <h1>NETFLIX MOOD RECOMMENDER</h1>

   <img src="https://www.euskadi.eus/contenidos/evento/gt_netflix_20/es_def/images/Netflix.jpg" alt="Portfolio Analysis" style="width: 70%; height: auto;">


---

<div style="text-align: left;">
  <h2>About the Project :movie_camera:	</h2>

 <p>
Lately, I have become interested in natural language processing (NLP), the machine learning technology that allows us to "translate" human language into a coding that machines can understand. I am drawn to the idea that an AI can not only interpret the frequency of elements in speech but also manage to interpret the context of what is being said.
 </p>
 <p>
I have dabbled in language processing before, such as in the <strong><a href="https://github.com/TonioDominguez/Fake_News_Detector">Fake News Detector project</a></strong>. In that project, I used NLP to measure the frequency of key terms in a large dataset and, based on that, developed a linear classification model to categorize new articles as True or False. Additionally, in the same project, I approached Sentiment Analysis at a basic level to demonstrate the hypothesis that Fake News is generally written from a very negative perspective.
</p>
<p>
Now, in this project, I am delving deeper into natural language processing. This time, through Mood Analysis. I process it using an NLP model called <strong><a href="https://huggingface.co/j-hartmann/emotion-english-distilroberta-base">Emotion English DistilRoBERTa-base</a></strong> from Hugging Face, a refined version of RoBERTa (a famous model that works by seeking relationships between language and context) that classifies moods into labels (joy, anger, disgust, fear…).
</p>
  
  <h3>Objective:</h3>
  <p>
    With this project, I primarily aim to break down the synopses of each entry to classify the titles in the Netflix catalog into different moods. This way, I can offer users the possibility of receiving a suggestion based on how they feel.
  </p>
  
  <h3>Methodology:</h3>
  <ol>
    <li><strong>Data Preprocessing and EDA:</strong> Preprocessing the dataset to properly tailor it to the information the user will receive when requesting a suggestion from the catalog. Additionally, exploring the data to gain a detailed understanding of the catalog's characteristics.</li>
    <li><strong>Mood Analysis:</strong> Applying NLP to the synopses of the titles through an ML pipeline that will classify the entries according to moods.</li>
    <li><strong>Netflix Recommender:</strong> Creating the code for the recommender, which will offer titles based on the inputs provided by the user.</li>
  </ol>

---

<div style="text-align: left;">
<h2>Project Structure :open_file_folder:</h2>

<p>
  This project is developed through three notebooks.
</p>

<ol>
  <li>
    <strong><a href="https://github.com/TonioDominguez/Netflix_mood_recommender/blob/main/Netflx_catalogue_EDA.ipynb">DATASET PREPROCESSING & EDA</a></strong>
  </li>
  
  <li>
    <strong><a href="https://github.com/TonioDominguez/Netflix_mood_recommender/blob/main/Sentiment_Analysis_Model.ipynb">CATALOGUE MOOD ANALYSIS</a></strong>
  </li>
  
  <li>
    <strong><a href="https://github.com/TonioDominguez/Netflix_mood_recommender/blob/main/Mood_recommender.ipynb">NETFLIX MOOD RECOMMENDER</a></strong>
  </li>
</ol>

---

<div style="text-align: left;">
  <h2>Work in Progress :warning:</h2>

  <p>
    
For now, I am still working on the project. It is almost finished (EDA complete, main recommender functions developed...), however, I still need to fine-tune the recommender's filtering options and create a Streamlit framework to present and demonstrate its functionality.
  </p>
</div>

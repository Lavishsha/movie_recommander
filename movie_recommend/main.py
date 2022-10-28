import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import tk
import difflib
import tkinter as tk

def recommand(movie_name):
  movies_data = pd.read_csv('moviedataset.csv')
  selected_features = ['genres' , 'keywords','tagline','cast','director']
  for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

  combined_features = movies_data['genres'] +' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
  vectorizer = TfidfVectorizer()
  feature_vectors = vectorizer.fit_transform(combined_features)

  similarity = cosine_similarity(feature_vectors)

  # movie_name = input("enter your fovourite movie name")
  list_of_all_titles = movies_data['title'].tolist()

  find_close_match = difflib.get_close_matches(movie_name , list_of_all_titles)
  close_match = find_close_match[0]
  index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

  similarity_score = list(enumerate(similarity[index_of_the_movie]))

  sorted_similar_movies = sorted(similarity_score ,key = lambda x:x[1] , reverse = True)

  print("Movies suggested for you :\n")
  i = 1
  list1 = []
  for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if (i<20):
      list1.append(title_from_index)
      i+=1
  return list1

def printMovie():
  inp  = movie_name.get(1.0 , "end-1c")
  l = recommand(inp)
  for i in l:
    output.insert(tk.END , "[ " + i + " ],")



window = tk.Tk()
window.geometry("600x600")
window.config(bg="#ABEBC6")
window.resizable(width=False, height=False)
window.title('Movie Name Suggestor')

l1 = tk.Label(window, text="Enter your favourite Movie so we can suggest you similar movie", font=("Arial", 15), fg="Black", bg="White")

movie_name = tk.Text(window,height = 1,width = 18)
movie_name.pack()
b1 = tk.Button(window, text="Suggest Movie", font=("Arial", 15), bg="darkgreen", fg="white",command=printMovie)
# recommand(movie_name)
l1.place(x=30, y=10)
b1.place(x=200, y=120)
# t1.place(x=15, y=120)
# lbl = tk.Label(window , text = "")
# lbl.pack(padx = 5 , pady=10)
# lbl.place(x = 150 , y = 150)
# lbl.pack()
output = tk.Text(window , height = 20 , width = 18)
output.place(x = 200 , y = 170)
movie_name.place(x=200 , y=80)
window.mainloop()






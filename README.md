# Music Analysis
This project analyzes a Spotify dataset to explore musical trends, 
focusing on attributes such as musical keys, modes, and other song features. 
The project aims to uncover patterns in song popularity, mood, and tonal preferences.

# Project Overview
The main goal of this project is to analyze song attributes and provide insights into the characteristics of popular songs in different musical keys and modes. 
Using Python libraries, such as Pandas, Seaborn, and Matplotlib, we visualize trends in song popularity, mode distribution, and other features.

# Dataset
The dataset used for this project consists of songs from Spotify, including various attributes:

- artistName: Name of the artist.
- trackName: Name of the song.
- key: Musical key of the song, represented as an integer (0-11).
- mode: Mode of the song (0 = minor, 1 = major).
- energy, danceability, valence, liveness, acousticness: Various audio features of the song, representing its mood and style.
- msPlayed: Duration of the song played in milliseconds.

# Prerequisites
The project requires the following libraries:

- pandas
- numpy
- matplotlib
- seaborn
- spotipy (if accessing Spotify API) you can refer https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3 by Vlad Gheorghe.

# Results
The analysis of the Spotify dataset provided several insights into the characteristics and trends of popular songs, focusing on musical attributes and listener preferences:

- Key and Mode Distribution: The majority of songs are composed in minor keys, particularly F minor, G minor, and C minor, indicating a preference for a somber or reflective mood. Major keys, while present, are less frequent, with B major and E major being the most popular among them.

- Correlation of Audio Features: The correlation heatmap revealed that certain features have a moderate to strong correlation:

- Energy and Danceability: Songs with higher energy tend to have higher danceability, suggesting that upbeat, high-energy tracks are often designed for dancing.
Valence and Acousticness: Negative correlation observed here may indicate that acoustic tracks tend to have a lower "valence" (happiness factor), often leading to more mellow or sadder tracks.
Popular Genres and Artists: The data highlighted certain genres and artists that dominate the dataset. Artists with higher song counts in specific keys and modes suggest their consistent stylistic preferences, possibly influencing their listener base.

- Trends Over Time: (If applicable) The time series analysis might have shown trends in feature preferences over the years, such as an increase in danceability and energy in recent years, reflecting current trends in music production.

- Distribution of Playtime: The analysis of playtime across different songs and artists provided insights into listener engagement, revealing which types of songs tend to have longer or more frequent play durations.

These findings offer a deeper understanding of musical trends and listener preferences within the dataset. Such insights could guide music producers, artists, and marketers in creating and promoting music that aligns with listener tastes. Furthermore, these patterns could be leveraged for predictive modeling, aiming to identify potential hit songs based on audio features.

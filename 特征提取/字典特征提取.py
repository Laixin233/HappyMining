
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()

measurements = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Francisco', 'temperature': 18.},
]

x = vec.fit_transform(measurements).toarray()
print(x)
print(vec.get_feature_names())

movie_entry = [{'category': ['thriller', 'drama'], 'year': 2003},
               {'category': ['animation', 'family'], 'year': 2011},
               {'year': 1974}]
x = vec.fit_transform(movie_entry).toarray()
print(x)

vec.get_feature_names()

vec.transform({'category': ['thriller'],
               'unseen_feature': '3'}).toarray()

pos_window = [
    {
        'word-2': 'the',
        'pos-2': 'DT',
        'word-1': 'cat',
        'pos-1': 'NN',
        'word+1': 'on',
        'pos+1': 'PP',
    },
    # in a real application one would extract many such dictionaries
]
vec = DictVectorizer()
pos_vectorized = vec.fit_transform(pos_window)
print(pos_vectorized)


x = pos_vectorized.toarray()
print(x)

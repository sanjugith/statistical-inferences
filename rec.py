#!/usr/bin/env python
# encoding: utf-8
"""
tag_clustering.py

"""

import csv

# from Pycluster import *
#from hcluster import *

from sklearn.metrics.pairwise import euclidean_distances

class TagClustering(object):

    def __init__(self):
        tag_data = self.load_link_data()
        # print tag_data
        all_tags = []
        all_urls = []
        for url,tags in tag_data.items():
            all_urls.append(url)
            all_tags.extend(tags)

        all_tags = list(set(all_tags)) # list of all tags in the space
        
        numerical_data = {} # create vectors for each item
        for url,tags in tag_data.items():
            v = []
            for t in all_tags:
                if t in tags:
                    v.append(1)
                else:
                    v.append(0)
            numerical_data[url] = v

        recommend_url = 'http://www.qwantz.com/index.php'
        results = {}
        print(numerical_data['http://www.qwantz.com/index.php'])

        for url,vector in numerical_data.items():
            d = euclidean_distances([numerical_data[recommend_url]],[numerical_data[url]])
            results[url] = d

        #print(sorted(results.items(), key=lambda u, s: (s, u)))
        print(sorted(results.items(), key=lambda sort_key: sort_key[1]))
        #print(sorted(results.items(), key=lambda sort_key: sort_key[1])[0:5])

    def load_link_data(self,filename="links.csv"):
        data = {}

        r = csv.reader(open(filename, 'r'))
        for row in r:
            data[row[0]] = row[1].split(',')

        return data
        

if __name__ == '__main__':
	t = TagClustering()


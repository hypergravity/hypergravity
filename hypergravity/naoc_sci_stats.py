# import os
# import requests
# import json
#
#
# def ads(lib_id="v89_ChWTSKOUFvCpxOm6Tg", token="6OEonb0MGO6EzpatpzomBSJrXXbJziaiz6qzPTQn", tofile=None, rows=500,
#         sep="%"):
#     """
#
#     Parameters
#     ----------
#     lib_id:
#         ads library ID
#     token:
#         ADS API token, get it from https://ui.adsabs.harvard.edu/user/settings/token
#     tofile:
#         if not None, save to text file
#     rows:
#         max entries
#     sep:
#         detaults to "%" (a line starts with "%")
#         the content above the sep line will be reserved during the update
#
#     Returns
#     -------
#     if tofile is None, return bibtex, else nothing
#
#     """
#     # get the data for a specific library
#     r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/{}".format(lib_id),
#                      headers={"Authorization": "Bearer " + token}, params={"rows": rows})
#     bibtags = r.json()["documents"]
#
#     # get the AASTeX entries for multiple bibcodes
#     payload = {"bibcode": bibtags,
#                "sort": "year desc"}
#     r = requests.post("https://api.adsabs.harvard.edu/v1/export/bibtex",
#                       headers={"Authorization": "Bearer " + token, "Content-type": "application/json"},
#                       data=json.dumps(payload))
#     print(r.json()["msg"])
#     bibtex = r.json()["export"]
#
#     if tofile is None:
#         return bibtex
#     else:
#         if not os.path.exists(tofile):
#             # if file does not exist
#             with open(tofile, "w+") as f:
#                 f.write(bibtex)
#         else:
#             # if file exists
#             with open(tofile, "r") as f:
#                 old = f.readlines()
#             reserved = []
#             for _i, _ in enumerate(old):
#                 if _.startswith(sep):
#                     reserved = old[:_i + 1]
#             # remove file
#             os.remove(tofile)
#             # write a new file
#             with open(tofile, "w+") as f:
#                 f.writelines(reserved)
#                 f.writelines(["\n", ])
#                 f.writelines(bibtex)
#         print("@Bo: bibtex saved to {}\n".format(tofile))
#         return
#
# r = ads(lib_id="v89_ChWTSKOUFvCpxOm6Tg", token="6OEonb0MGO6EzpatpzomBSJrXXbJziaiz6qzPTQn", tofile=None, rows=500, sep="%")
#
#
#
# import logging
# import tqdm
#
# from urllib.parse import urlencode
#
# def citation_stats(bibcode="2020ApJS..246....9Z", year=None, refereed=True):
#
# # query citations
# query = f'citations(bibcode:{bibcode})' if year is None else f'citations(bibcode:{bibcode}) year:{year}'
# # the "q" key below designates that this is the search query, while the "fl" refers to the fields to return
# encoded_query = urlencode({'q': query, 'fl': 'bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub'})
# results = requests.get("https://api.adsabs.harvard.edu/v1/search/bigquery?{}".format(encoded_query), \
#                        headers={'Authorization': 'Bearer ' + token}, params={"rows": 10000, property:"refereed"})
# # format the response in a nicely readable format
# cite_list = results.json()["response"]["docs"]
#
# query = f'bibcode:{bibcode}'
# # the "q" key below designates that this is the search query, while the "fl" refers to the fields to return
# encoded_query = urlencode({'q': query, 'fl': 'bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub'})
# results = requests.get("https://api.adsabs.harvard.edu/v1/search/bigquery?{}".format(encoded_query), \
#                        headers={'Authorization': 'Bearer ' + token}, params={"rows": 10000})
# # format the response in a nicely readable format
# paper_info = results.json()["response"]["docs"][0]
#
# paper_authors = {author.lower().replace("-", "") for author in paper_info["author"]}
# citation_others = []
# for citation in cite_list[::-1]:
#     citation_authors = {author.lower().replace("-", "") for author in citation["author"]}
#     if len(paper_authors.intersection(citation_authors)) > 0:
#         print("Found self-citation: {}".format(citation["bibcode"]))
#     else:
#         citation_others.append(citation)
#
# from astropy.table import Table
# Table(citation_others).show_in_browser()
#
#
#
#
#
#
# #%% browse a library
# lib_id="v89_ChWTSKOUFvCpxOm6Tg"
# token="6OEonb0MGO6EzpatpzomBSJrXXbJziaiz6qzPTQn"
# # get the data for a specific library
# r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/{}".format(lib_id),
#                  headers={"Authorization": "Bearer " + token}, params={"rows": 1000})
# bibtags = r.json()["documents"]
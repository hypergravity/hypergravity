from urllib.parse import urlencode
from collections import OrderedDict
import requests
from astropy.table import Table

from .enc import MY_ADSABS_TOKEN


def citation_stats(bibcode="2020ApJS..246....9Z", year="2000-2022", token=None):
    """Count refereed citation by others."""
    if token is None:
        print("Using default token ...")
        token = MY_ADSABS_TOKEN

    # query the paper
    print("Query for paper info ...")
    query = f'bibcode:{bibcode}'
    encoded_query = urlencode(
        {
            'q': query,
            'fl': 'bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub'
        }
    )
    results = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query),
        headers={'Authorization': 'Bearer ' + token},
        params={"rows": 10000}
    )
    paper_info = results.json()["response"]["docs"][0]

    # query citations
    print("Query for citation info ...")
    query = f'citations(bibcode:{bibcode})' if year is None else f'citations(bibcode:{bibcode}) year:{year}'
    encoded_query = urlencode(
        {
            'q': query,
            'fl': 'bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub',
            'sort': 'date+desc'
         }
    )
    results = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query),
        headers={'Authorization': 'Bearer ' + token},
        params={"rows": 10000, property: "refereed"}
    )
    citation_list = results.json()["response"]["docs"]

    # standardize authors
    paper_authors = {author.lower().replace("-", "") for author in paper_info["author"]}
    citation_others = []
    for citation in citation_list:
        citation_authors = {author.lower().replace("-", "") for author in citation["author"]}
        if "arxiv" in citation["bibcode"].lower():
            print(" - Eliminating non-refereed citation: {}".format(citation["bibcode"]))
        elif len(paper_authors.intersection(citation_authors)) > 0:
            print(" - Eliminating self-citation: {}".format(citation["bibcode"]))
        else:
            citation_others.append(OrderedDict(citation))
            citation_others[-1]["author"] = "; ".join(citation_others[-1]["author"])
    print(f"Result: {len(citation_others)} citations by others!")
    tbl_citation_others = Table(citation_others)
    tbl_citation_others.sort("date")
    # tbl_citation_others.show_in_browser()
    return tbl_citation_others

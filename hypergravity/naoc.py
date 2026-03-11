from collections import OrderedDict
from urllib.parse import urlencode

import requests
from astropy.table import Table, Column

from .config import load_token


def citation_stats(
    bibcode="2020ApJS..246....9Z", year="2000-2022", token=None, verbose=True
):
    """Count refereed citation by others.

    Parameters
    ----------
    bibcode:
        The `bibcode` of the article.
    year: str
        The `year` of citations.
    token: None or str
        The `adsabs` token.
    verbose: bool
        If true, print verbose info.
    """
    if token is None:
        token = load_token()
        if token is None:
            raise ValueError("No token found! Please set token first using: citation token set xxx")
        if verbose:
            print("\033[1;34m📝 Using token from ~/.hypergravity/ads_token\033[0m")

    # query the paper
    if verbose:
        print("\033[1;34m🔍 Querying paper info ...\033[0m")
    query = f"bibcode:{bibcode}"
    encoded_query = urlencode(
        {
            "q": query,
            "fl": "bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub",
        }
    )
    results = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query),
        headers={"Authorization": "Bearer " + token},
        params={"rows": 10000},
    )
    paper_info = results.json()["response"]["docs"][0]
    
    if verbose:
        print("\n" + "="*80)
        print(f"\033[1;36m📄 目标论文信息\033[0m")
        print("="*80)
        print(f"  \033[1mTitle:\033[0m {paper_info['title']}")
        print(f"  \033[1mBibcode:\033[0m {paper_info['bibcode']}")
        print(f"  \033[1mJournal:\033[0m {paper_info['pub']}")
        print(f"  \033[1mTotal Citations:\033[0m {paper_info['citation_count']}")
        print(f"  \033[1mAuthors:\033[0m {'; '.join(paper_info['author'])}")
        print("="*80 + "\n")

    # query citations
    if verbose:
        print("\033[1;34m📊 Querying citation info ...\033[0m\n")
    query = (
        f"citations(bibcode:{bibcode})"
        if year is None
        else f"citations(bibcode:{bibcode}) year:{year}"
    )
    encoded_query = urlencode(
        {
            "q": query,
            "fl": "bibcode,title,author,citation_count,date,pubdate,doi,volume,issue,page,pub",
            "sort": "date",
        }
    )
    results = requests.get(
        "https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query),
        headers={"Authorization": "Bearer " + token},
        params={"rows": 10000, property: "refereed"},
    )
    citation_list = results.json()["response"]["docs"]

    # standardize authors
    paper_authors_set = {author.lower().replace("-", "") for author in paper_info["author"]}
    paper_authors_original = paper_info["author"]
    citation_others = [
        OrderedDict(paper_info),
    ]
    citation_others[-1]["author"] = "; ".join(citation_others[-1]["author"])
    
    eliminated_non_refereed = []
    eliminated_self_citation = []
    
    for citation in citation_list:
        citation_authors_set = {
            author.lower().replace("-", "") for author in citation["author"]
        }
        
        def highlight_author(author):
            author_normalized = author.lower().replace("-", "")
            if author_normalized in paper_authors_set:
                return f"\033[1;93m{author}\033[0m"
            return author
        
        authors_formatted = "; ".join([highlight_author(a) for a in citation["author"]])
        
        if "arxiv" in citation["bibcode"].lower():
            eliminated_non_refereed.append((citation, authors_formatted))
        elif len(paper_authors_set.intersection(citation_authors_set)) > 0:
            eliminated_self_citation.append((citation, authors_formatted))
        else:
            citation_others.append(OrderedDict(citation))
            citation_others[-1]["author"] = "; ".join(citation_others[-1]["author"])
    
    if verbose:
        if eliminated_non_refereed:
            print("\033[1;31m❌ 排除非同行评议文章 ({})\033[0m".format(len(eliminated_non_refereed)))
            print("-"*80)
            for i, (citation, authors) in enumerate(eliminated_non_refereed, 1):
                print(f"\033[1;31m  [{i}]\033[0m Bibcode: {citation['bibcode']}")
                print(f"       Title: {citation['title']}")
                print(f"       Authors: {authors}")
                print()
        
        if eliminated_self_citation:
            print("\033[1;33m⚠️  排除自引文章 ({})\033[0m".format(len(eliminated_self_citation)))
            print("-"*80)
            for i, (citation, authors) in enumerate(eliminated_self_citation, 1):
                print(f"\033[1;33m  [{i}]\033[0m Bibcode: {citation['bibcode']}")
                print(f"       Title: {citation['title']}")
                print(f"       Authors: {authors}")
                print()
    
    print("\n" + "="*80)
    print(f"\033[1;32m✅ 结果统计\033[0m")
    print("="*80)
    print(f"  总引用数: {len(citation_list) + 1}")
    print(f"  排除非同行评议: {len(eliminated_non_refereed)}")
    print(f"  排除自引: {len(eliminated_self_citation)}")
    print(f"  \033[1;32m有效他引: {len(citation_others)}\033[0m")
    print("="*80 + "\n")
    tbl_citation_others = Table(citation_others)
    tbl_citation_others.sort("date")

    # add year column
    year = list(tbl_citation_others["date"].data)
    year = [str(y)[:4] for y in year]
    tbl_citation_others.add_column(Column(name="year", data=year))

    # reorder columns
    # title, pub, year, volume, issue, page, author, bibcode, etc
    result = tbl_citation_others[
        "title",
        "pub",
        "year",
        "volume",
        "issue",
        "page",
        "author",
        "bibcode",
        "date",
        "doi",
        "pubdate",
        "citation_count",
    ]

    # show in browser
    result.show_in_browser()
    
    return result

===============
Count citations
===============

Count citations by others, step-by-step:

1. Install `hypergravity` via

.. code-block:: bash

    $ pip install git+https://github.com/hypergravity/hypergravity.git

2. Run the code below with your article `bibcode`:

.. code-block:: python

    >>> from hypergravity.naoc import citation_stats
    >>> citation_stats(bibcode='2019ApJ...871..184T', year="2000-2022").show_in_browser()
    Using default token ...
    Query for paper info ...
    Query for citation info ...
     - Eliminating self-citation: 2022AJ....164..241Y
     - Eliminating non-refereed citation: 2020arXiv200507210L
     - Eliminating self-citation: 2021ApJ...919...66B
     - Eliminating self-citation: 2019ApJ...881..164Y
     - Eliminating self-citation: 2022RAA....22b5007Y
     - Eliminating self-citation: 2020ApJ...899..110T
     - Eliminating self-citation: 2020ApJS..248...28T
    Result: 16 citations by others!

3. Check the citations in the webpage carefully.

API
---

.. automodule:: hypergravity.naoc
    :members:

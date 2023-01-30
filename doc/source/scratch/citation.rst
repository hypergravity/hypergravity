===============
Count citations
===============

Count citations by others, step-by-step:

1. Install `hypergravity` via

.. code-block:: bash

    pip install git+https://github.com/hypergravity/hypergravity.git

You will see info like below:

.. code-block::

    Collecting git+https://github.com/hypergravity/hypergravity.git
      Cloning https://github.com/hypergravity/hypergravity.git to /private/var/folders/2y/b85hkd6543v71b_2f08ycrp00000gn/T/pip-req-build-_uaiq9mi
      Running command git clone --filter=blob:none --quiet https://github.com/hypergravity/hypergravity.git /private/var/folders/2y/b85hkd6543v71b_2f08ycrp00000gn/T/pip-req-build-_uaiq9mi
      Resolved https://github.com/hypergravity/hypergravity.git to commit d9c62a609a03fef5acd475fde9793fca29b00784
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
      Preparing metadata (pyproject.toml) ... done
    Building wheels for collected packages: hypergravity
      Building wheel for hypergravity (pyproject.toml) ... done
      Created wheel for hypergravity: filename=hypergravity-0.0.1-py3-none-any.whl size=2666 sha256=48767856df743fa4957cd617d4ef97701f1ce41fd12d61970b94408ed983e486
      Stored in directory: /private/var/folders/2y/b85hkd6543v71b_2f08ycrp00000gn/T/pip-ephem-wheel-cache-hnfq8nf8/wheels/56/de/79/b31b76373e8816382f799838320f7f090e2b8ff6326859f092
    Successfully built hypergravity
    Installing collected packages: hypergravity
    Successfully installed hypergravity-0.0.1

2. Run the code below with your article `bibcode`:

.. code-block:: python
    :linenos:

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

===============
Count citations
===============

Count citations by others, step-by-step:

1. Install `hypergravity` via

.. code-block:: bash

    $ pip install git+https://github.com/hypergravity/hypergravity.git

2. Set your ADSABS token (get it from https://ui.adsabs.harvard.edu/user/settings/token):

.. code-block:: bash

    $ citation token set your_adsabs_token_here

3. Verify your token:

.. code-block:: bash

    $ citation token show

4. Run the citation stats via command line:

.. code-block:: bash

    $ citation stats --bibcode=2020ApJS..246....9Z --year=2000-2025

Or use Python API:

.. code-block:: python

    >>> from hypergravity.naoc import citation_stats
    >>> result = citation_stats(bibcode='2020ApJS..246....9Z', year="2000-2025")

5. Check the citations in the webpage carefully.

Commands
--------

Token management:

.. code-block:: bash

    # Set token
    citation token set <your_token>
    
    # Show current token
    citation token show
    
    # Help
    citation token --help

Citation stats:

.. code-block:: bash

    # Basic usage
    citation stats --bibcode=<bibcode> --year=<year_range>
    
    # With custom token (optional)
    citation stats --bibcode=<bibcode> --year=<year_range> --token=<your_token>
    
    # Help
    citation stats --help

API
---

.. automodule:: hypergravity.naoc
    :members:

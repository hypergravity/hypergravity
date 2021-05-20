## A self-introduction
- I'm a post-doc/**LAMOST Fellow** at Department of Astronomy, Beijing Normal University (BNU).
- I'm interested in applying machine learning techniques to stellar spectroscopy.
- I'm recently working on spectroscopic binary stars.
- I have developed automated pipelines for the **SONG** and **BFOSC**.

## Related facilities: 
  - **LAMOST**: 
    A large optical spectroscopic survey at R=1,800/7,500
  - **SONG**: 
    A time-domain global observation network at R=36,000-180,000. 
  - Xinglong 2.16m:
    **BFOSC** E9+G10 (R=10,000) / **HRS** (R=40,000)
    
## Recent Events 
[last updated: 2021-05-20]
- 2021-05-20: Added SLAM+
  - A tutorial is [**here**](https://nbviewer.jupyter.org/github/hypergravity/laspec/blob/master/tutorial/20210520_slamplus_tutorial.ipynb), test data is [**here**](http://paperdata.china-vo.org/bozhang/slamplus/slamplus_test_data.dump).
- 2021-04-05: Uploaded RV & RVZPs of LAMOST MRS DR7
  - [https://github.com/hypergravity/paperdata](https://github.com/hypergravity/paperdata)
- 2021-01-23: Documentation for **laspec** [**NEW!**]:
  - [https://laspec.readthedocs.io/en/latest/](https://laspec.readthedocs.io/en/latest/)
- 2020-11-06: Paperdata:
  - paper data can be found in the repository [**paperdata**](https://github.com/hypergravity/paperdata).
- 2020-11-06: Spectroscopy slides
  - For the slides on spectroscopy @Nanjing, click [**here**](https://github.com/hypergravity/spectroscopy)

## My packages
- You can find some useful repositories in my github page, including
  - [slam](https://github.com/hypergravity/astroslam): extracting stellar parameters from spectra using a forward modelling
  - [laspec](https://github.com/hypergravity/laspec): several modules designed for LAMOST spectra
  - [berliner](https://github.com/hypergravity/berliner): some tools on processing stellar tracks and isochrones
  - [regli](https://github.com/hypergravity/regli): a fast, high-dimension linear interpolation tool (faster than the scipy version)
  - [songcn](https://github.com/hypergravity/songcn): a reduction pipeline (of echelle spectra) for the song-china project
- To install my packages
  - `pip install -U git+git://github.com/hypergravity/astroslam`
  - `pip install -U git+git://github.com/hypergravity/laspec`
  - `pip install -U git+git://github.com/hypergravity/berliner`
  - `pip install -U git+git://github.com/hypergravity/regli`
  - `pip install -U git+git://github.com/hypergravity/songcn`
- To install frequently used packages
  - `pip install -U astropy ginga scikit-learn joblib emcee corner ipyparallel`

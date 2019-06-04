# holes problem

Total of holes in each char per words

Some test cases:

    >>> num_buracos("Banana")
    5
    >>> num_buracos("olho")
    2
    >>> num_buracos("çzt")
    0

Running as script (works only with **Python 3**):

    $ python holes.py aça a10 bBc *g%

    palavra 'aça' contém '2' buraco(s)
    palavra 'a10' contém '1' buraco(s)
    palavra 'bBc' contém '3' buraco(s)
    palavra '*g%' contém '1' buraco(s)
    total de '7' buraco(s)

Running the test unit:

    $ python holes_tests.py 
    
    palavra '666' contém '0' buraco(s)
    palavra 'aaa' contém '3' buraco(s)
    palavra 'b01' contém '1' buraco(s)
    total de '4' buraco(s)
    palavra 'b01' contém '1' buraco(s)
    palavra 'b01' contém '1' buraco(s)
    palavra 'ABc' contém '3' buraco(s)
    .....
    ----------------------------------------------------------------------
    Ran 6 tests in 0.000s

    OK

The source passed the pylint checks:

    $ pylint3 holes.py 
    No config file found, using default configuration
    
    -------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 9.66/10, +0.34)


.. _API-enum-dvbfe-search:

=================
enum dvbfe_search
=================

*man enum dvbfe_search(9)*

*4.6.0-rc1*

search callback possible return status


Synopsis
========

.. code-block:: c

    enum dvbfe_search {
      DVBFE_ALGO_SEARCH_SUCCESS,
      DVBFE_ALGO_SEARCH_ASLEEP,
      DVBFE_ALGO_SEARCH_FAILED,
      DVBFE_ALGO_SEARCH_INVALID,
      DVBFE_ALGO_SEARCH_AGAIN,
      DVBFE_ALGO_SEARCH_ERROR
    };


Constants
=========

DVBFE_ALGO_SEARCH_SUCCESS
    The frontend search algorithm completed and returned successfully

DVBFE_ALGO_SEARCH_ASLEEP
    The frontend search algorithm is sleeping

DVBFE_ALGO_SEARCH_FAILED
    The frontend search for a signal failed

DVBFE_ALGO_SEARCH_INVALID
    The frontend search algorith was probably supplied with invalid parameters and the search is an invalid one

DVBFE_ALGO_SEARCH_AGAIN
    The frontend search algorithm was requested to search again

DVBFE_ALGO_SEARCH_ERROR
    The frontend search algorithm failed due to some error

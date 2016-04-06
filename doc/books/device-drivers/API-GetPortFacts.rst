
.. _API-GetPortFacts:

============
GetPortFacts
============

*man GetPortFacts(9)*

*4.6.0-rc1*

Send PortFacts request to MPT adapter.


Synopsis
========

.. c:function:: int GetPortFacts( MPT_ADAPTER * ioc, int portnum, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``portnum``
    Port number

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Returns 0 for success, non-zero for failure.


.. _API-GetIocFacts:

===========
GetIocFacts
===========

*man GetIocFacts(9)*

*4.6.0-rc1*

Send IOCFacts request to MPT adapter.


Synopsis
========

.. c:function:: int GetIocFacts( MPT_ADAPTER * ioc, int sleepFlag, int reason )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Specifies whether the process can sleep

``reason``
    If recovery, only update facts.


Description
===========

Returns 0 for success, non-zero for failure.

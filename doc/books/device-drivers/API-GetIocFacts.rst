.. -*- coding: utf-8; mode: rst -*-

.. _API-GetIocFacts:

===========
GetIocFacts
===========

*man GetIocFacts(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

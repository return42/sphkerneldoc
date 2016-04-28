.. -*- coding: utf-8; mode: rst -*-

.. _API-GetPortFacts:

============
GetPortFacts
============

*man GetPortFacts(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

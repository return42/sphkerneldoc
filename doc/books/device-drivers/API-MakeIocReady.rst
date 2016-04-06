
.. _API-MakeIocReady:

============
MakeIocReady
============

*man MakeIocReady(9)*

*4.6.0-rc1*

Get IOC to a READY state, using KickStart if needed.


Synopsis
========

.. c:function:: int MakeIocReady( MPT_ADAPTER * ioc, int force, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``force``
    Force hard KickStart of IOC

``sleepFlag``
    Specifies whether the process can sleep


Returns
=======

1 - DIAG reset and READY 0 - READY initially OR soft reset and READY -1 - Any failure on KickStart -2 - Msg Unit Reset Failed -3 - IO Unit Reset Failed -4 - IOC owned by a PEER

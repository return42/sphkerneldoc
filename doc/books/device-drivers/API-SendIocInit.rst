
.. _API-SendIocInit:

===========
SendIocInit
===========

*man SendIocInit(9)*

*4.6.0-rc1*

Send IOCInit request to MPT adapter.


Synopsis
========

.. c:function:: int SendIocInit( MPT_ADAPTER * ioc, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Send IOCInit followed by PortEnable to bring IOC to OPERATIONAL state.

Returns 0 for success, non-zero for failure.

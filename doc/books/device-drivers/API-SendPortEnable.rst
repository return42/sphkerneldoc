
.. _API-SendPortEnable:

==============
SendPortEnable
==============

*man SendPortEnable(9)*

*4.6.0-rc1*

Send PortEnable request to MPT adapter port.


Synopsis
========

.. c:function:: int SendPortEnable( MPT_ADAPTER * ioc, int portnum, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``portnum``
    Port number to enable

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Send PortEnable to bring IOC to OPERATIONAL state.

Returns 0 for success, non-zero for failure.

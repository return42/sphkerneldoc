
.. _API-SendIocReset:

============
SendIocReset
============

*man SendIocReset(9)*

*4.6.0-rc1*

Send IOCReset request to MPT adapter.


Synopsis
========

.. c:function:: int SendIocReset( MPT_ADAPTER * ioc, u8 reset_type, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``reset_type``
    reset type, expected values are ``MPI_FUNCTION_IOC_MESSAGE_UNIT_RESET`` or ``MPI_FUNCTION_IO_UNIT_RESET``

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Send IOCReset request to the MPT adapter.

Returns 0 for success, non-zero for failure.

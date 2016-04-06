
.. _API-mpt-register:

============
mpt_register
============

*man mpt_register(9)*

*4.6.0-rc1*

Register protocol-specific main callback handler.


Synopsis
========

.. c:function:: u8 mpt_register( MPT_CALLBACK cbfunc, MPT_DRIVER_CLASS dclass, char * func_name )

Arguments
=========

``cbfunc``
    callback function pointer

``dclass``
    Protocol driver's class (``MPT_DRIVER_CLASS`` enum value)

``func_name``
    call function's name


Description
===========

This routine is called by a protocol-specific driver (SCSI host, LAN, SCSI target) to register its reply callback routine. Each protocol-specific driver must do this before it will
be able to use any IOC resources, such as obtaining request frames.


NOTES
=====

The SCSI protocol driver currently calls this routine thrice in order to register separate callbacks; one for “normal” SCSI IO; one for MptScsiTaskMgmt requests; one for Scan/DV
requests.

Returns u8 valued “handle” in the range (and S.O.D. order) {N,...,7,6,5,...,1} if successful. A return value of MPT_MAX_PROTOCOL_DRIVERS (including zero!) should be considered
an error by the caller.

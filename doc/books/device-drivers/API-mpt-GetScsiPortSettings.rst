
.. _API-mpt-GetScsiPortSettings:

=======================
mpt_GetScsiPortSettings
=======================

*man mpt_GetScsiPortSettings(9)*

*4.6.0-rc1*

read SCSI Port Page 0 and 2


Synopsis
========

.. c:function:: int mpt_GetScsiPortSettings( MPT_ADAPTER * ioc, int portnum )

Arguments
=========

``ioc``
    Pointer to a Adapter Strucutre

``portnum``
    IOC port number


Return
======

-EFAULT if read of config page header fails or if no nvram If read of SCSI Port Page 0 fails, NVRAM = MPT_HOST_NVRAM_INVALID (0xFFFFFFFF)


Adapter settings
================

async, narrow Return 1 If read of SCSI Port Page 2 fails, Adapter settings valid NVRAM = MPT_HOST_NVRAM_INVALID (0xFFFFFFFF) Return 1 Else Both valid Return 0 CHECK - what type
of locking mechanisms should be used????

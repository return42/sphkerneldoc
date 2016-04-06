
.. _API-WaitForDoorbellInt:

==================
WaitForDoorbellInt
==================

*man WaitForDoorbellInt(9)*

*4.6.0-rc1*

Wait for IOC to set its doorbell interrupt bit


Synopsis
========

.. c:function:: int WaitForDoorbellInt( MPT_ADAPTER * ioc, int howlong, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``howlong``
    How long to wait (in seconds)

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

This routine waits (up to ~2 seconds max) for IOC doorbell interrupt (MPI_HIS_DOORBELL_INTERRUPT) to be set in the IntStatus register.

Returns a negative value on failure, else wait loop count.

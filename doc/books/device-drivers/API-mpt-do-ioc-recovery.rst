
.. _API-mpt-do-ioc-recovery:

===================
mpt_do_ioc_recovery
===================

*man mpt_do_ioc_recovery(9)*

*4.6.0-rc1*

Initialize or recover MPT adapter.


Synopsis
========

.. c:function:: int mpt_do_ioc_recovery( MPT_ADAPTER * ioc, u32 reason, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT adapter structure

``reason``
    Event word / reason

``sleepFlag``
    Use schedule if CAN_SLEEP else use udelay.


Description
===========

This routine performs all the steps necessary to bring the IOC to a OPERATIONAL state.

This routine also pre-fetches the LAN MAC address of a Fibre Channel MPT adapter.


Returns
=======

0 for success -1 if failed to get board READY -2 if READY but IOCFacts Failed -3 if READY but PrimeIOCFifos Failed -4 if READY but IOCInit Failed -5 if failed to enable_device
and/or request_selected_regions -6 if failed to upload firmware

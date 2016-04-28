.. -*- coding: utf-8; mode: rst -*-

.. _API-KickStart:

=========
KickStart
=========

*man KickStart(9)*

*4.6.0-rc5*

Perform hard reset of MPT adapter.


Synopsis
========

.. c:function:: int KickStart( MPT_ADAPTER * ioc, int force, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``force``
    Force hard reset

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

This routine places MPT adapter in diagnostic mode via the WriteSequence
register, and then performs a hard reset of adapter via the Diagnostic
register.


Inputs
======

sleepflag - CAN_SLEEP (non-interrupt thread) or NO_SLEEP (interrupt
thread, use mdelay) force - 1 if doorbell active, board fault state
board operational, IOC_RECOVERY or IOC_BRINGUP and there is an
alt_ioc. 0 else


Returns
=======

1 - hard reset, READY 0 - no reset due to History bit, READY -1 - no
reset due to History bit but not READY OR reset but failed to come READY
-2 - no reset, could not enter DIAG mode -3 - reset but bad FW bit


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

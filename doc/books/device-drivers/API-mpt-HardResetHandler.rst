.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-HardResetHandler:

====================
mpt_HardResetHandler
====================

*man mpt_HardResetHandler(9)*

*4.6.0-rc5*

Generic reset handler


Synopsis
========

.. c:function:: int mpt_HardResetHandler( MPT_ADAPTER * ioc, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Indicates if sleep or schedule must be called.


Description
===========

Issues SCSI Task Management call based on input arg values. If TaskMgmt
fails, returns associated SCSI request.


Remark
======

_HardResetHandler can be invoked from an interrupt thread (timer) or a
non-interrupt thread. In the former, must not call ``schedule``.


Note
====

A return of -1 is a FATAL error case, as it means a FW
reload/initialization failed.

Returns 0 for SUCCESS or -1 if FAILED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

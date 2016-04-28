.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-Soft-Hard-ResetHandler:

==========================
mpt_Soft_Hard_ResetHandler
==========================

*man mpt_Soft_Hard_ResetHandler(9)*

*4.6.0-rc5*

Try less expensive reset


Synopsis
========

.. c:function:: int mpt_Soft_Hard_ResetHandler( MPT_ADAPTER * ioc, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Indicates if sleep or schedule must be called.


Description
===========

Returns 0 for SUCCESS or -1 if FAILED. Try for softreset first, only if
it fails go for expensive HardReset.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

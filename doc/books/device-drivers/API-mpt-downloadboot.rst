.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-downloadboot:

================
mpt_downloadboot
================

*man mpt_downloadboot(9)*

*4.6.0-rc5*

DownloadBoot code


Synopsis
========

.. c:function:: int mpt_downloadboot( MPT_ADAPTER * ioc, MpiFwHeader_t * pFwHeader, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``pFwHeader``
    Pointer to firmware header info

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

FwDownloadBoot requires Programmed IO access.

Returns 0 for success -1 FW Image size is 0 -2 No valid cached_fw
Pointer <0 for fw upload failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

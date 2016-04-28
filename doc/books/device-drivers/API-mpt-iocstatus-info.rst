.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-iocstatus-info:

==================
mpt_iocstatus_info
==================

*man mpt_iocstatus_info(9)*

*4.6.0-rc5*

IOCSTATUS information returned from IOC.


Synopsis
========

.. c:function:: void mpt_iocstatus_info( MPT_ADAPTER * ioc, u32 ioc_status, MPT_FRAME_HDR * mf )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``ioc_status``
    U32 IOCStatus word from IOC

``mf``
    Pointer to MPT request frame


Description
===========

Refer to lsi/mpi.h.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-sas-log-info:

================
mpt_sas_log_info
================

*man mpt_sas_log_info(9)*

*4.6.0-rc5*

Log information returned from SAS IOC.


Synopsis
========

.. c:function:: void mpt_sas_log_info( MPT_ADAPTER * ioc, u32 log_info, u8 cb_idx )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``log_info``
    U32 LogInfo reply word from the IOC

``cb_idx``
    callback function's handle


Description
===========

Refer to lsi/mpi_log_sas.h.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

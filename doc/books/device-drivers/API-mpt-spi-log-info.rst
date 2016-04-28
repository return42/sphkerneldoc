.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-spi-log-info:

================
mpt_spi_log_info
================

*man mpt_spi_log_info(9)*

*4.6.0-rc5*

Log information returned from SCSI Parallel IOC.


Synopsis
========

.. c:function:: void mpt_spi_log_info( MPT_ADAPTER * ioc, u32 log_info )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``log_info``
    U32 LogInfo word from the IOC


Description
===========

Refer to lsi/sp_log.h.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

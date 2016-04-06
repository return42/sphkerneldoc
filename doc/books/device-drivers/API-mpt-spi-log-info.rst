
.. _API-mpt-spi-log-info:

================
mpt_spi_log_info
================

*man mpt_spi_log_info(9)*

*4.6.0-rc1*

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

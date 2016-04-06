
.. _API-mpt-sas-log-info:

================
mpt_sas_log_info
================

*man mpt_sas_log_info(9)*

*4.6.0-rc1*

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


.. _API-mpt-fc-log-info:

===============
mpt_fc_log_info
===============

*man mpt_fc_log_info(9)*

*4.6.0-rc1*

Log information returned from Fibre Channel IOC.


Synopsis
========

.. c:function:: void mpt_fc_log_info( MPT_ADAPTER * ioc, u32 log_info )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``log_info``
    U32 LogInfo reply word from the IOC


Description
===========

Refer to lsi/mpi_log_fc.h.

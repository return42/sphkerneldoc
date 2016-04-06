
.. _API-mpt-iocstatus-info-config:

=========================
mpt_iocstatus_info_config
=========================

*man mpt_iocstatus_info_config(9)*

*4.6.0-rc1*

IOCSTATUS information for config pages


Synopsis
========

.. c:function:: void mpt_iocstatus_info_config( MPT_ADAPTER * ioc, u32 ioc_status, MPT_FRAME_HDR * mf )

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

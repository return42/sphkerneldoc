
.. _API-mpt-host-page-access-control:

============================
mpt_host_page_access_control
============================

*man mpt_host_page_access_control(9)*

*4.6.0-rc1*

control the IOC's Host Page Buffer access


Synopsis
========

.. c:function:: int mpt_host_page_access_control( MPT_ADAPTER * ioc, u8 access_control_value, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT adapter structure

``access_control_value``
    define bits below

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Provides mechanism for the host driver to control the IOC's Host Page Buffer access.

Access Control Value - bits[15:12] 0h Reserved 1h Enable Access { MPI_DB_HPBAC_ENABLE_ACCESS } 2h Disable Access { MPI_DB_HPBAC_DISABLE_ACCESS } 3h Free Buffer {
MPI_DB_HPBAC_FREE_BUFFER }

Returns 0 for success, non-zero for failure.

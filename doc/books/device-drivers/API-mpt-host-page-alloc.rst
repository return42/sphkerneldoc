
.. _API-mpt-host-page-alloc:

===================
mpt_host_page_alloc
===================

*man mpt_host_page_alloc(9)*

*4.6.0-rc1*

allocate system memory for the fw


Synopsis
========

.. c:function:: int mpt_host_page_alloc( MPT_ADAPTER * ioc, pIOCInit_t ioc_init )

Arguments
=========

``ioc``
    Pointer to pointer to IOC adapter

``ioc_init``
    Pointer to ioc init config page


Description
===========

If we already allocated memory in past, then resend the same pointer. Returns 0 for success, non-zero for failure.

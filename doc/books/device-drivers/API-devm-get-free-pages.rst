
.. _API-devm-get-free-pages:

===================
devm_get_free_pages
===================

*man devm_get_free_pages(9)*

*4.6.0-rc1*

Resource-managed __get_free_pages


Synopsis
========

.. c:function:: unsigned long devm_get_free_pages( struct device * dev, gfp_t gfp_mask, unsigned int order )

Arguments
=========

``dev``
    Device to allocate memory for

``gfp_mask``
    Allocation gfp flags

``order``
    Allocation size is (1 << order) pages


Description
===========

Managed get_free_pages. Memory allocated with this function is automatically freed on driver detach.


RETURNS
=======

Address of allocated memory on success, 0 on failure.

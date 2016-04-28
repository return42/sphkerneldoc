.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-get-free-pages:

===================
devm_get_free_pages
===================

*man devm_get_free_pages(9)*

*4.6.0-rc5*

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

Managed get_free_pages. Memory allocated with this function is
automatically freed on driver detach.


RETURNS
=======

Address of allocated memory on success, 0 on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

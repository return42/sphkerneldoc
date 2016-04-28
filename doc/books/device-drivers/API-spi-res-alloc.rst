.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-res-alloc:

=============
spi_res_alloc
=============

*man spi_res_alloc(9)*

*4.6.0-rc5*

allocate a spi resource that is life-cycle managed during the processing
of a spi_message while using spi_transfer_one


Synopsis
========

.. c:function:: void * spi_res_alloc( struct spi_device * spi, spi_res_release_t release, size_t size, gfp_t gfp )

Arguments
=========

``spi``
    the spi device for which we allocate memory

``release``
    the release code to execute for this resource

``size``
    size to alloc and return

``gfp``
    GFP allocation flags


Return
======

the pointer to the allocated data

This may get enhanced in the future to allocate from a memory pool of
the ``spi_device`` or ``spi_master`` to avoid repeated allocations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-prime-import:

====================
drm_gem_prime_import
====================

*man drm_gem_prime_import(9)*

*4.6.0-rc5*

helper library implementation of the import callback


Synopsis
========

.. c:function:: struct drm_gem_object * drm_gem_prime_import( struct drm_device * dev, struct dma_buf * dma_buf )

Arguments
=========

``dev``
    drm_device to import into

``dma_buf``
    dma-buf object to import


Description
===========

This is the implementation of the gem_prime_import functions for GEM
drivers using the PRIME helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

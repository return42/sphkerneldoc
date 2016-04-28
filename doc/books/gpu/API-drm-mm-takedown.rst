.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-takedown:

===============
drm_mm_takedown
===============

*man drm_mm_takedown(9)*

*4.6.0-rc5*

clean up a drm_mm allocator


Synopsis
========

.. c:function:: void drm_mm_takedown( struct drm_mm * mm )

Arguments
=========

``mm``
    drm_mm allocator to clean up


Description
===========

Note that it is a bug to call this function on an allocator which is not
clean.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

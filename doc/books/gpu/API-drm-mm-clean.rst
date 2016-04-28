.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-clean:

============
drm_mm_clean
============

*man drm_mm_clean(9)*

*4.6.0-rc5*

checks whether an allocator is clean


Synopsis
========

.. c:function:: bool drm_mm_clean( struct drm_mm * mm )

Arguments
=========

``mm``
    drm_mm allocator to check


Returns
=======

True if the allocator is completely free, false if there's still a node
allocated in it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

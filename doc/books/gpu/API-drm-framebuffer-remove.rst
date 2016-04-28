.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-framebuffer-remove:

======================
drm_framebuffer_remove
======================

*man drm_framebuffer_remove(9)*

*4.6.0-rc5*

remove and unreference a framebuffer object


Synopsis
========

.. c:function:: void drm_framebuffer_remove( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer to remove


Description
===========

Scans all the CRTCs and planes in ``dev``'s mode_config. If they're
using ``fb``, removes it, setting it to NULL. Then drops the reference
to the passed-in framebuffer. Might take the modeset locks.

Note that this function optimizes the cleanup away if the caller holds
the last reference to the framebuffer. It is also guaranteed to not take
the modeset locks in this case.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

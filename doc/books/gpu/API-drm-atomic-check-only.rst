.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-check-only:

=====================
drm_atomic_check_only
=====================

*man drm_atomic_check_only(9)*

*4.6.0-rc5*

check whether a given config would work


Synopsis
========

.. c:function:: int drm_atomic_check_only( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic configuration to check


Description
===========

Note that this function can return -EDEADLK if the driver needed to
acquire more locks but encountered a deadlock. The caller must then do
the usual w/w backoff dance and restart. All other errors are fatal.


Returns
=======

0 on success, negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-default-clear:

==============================
drm_atomic_state_default_clear
==============================

*man drm_atomic_state_default_clear(9)*

*4.6.0-rc5*

clear base atomic state


Synopsis
========

.. c:function:: void drm_atomic_state_default_clear( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state


Description
===========

Default implementation for clearing atomic state. This is useful for
drivers that subclass the atomic state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

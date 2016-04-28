.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-dp-drrs-init:

==================
intel_dp_drrs_init
==================

*man intel_dp_drrs_init(9)*

*4.6.0-rc5*

Init basic DRRS work and mutex.


Synopsis
========

.. c:function:: struct drm_display_mode * intel_dp_drrs_init( struct intel_connector * intel_connector, struct drm_display_mode * fixed_mode )

Arguments
=========

``intel_connector``
    eDP connector

``fixed_mode``
    preferred mode of panel


Description
===========

This function is called only once at driver load to initialize basic
DRRS stuff.


Returns
=======

Downclock mode if panel supports it, else return NULL. DRRS support is
determined by the presence of downclock mode (apart from VBT setting).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

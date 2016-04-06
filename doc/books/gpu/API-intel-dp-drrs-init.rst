
.. _API-intel-dp-drrs-init:

==================
intel_dp_drrs_init
==================

*man intel_dp_drrs_init(9)*

*4.6.0-rc1*

Init basic DRRS work and mutex.


Synopsis
========

.. c:function:: struct drm_display_mode ⋆ intel_dp_drrs_init( struct intel_connector * intel_connector, struct drm_display_mode * fixed_mode )

Arguments
=========

``intel_connector``
    eDP connector

``fixed_mode``
    preferred mode of panel


Description
===========

This function is called only once at driver load to initialize basic DRRS stuff.


Returns
=======

Downclock mode if panel supports it, else return NULL. DRRS support is determined by the presence of downclock mode (apart from VBT setting).

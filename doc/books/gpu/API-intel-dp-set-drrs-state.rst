.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-dp-set-drrs-state:

=======================
intel_dp_set_drrs_state
=======================

*man intel_dp_set_drrs_state(9)*

*4.6.0-rc5*

program registers for RR switch to take effect


Synopsis
========

.. c:function:: void intel_dp_set_drrs_state( struct drm_device * dev, int refresh_rate )

Arguments
=========

``dev``
    DRM device

``refresh_rate``
    RR to be programmed


Description
===========

This function gets called when refresh rate (RR) has to be changed from
one frequency to another. Switches can be between high and low RR
supported by the panel or to any other RR based on media playback (in
this case, RR value needs to be passed from user space).

The caller of this function needs to take a lock on dev_priv->drrs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-reset-vcpi-slots:

===========================
drm_dp_mst_reset_vcpi_slots
===========================

*man drm_dp_mst_reset_vcpi_slots(9)*

*4.6.0-rc5*

Reset number of slots to 0 for VCPI


Synopsis
========

.. c:function:: void drm_dp_mst_reset_vcpi_slots( struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``mgr``
    manager for this port

``port``
    unverified pointer to a port.


Description
===========

This just resets the number of slots for the ports VCPI for later
programming.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

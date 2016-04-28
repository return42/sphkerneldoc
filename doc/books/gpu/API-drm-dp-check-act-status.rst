.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-check-act-status:

=======================
drm_dp_check_act_status
=======================

*man drm_dp_check_act_status(9)*

*4.6.0-rc5*

Check ACT handled status.


Synopsis
========

.. c:function:: int drm_dp_check_act_status( struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``mgr``
    manager to use


Description
===========

Check the payload status bits in the DPCD for ACT handled completion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-drm-dp-check-act-status:

=======================
drm_dp_check_act_status
=======================

*man drm_dp_check_act_status(9)*

*4.6.0-rc1*

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

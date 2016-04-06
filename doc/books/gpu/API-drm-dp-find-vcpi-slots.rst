
.. _API-drm-dp-find-vcpi-slots:

======================
drm_dp_find_vcpi_slots
======================

*man drm_dp_find_vcpi_slots(9)*

*4.6.0-rc1*

find slots for this PBN value


Synopsis
========

.. c:function:: int drm_dp_find_vcpi_slots( struct drm_dp_mst_topology_mgr * mgr, int pbn )

Arguments
=========

``mgr``
    manager to use

``pbn``
    payload bandwidth to convert into slots.

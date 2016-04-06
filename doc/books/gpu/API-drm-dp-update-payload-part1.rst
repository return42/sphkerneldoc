
.. _API-drm-dp-update-payload-part1:

===========================
drm_dp_update_payload_part1
===========================

*man drm_dp_update_payload_part1(9)*

*4.6.0-rc1*

Execute payload update part 1


Synopsis
========

.. c:function:: int drm_dp_update_payload_part1( struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``mgr``
    manager to use.


Description
===========

This iterates over all proposed virtual channels, and tries to allocate space in the link for them. For 0->slots transitions, this step just writes the VCPI to the MST device. For
slots->0 transitions, this writes the updated VCPIs and removes the remote VC payloads.

after calling this the driver should generate ACT and payload packets.

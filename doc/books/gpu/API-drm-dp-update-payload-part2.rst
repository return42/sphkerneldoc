.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-update-payload-part2:

===========================
drm_dp_update_payload_part2
===========================

*man drm_dp_update_payload_part2(9)*

*4.6.0-rc5*

Execute payload update part 2


Synopsis
========

.. c:function:: int drm_dp_update_payload_part2( struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``mgr``
    manager to use.


Description
===========

This iterates over all proposed virtual channels, and tries to allocate
space in the link for them. For 0->slots transitions, this step writes
the remote VC payload commands. For slots->0 this just resets some
internal state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

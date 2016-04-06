
.. _API-drm-dp-mst-hpd-irq:

==================
drm_dp_mst_hpd_irq
==================

*man drm_dp_mst_hpd_irq(9)*

*4.6.0-rc1*

MST hotplug IRQ notify


Synopsis
========

.. c:function:: int drm_dp_mst_hpd_irq( struct drm_dp_mst_topology_mgr * mgr, u8 * esi, bool * handled )

Arguments
=========

``mgr``
    manager to notify irq for.

``esi``
    4 bytes from SINK_COUNT_ESI

``handled``
    whether the hpd interrupt was consumed or not


Description
===========

This should be called from the driver when it detects a short IRQ, along with the value of the DEVICE_SERVICE_IRQ_VECTOR_ESI0. The topology manager will process the sideband
messages received as a result of this.

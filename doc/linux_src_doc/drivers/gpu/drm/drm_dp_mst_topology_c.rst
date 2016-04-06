.. -*- coding: utf-8; mode: rst -*-

=====================
drm_dp_mst_topology.c
=====================



.. _xref_drm_dp_update_payload_part1:

drm_dp_update_payload_part1
===========================

.. c:function:: int drm_dp_update_payload_part1 (struct drm_dp_mst_topology_mgr * mgr)

    Execute payload update part 1

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to use.



Description
-----------

This iterates over all proposed virtual channels, and tries to
allocate space in the link for them. For 0->slots transitions,
this step just writes the VCPI to the MST device. For slots->0
transitions, this writes the updated VCPIs and removes the
remote VC payloads.


after calling this the driver should generate ACT and payload
packets.




.. _xref_drm_dp_update_payload_part2:

drm_dp_update_payload_part2
===========================

.. c:function:: int drm_dp_update_payload_part2 (struct drm_dp_mst_topology_mgr * mgr)

    Execute payload update part 2

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to use.



Description
-----------

This iterates over all proposed virtual channels, and tries to
allocate space in the link for them. For 0->slots transitions,
this step writes the remote VC payload commands. For slots->0
this just resets some internal state.




.. _xref_drm_dp_mst_topology_mgr_set_mst:

drm_dp_mst_topology_mgr_set_mst
===============================

.. c:function:: int drm_dp_mst_topology_mgr_set_mst (struct drm_dp_mst_topology_mgr * mgr, bool mst_state)

    Set the MST state for a topology manager

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to set state for

    :param bool mst_state:
        true to enable MST on this connector - false to disable.



Description
-----------

This is called by the driver when it detects an MST capable device plugged
into a DP MST capable port, or when a DP MST capable device is unplugged.




.. _xref_drm_dp_mst_topology_mgr_suspend:

drm_dp_mst_topology_mgr_suspend
===============================

.. c:function:: void drm_dp_mst_topology_mgr_suspend (struct drm_dp_mst_topology_mgr * mgr)

    suspend the MST manager

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to suspend



Description
-----------

This function tells the MST device that we can't handle UP messages
anymore. This should stop it from sending any since we are suspended.




.. _xref_drm_dp_mst_topology_mgr_resume:

drm_dp_mst_topology_mgr_resume
==============================

.. c:function:: int drm_dp_mst_topology_mgr_resume (struct drm_dp_mst_topology_mgr * mgr)

    resume the MST manager

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to resume



Description
-----------

This will fetch DPCD and see if the device is still there,
if it is, it will rewrite the MSTM control bits, and return.


if the device fails this returns -1, and the driver should do
a full MST reprobe, in case we were undocked.




.. _xref_drm_dp_mst_hpd_irq:

drm_dp_mst_hpd_irq
==================

.. c:function:: int drm_dp_mst_hpd_irq (struct drm_dp_mst_topology_mgr * mgr, u8 * esi, bool * handled)

    MST hotplug IRQ notify

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to notify irq for.

    :param u8 * esi:
        4 bytes from SINK_COUNT_ESI

    :param bool * handled:
        whether the hpd interrupt was consumed or not



Description
-----------

This should be called from the driver when it detects a short IRQ,
along with the value of the DEVICE_SERVICE_IRQ_VECTOR_ESI0. The
topology manager will process the sideband messages received as a result
of this.




.. _xref_drm_dp_mst_detect_port:

drm_dp_mst_detect_port
======================

.. c:function:: enum drm_connector_status drm_dp_mst_detect_port (struct drm_connector * connector, struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port)

    get connection status for an MST port

    :param struct drm_connector * connector:

        _undescribed_

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        unverified pointer to a port



Description
-----------

This returns the current connection state for a port. It validates the
port pointer still exists so the caller doesn't require a reference




.. _xref_drm_dp_mst_port_has_audio:

drm_dp_mst_port_has_audio
=========================

.. c:function:: bool drm_dp_mst_port_has_audio (struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port)

    Check whether port has audio capability or not

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        unverified pointer to a port.



Description
-----------

This returns whether the port supports audio or not.




.. _xref_drm_dp_mst_get_edid:

drm_dp_mst_get_edid
===================

.. c:function:: struct edid * drm_dp_mst_get_edid (struct drm_connector * connector, struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port)

    get EDID for an MST port

    :param struct drm_connector * connector:
        toplevel connector to get EDID for

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        unverified pointer to a port.



Description
-----------

This returns an EDID for the port connected to a connector,
It validates the pointer still exists so the caller doesn't require a
reference.




.. _xref_drm_dp_find_vcpi_slots:

drm_dp_find_vcpi_slots
======================

.. c:function:: int drm_dp_find_vcpi_slots (struct drm_dp_mst_topology_mgr * mgr, int pbn)

    find slots for this PBN value

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to use

    :param int pbn:
        payload bandwidth to convert into slots.




.. _xref_drm_dp_mst_allocate_vcpi:

drm_dp_mst_allocate_vcpi
========================

.. c:function:: bool drm_dp_mst_allocate_vcpi (struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port, int pbn, int * slots)

    Allocate a virtual channel

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        port to allocate a virtual channel for.

    :param int pbn:
        payload bandwidth number to request

    :param int * slots:
        returned number of slots for this PBN.




.. _xref_drm_dp_mst_reset_vcpi_slots:

drm_dp_mst_reset_vcpi_slots
===========================

.. c:function:: void drm_dp_mst_reset_vcpi_slots (struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port)

    Reset number of slots to 0 for VCPI

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        unverified pointer to a port.



Description
-----------

This just resets the number of slots for the ports VCPI for later programming.




.. _xref_drm_dp_mst_deallocate_vcpi:

drm_dp_mst_deallocate_vcpi
==========================

.. c:function:: void drm_dp_mst_deallocate_vcpi (struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port)

    deallocate a VCPI

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager for this port

    :param struct drm_dp_mst_port * port:
        unverified port to deallocate vcpi for




.. _xref_drm_dp_check_act_status:

drm_dp_check_act_status
=======================

.. c:function:: int drm_dp_check_act_status (struct drm_dp_mst_topology_mgr * mgr)

    Check ACT handled status.

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to use



Description
-----------

Check the payload status bits in the DPCD for ACT handled completion.




.. _xref_drm_dp_calc_pbn_mode:

drm_dp_calc_pbn_mode
====================

.. c:function:: int drm_dp_calc_pbn_mode (int clock, int bpp)

    Calculate the PBN for a mode.

    :param int clock:
        dot clock for the mode

    :param int bpp:
        bpp for the mode.



Description
-----------

This uses the formula in the spec to calculate the PBN value for a mode.




.. _xref_drm_dp_mst_dump_topology:

drm_dp_mst_dump_topology
========================

.. c:function:: void drm_dp_mst_dump_topology (struct seq_file * m, struct drm_dp_mst_topology_mgr * mgr)

    

    :param struct seq_file * m:
        seq_file to dump output to

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to dump current topology for.



Description
-----------

helper to dump MST topology to a seq file for debugfs.




.. _xref_drm_dp_mst_topology_mgr_init:

drm_dp_mst_topology_mgr_init
============================

.. c:function:: int drm_dp_mst_topology_mgr_init (struct drm_dp_mst_topology_mgr * mgr, struct device * dev, struct drm_dp_aux * aux, int max_dpcd_transaction_bytes, int max_payloads, int conn_base_id)

    initialise a topology manager

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager struct to initialise

    :param struct device * dev:
        device providing this structure - for i2c addition.

    :param struct drm_dp_aux * aux:
        DP helper aux channel to talk to this device

    :param int max_dpcd_transaction_bytes:
        hw specific DPCD transaction limit

    :param int max_payloads:
        maximum number of payloads this GPU can source

    :param int conn_base_id:
        the connector object ID the MST device is connected to.



Description
-----------

Return 0 for success, or negative error code on failure




.. _xref_drm_dp_mst_topology_mgr_destroy:

drm_dp_mst_topology_mgr_destroy
===============================

.. c:function:: void drm_dp_mst_topology_mgr_destroy (struct drm_dp_mst_topology_mgr * mgr)

    destroy topology manager.

    :param struct drm_dp_mst_topology_mgr * mgr:
        manager to destroy




.. _xref_drm_dp_mst_register_i2c_bus:

drm_dp_mst_register_i2c_bus
===========================

.. c:function:: int drm_dp_mst_register_i2c_bus (struct drm_dp_aux * aux)

    register an I2C adapter for I2C-over-AUX

    :param struct drm_dp_aux * aux:
        DisplayPort AUX channel



Description
-----------

Returns 0 on success or a negative error code on failure.




.. _xref_drm_dp_mst_unregister_i2c_bus:

drm_dp_mst_unregister_i2c_bus
=============================

.. c:function:: void drm_dp_mst_unregister_i2c_bus (struct drm_dp_aux * aux)

    unregister an I2C-over-AUX adapter

    :param struct drm_dp_aux * aux:
        DisplayPort AUX channel



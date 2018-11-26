.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dp_mst_topology.c

.. _`dp-mst-helper`:

dp mst helper
=============

These functions contain parts of the DisplayPort 1.2a MultiStream Transport
protocol. The helpers contain a topology manager and bandwidth manager.
The helpers encapsulate the sending and received of sideband msgs.

.. _`drm_dp_update_payload_part1`:

drm_dp_update_payload_part1
===========================

.. c:function:: int drm_dp_update_payload_part1(struct drm_dp_mst_topology_mgr *mgr)

    Execute payload update part 1

    :param mgr:
        manager to use.
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_update_payload_part1.description`:

Description
-----------

This iterates over all proposed virtual channels, and tries to
allocate space in the link for them. For 0->slots transitions,
this step just writes the VCPI to the MST device. For slots->0
transitions, this writes the updated VCPIs and removes the
remote VC payloads.

after calling this the driver should generate ACT and payload
packets.

.. _`drm_dp_update_payload_part2`:

drm_dp_update_payload_part2
===========================

.. c:function:: int drm_dp_update_payload_part2(struct drm_dp_mst_topology_mgr *mgr)

    Execute payload update part 2

    :param mgr:
        manager to use.
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_update_payload_part2.description`:

Description
-----------

This iterates over all proposed virtual channels, and tries to
allocate space in the link for them. For 0->slots transitions,
this step writes the remote VC payload commands. For slots->0
this just resets some internal state.

.. _`drm_dp_mst_topology_mgr_set_mst`:

drm_dp_mst_topology_mgr_set_mst
===============================

.. c:function:: int drm_dp_mst_topology_mgr_set_mst(struct drm_dp_mst_topology_mgr *mgr, bool mst_state)

    Set the MST state for a topology manager

    :param mgr:
        manager to set state for
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param mst_state:
        true to enable MST on this connector - false to disable.
    :type mst_state: bool

.. _`drm_dp_mst_topology_mgr_set_mst.description`:

Description
-----------

This is called by the driver when it detects an MST capable device plugged
into a DP MST capable port, or when a DP MST capable device is unplugged.

.. _`drm_dp_mst_topology_mgr_suspend`:

drm_dp_mst_topology_mgr_suspend
===============================

.. c:function:: void drm_dp_mst_topology_mgr_suspend(struct drm_dp_mst_topology_mgr *mgr)

    suspend the MST manager

    :param mgr:
        manager to suspend
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_mst_topology_mgr_suspend.description`:

Description
-----------

This function tells the MST device that we can't handle UP messages
anymore. This should stop it from sending any since we are suspended.

.. _`drm_dp_mst_topology_mgr_resume`:

drm_dp_mst_topology_mgr_resume
==============================

.. c:function:: int drm_dp_mst_topology_mgr_resume(struct drm_dp_mst_topology_mgr *mgr)

    resume the MST manager

    :param mgr:
        manager to resume
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_mst_topology_mgr_resume.description`:

Description
-----------

This will fetch DPCD and see if the device is still there,
if it is, it will rewrite the MSTM control bits, and return.

if the device fails this returns -1, and the driver should do
a full MST reprobe, in case we were undocked.

.. _`drm_dp_mst_hpd_irq`:

drm_dp_mst_hpd_irq
==================

.. c:function:: int drm_dp_mst_hpd_irq(struct drm_dp_mst_topology_mgr *mgr, u8 *esi, bool *handled)

    MST hotplug IRQ notify

    :param mgr:
        manager to notify irq for.
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param esi:
        4 bytes from SINK_COUNT_ESI
    :type esi: u8 \*

    :param handled:
        whether the hpd interrupt was consumed or not
    :type handled: bool \*

.. _`drm_dp_mst_hpd_irq.description`:

Description
-----------

This should be called from the driver when it detects a short IRQ,
along with the value of the DEVICE_SERVICE_IRQ_VECTOR_ESI0. The
topology manager will process the sideband messages received as a result
of this.

.. _`drm_dp_mst_detect_port`:

drm_dp_mst_detect_port
======================

.. c:function:: enum drm_connector_status drm_dp_mst_detect_port(struct drm_connector *connector, struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port)

    get connection status for an MST port

    :param connector:
        DRM connector for this port
    :type connector: struct drm_connector \*

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        unverified pointer to a port
    :type port: struct drm_dp_mst_port \*

.. _`drm_dp_mst_detect_port.description`:

Description
-----------

This returns the current connection state for a port. It validates the
port pointer still exists so the caller doesn't require a reference

.. _`drm_dp_mst_port_has_audio`:

drm_dp_mst_port_has_audio
=========================

.. c:function:: bool drm_dp_mst_port_has_audio(struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port)

    Check whether port has audio capability or not

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        unverified pointer to a port.
    :type port: struct drm_dp_mst_port \*

.. _`drm_dp_mst_port_has_audio.description`:

Description
-----------

This returns whether the port supports audio or not.

.. _`drm_dp_mst_get_edid`:

drm_dp_mst_get_edid
===================

.. c:function:: struct edid *drm_dp_mst_get_edid(struct drm_connector *connector, struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port)

    get EDID for an MST port

    :param connector:
        toplevel connector to get EDID for
    :type connector: struct drm_connector \*

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        unverified pointer to a port.
    :type port: struct drm_dp_mst_port \*

.. _`drm_dp_mst_get_edid.description`:

Description
-----------

This returns an EDID for the port connected to a connector,
It validates the pointer still exists so the caller doesn't require a
reference.

.. _`drm_dp_find_vcpi_slots`:

drm_dp_find_vcpi_slots
======================

.. c:function:: int drm_dp_find_vcpi_slots(struct drm_dp_mst_topology_mgr *mgr, int pbn)

    find slots for this PBN value

    :param mgr:
        manager to use
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param pbn:
        payload bandwidth to convert into slots.
    :type pbn: int

.. _`drm_dp_atomic_find_vcpi_slots`:

drm_dp_atomic_find_vcpi_slots
=============================

.. c:function:: int drm_dp_atomic_find_vcpi_slots(struct drm_atomic_state *state, struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port, int pbn)

    Find and add vcpi slots to the state

    :param state:
        global atomic state
    :type state: struct drm_atomic_state \*

    :param mgr:
        MST topology manager for the port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        port to find vcpi slots for
    :type port: struct drm_dp_mst_port \*

    :param pbn:
        bandwidth required for the mode in PBN
    :type pbn: int

.. _`drm_dp_atomic_find_vcpi_slots.return`:

Return
------

Total slots in the atomic state assigned for this port or error

.. _`drm_dp_atomic_release_vcpi_slots`:

drm_dp_atomic_release_vcpi_slots
================================

.. c:function:: int drm_dp_atomic_release_vcpi_slots(struct drm_atomic_state *state, struct drm_dp_mst_topology_mgr *mgr, int slots)

    Release allocated vcpi slots

    :param state:
        global atomic state
    :type state: struct drm_atomic_state \*

    :param mgr:
        MST topology manager for the port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param slots:
        number of vcpi slots to release
    :type slots: int

.. _`drm_dp_atomic_release_vcpi_slots.return`:

Return
------

0 if \ ``slots``\  were added back to \ :c:type:`drm_dp_mst_topology_state->avail_slots <drm_dp_mst_topology_state>`\  or
negative error code

.. _`drm_dp_mst_allocate_vcpi`:

drm_dp_mst_allocate_vcpi
========================

.. c:function:: bool drm_dp_mst_allocate_vcpi(struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port, int pbn, int slots)

    Allocate a virtual channel

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        port to allocate a virtual channel for.
    :type port: struct drm_dp_mst_port \*

    :param pbn:
        payload bandwidth number to request
    :type pbn: int

    :param slots:
        returned number of slots for this PBN.
    :type slots: int

.. _`drm_dp_mst_reset_vcpi_slots`:

drm_dp_mst_reset_vcpi_slots
===========================

.. c:function:: void drm_dp_mst_reset_vcpi_slots(struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port)

    Reset number of slots to 0 for VCPI

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        unverified pointer to a port.
    :type port: struct drm_dp_mst_port \*

.. _`drm_dp_mst_reset_vcpi_slots.description`:

Description
-----------

This just resets the number of slots for the ports VCPI for later programming.

.. _`drm_dp_mst_deallocate_vcpi`:

drm_dp_mst_deallocate_vcpi
==========================

.. c:function:: void drm_dp_mst_deallocate_vcpi(struct drm_dp_mst_topology_mgr *mgr, struct drm_dp_mst_port *port)

    deallocate a VCPI

    :param mgr:
        manager for this port
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param port:
        unverified port to deallocate vcpi for
    :type port: struct drm_dp_mst_port \*

.. _`drm_dp_check_act_status`:

drm_dp_check_act_status
=======================

.. c:function:: int drm_dp_check_act_status(struct drm_dp_mst_topology_mgr *mgr)

    Check ACT handled status.

    :param mgr:
        manager to use
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_check_act_status.description`:

Description
-----------

Check the payload status bits in the DPCD for ACT handled completion.

.. _`drm_dp_calc_pbn_mode`:

drm_dp_calc_pbn_mode
====================

.. c:function:: int drm_dp_calc_pbn_mode(int clock, int bpp)

    Calculate the PBN for a mode.

    :param clock:
        dot clock for the mode
    :type clock: int

    :param bpp:
        bpp for the mode.
    :type bpp: int

.. _`drm_dp_calc_pbn_mode.description`:

Description
-----------

This uses the formula in the spec to calculate the PBN value for a mode.

.. _`drm_dp_mst_dump_topology`:

drm_dp_mst_dump_topology
========================

.. c:function:: void drm_dp_mst_dump_topology(struct seq_file *m, struct drm_dp_mst_topology_mgr *mgr)

    dump topology to seq file.

    :param m:
        seq_file to dump output to
    :type m: struct seq_file \*

    :param mgr:
        manager to dump current topology for.
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_mst_dump_topology.description`:

Description
-----------

helper to dump MST topology to a seq file for debugfs.

.. _`drm_atomic_get_mst_topology_state`:

drm_atomic_get_mst_topology_state
=================================

.. c:function:: struct drm_dp_mst_topology_state *drm_atomic_get_mst_topology_state(struct drm_atomic_state *state, struct drm_dp_mst_topology_mgr *mgr)

    get MST topology state

    :param state:
        global atomic state
    :type state: struct drm_atomic_state \*

    :param mgr:
        MST topology manager, also the private object in this case
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_atomic_get_mst_topology_state.description`:

Description
-----------

This function wraps \ :c:func:`drm_atomic_get_priv_obj_state`\  passing in the MST atomic
state vtable so that the private object state returned is that of a MST
topology object. Also, \ :c:func:`drm_atomic_get_private_obj_state`\  expects the caller
to care of the locking, so warn if don't hold the connection_mutex.

.. _`drm_atomic_get_mst_topology_state.return`:

Return
------


The MST topology state or error pointer.

.. _`drm_dp_mst_topology_mgr_init`:

drm_dp_mst_topology_mgr_init
============================

.. c:function:: int drm_dp_mst_topology_mgr_init(struct drm_dp_mst_topology_mgr *mgr, struct drm_device *dev, struct drm_dp_aux *aux, int max_dpcd_transaction_bytes, int max_payloads, int conn_base_id)

    initialise a topology manager

    :param mgr:
        manager struct to initialise
    :type mgr: struct drm_dp_mst_topology_mgr \*

    :param dev:
        device providing this structure - for i2c addition.
    :type dev: struct drm_device \*

    :param aux:
        DP helper aux channel to talk to this device
    :type aux: struct drm_dp_aux \*

    :param max_dpcd_transaction_bytes:
        hw specific DPCD transaction limit
    :type max_dpcd_transaction_bytes: int

    :param max_payloads:
        maximum number of payloads this GPU can source
    :type max_payloads: int

    :param conn_base_id:
        the connector object ID the MST device is connected to.
    :type conn_base_id: int

.. _`drm_dp_mst_topology_mgr_init.description`:

Description
-----------

Return 0 for success, or negative error code on failure

.. _`drm_dp_mst_topology_mgr_destroy`:

drm_dp_mst_topology_mgr_destroy
===============================

.. c:function:: void drm_dp_mst_topology_mgr_destroy(struct drm_dp_mst_topology_mgr *mgr)

    destroy topology manager.

    :param mgr:
        manager to destroy
    :type mgr: struct drm_dp_mst_topology_mgr \*

.. _`drm_dp_mst_register_i2c_bus`:

drm_dp_mst_register_i2c_bus
===========================

.. c:function:: int drm_dp_mst_register_i2c_bus(struct drm_dp_aux *aux)

    register an I2C adapter for I2C-over-AUX

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. _`drm_dp_mst_register_i2c_bus.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_mst_unregister_i2c_bus`:

drm_dp_mst_unregister_i2c_bus
=============================

.. c:function:: void drm_dp_mst_unregister_i2c_bus(struct drm_dp_aux *aux)

    unregister an I2C-over-AUX adapter

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. This file was automatic generated / don't edit.


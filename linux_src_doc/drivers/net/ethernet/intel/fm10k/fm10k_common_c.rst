.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_common.c

.. _`fm10k_get_bus_info_generic`:

fm10k_get_bus_info_generic
==========================

.. c:function:: s32 fm10k_get_bus_info_generic(struct fm10k_hw *hw)

    Generic set PCI bus info

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_get_bus_info_generic.description`:

Description
-----------

Gets the PCI bus info (speed, width, type) then calls helper function to
store this data within the fm10k_hw structure.

.. _`fm10k_get_invariants_generic`:

fm10k_get_invariants_generic
============================

.. c:function:: s32 fm10k_get_invariants_generic(struct fm10k_hw *hw)

    Inits constant values

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_get_invariants_generic.description`:

Description
-----------

Initialize the common invariants for the device.

.. _`fm10k_start_hw_generic`:

fm10k_start_hw_generic
======================

.. c:function:: s32 fm10k_start_hw_generic(struct fm10k_hw *hw)

    Prepare hardware for Tx/Rx

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_start_hw_generic.description`:

Description
-----------

This function sets the Tx ready flag to indicate that the Tx path has
been initialized.

.. _`fm10k_disable_queues_generic`:

fm10k_disable_queues_generic
============================

.. c:function:: s32 fm10k_disable_queues_generic(struct fm10k_hw *hw, u16 q_cnt)

    Stop Tx/Rx queues

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param q_cnt:
        number of queues to be disabled
    :type q_cnt: u16

.. _`fm10k_stop_hw_generic`:

fm10k_stop_hw_generic
=====================

.. c:function:: s32 fm10k_stop_hw_generic(struct fm10k_hw *hw)

    Stop Tx/Rx units

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_read_hw_stats_32b`:

fm10k_read_hw_stats_32b
=======================

.. c:function:: u32 fm10k_read_hw_stats_32b(struct fm10k_hw *hw, u32 addr, struct fm10k_hw_stat *stat)

    Reads value of 32-bit registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

    :param addr:
        address of register containing a 32-bit value
    :type addr: u32

    :param stat:
        pointer to structure holding hw stat information
    :type stat: struct fm10k_hw_stat \*

.. _`fm10k_read_hw_stats_32b.description`:

Description
-----------

Function reads the content of the register and returns the delta
between the base and the current value.

.. _`fm10k_read_hw_stats_48b`:

fm10k_read_hw_stats_48b
=======================

.. c:function:: u64 fm10k_read_hw_stats_48b(struct fm10k_hw *hw, u32 addr, struct fm10k_hw_stat *stat)

    Reads value of 48-bit registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

    :param addr:
        address of register containing the lower 32-bit value
    :type addr: u32

    :param stat:
        pointer to structure holding hw stat information
    :type stat: struct fm10k_hw_stat \*

.. _`fm10k_read_hw_stats_48b.description`:

Description
-----------

Function reads the content of 2 registers, combined to represent a 48-bit
statistical value. Extra processing is required to handle overflowing.
Finally, a delta value is returned representing the difference between the
values stored in registers and values stored in the statistic counters.

.. _`fm10k_update_hw_base_48b`:

fm10k_update_hw_base_48b
========================

.. c:function:: void fm10k_update_hw_base_48b(struct fm10k_hw_stat *stat, u64 delta)

    Updates 48-bit statistic base value

    :param stat:
        pointer to the hardware statistic structure
    :type stat: struct fm10k_hw_stat \*

    :param delta:
        value to be updated into the hardware statistic structure
    :type delta: u64

.. _`fm10k_update_hw_base_48b.description`:

Description
-----------

Function receives a value and determines if an update is required based on
a delta calculation. Only the base value will be updated.

.. _`fm10k_update_hw_stats_tx_q`:

fm10k_update_hw_stats_tx_q
==========================

.. c:function:: void fm10k_update_hw_stats_tx_q(struct fm10k_hw *hw, struct fm10k_hw_stats_q *q, u32 idx)

    Updates TX queue statistics counters

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

    :param q:
        pointer to the ring of hardware statistics queue
    :type q: struct fm10k_hw_stats_q \*

    :param idx:
        index pointing to the start of the ring iteration
    :type idx: u32

.. _`fm10k_update_hw_stats_tx_q.description`:

Description
-----------

Function updates the TX queue statistics counters that are related to the
hardware.

.. _`fm10k_update_hw_stats_rx_q`:

fm10k_update_hw_stats_rx_q
==========================

.. c:function:: void fm10k_update_hw_stats_rx_q(struct fm10k_hw *hw, struct fm10k_hw_stats_q *q, u32 idx)

    Updates RX queue statistics counters

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

    :param q:
        pointer to the ring of hardware statistics queue
    :type q: struct fm10k_hw_stats_q \*

    :param idx:
        index pointing to the start of the ring iteration
    :type idx: u32

.. _`fm10k_update_hw_stats_rx_q.description`:

Description
-----------

Function updates the RX queue statistics counters that are related to the
hardware.

.. _`fm10k_update_hw_stats_q`:

fm10k_update_hw_stats_q
=======================

.. c:function:: void fm10k_update_hw_stats_q(struct fm10k_hw *hw, struct fm10k_hw_stats_q *q, u32 idx, u32 count)

    Updates queue statistics counters

    :param hw:
        pointer to the hardware structure
    :type hw: struct fm10k_hw \*

    :param q:
        pointer to the ring of hardware statistics queue
    :type q: struct fm10k_hw_stats_q \*

    :param idx:
        index pointing to the start of the ring iteration
    :type idx: u32

    :param count:
        number of queues to iterate over
    :type count: u32

.. _`fm10k_update_hw_stats_q.description`:

Description
-----------

Function updates the queue statistics counters that are related to the
hardware.

.. _`fm10k_unbind_hw_stats_q`:

fm10k_unbind_hw_stats_q
=======================

.. c:function:: void fm10k_unbind_hw_stats_q(struct fm10k_hw_stats_q *q, u32 idx, u32 count)

    Unbind the queue counters from their queues

    :param q:
        pointer to the ring of hardware statistics queue
    :type q: struct fm10k_hw_stats_q \*

    :param idx:
        index pointing to the start of the ring iteration
    :type idx: u32

    :param count:
        number of queues to iterate over
    :type count: u32

.. _`fm10k_unbind_hw_stats_q.description`:

Description
-----------

Function invalidates the index values for the queues so any updates that
may have happened are ignored and the base for the queue stats is reset.

.. _`fm10k_get_host_state_generic`:

fm10k_get_host_state_generic
============================

.. c:function:: s32 fm10k_get_host_state_generic(struct fm10k_hw *hw, bool *host_ready)

    Returns the state of the host

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param host_ready:
        pointer to boolean value that will record host state
    :type host_ready: bool \*

.. _`fm10k_get_host_state_generic.description`:

Description
-----------

This function will check the health of the mailbox and Tx queue 0
in order to determine if we should report that the link is up or not.

.. This file was automatic generated / don't edit.


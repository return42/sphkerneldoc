.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_txrx_common.h

.. _`build_ctob`:

build_ctob
==========

.. c:function:: __le64 build_ctob(u32 td_cmd, u32 td_offset, unsigned int size, u32 td_tag)

    Builds the Tx descriptor (cmd, offset and type) qword

    :param td_cmd:
        *undescribed*
    :type td_cmd: u32

    :param td_offset:
        *undescribed*
    :type td_offset: u32

    :param size:
        *undescribed*
    :type size: unsigned int

    :param td_tag:
        *undescribed*
    :type td_tag: u32

.. _`i40e_update_tx_stats`:

i40e_update_tx_stats
====================

.. c:function:: void i40e_update_tx_stats(struct i40e_ring *tx_ring, unsigned int total_packets, unsigned int total_bytes)

    Update the egress statistics for the Tx ring

    :param tx_ring:
        Tx ring to update
    :type tx_ring: struct i40e_ring \*

    :param total_packets:
        *undescribed*
    :type total_packets: unsigned int

    :param total_bytes:
        total bytes sent
    :type total_bytes: unsigned int

.. _`i40e_arm_wb`:

i40e_arm_wb
===========

.. c:function:: void i40e_arm_wb(struct i40e_ring *tx_ring, struct i40e_vsi *vsi, int budget)

    (Possibly) arms Tx write-back

    :param tx_ring:
        Tx ring to update
    :type tx_ring: struct i40e_ring \*

    :param vsi:
        the VSI
    :type vsi: struct i40e_vsi \*

    :param budget:
        the NAPI budget left
    :type budget: int

.. This file was automatic generated / don't edit.


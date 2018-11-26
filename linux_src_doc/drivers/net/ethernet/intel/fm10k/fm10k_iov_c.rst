.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_iov.c

.. _`fm10k_iov_msg_queue_mac_vlan`:

fm10k_iov_msg_queue_mac_vlan
============================

.. c:function:: s32 fm10k_iov_msg_queue_mac_vlan(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for MAC/VLAN request from VF

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        Pointer array to message, results[0] is pointer to message
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_iov_msg_queue_mac_vlan.description`:

Description
-----------

This function is a custom handler for MAC/VLAN requests from the VF. The
assumption is that it is acceptable to directly hand off the message from
the VF to the PF's switch manager. However, we use a MAC/VLAN message
queue to avoid overloading the mailbox when a large number of requests
come in.

.. This file was automatic generated / don't edit.


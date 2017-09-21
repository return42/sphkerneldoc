.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_dev.c

.. _`get_capability`:

get_capability
==============

.. c:function:: int get_capability(struct hinic_hwdev *hwdev, struct hinic_dev_cap *dev_cap)

    convert device capabilities to NIC capabilities

    :param struct hinic_hwdev \*hwdev:
        the HW device to set and convert device capabilities for

    :param struct hinic_dev_cap \*dev_cap:
        device capabilities from FW

.. _`get_capability.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_cap_from_fw`:

get_cap_from_fw
===============

.. c:function:: int get_cap_from_fw(struct hinic_pfhwdev *pfhwdev)

    get device capabilities from FW

    :param struct hinic_pfhwdev \*pfhwdev:
        the PF HW device to get capabilities for

.. _`get_cap_from_fw.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_dev_cap`:

get_dev_cap
===========

.. c:function:: int get_dev_cap(struct hinic_hwdev *hwdev)

    get device capabilities

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device to get capabilities for

.. _`get_dev_cap.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_msix`:

init_msix
=========

.. c:function:: int init_msix(struct hinic_hwdev *hwdev)

    enable the msix and save the entries

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`init_msix.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`disable_msix`:

disable_msix
============

.. c:function:: void disable_msix(struct hinic_hwdev *hwdev)

    disable the msix

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`hinic_port_msg_cmd`:

hinic_port_msg_cmd
==================

.. c:function:: int hinic_port_msg_cmd(struct hinic_hwdev *hwdev, enum hinic_port_cmd cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size)

    send port msg to mgmt

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param enum hinic_port_cmd cmd:
        the port command

    :param void \*buf_in:
        input buffer

    :param u16 in_size:
        input size

    :param void \*buf_out:
        output buffer

    :param u16 \*out_size:
        returned output size

.. _`hinic_port_msg_cmd.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_fw_ctxt`:

init_fw_ctxt
============

.. c:function:: int init_fw_ctxt(struct hinic_hwdev *hwdev)

    Init Firmware tables before network mgmt and io operations

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`init_fw_ctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`set_hw_ioctxt`:

set_hw_ioctxt
=============

.. c:function:: int set_hw_ioctxt(struct hinic_hwdev *hwdev, unsigned int rq_depth, unsigned int sq_depth)

    set the shape of the IO queues in FW

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param unsigned int rq_depth:
        rq depth

    :param unsigned int sq_depth:
        sq depth

.. _`set_hw_ioctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`clear_io_resources`:

clear_io_resources
==================

.. c:function:: int clear_io_resources(struct hinic_hwdev *hwdev)

    set the IO resources as not active in the NIC

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`clear_io_resources.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`set_resources_state`:

set_resources_state
===================

.. c:function:: int set_resources_state(struct hinic_hwdev *hwdev, enum hinic_res_state state)

    set the state of the resources in the NIC

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param enum hinic_res_state state:
        the state to set

.. _`set_resources_state.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_base_qpn`:

get_base_qpn
============

.. c:function:: int get_base_qpn(struct hinic_hwdev *hwdev, u16 *base_qpn)

    get the first qp number

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param u16 \*base_qpn:
        returned qp number

.. _`get_base_qpn.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_ifup`:

hinic_hwdev_ifup
================

.. c:function:: int hinic_hwdev_ifup(struct hinic_hwdev *hwdev)

    Preparing the HW for passing IO

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`hinic_hwdev_ifup.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_ifdown`:

hinic_hwdev_ifdown
==================

.. c:function:: void hinic_hwdev_ifdown(struct hinic_hwdev *hwdev)

    Closing the HW for passing IO

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`hinic_hwdev_cb_register`:

hinic_hwdev_cb_register
=======================

.. c:function:: void hinic_hwdev_cb_register(struct hinic_hwdev *hwdev, enum hinic_mgmt_msg_cmd cmd, void *handle, void (*handler)(void *handle, void *buf_in, u16 in_size, void *buf_out, u16 *out_size))

    register callback handler for MGMT events

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param enum hinic_mgmt_msg_cmd cmd:
        the mgmt event

    :param void \*handle:
        private data for the handler

    :param void (\*handler)(void \*handle, void \*buf_in, u16 in_size, void \*buf_out, u16 \*out_size):
        event handler

.. _`hinic_hwdev_cb_unregister`:

hinic_hwdev_cb_unregister
=========================

.. c:function:: void hinic_hwdev_cb_unregister(struct hinic_hwdev *hwdev, enum hinic_mgmt_msg_cmd cmd)

    unregister callback handler for MGMT events

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param enum hinic_mgmt_msg_cmd cmd:
        the mgmt event

.. _`nic_mgmt_msg_handler`:

nic_mgmt_msg_handler
====================

.. c:function:: void nic_mgmt_msg_handler(void *handle, u8 cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size)

    nic mgmt event handler

    :param void \*handle:
        private data for the handler

    :param u8 cmd:
        *undescribed*

    :param void \*buf_in:
        input buffer

    :param u16 in_size:
        input size

    :param void \*buf_out:
        output buffer

    :param u16 \*out_size:
        returned output size

.. _`init_pfhwdev`:

init_pfhwdev
============

.. c:function:: int init_pfhwdev(struct hinic_pfhwdev *pfhwdev)

    Initialize the extended components of PF

    :param struct hinic_pfhwdev \*pfhwdev:
        the HW device for PF

.. _`init_pfhwdev.description`:

Description
-----------

Return 0 - success, negative - failure

.. _`free_pfhwdev`:

free_pfhwdev
============

.. c:function:: void free_pfhwdev(struct hinic_pfhwdev *pfhwdev)

    Free the extended components of PF

    :param struct hinic_pfhwdev \*pfhwdev:
        the HW device for PF

.. _`hinic_init_hwdev`:

hinic_init_hwdev
================

.. c:function:: struct hinic_hwdev *hinic_init_hwdev(struct pci_dev *pdev)

    Initialize the NIC HW

    :param struct pci_dev \*pdev:
        the NIC pci device

.. _`hinic_init_hwdev.description`:

Description
-----------

Return initialized NIC HW device

Initialize the NIC HW device and return a pointer to it

.. _`hinic_free_hwdev`:

hinic_free_hwdev
================

.. c:function:: void hinic_free_hwdev(struct hinic_hwdev *hwdev)

    Free the NIC HW device

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`hinic_hwdev_num_qps`:

hinic_hwdev_num_qps
===================

.. c:function:: int hinic_hwdev_num_qps(struct hinic_hwdev *hwdev)

    return the number QPs available for use

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

.. _`hinic_hwdev_num_qps.description`:

Description
-----------

Return number QPs available for use

.. _`hinic_hwdev_get_sq`:

hinic_hwdev_get_sq
==================

.. c:function:: struct hinic_sq *hinic_hwdev_get_sq(struct hinic_hwdev *hwdev, int i)

    get SQ

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param int i:
        the position of the SQ

.. _`hinic_hwdev_get_sq.return`:

Return
------

the SQ in the i position

.. _`hinic_hwdev_get_rq`:

hinic_hwdev_get_rq
==================

.. c:function:: struct hinic_rq *hinic_hwdev_get_rq(struct hinic_hwdev *hwdev, int i)

    get RQ

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param int i:
        the position of the RQ

.. _`hinic_hwdev_get_rq.return`:

Return
------

the RQ in the i position

.. _`hinic_hwdev_msix_cnt_set`:

hinic_hwdev_msix_cnt_set
========================

.. c:function:: int hinic_hwdev_msix_cnt_set(struct hinic_hwdev *hwdev, u16 msix_index)

    clear message attribute counters for msix entry

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param u16 msix_index:
        msix_index

.. _`hinic_hwdev_msix_cnt_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_msix_set`:

hinic_hwdev_msix_set
====================

.. c:function:: int hinic_hwdev_msix_set(struct hinic_hwdev *hwdev, u16 msix_index, u8 pending_limit, u8 coalesc_timer, u8 lli_timer_cfg, u8 lli_credit_limit, u8 resend_timer)

    set message attribute for msix entry

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param u16 msix_index:
        msix_index

    :param u8 pending_limit:
        the maximum pending interrupt events (unit 8)

    :param u8 coalesc_timer:
        coalesc period for interrupt (unit 8 us)

    :param u8 lli_timer_cfg:
        *undescribed*

    :param u8 lli_credit_limit:
        maximum credits for low latency msix messages (unit 8)

    :param u8 resend_timer:
        maximum wait for resending msix (unit coalesc period)

.. _`hinic_hwdev_msix_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_hw_ci_addr_set`:

hinic_hwdev_hw_ci_addr_set
==========================

.. c:function:: int hinic_hwdev_hw_ci_addr_set(struct hinic_hwdev *hwdev, struct hinic_sq *sq, u8 pending_limit, u8 coalesc_timer)

    set cons idx addr and attributes in HW for sq

    :param struct hinic_hwdev \*hwdev:
        the NIC HW device

    :param struct hinic_sq \*sq:
        send queue

    :param u8 pending_limit:
        the maximum pending update ci events (unit 8)

    :param u8 coalesc_timer:
        coalesc period for update ci (unit 8 us)

.. _`hinic_hwdev_hw_ci_addr_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. This file was automatic generated / don't edit.


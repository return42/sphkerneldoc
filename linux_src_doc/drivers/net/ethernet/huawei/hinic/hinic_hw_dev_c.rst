.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_dev.c

.. _`get_capability`:

get_capability
==============

.. c:function:: int get_capability(struct hinic_hwdev *hwdev, struct hinic_dev_cap *dev_cap)

    convert device capabilities to NIC capabilities

    :param hwdev:
        the HW device to set and convert device capabilities for
    :type hwdev: struct hinic_hwdev \*

    :param dev_cap:
        device capabilities from FW
    :type dev_cap: struct hinic_dev_cap \*

.. _`get_capability.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_cap_from_fw`:

get_cap_from_fw
===============

.. c:function:: int get_cap_from_fw(struct hinic_pfhwdev *pfhwdev)

    get device capabilities from FW

    :param pfhwdev:
        the PF HW device to get capabilities for
    :type pfhwdev: struct hinic_pfhwdev \*

.. _`get_cap_from_fw.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_dev_cap`:

get_dev_cap
===========

.. c:function:: int get_dev_cap(struct hinic_hwdev *hwdev)

    get device capabilities

    :param hwdev:
        the NIC HW device to get capabilities for
    :type hwdev: struct hinic_hwdev \*

.. _`get_dev_cap.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_msix`:

init_msix
=========

.. c:function:: int init_msix(struct hinic_hwdev *hwdev)

    enable the msix and save the entries

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`init_msix.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`disable_msix`:

disable_msix
============

.. c:function:: void disable_msix(struct hinic_hwdev *hwdev)

    disable the msix

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`hinic_port_msg_cmd`:

hinic_port_msg_cmd
==================

.. c:function:: int hinic_port_msg_cmd(struct hinic_hwdev *hwdev, enum hinic_port_cmd cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size)

    send port msg to mgmt

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param cmd:
        the port command
    :type cmd: enum hinic_port_cmd

    :param buf_in:
        input buffer
    :type buf_in: void \*

    :param in_size:
        input size
    :type in_size: u16

    :param buf_out:
        output buffer
    :type buf_out: void \*

    :param out_size:
        returned output size
    :type out_size: u16 \*

.. _`hinic_port_msg_cmd.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`init_fw_ctxt`:

init_fw_ctxt
============

.. c:function:: int init_fw_ctxt(struct hinic_hwdev *hwdev)

    Init Firmware tables before network mgmt and io operations

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`init_fw_ctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`set_hw_ioctxt`:

set_hw_ioctxt
=============

.. c:function:: int set_hw_ioctxt(struct hinic_hwdev *hwdev, unsigned int rq_depth, unsigned int sq_depth)

    set the shape of the IO queues in FW

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param rq_depth:
        rq depth
    :type rq_depth: unsigned int

    :param sq_depth:
        sq depth
    :type sq_depth: unsigned int

.. _`set_hw_ioctxt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`clear_io_resources`:

clear_io_resources
==================

.. c:function:: int clear_io_resources(struct hinic_hwdev *hwdev)

    set the IO resources as not active in the NIC

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`clear_io_resources.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`set_resources_state`:

set_resources_state
===================

.. c:function:: int set_resources_state(struct hinic_hwdev *hwdev, enum hinic_res_state state)

    set the state of the resources in the NIC

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param state:
        the state to set
    :type state: enum hinic_res_state

.. _`set_resources_state.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`get_base_qpn`:

get_base_qpn
============

.. c:function:: int get_base_qpn(struct hinic_hwdev *hwdev, u16 *base_qpn)

    get the first qp number

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param base_qpn:
        returned qp number
    :type base_qpn: u16 \*

.. _`get_base_qpn.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_ifup`:

hinic_hwdev_ifup
================

.. c:function:: int hinic_hwdev_ifup(struct hinic_hwdev *hwdev)

    Preparing the HW for passing IO

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`hinic_hwdev_ifup.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_ifdown`:

hinic_hwdev_ifdown
==================

.. c:function:: void hinic_hwdev_ifdown(struct hinic_hwdev *hwdev)

    Closing the HW for passing IO

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`hinic_hwdev_cb_register`:

hinic_hwdev_cb_register
=======================

.. c:function:: void hinic_hwdev_cb_register(struct hinic_hwdev *hwdev, enum hinic_mgmt_msg_cmd cmd, void *handle, void (*handler)(void *handle, void *buf_in, u16 in_size, void *buf_out, u16 *out_size))

    register callback handler for MGMT events

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param cmd:
        the mgmt event
    :type cmd: enum hinic_mgmt_msg_cmd

    :param handle:
        private data for the handler
    :type handle: void \*

    :param void (\*handler)(void \*handle, void \*buf_in, u16 in_size, void \*buf_out, u16 \*out_size):
        event handler

.. _`hinic_hwdev_cb_unregister`:

hinic_hwdev_cb_unregister
=========================

.. c:function:: void hinic_hwdev_cb_unregister(struct hinic_hwdev *hwdev, enum hinic_mgmt_msg_cmd cmd)

    unregister callback handler for MGMT events

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param cmd:
        the mgmt event
    :type cmd: enum hinic_mgmt_msg_cmd

.. _`nic_mgmt_msg_handler`:

nic_mgmt_msg_handler
====================

.. c:function:: void nic_mgmt_msg_handler(void *handle, u8 cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size)

    nic mgmt event handler

    :param handle:
        private data for the handler
    :type handle: void \*

    :param cmd:
        *undescribed*
    :type cmd: u8

    :param buf_in:
        input buffer
    :type buf_in: void \*

    :param in_size:
        input size
    :type in_size: u16

    :param buf_out:
        output buffer
    :type buf_out: void \*

    :param out_size:
        returned output size
    :type out_size: u16 \*

.. _`init_pfhwdev`:

init_pfhwdev
============

.. c:function:: int init_pfhwdev(struct hinic_pfhwdev *pfhwdev)

    Initialize the extended components of PF

    :param pfhwdev:
        the HW device for PF
    :type pfhwdev: struct hinic_pfhwdev \*

.. _`init_pfhwdev.description`:

Description
-----------

Return 0 - success, negative - failure

.. _`free_pfhwdev`:

free_pfhwdev
============

.. c:function:: void free_pfhwdev(struct hinic_pfhwdev *pfhwdev)

    Free the extended components of PF

    :param pfhwdev:
        the HW device for PF
    :type pfhwdev: struct hinic_pfhwdev \*

.. _`hinic_init_hwdev`:

hinic_init_hwdev
================

.. c:function:: struct hinic_hwdev *hinic_init_hwdev(struct pci_dev *pdev)

    Initialize the NIC HW

    :param pdev:
        the NIC pci device
    :type pdev: struct pci_dev \*

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

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`hinic_hwdev_num_qps`:

hinic_hwdev_num_qps
===================

.. c:function:: int hinic_hwdev_num_qps(struct hinic_hwdev *hwdev)

    return the number QPs available for use

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

.. _`hinic_hwdev_num_qps.description`:

Description
-----------

Return number QPs available for use

.. _`hinic_hwdev_get_sq`:

hinic_hwdev_get_sq
==================

.. c:function:: struct hinic_sq *hinic_hwdev_get_sq(struct hinic_hwdev *hwdev, int i)

    get SQ

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param i:
        the position of the SQ
    :type i: int

.. _`hinic_hwdev_get_sq.return`:

Return
------

the SQ in the i position

.. _`hinic_hwdev_get_rq`:

hinic_hwdev_get_rq
==================

.. c:function:: struct hinic_rq *hinic_hwdev_get_rq(struct hinic_hwdev *hwdev, int i)

    get RQ

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param i:
        the position of the RQ
    :type i: int

.. _`hinic_hwdev_get_rq.return`:

Return
------

the RQ in the i position

.. _`hinic_hwdev_msix_cnt_set`:

hinic_hwdev_msix_cnt_set
========================

.. c:function:: int hinic_hwdev_msix_cnt_set(struct hinic_hwdev *hwdev, u16 msix_index)

    clear message attribute counters for msix entry

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param msix_index:
        msix_index
    :type msix_index: u16

.. _`hinic_hwdev_msix_cnt_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_msix_set`:

hinic_hwdev_msix_set
====================

.. c:function:: int hinic_hwdev_msix_set(struct hinic_hwdev *hwdev, u16 msix_index, u8 pending_limit, u8 coalesc_timer, u8 lli_timer_cfg, u8 lli_credit_limit, u8 resend_timer)

    set message attribute for msix entry

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param msix_index:
        msix_index
    :type msix_index: u16

    :param pending_limit:
        the maximum pending interrupt events (unit 8)
    :type pending_limit: u8

    :param coalesc_timer:
        coalesc period for interrupt (unit 8 us)
    :type coalesc_timer: u8

    :param lli_timer_cfg:
        *undescribed*
    :type lli_timer_cfg: u8

    :param lli_credit_limit:
        maximum credits for low latency msix messages (unit 8)
    :type lli_credit_limit: u8

    :param resend_timer:
        maximum wait for resending msix (unit coalesc period)
    :type resend_timer: u8

.. _`hinic_hwdev_msix_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_hwdev_hw_ci_addr_set`:

hinic_hwdev_hw_ci_addr_set
==========================

.. c:function:: int hinic_hwdev_hw_ci_addr_set(struct hinic_hwdev *hwdev, struct hinic_sq *sq, u8 pending_limit, u8 coalesc_timer)

    set cons idx addr and attributes in HW for sq

    :param hwdev:
        the NIC HW device
    :type hwdev: struct hinic_hwdev \*

    :param sq:
        send queue
    :type sq: struct hinic_sq \*

    :param pending_limit:
        the maximum pending update ci events (unit 8)
    :type pending_limit: u8

    :param coalesc_timer:
        coalesc period for update ci (unit 8 us)
    :type coalesc_timer: u8

.. _`hinic_hwdev_hw_ci_addr_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_hw.c

.. _`nes_nic_init_timer_defaults`:

nes_nic_init_timer_defaults
===========================

.. c:function:: void nes_nic_init_timer_defaults(struct nes_device *nesdev, u8 jumbomode)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param jumbomode:
        *undescribed*
    :type jumbomode: u8

.. _`nes_nic_init_timer`:

nes_nic_init_timer
==================

.. c:function:: void nes_nic_init_timer(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_nic_tune_timer`:

nes_nic_tune_timer
==================

.. c:function:: void nes_nic_tune_timer(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_init_adapter`:

nes_init_adapter
================

.. c:function:: struct nes_adapter *nes_init_adapter(struct nes_device *nesdev, u8 hw_rev)

    initialize adapter

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param hw_rev:
        *undescribed*
    :type hw_rev: u8

.. _`nes_reset_adapter_ne020`:

nes_reset_adapter_ne020
=======================

.. c:function:: unsigned int nes_reset_adapter_ne020(struct nes_device *nesdev, u8 *OneG_Mode)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param OneG_Mode:
        *undescribed*
    :type OneG_Mode: u8 \*

.. _`nes_init_serdes`:

nes_init_serdes
===============

.. c:function:: int nes_init_serdes(struct nes_device *nesdev, u8 hw_rev, u8 port_count, struct nes_adapter *nesadapter, u8 OneG_Mode)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param hw_rev:
        *undescribed*
    :type hw_rev: u8

    :param port_count:
        *undescribed*
    :type port_count: u8

    :param nesadapter:
        *undescribed*
    :type nesadapter: struct nes_adapter \*

    :param OneG_Mode:
        *undescribed*
    :type OneG_Mode: u8

.. _`nes_init_csr_ne020`:

nes_init_csr_ne020
==================

.. c:function:: void nes_init_csr_ne020(struct nes_device *nesdev, u8 hw_rev, u8 port_count)

    Initialize registers for ne020 hardware

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param hw_rev:
        *undescribed*
    :type hw_rev: u8

    :param port_count:
        *undescribed*
    :type port_count: u8

.. _`nes_destroy_adapter`:

nes_destroy_adapter
===================

.. c:function:: void nes_destroy_adapter(struct nes_adapter *nesadapter)

    destroy the adapter structure

    :param nesadapter:
        *undescribed*
    :type nesadapter: struct nes_adapter \*

.. _`nes_init_cqp`:

nes_init_cqp
============

.. c:function:: int nes_init_cqp(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_destroy_cqp`:

nes_destroy_cqp
===============

.. c:function:: int nes_destroy_cqp(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_init_1g_phy`:

nes_init_1g_phy
===============

.. c:function:: int nes_init_1g_phy(struct nes_device *nesdev, u8 phy_type, u8 phy_index)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_type:
        *undescribed*
    :type phy_type: u8

    :param phy_index:
        *undescribed*
    :type phy_index: u8

.. _`nes_init_2025_phy`:

nes_init_2025_phy
=================

.. c:function:: int nes_init_2025_phy(struct nes_device *nesdev, u8 phy_type, u8 phy_index)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_type:
        *undescribed*
    :type phy_type: u8

    :param phy_index:
        *undescribed*
    :type phy_index: u8

.. _`nes_init_phy`:

nes_init_phy
============

.. c:function:: int nes_init_phy(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_replenish_nic_rq`:

nes_replenish_nic_rq
====================

.. c:function:: void nes_replenish_nic_rq(struct nes_vnic *nesvnic)

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

.. _`nes_rq_wqes_timeout`:

nes_rq_wqes_timeout
===================

.. c:function:: void nes_rq_wqes_timeout(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`nes_init_nic_qp`:

nes_init_nic_qp
===============

.. c:function:: int nes_init_nic_qp(struct nes_device *nesdev, struct net_device *netdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_destroy_nic_qp`:

nes_destroy_nic_qp
==================

.. c:function:: void nes_destroy_nic_qp(struct nes_vnic *nesvnic)

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

.. _`nes_napi_isr`:

nes_napi_isr
============

.. c:function:: int nes_napi_isr(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_dpc`:

nes_dpc
=======

.. c:function:: void nes_dpc(unsigned long param)

    :param param:
        *undescribed*
    :type param: unsigned long

.. _`nes_process_ceq`:

nes_process_ceq
===============

.. c:function:: void nes_process_ceq(struct nes_device *nesdev, struct nes_hw_ceq *ceq)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param ceq:
        *undescribed*
    :type ceq: struct nes_hw_ceq \*

.. _`nes_process_aeq`:

nes_process_aeq
===============

.. c:function:: void nes_process_aeq(struct nes_device *nesdev, struct nes_hw_aeq *aeq)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param aeq:
        *undescribed*
    :type aeq: struct nes_hw_aeq \*

.. _`nes_process_mac_intr`:

nes_process_mac_intr
====================

.. c:function:: void nes_process_mac_intr(struct nes_device *nesdev, u32 mac_number)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param mac_number:
        *undescribed*
    :type mac_number: u32

.. _`nes_nic_ce_handler`:

nes_nic_ce_handler
==================

.. c:function:: void nes_nic_ce_handler(struct nes_device *nesdev, struct nes_hw_nic_cq *cq)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param cq:
        *undescribed*
    :type cq: struct nes_hw_nic_cq \*

.. _`nes_cqp_ce_handler`:

nes_cqp_ce_handler
==================

.. c:function:: void nes_cqp_ce_handler(struct nes_device *nesdev, struct nes_hw_cq *cq)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param cq:
        *undescribed*
    :type cq: struct nes_hw_cq \*

.. _`nes_process_iwarp_aeqe`:

nes_process_iwarp_aeqe
======================

.. c:function:: void nes_process_iwarp_aeqe(struct nes_device *nesdev, struct nes_hw_aeqe *aeqe)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param aeqe:
        *undescribed*
    :type aeqe: struct nes_hw_aeqe \*

.. _`nes_iwarp_ce_handler`:

nes_iwarp_ce_handler
====================

.. c:function:: void nes_iwarp_ce_handler(struct nes_device *nesdev, struct nes_hw_cq *hw_cq)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param hw_cq:
        *undescribed*
    :type hw_cq: struct nes_hw_cq \*

.. _`nes_manage_apbvt`:

nes_manage_apbvt
================

.. c:function:: int nes_manage_apbvt(struct nes_vnic *nesvnic, u32 accel_local_port, u32 nic_index, u32 add_port)

    :param nesvnic:
        *undescribed*
    :type nesvnic: struct nes_vnic \*

    :param accel_local_port:
        *undescribed*
    :type accel_local_port: u32

    :param nic_index:
        *undescribed*
    :type nic_index: u32

    :param add_port:
        *undescribed*
    :type add_port: u32

.. _`nes_manage_arp_cache`:

nes_manage_arp_cache
====================

.. c:function:: void nes_manage_arp_cache(struct net_device *netdev, unsigned char *mac_addr, u32 ip_addr, u32 action)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param mac_addr:
        *undescribed*
    :type mac_addr: unsigned char \*

    :param ip_addr:
        *undescribed*
    :type ip_addr: u32

    :param action:
        *undescribed*
    :type action: u32

.. _`flush_wqes`:

flush_wqes
==========

.. c:function:: void flush_wqes(struct nes_device *nesdev, struct nes_qp *nesqp, u32 which_wq, u32 wait_completion)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param nesqp:
        *undescribed*
    :type nesqp: struct nes_qp \*

    :param which_wq:
        *undescribed*
    :type which_wq: u32

    :param wait_completion:
        *undescribed*
    :type wait_completion: u32

.. This file was automatic generated / don't edit.


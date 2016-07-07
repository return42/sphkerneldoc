.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_hw.c

.. _`nes_nic_init_timer_defaults`:

nes_nic_init_timer_defaults
===========================

.. c:function:: void nes_nic_init_timer_defaults(struct nes_device *nesdev, u8 jumbomode)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 jumbomode:
        *undescribed*

.. _`nes_nic_init_timer`:

nes_nic_init_timer
==================

.. c:function:: void nes_nic_init_timer(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_nic_tune_timer`:

nes_nic_tune_timer
==================

.. c:function:: void nes_nic_tune_timer(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_init_adapter`:

nes_init_adapter
================

.. c:function:: struct nes_adapter *nes_init_adapter(struct nes_device *nesdev, u8 hw_rev)

    initialize adapter

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 hw_rev:
        *undescribed*

.. _`nes_reset_adapter_ne020`:

nes_reset_adapter_ne020
=======================

.. c:function:: unsigned int nes_reset_adapter_ne020(struct nes_device *nesdev, u8 *OneG_Mode)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 \*OneG_Mode:
        *undescribed*

.. _`nes_init_serdes`:

nes_init_serdes
===============

.. c:function:: int nes_init_serdes(struct nes_device *nesdev, u8 hw_rev, u8 port_count, struct nes_adapter *nesadapter, u8 OneG_Mode)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 hw_rev:
        *undescribed*

    :param u8 port_count:
        *undescribed*

    :param struct nes_adapter \*nesadapter:
        *undescribed*

    :param u8 OneG_Mode:
        *undescribed*

.. _`nes_init_csr_ne020`:

nes_init_csr_ne020
==================

.. c:function:: void nes_init_csr_ne020(struct nes_device *nesdev, u8 hw_rev, u8 port_count)

    Initialize registers for ne020 hardware

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 hw_rev:
        *undescribed*

    :param u8 port_count:
        *undescribed*

.. _`nes_destroy_adapter`:

nes_destroy_adapter
===================

.. c:function:: void nes_destroy_adapter(struct nes_adapter *nesadapter)

    destroy the adapter structure

    :param struct nes_adapter \*nesadapter:
        *undescribed*

.. _`nes_init_cqp`:

nes_init_cqp
============

.. c:function:: int nes_init_cqp(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_destroy_cqp`:

nes_destroy_cqp
===============

.. c:function:: int nes_destroy_cqp(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_init_1g_phy`:

nes_init_1g_phy
===============

.. c:function:: int nes_init_1g_phy(struct nes_device *nesdev, u8 phy_type, u8 phy_index)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 phy_type:
        *undescribed*

    :param u8 phy_index:
        *undescribed*

.. _`nes_init_2025_phy`:

nes_init_2025_phy
=================

.. c:function:: int nes_init_2025_phy(struct nes_device *nesdev, u8 phy_type, u8 phy_index)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 phy_type:
        *undescribed*

    :param u8 phy_index:
        *undescribed*

.. _`nes_init_phy`:

nes_init_phy
============

.. c:function:: int nes_init_phy(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_replenish_nic_rq`:

nes_replenish_nic_rq
====================

.. c:function:: void nes_replenish_nic_rq(struct nes_vnic *nesvnic)

    :param struct nes_vnic \*nesvnic:
        *undescribed*

.. _`nes_rq_wqes_timeout`:

nes_rq_wqes_timeout
===================

.. c:function:: void nes_rq_wqes_timeout(unsigned long parm)

    :param unsigned long parm:
        *undescribed*

.. _`nes_init_nic_qp`:

nes_init_nic_qp
===============

.. c:function:: int nes_init_nic_qp(struct nes_device *nesdev, struct net_device *netdev)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct net_device \*netdev:
        *undescribed*

.. _`nes_destroy_nic_qp`:

nes_destroy_nic_qp
==================

.. c:function:: void nes_destroy_nic_qp(struct nes_vnic *nesvnic)

    :param struct nes_vnic \*nesvnic:
        *undescribed*

.. _`nes_napi_isr`:

nes_napi_isr
============

.. c:function:: int nes_napi_isr(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_dpc`:

nes_dpc
=======

.. c:function:: void nes_dpc(unsigned long param)

    :param unsigned long param:
        *undescribed*

.. _`nes_process_ceq`:

nes_process_ceq
===============

.. c:function:: void nes_process_ceq(struct nes_device *nesdev, struct nes_hw_ceq *ceq)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_ceq \*ceq:
        *undescribed*

.. _`nes_process_aeq`:

nes_process_aeq
===============

.. c:function:: void nes_process_aeq(struct nes_device *nesdev, struct nes_hw_aeq *aeq)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_aeq \*aeq:
        *undescribed*

.. _`nes_process_mac_intr`:

nes_process_mac_intr
====================

.. c:function:: void nes_process_mac_intr(struct nes_device *nesdev, u32 mac_number)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u32 mac_number:
        *undescribed*

.. _`nes_nic_ce_handler`:

nes_nic_ce_handler
==================

.. c:function:: void nes_nic_ce_handler(struct nes_device *nesdev, struct nes_hw_nic_cq *cq)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_nic_cq \*cq:
        *undescribed*

.. _`nes_cqp_ce_handler`:

nes_cqp_ce_handler
==================

.. c:function:: void nes_cqp_ce_handler(struct nes_device *nesdev, struct nes_hw_cq *cq)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_cq \*cq:
        *undescribed*

.. _`nes_process_iwarp_aeqe`:

nes_process_iwarp_aeqe
======================

.. c:function:: void nes_process_iwarp_aeqe(struct nes_device *nesdev, struct nes_hw_aeqe *aeqe)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_aeqe \*aeqe:
        *undescribed*

.. _`nes_iwarp_ce_handler`:

nes_iwarp_ce_handler
====================

.. c:function:: void nes_iwarp_ce_handler(struct nes_device *nesdev, struct nes_hw_cq *hw_cq)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_hw_cq \*hw_cq:
        *undescribed*

.. _`nes_manage_apbvt`:

nes_manage_apbvt
================

.. c:function:: int nes_manage_apbvt(struct nes_vnic *nesvnic, u32 accel_local_port, u32 nic_index, u32 add_port)

    :param struct nes_vnic \*nesvnic:
        *undescribed*

    :param u32 accel_local_port:
        *undescribed*

    :param u32 nic_index:
        *undescribed*

    :param u32 add_port:
        *undescribed*

.. _`nes_manage_arp_cache`:

nes_manage_arp_cache
====================

.. c:function:: void nes_manage_arp_cache(struct net_device *netdev, unsigned char *mac_addr, u32 ip_addr, u32 action)

    :param struct net_device \*netdev:
        *undescribed*

    :param unsigned char \*mac_addr:
        *undescribed*

    :param u32 ip_addr:
        *undescribed*

    :param u32 action:
        *undescribed*

.. _`flush_wqes`:

flush_wqes
==========

.. c:function:: void flush_wqes(struct nes_device *nesdev, struct nes_qp *nesqp, u32 which_wq, u32 wait_completion)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_qp \*nesqp:
        *undescribed*

    :param u32 which_wq:
        *undescribed*

    :param u32 wait_completion:
        *undescribed*

.. This file was automatic generated / don't edit.


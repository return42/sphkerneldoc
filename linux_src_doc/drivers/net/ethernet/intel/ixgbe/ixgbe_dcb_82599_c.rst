.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_dcb_82599.c

.. _`ixgbe_dcb_config_rx_arbiter_82599`:

ixgbe_dcb_config_rx_arbiter_82599
=================================

.. c:function:: s32 ixgbe_dcb_config_rx_arbiter_82599(struct ixgbe_hw *hw, u16 *refill, u16 *max, u8 *bwg_id, u8 *prio_type, u8 *prio_tc)

    Config Rx Data arbiter

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param refill:
        refill credits index by traffic class
    :type refill: u16 \*

    :param max:
        max credits index by traffic class
    :type max: u16 \*

    :param bwg_id:
        bandwidth grouping indexed by traffic class
    :type bwg_id: u8 \*

    :param prio_type:
        priority type indexed by traffic class
    :type prio_type: u8 \*

    :param prio_tc:
        priority to tc assignments indexed by priority
    :type prio_tc: u8 \*

.. _`ixgbe_dcb_config_rx_arbiter_82599.description`:

Description
-----------

Configure Rx Packet Arbiter and credits for each traffic class.

.. _`ixgbe_dcb_config_tx_desc_arbiter_82599`:

ixgbe_dcb_config_tx_desc_arbiter_82599
======================================

.. c:function:: s32 ixgbe_dcb_config_tx_desc_arbiter_82599(struct ixgbe_hw *hw, u16 *refill, u16 *max, u8 *bwg_id, u8 *prio_type)

    Config Tx Desc. arbiter

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param refill:
        refill credits index by traffic class
    :type refill: u16 \*

    :param max:
        max credits index by traffic class
    :type max: u16 \*

    :param bwg_id:
        bandwidth grouping indexed by traffic class
    :type bwg_id: u8 \*

    :param prio_type:
        priority type indexed by traffic class
    :type prio_type: u8 \*

.. _`ixgbe_dcb_config_tx_desc_arbiter_82599.description`:

Description
-----------

Configure Tx Descriptor Arbiter and credits for each traffic class.

.. _`ixgbe_dcb_config_tx_data_arbiter_82599`:

ixgbe_dcb_config_tx_data_arbiter_82599
======================================

.. c:function:: s32 ixgbe_dcb_config_tx_data_arbiter_82599(struct ixgbe_hw *hw, u16 *refill, u16 *max, u8 *bwg_id, u8 *prio_type, u8 *prio_tc)

    Config Tx Data arbiter

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param refill:
        refill credits index by traffic class
    :type refill: u16 \*

    :param max:
        max credits index by traffic class
    :type max: u16 \*

    :param bwg_id:
        bandwidth grouping indexed by traffic class
    :type bwg_id: u8 \*

    :param prio_type:
        priority type indexed by traffic class
    :type prio_type: u8 \*

    :param prio_tc:
        priority to tc assignments indexed by priority
    :type prio_tc: u8 \*

.. _`ixgbe_dcb_config_tx_data_arbiter_82599.description`:

Description
-----------

Configure Tx Packet Arbiter and credits for each traffic class.

.. _`ixgbe_dcb_config_pfc_82599`:

ixgbe_dcb_config_pfc_82599
==========================

.. c:function:: s32 ixgbe_dcb_config_pfc_82599(struct ixgbe_hw *hw, u8 pfc_en, u8 *prio_tc)

    Configure priority flow control

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param pfc_en:
        enabled pfc bitmask
    :type pfc_en: u8

    :param prio_tc:
        priority to tc assignments indexed by priority
    :type prio_tc: u8 \*

.. _`ixgbe_dcb_config_pfc_82599.description`:

Description
-----------

Configure Priority Flow Control (PFC) for each traffic class.

.. _`ixgbe_dcb_config_tc_stats_82599`:

ixgbe_dcb_config_tc_stats_82599
===============================

.. c:function:: s32 ixgbe_dcb_config_tc_stats_82599(struct ixgbe_hw *hw)

    Config traffic class statistics

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_dcb_config_tc_stats_82599.description`:

Description
-----------

Configure queue statistics registers, all queues belonging to same traffic
class uses a single set of queue statistics counters.

.. _`ixgbe_dcb_hw_config_82599`:

ixgbe_dcb_hw_config_82599
=========================

.. c:function:: s32 ixgbe_dcb_hw_config_82599(struct ixgbe_hw *hw, u8 pfc_en, u16 *refill, u16 *max, u8 *bwg_id, u8 *prio_type, u8 *prio_tc)

    Configure and enable DCB

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param pfc_en:
        enabled pfc bitmask
    :type pfc_en: u8

    :param refill:
        refill credits index by traffic class
    :type refill: u16 \*

    :param max:
        max credits index by traffic class
    :type max: u16 \*

    :param bwg_id:
        bandwidth grouping indexed by traffic class
    :type bwg_id: u8 \*

    :param prio_type:
        priority type indexed by traffic class
    :type prio_type: u8 \*

    :param prio_tc:
        priority to tc assignments indexed by priority
    :type prio_tc: u8 \*

.. _`ixgbe_dcb_hw_config_82599.description`:

Description
-----------

Configure dcb settings and enable dcb mode.

.. This file was automatic generated / don't edit.


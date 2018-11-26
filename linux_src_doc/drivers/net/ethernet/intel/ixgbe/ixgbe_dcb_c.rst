.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_dcb.c

.. _`ixgbe_ieee_credits`:

ixgbe_ieee_credits
==================

.. c:function:: s32 ixgbe_ieee_credits(__u8 *bw, __u16 *refill, __u16 *max, int max_frame)

    This calculates the ieee traffic class credits from the configured bandwidth percentages. Credits are the smallest unit programmable into the underlying hardware. The IEEE 802.1Qaz specification do not use bandwidth groups so this is much simplified from the CEE case.

    :param bw:
        bandwidth index by traffic class
    :type bw: __u8 \*

    :param refill:
        refill credits index by traffic class
    :type refill: __u16 \*

    :param max:
        max credits by traffic class
    :type max: __u16 \*

    :param max_frame:
        maximum frame size
    :type max_frame: int

.. _`ixgbe_dcb_calculate_tc_credits`:

ixgbe_dcb_calculate_tc_credits
==============================

.. c:function:: s32 ixgbe_dcb_calculate_tc_credits(struct ixgbe_hw *hw, struct ixgbe_dcb_config *dcb_config, int max_frame, u8 direction)

    Calculates traffic class credits

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param dcb_config:
        Struct containing DCB settings
    :type dcb_config: struct ixgbe_dcb_config \*

    :param max_frame:
        Maximum frame size
    :type max_frame: int

    :param direction:
        Configuring either Tx or Rx
    :type direction: u8

.. _`ixgbe_dcb_calculate_tc_credits.description`:

Description
-----------

This function calculates the credits allocated to each traffic class.
It should be called only after the rules are checked by
\ :c:func:`ixgbe_dcb_check_config`\ .

.. _`ixgbe_dcb_hw_config`:

ixgbe_dcb_hw_config
===================

.. c:function:: s32 ixgbe_dcb_hw_config(struct ixgbe_hw *hw, struct ixgbe_dcb_config *dcb_config)

    Config and enable DCB

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param dcb_config:
        pointer to ixgbe_dcb_config structure
    :type dcb_config: struct ixgbe_dcb_config \*

.. _`ixgbe_dcb_hw_config.description`:

Description
-----------

Configure dcb settings and enable dcb mode.

.. This file was automatic generated / don't edit.


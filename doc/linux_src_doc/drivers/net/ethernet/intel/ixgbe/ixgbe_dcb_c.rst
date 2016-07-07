.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_dcb.c

.. _`ixgbe_ieee_credits`:

ixgbe_ieee_credits
==================

.. c:function:: s32 ixgbe_ieee_credits(__u8 *bw, __u16 *refill, __u16 *max, int max_frame)

    This calculates the ieee traffic class credits from the configured bandwidth percentages. Credits are the smallest unit programmable into the underlying hardware. The IEEE 802.1Qaz specification do not use bandwidth groups so this is much simplified from the CEE case.

    :param __u8 \*bw:
        *undescribed*

    :param __u16 \*refill:
        *undescribed*

    :param __u16 \*max:
        *undescribed*

    :param int max_frame:
        *undescribed*

.. _`ixgbe_dcb_calculate_tc_credits`:

ixgbe_dcb_calculate_tc_credits
==============================

.. c:function:: s32 ixgbe_dcb_calculate_tc_credits(struct ixgbe_hw *hw, struct ixgbe_dcb_config *dcb_config, int max_frame, u8 direction)

    Calculates traffic class credits

    :param struct ixgbe_hw \*hw:
        *undescribed*

    :param struct ixgbe_dcb_config \*dcb_config:
        *undescribed*

    :param int max_frame:
        *undescribed*

    :param u8 direction:
        Configuring either Tx or Rx.

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

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param struct ixgbe_dcb_config \*dcb_config:
        pointer to ixgbe_dcb_config structure

.. _`ixgbe_dcb_hw_config.description`:

Description
-----------

Configure dcb settings and enable dcb mode.

.. This file was automatic generated / don't edit.


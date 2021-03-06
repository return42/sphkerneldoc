.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_phy.c

.. _`pch_gbe_phy_get_id`:

pch_gbe_phy_get_id
==================

.. c:function:: s32 pch_gbe_phy_get_id(struct pch_gbe_hw *hw)

    Retrieve the PHY ID and revision

    :param hw:
        Pointer to the HW structure
        Returns
        0:                      Successful.
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_get_id.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_phy_read_reg_miic`:

pch_gbe_phy_read_reg_miic
=========================

.. c:function:: s32 pch_gbe_phy_read_reg_miic(struct pch_gbe_hw *hw, u32 offset, u16 *data)

    Read MII control register

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param offset:
        Register offset to be read
    :type offset: u32

    :param data:
        Pointer to the read data
        Returns
        0:              Successful.
        -EINVAL:        Invalid argument.
    :type data: u16 \*

.. _`pch_gbe_phy_write_reg_miic`:

pch_gbe_phy_write_reg_miic
==========================

.. c:function:: s32 pch_gbe_phy_write_reg_miic(struct pch_gbe_hw *hw, u32 offset, u16 data)

    Write MII control register

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param offset:
        Register offset to be read
    :type offset: u32

    :param data:
        data to write to register at offset
        Returns
        0:              Successful.
        -EINVAL:        Invalid argument.
    :type data: u16

.. _`pch_gbe_phy_sw_reset`:

pch_gbe_phy_sw_reset
====================

.. c:function:: void pch_gbe_phy_sw_reset(struct pch_gbe_hw *hw)

    PHY software reset

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_hw_reset`:

pch_gbe_phy_hw_reset
====================

.. c:function:: void pch_gbe_phy_hw_reset(struct pch_gbe_hw *hw)

    PHY hardware reset

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_power_up`:

pch_gbe_phy_power_up
====================

.. c:function:: void pch_gbe_phy_power_up(struct pch_gbe_hw *hw)

    restore link in case the phy was powered down

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_power_down`:

pch_gbe_phy_power_down
======================

.. c:function:: void pch_gbe_phy_power_down(struct pch_gbe_hw *hw)

    Power down PHY

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_set_rgmii`:

pch_gbe_phy_set_rgmii
=====================

.. c:function:: void pch_gbe_phy_set_rgmii(struct pch_gbe_hw *hw)

    RGMII interface setting

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_tx_clk_delay`:

pch_gbe_phy_tx_clk_delay
========================

.. c:function:: int pch_gbe_phy_tx_clk_delay(struct pch_gbe_hw *hw)

    Setup TX clock delay via the PHY

    :param hw:
        Pointer to the HW structure
        Returns
        0:              Successful.
        -EINVAL:        Invalid argument.
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_init_setting`:

pch_gbe_phy_init_setting
========================

.. c:function:: void pch_gbe_phy_init_setting(struct pch_gbe_hw *hw)

    PHY initial setting

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_phy_disable_hibernate`:

pch_gbe_phy_disable_hibernate
=============================

.. c:function:: int pch_gbe_phy_disable_hibernate(struct pch_gbe_hw *hw)

    Disable the PHY low power state

    :param hw:
        Pointer to the HW structure
        Returns
        0:              Successful.
        -EINVAL:        Invalid argument.
    :type hw: struct pch_gbe_hw \*

.. This file was automatic generated / don't edit.


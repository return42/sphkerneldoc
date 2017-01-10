.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/macb.h

.. _`macb_platform_data`:

struct macb_platform_data
=========================

.. c:type:: struct macb_platform_data

    platform data for MACB Ethernet

.. _`macb_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct macb_platform_data {
        u32 phy_mask;
        int phy_irq_pin;
        u8 is_rmii;
        u8 rev_eth_addr;
        struct clk *pclk;
        struct clk *hclk;
    }

.. _`macb_platform_data.members`:

Members
-------

phy_mask
    phy mask passed when register the MDIO bus
    within the driver

phy_irq_pin
    PHY IRQ

is_rmii
    using RMII interface?

rev_eth_addr
    reverse Ethernet address byte order

pclk
    platform clock

hclk
    AHB clock

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/phy-stih41x-usb.c

.. _`stih41x_usb_cfg`:

struct stih41x_usb_cfg
======================

.. c:type:: struct stih41x_usb_cfg

    SoC specific PHY register mapping

.. _`stih41x_usb_cfg.definition`:

Definition
----------

.. code-block:: c

    struct stih41x_usb_cfg {
        u32 syscfg;
        u32 cfg_mask;
        u32 cfg;
        u32 oscok;
    }

.. _`stih41x_usb_cfg.members`:

Members
-------

syscfg
    Offset in syscfg registers bank

cfg_mask
    Bits mask for PHY configuration

cfg
    Static configuration value for PHY

oscok
    Notify the PHY oscillator clock is ready
    Setting this bit enable the PHY

.. _`stih41x_usb_phy`:

struct stih41x_usb_phy
======================

.. c:type:: struct stih41x_usb_phy

    Private data for the PHY

.. _`stih41x_usb_phy.definition`:

Definition
----------

.. code-block:: c

    struct stih41x_usb_phy {
        struct device *dev;
        struct regmap *regmap;
        const struct stih41x_usb_cfg *cfg;
        struct clk *clk;
    }

.. _`stih41x_usb_phy.members`:

Members
-------

dev
    device for this controller

regmap
    Syscfg registers bank in which PHY is configured

cfg
    SoC specific PHY register mapping

clk
    Oscillator used by the PHY

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/samsung/phy-exynos5-usbdrd.c

.. _`exynos5_usbdrd_phy`:

struct exynos5_usbdrd_phy
=========================

.. c:type:: struct exynos5_usbdrd_phy

    driver data for USB 3.0 PHY

.. _`exynos5_usbdrd_phy.definition`:

Definition
----------

.. code-block:: c

    struct exynos5_usbdrd_phy {
        struct device *dev;
        void __iomem *reg_phy;
        struct clk *clk;
        struct clk *pipeclk;
        struct clk *utmiclk;
        struct clk *itpclk;
        const struct exynos5_usbdrd_phy_drvdata *drv_data;
        struct phy_usb_instance phys;
        u32 extrefclk;
        struct clk *ref_clk;
        struct regulator *vbus;
        struct regulator *vbus_boost;
    }

.. _`exynos5_usbdrd_phy.members`:

Members
-------

dev
    pointer to device instance of this platform device

reg_phy
    usb phy controller register memory base

clk
    phy clock for register access

pipeclk
    clock for pipe3 phy

utmiclk
    clock for utmi+ phy

itpclk
    clock for ITP generation

drv_data
    pointer to SoC level driver data structure

phys
    array for 'EXYNOS5_DRDPHYS_NUM' number of PHY
    instances each with its 'phy' and 'phy_cfg'.

extrefclk
    frequency select settings when using 'separate
    reference clocks' for SS and HS operations

ref_clk
    reference clock to PHY block from which PHY's
    operational clocks are derived

vbus
    *undescribed*

vbus_boost
    *undescribed*

.. _`exynos5_usbdrd_phy.vbus`:

vbus
----

VBUS regulator for phy

.. _`exynos5_usbdrd_phy.vbus_boost`:

vbus_boost
----------

Boost regulator for VBUS present on few Exynos boards

.. This file was automatic generated / don't edit.


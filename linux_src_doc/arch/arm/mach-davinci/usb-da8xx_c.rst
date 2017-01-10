.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-davinci/usb-da8xx.c

.. _`da8xx_register_usb_refclkin`:

da8xx_register_usb_refclkin
===========================

.. c:function:: int da8xx_register_usb_refclkin(int rate)

    register USB_REFCLKIN clock

    :param int rate:
        The clock rate in Hz

.. _`da8xx_register_usb_refclkin.description`:

Description
-----------

This clock is only needed if the board provides an external USB_REFCLKIN
signal, in which case it will be used as the parent of usb20_phy_clk and/or
usb11_phy_clk.

.. _`da8xx_register_usb20_phy_clk`:

da8xx_register_usb20_phy_clk
============================

.. c:function:: int da8xx_register_usb20_phy_clk(bool use_usb_refclkin)

    register USB0PHYCLKMUX clock

    :param bool use_usb_refclkin:
        Selects the parent clock - either "usb_refclkin" if true
        or "pll0_aux" if false.

.. _`da8xx_register_usb11_phy_clk`:

da8xx_register_usb11_phy_clk
============================

.. c:function:: int da8xx_register_usb11_phy_clk(bool use_usb_refclkin)

    register USB1PHYCLKMUX clock

    :param bool use_usb_refclkin:
        Selects the parent clock - either "usb_refclkin" if true
        or "usb20_phy" if false.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/ti/phy-omap-control.c

.. _`omap_control_pcie_pcs`:

omap_control_pcie_pcs
=====================

.. c:function:: void omap_control_pcie_pcs(struct device *dev, u8 delay)

    set the PCS delay count

    :param dev:
        the control module device
    :type dev: struct device \*

    :param delay:
        8 bit delay value
    :type delay: u8

.. _`omap_control_phy_power`:

omap_control_phy_power
======================

.. c:function:: void omap_control_phy_power(struct device *dev, int on)

    power on/off the phy using control module reg

    :param dev:
        the control module device
    :type dev: struct device \*

    :param on:
        0 or 1, based on powering on or off the PHY
    :type on: int

.. _`omap_control_usb_host_mode`:

omap_control_usb_host_mode
==========================

.. c:function:: void omap_control_usb_host_mode(struct omap_control_phy *ctrl_phy)

    set AVALID, VBUSVALID and ID pin in grounded

    :param ctrl_phy:
        struct omap_control_phy \*
    :type ctrl_phy: struct omap_control_phy \*

.. _`omap_control_usb_host_mode.description`:

Description
-----------

Writes to the mailbox register to notify the usb core that a usb
device has been connected.

.. _`omap_control_usb_device_mode`:

omap_control_usb_device_mode
============================

.. c:function:: void omap_control_usb_device_mode(struct omap_control_phy *ctrl_phy)

    set AVALID, VBUSVALID and ID pin in high impedance

    :param ctrl_phy:
        struct omap_control_phy \*
    :type ctrl_phy: struct omap_control_phy \*

.. _`omap_control_usb_device_mode.description`:

Description
-----------

Writes to the mailbox register to notify the usb core that it has been
connected to a usb host.

.. _`omap_control_usb_set_sessionend`:

omap_control_usb_set_sessionend
===============================

.. c:function:: void omap_control_usb_set_sessionend(struct omap_control_phy *ctrl_phy)

    Enable SESSIONEND and IDIG to high impedance

    :param ctrl_phy:
        struct omap_control_phy \*
    :type ctrl_phy: struct omap_control_phy \*

.. _`omap_control_usb_set_sessionend.description`:

Description
-----------

Writes to the mailbox register to notify the usb core it's now in
disconnected state.

.. _`omap_control_usb_set_mode`:

omap_control_usb_set_mode
=========================

.. c:function:: void omap_control_usb_set_mode(struct device *dev, enum omap_control_usb_mode mode)

    Calls to functions to set USB in one of host mode or device mode or to denote disconnected state

    :param dev:
        the control module device
    :type dev: struct device \*

    :param mode:
        The mode to which usb should be configured
    :type mode: enum omap_control_usb_mode

.. _`omap_control_usb_set_mode.description`:

Description
-----------

This is an API to write to the mailbox register to notify the usb core that
a usb device has been connected.

.. This file was automatic generated / don't edit.


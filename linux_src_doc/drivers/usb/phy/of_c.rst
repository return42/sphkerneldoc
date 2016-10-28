.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/phy/of.c

.. _`of_usb_get_phy_mode`:

of_usb_get_phy_mode
===================

.. c:function:: enum usb_phy_interface of_usb_get_phy_mode(struct device_node *np)

    Get phy mode for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node

.. _`of_usb_get_phy_mode.description`:

Description
-----------

The function gets phy interface string from property 'phy_type',
and returns the corresponding enum usb_phy_interface

.. This file was automatic generated / don't edit.


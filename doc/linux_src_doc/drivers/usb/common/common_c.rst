.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/common/common.c

.. _`of_usb_get_dr_mode_by_phy`:

of_usb_get_dr_mode_by_phy
=========================

.. c:function:: enum usb_dr_mode of_usb_get_dr_mode_by_phy(struct device_node *phy_np)

    Get dual role mode for the controller device which is associated with the given phy device_node

    :param struct device_node \*phy_np:
        *undescribed*

.. _`of_usb_get_dr_mode_by_phy.description`:

Description
-----------

In dts a usb controller associates with phy devices.  The function gets
the string from property 'dr_mode' of the controller associated with the
given phy device node, and returns the correspondig enum usb_dr_mode.

.. _`of_usb_host_tpl_support`:

of_usb_host_tpl_support
=======================

.. c:function:: bool of_usb_host_tpl_support(struct device_node *np)

    to get if Targeted Peripheral List is supported for given targeted hosts (non-PC hosts)

    :param struct device_node \*np:
        Pointer to the given device_node

.. _`of_usb_host_tpl_support.description`:

Description
-----------

The function gets if the targeted hosts support TPL or not

.. _`of_usb_update_otg_caps`:

of_usb_update_otg_caps
======================

.. c:function:: int of_usb_update_otg_caps(struct device_node *np, struct usb_otg_caps *otg_caps)

    to update usb otg capabilities according to the passed properties in DT.

    :param struct device_node \*np:
        Pointer to the given device_node

    :param struct usb_otg_caps \*otg_caps:
        Pointer to the target usb_otg_caps to be set

.. _`of_usb_update_otg_caps.description`:

Description
-----------

The function updates the otg capabilities

.. This file was automatic generated / don't edit.


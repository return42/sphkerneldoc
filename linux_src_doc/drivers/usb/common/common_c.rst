.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/common/common.c

.. _`of_usb_get_dr_mode_by_phy`:

of_usb_get_dr_mode_by_phy
=========================

.. c:function:: enum usb_dr_mode of_usb_get_dr_mode_by_phy(struct device_node *np, int arg0)

    Get dual role mode for the controller device which is associated with the given phy device_node

    :param np:
        Pointer to the given phy device_node
    :type np: struct device_node \*

    :param arg0:
        phandle args[0] for phy's with #phy-cells >= 1, or -1 for
        phys which do not have phy-cells
    :type arg0: int

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

    :param np:
        Pointer to the given device_node
    :type np: struct device_node \*

.. _`of_usb_host_tpl_support.description`:

Description
-----------

The function gets if the targeted hosts support TPL or not

.. _`of_usb_update_otg_caps`:

of_usb_update_otg_caps
======================

.. c:function:: int of_usb_update_otg_caps(struct device_node *np, struct usb_otg_caps *otg_caps)

    to update usb otg capabilities according to the passed properties in DT.

    :param np:
        Pointer to the given device_node
    :type np: struct device_node \*

    :param otg_caps:
        Pointer to the target usb_otg_caps to be set
    :type otg_caps: struct usb_otg_caps \*

.. _`of_usb_update_otg_caps.description`:

Description
-----------

The function updates the otg capabilities

.. _`usb_of_get_companion_dev`:

usb_of_get_companion_dev
========================

.. c:function:: struct device *usb_of_get_companion_dev(struct device *dev)

    Find the companion device

    :param dev:
        the device pointer to find a companion
    :type dev: struct device \*

.. _`usb_of_get_companion_dev.description`:

Description
-----------

Find the companion device from platform bus.

Takes a reference to the returned struct device which needs to be dropped
after use.

.. _`usb_of_get_companion_dev.return`:

Return
------

On success, a pointer to the companion device, \ ``NULL``\  on failure.

.. This file was automatic generated / don't edit.


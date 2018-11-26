.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/common/roles.c

.. _`usb_role_switch_set_role`:

usb_role_switch_set_role
========================

.. c:function:: int usb_role_switch_set_role(struct usb_role_switch *sw, enum usb_role role)

    Set USB role for a switch

    :param sw:
        USB role switch
    :type sw: struct usb_role_switch \*

    :param role:
        USB role to be switched to
    :type role: enum usb_role

.. _`usb_role_switch_set_role.description`:

Description
-----------

Set USB role \ ``role``\  for \ ``sw``\ .

.. _`usb_role_switch_get_role`:

usb_role_switch_get_role
========================

.. c:function:: enum usb_role usb_role_switch_get_role(struct usb_role_switch *sw)

    Get the USB role for a switch

    :param sw:
        USB role switch
    :type sw: struct usb_role_switch \*

.. _`usb_role_switch_get_role.description`:

Description
-----------

Depending on the role-switch-driver this function returns either a cached
value of the last set role, or reads back the actual value from the hardware.

.. _`usb_role_switch_get`:

usb_role_switch_get
===================

.. c:function:: struct usb_role_switch *usb_role_switch_get(struct device *dev)

    Find USB role switch linked with the caller

    :param dev:
        The caller device
    :type dev: struct device \*

.. _`usb_role_switch_get.description`:

Description
-----------

Finds and returns role switch linked with \ ``dev``\ . The reference count for the
found switch is incremented.

.. _`usb_role_switch_put`:

usb_role_switch_put
===================

.. c:function:: void usb_role_switch_put(struct usb_role_switch *sw)

    Release handle to a switch

    :param sw:
        USB Role Switch
    :type sw: struct usb_role_switch \*

.. _`usb_role_switch_put.description`:

Description
-----------

Decrement reference count for \ ``sw``\ .

.. _`usb_role_switch_register`:

usb_role_switch_register
========================

.. c:function:: struct usb_role_switch *usb_role_switch_register(struct device *parent, const struct usb_role_switch_desc *desc)

    Register USB Role Switch

    :param parent:
        Parent device for the switch
    :type parent: struct device \*

    :param desc:
        Description of the switch
    :type desc: const struct usb_role_switch_desc \*

.. _`usb_role_switch_register.description`:

Description
-----------

USB Role Switch is a device capable or choosing the role for USB connector.
On platforms where the USB controller is dual-role capable, the controller
driver will need to register the switch. On platforms where the USB host and
USB device controllers behind the connector are separate, there will be a
mux, and the driver for that mux will need to register the switch.

Returns handle to a new role switch or ERR_PTR. The content of \ ``desc``\  is
copied.

.. _`usb_role_switch_unregister`:

usb_role_switch_unregister
==========================

.. c:function:: void usb_role_switch_unregister(struct usb_role_switch *sw)

    Unregsiter USB Role Switch

    :param sw:
        USB Role Switch
    :type sw: struct usb_role_switch \*

.. _`usb_role_switch_unregister.description`:

Description
-----------

Unregister switch that was registered with \ :c:func:`usb_role_switch_register`\ .

.. This file was automatic generated / don't edit.


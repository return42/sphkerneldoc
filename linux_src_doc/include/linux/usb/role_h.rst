.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/role.h

.. _`usb_role_switch_desc`:

struct usb_role_switch_desc
===========================

.. c:type:: struct usb_role_switch_desc

    USB Role Switch Descriptor

.. _`usb_role_switch_desc.definition`:

Definition
----------

.. code-block:: c

    struct usb_role_switch_desc {
        struct device *usb2_port;
        struct device *usb3_port;
        struct device *udc;
        usb_role_switch_set_t set;
        usb_role_switch_get_t get;
        bool allow_userspace_control;
    }

.. _`usb_role_switch_desc.members`:

Members
-------

usb2_port
    Optional reference to the host controller port device (USB2)

usb3_port
    Optional reference to the host controller port device (USB3)

udc
    Optional reference to the peripheral controller device

set
    Callback for setting the role

get
    Callback for getting the role (optional)

allow_userspace_control
    If true userspace may change the role through sysfs

.. _`usb_role_switch_desc.description`:

Description
-----------

\ ``usb2_port``\  and \ ``usb3_port``\  will point to the USB host port and \ ``udc``\  to the USB
device controller behind the USB connector with the role switch. If
\ ``usb2_port``\ , \ ``usb3_port``\  and \ ``udc``\  are included in the description, the
reference count for them should be incremented by the caller of
\ :c:func:`usb_role_switch_register`\  before registering the switch.

.. This file was automatic generated / don't edit.


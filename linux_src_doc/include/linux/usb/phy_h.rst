.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/phy.h

.. _`usb_phy_bind`:

struct usb_phy_bind
===================

.. c:type:: struct usb_phy_bind

    represent the binding for the phy

.. _`usb_phy_bind.definition`:

Definition
----------

.. code-block:: c

    struct usb_phy_bind {
        const char *dev_name;
        const char *phy_dev_name;
        u8 index;
        struct usb_phy *phy;
        struct list_head list;
    }

.. _`usb_phy_bind.members`:

Members
-------

dev_name
    the device name of the device that will bind to the phy

phy_dev_name
    the device name of the phy

index
    used if a single controller uses multiple phys

phy
    reference to the phy

list
    to maintain a linked list of the binding information

.. This file was automatic generated / don't edit.


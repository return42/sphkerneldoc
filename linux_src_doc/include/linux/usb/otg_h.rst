.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/otg.h

.. _`usb_otg_caps`:

struct usb_otg_caps
===================

.. c:type:: struct usb_otg_caps

    describes the otg capabilities of the device

.. _`usb_otg_caps.definition`:

Definition
----------

.. code-block:: c

    struct usb_otg_caps {
        u16 otg_rev;
        bool hnp_support;
        bool srp_support;
        bool adp_support;
    }

.. _`usb_otg_caps.members`:

Members
-------

otg_rev
    The OTG revision number the device is compliant with, it's
    in binary-coded decimal (i.e. 2.0 is 0200H).

hnp_support
    Indicates if the device supports HNP.

srp_support
    Indicates if the device supports SRP.

adp_support
    Indicates if the device supports ADP.

.. _`usb_get_dr_mode`:

usb_get_dr_mode
===============

.. c:function:: enum usb_dr_mode usb_get_dr_mode(struct device *dev)

    Get dual role mode for given device

    :param dev:
        Pointer to the given device
    :type dev: struct device \*

.. _`usb_get_dr_mode.description`:

Description
-----------

The function gets phy interface string from property 'dr_mode',
and returns the correspondig enum usb_dr_mode

.. This file was automatic generated / don't edit.


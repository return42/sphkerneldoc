.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/wusbcore/wa-hc.c

.. _`wa_create`:

wa_create
=========

.. c:function:: int wa_create(struct wahc *wa, struct usb_interface *iface, kernel_ulong_t quirks)

    :param wa:
        *undescribed*
    :type wa: struct wahc \*

    :param iface:
        *undescribed*
    :type iface: struct usb_interface \*

    :param quirks:
        *undescribed*
    :type quirks: kernel_ulong_t

.. _`wa_create.description`:

Description
-----------

wa->usb_dev and wa->usb_iface initialized and refcounted,
wa->wa_descr initialized.

.. _`wa_reset_all`:

wa_reset_all
============

.. c:function:: void wa_reset_all(struct wahc *wa)

    reset the WA device

    :param wa:
        the WA to be reset
    :type wa: struct wahc \*

.. _`wa_reset_all.description`:

Description
-----------

For HWAs the radio controller and all other PALs are also reset.

.. This file was automatic generated / don't edit.


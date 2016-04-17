.. -*- coding: utf-8; mode: rst -*-

=======
wa-hc.c
=======


.. _`wa_create`:

wa_create
=========

.. c:function:: int wa_create (struct wahc *wa, struct usb_interface *iface, kernel_ulong_t quirks)

    :param struct wahc \*wa:

        *undescribed*

    :param struct usb_interface \*iface:

        *undescribed*

    :param kernel_ulong_t quirks:

        *undescribed*



.. _`wa_create.description`:

Description
-----------


wa->usb_dev and wa->usb_iface initialized and refcounted,
wa->wa_descr initialized.



.. _`wa_reset_all`:

wa_reset_all
============

.. c:function:: void wa_reset_all (struct wahc *wa)

    reset the WA device

    :param struct wahc \*wa:
        the WA to be reset



.. _`wa_reset_all.description`:

Description
-----------

For HWAs the radio controller and all other PALs are also reset.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/function/f_acm.c

.. _`acm_cdc_notify`:

acm_cdc_notify
==============

.. c:function:: int acm_cdc_notify(struct f_acm *acm, u8 type, u16 value, void *data, unsigned length)

    issue CDC notification to host

    :param struct f_acm \*acm:
        wraps host to be notified

    :param u8 type:
        notification type

    :param u16 value:
        Refer to cdc specs, wValue field.

    :param void \*data:
        data to be sent

    :param unsigned length:
        size of data

.. _`acm_cdc_notify.context`:

Context
-------

irqs blocked, acm->lock held, acm_notify_req non-null

.. _`acm_cdc_notify.description`:

Description
-----------

Returns zero on success or a negative errno.

See section 6.3.5 of the CDC 1.1 specification for information

.. _`acm_cdc_notify.about-the-only-notification-we-issue`:

about the only notification we issue
------------------------------------

SerialState change.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/wacom_sys.c

.. _`wacom_led_next`:

wacom_led_next
==============

.. c:function:: struct wacom_led *wacom_led_next(struct wacom *wacom, struct wacom_led *cur)

    gives the next available led with a wacom trigger.

    :param wacom:
        *undescribed*
    :type wacom: struct wacom \*

    :param cur:
        *undescribed*
    :type cur: struct wacom_led \*

.. _`wacom_led_next.description`:

Description
-----------

returns the next available struct wacom_led which has its default trigger
or the current one if none is available.

.. This file was automatic generated / don't edit.


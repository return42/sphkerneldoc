.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-logitech-hidpp.c

.. _`hidpp_send_message_sync`:

hidpp_send_message_sync
=======================

.. c:function:: int hidpp_send_message_sync(struct hidpp_device *hidpp, struct hidpp_report *message, struct hidpp_report *response)

    in case of a failure. - If ' something else' is positive, that means that an error has been raised by the protocol itself. - If ' something else' is negative, that means that we had a classic error (-ENOMEM, -EPIPE, etc...)

    :param struct hidpp_device \*hidpp:
        *undescribed*

    :param struct hidpp_report \*message:
        *undescribed*

    :param struct hidpp_report \*response:
        *undescribed*

.. _`hidpp_prefix_name`:

hidpp_prefix_name
=================

.. c:function:: void hidpp_prefix_name(char **name, int name_length)

    :param char \*\*name:
        *undescribed*

    :param int name_length:
        *undescribed*

.. _`hidpp_touchpad_fw_items_set`:

hidpp_touchpad_fw_items_set
===========================

.. c:function:: int hidpp_touchpad_fw_items_set(struct hidpp_device *hidpp, u8 feature_index, struct hidpp_touchpad_fw_items *items)

    >state field. items is then filled with the current state.

    :param struct hidpp_device \*hidpp:
        *undescribed*

    :param u8 feature_index:
        *undescribed*

    :param struct hidpp_touchpad_fw_items \*items:
        *undescribed*

.. This file was automatic generated / don't edit.


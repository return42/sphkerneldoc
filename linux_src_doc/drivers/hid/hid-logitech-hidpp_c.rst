.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-logitech-hidpp.c

.. _`hidpp_send_message_sync`:

hidpp_send_message_sync
=======================

.. c:function:: int hidpp_send_message_sync(struct hidpp_device *hidpp, struct hidpp_report *message, struct hidpp_report *response)

    in case of a failure. - If ' something else' is positive, that means that an error has been raised by the protocol itself. - If ' something else' is negative, that means that we had a classic error (-ENOMEM, -EPIPE, etc...)

    :param hidpp:
        *undescribed*
    :type hidpp: struct hidpp_device \*

    :param message:
        *undescribed*
    :type message: struct hidpp_report \*

    :param response:
        *undescribed*
    :type response: struct hidpp_report \*

.. _`hidpp_prefix_name`:

hidpp_prefix_name
=================

.. c:function:: void hidpp_prefix_name(char **name, int name_length)

    :param name:
        *undescribed*
    :type name: char \*\*

    :param name_length:
        *undescribed*
    :type name_length: int

.. _`hidpp_touchpad_fw_items_set`:

hidpp_touchpad_fw_items_set
===========================

.. c:function:: int hidpp_touchpad_fw_items_set(struct hidpp_device *hidpp, u8 feature_index, struct hidpp_touchpad_fw_items *items)

    >state field. items is then filled with the current state.

    :param hidpp:
        *undescribed*
    :type hidpp: struct hidpp_device \*

    :param feature_index:
        *undescribed*
    :type feature_index: u8

    :param items:
        *undescribed*
    :type items: struct hidpp_touchpad_fw_items \*

.. This file was automatic generated / don't edit.


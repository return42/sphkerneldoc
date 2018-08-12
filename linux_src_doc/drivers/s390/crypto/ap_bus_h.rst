.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/ap_bus.h

.. _`ap_init_message`:

ap_init_message
===============

.. c:function:: void ap_init_message(struct ap_message *ap_msg)

    Initialize ap_message. Initialize a message before using. Otherwise this might result in unexpected behaviour.

    :param struct ap_message \*ap_msg:
        *undescribed*

.. _`ap_release_message`:

ap_release_message
==================

.. c:function:: void ap_release_message(struct ap_message *ap_msg)

    Release ap_message. Releases all memory used internal within the ap_message struct Currently this is the message and private field.

    :param struct ap_message \*ap_msg:
        *undescribed*

.. This file was automatic generated / don't edit.


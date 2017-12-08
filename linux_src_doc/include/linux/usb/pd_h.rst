.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/pd.h

.. _`pd_message`:

struct pd_message
=================

.. c:type:: struct pd_message

    PD message as seen on wire

.. _`pd_message.definition`:

Definition
----------

.. code-block:: c

    struct pd_message {
        __le16 header;
        __le32 payload[PD_MAX_PAYLOAD];
    }

.. _`pd_message.members`:

Members
-------

header
    PD message header

payload
    PD message payload

.. This file was automatic generated / don't edit.


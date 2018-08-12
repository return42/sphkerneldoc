.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/pd.h

.. _`pd_chunked_ext_message_data`:

struct pd_chunked_ext_message_data
==================================

.. c:type:: struct pd_chunked_ext_message_data

    PD chunked extended message data as seen on wire

.. _`pd_chunked_ext_message_data.definition`:

Definition
----------

.. code-block:: c

    struct pd_chunked_ext_message_data {
        __le16 header;
        u8 data[PD_EXT_MAX_CHUNK_DATA];
    }

.. _`pd_chunked_ext_message_data.members`:

Members
-------

header
    PD extended message header

data
    PD extended message data

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
        union {
            __le32 payload[PD_MAX_PAYLOAD];
            struct pd_chunked_ext_message_data ext_msg;
        } ;
    }

.. _`pd_message.members`:

Members
-------

header
    PD message header

{unnamed_union}
    anonymous

payload
    PD message payload

ext_msg
    PD message chunked extended message data

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/arm_scmi/common.h

.. _`scmi_msg_resp_prot_version`:

struct scmi_msg_resp_prot_version
=================================

.. c:type:: struct scmi_msg_resp_prot_version

    Response for a message

.. _`scmi_msg_resp_prot_version.definition`:

Definition
----------

.. code-block:: c

    struct scmi_msg_resp_prot_version {
        __le16 minor_version;
        __le16 major_version;
    }

.. _`scmi_msg_resp_prot_version.members`:

Members
-------

minor_version
    Minor version of the ABI that firmware supports

major_version
    Major version of the ABI that firmware supports

.. _`scmi_msg_resp_prot_version.description`:

Description
-----------

In general, ABI version changes follow the rule that minor version increments
are backward compatible. Major revision changes in ABI may not be
backward compatible.

Response to a generic message with message type SCMI_MSG_VERSION

.. _`scmi_msg_hdr`:

struct scmi_msg_hdr
===================

.. c:type:: struct scmi_msg_hdr

    Message(Tx/Rx) header

.. _`scmi_msg_hdr.definition`:

Definition
----------

.. code-block:: c

    struct scmi_msg_hdr {
        u8 id;
        u8 protocol_id;
        u16 seq;
        u32 status;
        bool poll_completion;
    }

.. _`scmi_msg_hdr.members`:

Members
-------

id
    The identifier of the command being sent

protocol_id
    The identifier of the protocol used to send \ ``id``\  command

seq
    The token to identify the message. when a message/command returns,
    the platform returns the whole message header unmodified including
    the token

status
    Status of the transfer once it's complete

poll_completion
    Indicate if the transfer needs to be polled for
    completion or interrupt mode is used

.. _`scmi_msg`:

struct scmi_msg
===============

.. c:type:: struct scmi_msg

    Message(Tx/Rx) structure

.. _`scmi_msg.definition`:

Definition
----------

.. code-block:: c

    struct scmi_msg {
        void *buf;
        size_t len;
    }

.. _`scmi_msg.members`:

Members
-------

buf
    Buffer pointer

len
    Length of data in the Buffer

.. _`scmi_xfer`:

struct scmi_xfer
================

.. c:type:: struct scmi_xfer

    Structure representing a message flow

.. _`scmi_xfer.definition`:

Definition
----------

.. code-block:: c

    struct scmi_xfer {
        struct scmi_msg_hdr hdr;
        struct scmi_msg tx;
        struct scmi_msg rx;
        struct completion done;
    }

.. _`scmi_xfer.members`:

Members
-------

hdr
    Transmit message header

tx
    Transmit message

rx
    Receive message, the buffer should be pre-allocated to store
    message. If request-ACK protocol is used, we can reuse the same
    buffer for the rx path as we use for the tx path.

done
    completion event

.. This file was automatic generated / don't edit.


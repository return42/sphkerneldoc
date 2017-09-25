.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/cec.h

.. _`cec_msg`:

struct cec_msg
==============

.. c:type:: struct cec_msg

    CEC message structure.

.. _`cec_msg.definition`:

Definition
----------

.. code-block:: c

    struct cec_msg {
        __u64 tx_ts;
        __u64 rx_ts;
        __u32 len;
        __u32 timeout;
        __u32 sequence;
        __u32 flags;
        __u8 msg[CEC_MAX_MSG_SIZE];
        __u8 reply;
        __u8 rx_status;
        __u8 tx_status;
        __u8 tx_arb_lost_cnt;
        __u8 tx_nack_cnt;
        __u8 tx_low_drive_cnt;
        __u8 tx_error_cnt;
    }

.. _`cec_msg.members`:

Members
-------

tx_ts
    Timestamp in nanoseconds using CLOCK_MONOTONIC. Set by the
    driver when the message transmission has finished.

rx_ts
    Timestamp in nanoseconds using CLOCK_MONOTONIC. Set by the
    driver when the message was received.

len
    Length in bytes of the message.

timeout
    The timeout (in ms) that is used to timeout CEC_RECEIVE.
    Set to 0 if you want to wait forever. This timeout can also be
    used with CEC_TRANSMIT as the timeout for waiting for a reply.
    If 0, then it will use a 1 second timeout instead of waiting
    forever as is done with CEC_RECEIVE.

sequence
    The framework assigns a sequence number to messages that are
    sent. This can be used to track replies to previously sent
    messages.

flags
    Set to 0.

msg
    The message payload.

reply
    This field is ignored with CEC_RECEIVE and is only used by
    CEC_TRANSMIT. If non-zero, then wait for a reply with this
    opcode. Set to CEC_MSG_FEATURE_ABORT if you want to wait for
    a possible ABORT reply. If there was an error when sending the
    msg or FeatureAbort was returned, then reply is set to 0.
    If reply is non-zero upon return, then len/msg are set to
    the received message.
    If reply is zero upon return and status has the
    CEC_TX_STATUS_FEATURE_ABORT bit set, then len/msg are set to
    the received feature abort message.
    If reply is zero upon return and status has the
    CEC_TX_STATUS_MAX_RETRIES bit set, then no reply was seen at
    all. If reply is non-zero for CEC_TRANSMIT and the message is a
    broadcast, then -EINVAL is returned.
    if reply is non-zero, then timeout is set to 1000 (the required
    maximum response time).

rx_status
    The message receive status bits. Set by the driver.

tx_status
    The message transmit status bits. Set by the driver.

tx_arb_lost_cnt
    The number of 'Arbitration Lost' events. Set by the driver.

tx_nack_cnt
    The number of 'Not Acknowledged' events. Set by the driver.

tx_low_drive_cnt
    The number of 'Low Drive Detected' events. Set by the
    driver.

tx_error_cnt
    The number of 'Error' events. Set by the driver.

.. _`cec_msg_initiator`:

cec_msg_initiator
=================

.. c:function:: __u8 cec_msg_initiator(const struct cec_msg *msg)

    return the initiator's logical address.

    :param const struct cec_msg \*msg:
        the message structure

.. _`cec_msg_destination`:

cec_msg_destination
===================

.. c:function:: __u8 cec_msg_destination(const struct cec_msg *msg)

    return the destination's logical address.

    :param const struct cec_msg \*msg:
        the message structure

.. _`cec_msg_opcode`:

cec_msg_opcode
==============

.. c:function:: int cec_msg_opcode(const struct cec_msg *msg)

    return the opcode of the message, -1 for poll

    :param const struct cec_msg \*msg:
        the message structure

.. _`cec_msg_is_broadcast`:

cec_msg_is_broadcast
====================

.. c:function:: int cec_msg_is_broadcast(const struct cec_msg *msg)

    return true if this is a broadcast message.

    :param const struct cec_msg \*msg:
        the message structure

.. _`cec_msg_init`:

cec_msg_init
============

.. c:function:: void cec_msg_init(struct cec_msg *msg, __u8 initiator, __u8 destination)

    initialize the message structure.

    :param struct cec_msg \*msg:
        the message structure

    :param __u8 initiator:
        the logical address of the initiator

    :param __u8 destination:
        the logical address of the destination (0xf for broadcast)

.. _`cec_msg_init.description`:

Description
-----------

The whole structure is zeroed, the len field is set to 1 (i.e. a poll
message) and the initiator and destination are filled in.

.. _`cec_msg_set_reply_to`:

cec_msg_set_reply_to
====================

.. c:function:: void cec_msg_set_reply_to(struct cec_msg *msg, struct cec_msg *orig)

    fill in destination/initiator in a reply message.

    :param struct cec_msg \*msg:
        the message structure for the reply

    :param struct cec_msg \*orig:
        the original message structure

.. _`cec_msg_set_reply_to.description`:

Description
-----------

Set the msg destination to the orig initiator and the msg initiator to the
orig destination. Note that msg and orig may be the same pointer, in which
case the change is done in place.

.. _`cec_caps`:

struct cec_caps
===============

.. c:type:: struct cec_caps

    CEC capabilities structure.

.. _`cec_caps.definition`:

Definition
----------

.. code-block:: c

    struct cec_caps {
        char driver[32];
        char name[32];
        __u32 available_log_addrs;
        __u32 capabilities;
        __u32 version;
    }

.. _`cec_caps.members`:

Members
-------

driver
    name of the CEC device driver.

name
    name of the CEC device. \ ``driver``\  + \ ``name``\  must be unique.

available_log_addrs
    number of available logical addresses.

capabilities
    capabilities of the CEC adapter.

version
    version of the CEC adapter framework.

.. _`cec_log_addrs`:

struct cec_log_addrs
====================

.. c:type:: struct cec_log_addrs

    CEC logical addresses structure.

.. _`cec_log_addrs.definition`:

Definition
----------

.. code-block:: c

    struct cec_log_addrs {
        __u8 log_addr[CEC_MAX_LOG_ADDRS];
        __u16 log_addr_mask;
        __u8 cec_version;
        __u8 num_log_addrs;
        __u32 vendor_id;
        __u32 flags;
        char osd_name[15];
        __u8 primary_device_type[CEC_MAX_LOG_ADDRS];
        __u8 log_addr_type[CEC_MAX_LOG_ADDRS];
        __u8 all_device_types[CEC_MAX_LOG_ADDRS];
        __u8 features[CEC_MAX_LOG_ADDRS][12];
    }

.. _`cec_log_addrs.members`:

Members
-------

log_addr
    the claimed logical addresses. Set by the driver.

log_addr_mask
    current logical address mask. Set by the driver.

cec_version
    the CEC version that the adapter should implement. Set by the
    caller.

num_log_addrs
    how many logical addresses should be claimed. Set by the
    caller.

vendor_id
    the vendor ID of the device. Set by the caller.

flags
    flags.

osd_name
    the OSD name of the device. Set by the caller.

primary_device_type
    the primary device type for each logical address.
    Set by the caller.

log_addr_type
    the logical address types. Set by the caller.

all_device_types
    CEC 2.0: all device types represented by the logical
    address. Set by the caller.

features
    CEC 2.0: The logical address features. Set by the caller.

.. _`cec_event_state_change`:

struct cec_event_state_change
=============================

.. c:type:: struct cec_event_state_change

    used when the CEC adapter changes state.

.. _`cec_event_state_change.definition`:

Definition
----------

.. code-block:: c

    struct cec_event_state_change {
        __u16 phys_addr;
        __u16 log_addr_mask;
    }

.. _`cec_event_state_change.members`:

Members
-------

phys_addr
    the current physical address

log_addr_mask
    the current logical address mask

.. _`cec_event_lost_msgs`:

struct cec_event_lost_msgs
==========================

.. c:type:: struct cec_event_lost_msgs

    tells you how many messages were lost.

.. _`cec_event_lost_msgs.definition`:

Definition
----------

.. code-block:: c

    struct cec_event_lost_msgs {
        __u32 lost_msgs;
    }

.. _`cec_event_lost_msgs.members`:

Members
-------

lost_msgs
    how many messages were lost.

.. _`cec_event`:

struct cec_event
================

.. c:type:: struct cec_event

    CEC event structure

.. _`cec_event.definition`:

Definition
----------

.. code-block:: c

    struct cec_event {
        __u64 ts;
        __u32 event;
        __u32 flags;
        union {
            struct cec_event_state_change state_change;
            struct cec_event_lost_msgs lost_msgs;
            __u32 raw[16];
        } ;
    }

.. _`cec_event.members`:

Members
-------

ts
    the timestamp of when the event was sent.

event
    the event.
    array.

flags
    *undescribed*

{unnamed_union}
    anonymous

.. This file was automatic generated / don't edit.


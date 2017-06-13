.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/ti_sci.h

.. _`ti_sci_msg_hdr`:

struct ti_sci_msg_hdr
=====================

.. c:type:: struct ti_sci_msg_hdr

    Generic Message Header for All messages and responses

.. _`ti_sci_msg_hdr.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_hdr {
        u16 type;
        u8 host;
        u8 seq;
    #define TI_SCI_MSG_FLAGval 1 << val
    #define TI_SCI_FLAG_REQ_GENERIC_NORESPONSE 0x0
    #define TI_SCI_FLAG_REQ_ACK_ON_RECEIVED TI_SCI_MSG_FLAG0
    #define TI_SCI_FLAG_REQ_ACK_ON_PROCESSED TI_SCI_MSG_FLAG1
    #define TI_SCI_FLAG_RESP_GENERIC_NACK 0x0
    #define TI_SCI_FLAG_RESP_GENERIC_ACK TI_SCI_MSG_FLAG1
        u32 flags;
    }

.. _`ti_sci_msg_hdr.members`:

Members
-------

type
    Type of messages: One of TI_SCI_MSG\* values

host
    Host of the message

seq
    Message identifier indicating a transfer sequence

flags
    Flag for the message

.. _`ti_sci_msg_resp_version`:

struct ti_sci_msg_resp_version
==============================

.. c:type:: struct ti_sci_msg_resp_version

    Response for a message

.. _`ti_sci_msg_resp_version.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_version {
        struct ti_sci_msg_hdr hdr;
        char firmware_description;
        u16 firmware_revision;
        u8 abi_major;
        u8 abi_minor;
    }

.. _`ti_sci_msg_resp_version.members`:

Members
-------

hdr
    Generic header

firmware_description
    String describing the firmware

firmware_revision
    Firmware revision

abi_major
    Major version of the ABI that firmware supports

abi_minor
    Minor version of the ABI that firmware supports

.. _`ti_sci_msg_resp_version.description`:

Description
-----------

In general, ABI version changes follow the rule that minor version increments
are backward compatible. Major revision changes in ABI may not be
backward compatible.

Response to a generic message with message type TI_SCI_MSG_VERSION

.. _`ti_sci_msg_req_reboot`:

struct ti_sci_msg_req_reboot
============================

.. c:type:: struct ti_sci_msg_req_reboot

    Reboot the SoC

.. _`ti_sci_msg_req_reboot.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_reboot {
        struct ti_sci_msg_hdr hdr;
    }

.. _`ti_sci_msg_req_reboot.members`:

Members
-------

hdr
    Generic Header

.. _`ti_sci_msg_req_reboot.description`:

Description
-----------

Request type is TI_SCI_MSG_SYS_RESET, responded with a generic
ACK/NACK message.

.. _`ti_sci_msg_req_set_device_state`:

struct ti_sci_msg_req_set_device_state
======================================

.. c:type:: struct ti_sci_msg_req_set_device_state

    Set the desired state of the device

.. _`ti_sci_msg_req_set_device_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_set_device_state {
    #define MSG_FLAG_DEVICE_WAKE_ENABLED TI_SCI_MSG_FLAG8
    #define MSG_FLAG_DEVICE_RESET_ISO TI_SCI_MSG_FLAG9
    #define MSG_FLAG_DEVICE_EXCLUSIVE TI_SCI_MSG_FLAG10
        struct ti_sci_msg_hdr hdr;
        u32 id;
        u32 reserved;
    #define MSG_DEVICE_SW_STATE_AUTO_OFF 0
    #define MSG_DEVICE_SW_STATE_RETENTION 1
    #define MSG_DEVICE_SW_STATE_ON 2
        u8 state;
    }

.. _`ti_sci_msg_req_set_device_state.members`:

Members
-------

hdr
    Generic header

id
    Indicates which device to modify

reserved
    Reserved space in message, must be 0 for backward compatibility

state
    The desired state of the device.

.. _`ti_sci_msg_req_set_device_state.certain-flags-can-also-be-set-to-alter-the-device-state`:

Certain flags can also be set to alter the device state
-------------------------------------------------------

+ MSG_FLAG_DEVICE_WAKE_ENABLED - Configure the device to be a wake source.
The meaning of this flag will vary slightly from device to device and from
SoC to SoC but it generally allows the device to wake the SoC out of deep
suspend states.
+ MSG_FLAG_DEVICE_RESET_ISO - Enable reset isolation for this device.
+ MSG_FLAG_DEVICE_EXCLUSIVE - Claim this device exclusively. When passed
with STATE_RETENTION or STATE_ON, it will claim the device exclusively.
If another host already has this device set to STATE_RETENTION or STATE_ON,
the message will fail. Once successful, other hosts attempting to set
STATE_RETENTION or STATE_ON will fail.

Request type is TI_SCI_MSG_SET_DEVICE_STATE, responded with a generic
ACK/NACK message.

.. _`ti_sci_msg_req_get_device_state`:

struct ti_sci_msg_req_get_device_state
======================================

.. c:type:: struct ti_sci_msg_req_get_device_state

    Request to get device.

.. _`ti_sci_msg_req_get_device_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_get_device_state {
        struct ti_sci_msg_hdr hdr;
        u32 id;
    }

.. _`ti_sci_msg_req_get_device_state.members`:

Members
-------

hdr
    Generic header

id
    Device Identifier

.. _`ti_sci_msg_req_get_device_state.description`:

Description
-----------

Request type is TI_SCI_MSG_GET_DEVICE_STATE, responded device state
information

.. _`ti_sci_msg_resp_get_device_state`:

struct ti_sci_msg_resp_get_device_state
=======================================

.. c:type:: struct ti_sci_msg_resp_get_device_state

    Response to get device request.

.. _`ti_sci_msg_resp_get_device_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_get_device_state {
        struct ti_sci_msg_hdr hdr;
        u32 context_loss_count;
        u32 resets;
        u8 programmed_state;
    #define MSG_DEVICE_HW_STATE_OFF 0
    #define MSG_DEVICE_HW_STATE_ON 1
    #define MSG_DEVICE_HW_STATE_TRANS 2
        u8 current_state;
    }

.. _`ti_sci_msg_resp_get_device_state.members`:

Members
-------

hdr
    Generic header

context_loss_count
    Indicates how many times the device has lost context. A
    driver can use this monotonic counter to determine if the device has
    lost context since the last time this message was exchanged.

resets
    Programmed state of the reset lines.

programmed_state
    The state as programmed by set_device.
    - Uses the MSG_DEVICE_SW\_\* macros

current_state
    The actual state of the hardware.

.. _`ti_sci_msg_resp_get_device_state.description`:

Description
-----------

Response to request TI_SCI_MSG_GET_DEVICE_STATE.

.. _`ti_sci_msg_req_set_device_resets`:

struct ti_sci_msg_req_set_device_resets
=======================================

.. c:type:: struct ti_sci_msg_req_set_device_resets

    Set the desired resets configuration of the device

.. _`ti_sci_msg_req_set_device_resets.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_set_device_resets {
        struct ti_sci_msg_hdr hdr;
        u32 id;
        u32 resets;
    }

.. _`ti_sci_msg_req_set_device_resets.members`:

Members
-------

hdr
    Generic header

id
    Indicates which device to modify

resets
    A bit field of resets for the device. The meaning, behavior,
    and usage of the reset flags are device specific. 0 for a bit
    indicates releasing the reset represented by that bit while 1
    indicates keeping it held.

.. _`ti_sci_msg_req_set_device_resets.description`:

Description
-----------

Request type is TI_SCI_MSG_SET_DEVICE_RESETS, responded with a generic
ACK/NACK message.

.. _`ti_sci_msg_req_set_clock_state`:

struct ti_sci_msg_req_set_clock_state
=====================================

.. c:type:: struct ti_sci_msg_req_set_clock_state

    Request to setup a Clock state

.. _`ti_sci_msg_req_set_clock_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_set_clock_state {
    #define MSG_FLAG_CLOCK_ALLOW_SSC TI_SCI_MSG_FLAG8
    #define MSG_FLAG_CLOCK_ALLOW_FREQ_CHANGE TI_SCI_MSG_FLAG9
    #define MSG_FLAG_CLOCK_INPUT_TERM TI_SCI_MSG_FLAG10
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
    #define MSG_CLOCK_SW_STATE_UNREQ 0
    #define MSG_CLOCK_SW_STATE_AUTO 1
    #define MSG_CLOCK_SW_STATE_REQ 2
        u8 request_state;
    }

.. _`ti_sci_msg_req_set_clock_state.members`:

Members
-------

hdr
    Generic Header, Certain flags can be set specific to the clocks:
    MSG_FLAG_CLOCK_ALLOW_SSC: Allow this clock to be modified
    via spread spectrum clocking.
    MSG_FLAG_CLOCK_ALLOW_FREQ_CHANGE: Allow this clock's
    frequency to be changed while it is running so long as it
    is within the min/max limits.
    MSG_FLAG_CLOCK_INPUT_TERM: Enable input termination, this
    is only applicable to clock inputs on the SoC pseudo-device.

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.
    Each device has it's own set of clock inputs. This indexes
    which clock input to modify.

request_state
    Request the state for the clock to be set to.
    MSG_CLOCK_SW_STATE_UNREQ: The IP does not require this clock,
    it can be disabled, regardless of the state of the device
    MSG_CLOCK_SW_STATE_AUTO: Allow the System Controller to
    automatically manage the state of this clock. If the device
    is enabled, then the clock is enabled. If the device is set
    to off or retention, then the clock is internally set as not
    being required by the device.(default)
    MSG_CLOCK_SW_STATE_REQ:  Configure the clock to be enabled,
    regardless of the state of the device.

.. _`ti_sci_msg_req_set_clock_state.description`:

Description
-----------

Normally, all required clocks are managed by TISCI entity, this is used
only for specific control \*IF\* required. Auto managed state is
MSG_CLOCK_SW_STATE_AUTO, in other states, TISCI entity assume remote
will explicitly control.

Request type is TI_SCI_MSG_SET_CLOCK_STATE, response is a generic
ACK or NACK message.

.. _`ti_sci_msg_req_get_clock_state`:

struct ti_sci_msg_req_get_clock_state
=====================================

.. c:type:: struct ti_sci_msg_req_get_clock_state

    Request for clock state

.. _`ti_sci_msg_req_get_clock_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_get_clock_state {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_get_clock_state.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.
    Each device has it's own set of clock inputs. This indexes
    which clock input to get state of.

.. _`ti_sci_msg_req_get_clock_state.description`:

Description
-----------

Request type is TI_SCI_MSG_GET_CLOCK_STATE, response is state
of the clock

.. _`ti_sci_msg_resp_get_clock_state`:

struct ti_sci_msg_resp_get_clock_state
======================================

.. c:type:: struct ti_sci_msg_resp_get_clock_state

    Response to get clock state

.. _`ti_sci_msg_resp_get_clock_state.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_get_clock_state {
        struct ti_sci_msg_hdr hdr;
        u8 programmed_state;
    #define MSG_CLOCK_HW_STATE_NOT_READY 0
    #define MSG_CLOCK_HW_STATE_READY 1
        u8 current_state;
    }

.. _`ti_sci_msg_resp_get_clock_state.members`:

Members
-------

hdr
    Generic Header

programmed_state
    Any programmed state of the clock. This is one of
    MSG_CLOCK_SW_STATE\* values.

current_state
    Current state of the clock. This is one of:
    MSG_CLOCK_HW_STATE_NOT_READY: Clock is not ready
    MSG_CLOCK_HW_STATE_READY: Clock is ready

.. _`ti_sci_msg_resp_get_clock_state.description`:

Description
-----------

Response to TI_SCI_MSG_GET_CLOCK_STATE.

.. _`ti_sci_msg_req_set_clock_parent`:

struct ti_sci_msg_req_set_clock_parent
======================================

.. c:type:: struct ti_sci_msg_req_set_clock_parent

    Set the clock parent

.. _`ti_sci_msg_req_set_clock_parent.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_set_clock_parent {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
        u8 parent_id;
    }

.. _`ti_sci_msg_req_set_clock_parent.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.
    Each device has it's own set of clock inputs. This indexes
    which clock input to modify.

parent_id
    The new clock parent is selectable by an index via this
    parameter.

.. _`ti_sci_msg_req_set_clock_parent.description`:

Description
-----------

Request type is TI_SCI_MSG_SET_CLOCK_PARENT, response is generic
ACK / NACK message.

.. _`ti_sci_msg_req_get_clock_parent`:

struct ti_sci_msg_req_get_clock_parent
======================================

.. c:type:: struct ti_sci_msg_req_get_clock_parent

    Get the clock parent

.. _`ti_sci_msg_req_get_clock_parent.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_get_clock_parent {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_get_clock_parent.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.
    Each device has it's own set of clock inputs. This indexes
    which clock input to get the parent for.

.. _`ti_sci_msg_req_get_clock_parent.description`:

Description
-----------

Request type is TI_SCI_MSG_GET_CLOCK_PARENT, response is parent information

.. _`ti_sci_msg_resp_get_clock_parent`:

struct ti_sci_msg_resp_get_clock_parent
=======================================

.. c:type:: struct ti_sci_msg_resp_get_clock_parent

    Response with clock parent

.. _`ti_sci_msg_resp_get_clock_parent.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_get_clock_parent {
        struct ti_sci_msg_hdr hdr;
        u8 parent_id;
    }

.. _`ti_sci_msg_resp_get_clock_parent.members`:

Members
-------

hdr
    Generic Header

parent_id
    The current clock parent

.. _`ti_sci_msg_resp_get_clock_parent.description`:

Description
-----------

Response to TI_SCI_MSG_GET_CLOCK_PARENT.

.. _`ti_sci_msg_req_get_clock_num_parents`:

struct ti_sci_msg_req_get_clock_num_parents
===========================================

.. c:type:: struct ti_sci_msg_req_get_clock_num_parents

    Request to get clock parents

.. _`ti_sci_msg_req_get_clock_num_parents.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_get_clock_num_parents {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_get_clock_num_parents.members`:

Members
-------

hdr
    Generic header

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.

.. _`ti_sci_msg_req_get_clock_num_parents.description`:

Description
-----------

This request provides information about how many clock parent options
are available for a given clock to a device. This is typically used
for input clocks.

Request type is TI_SCI_MSG_GET_NUM_CLOCK_PARENTS, response is appropriate
message, or NACK in case of inability to satisfy request.

.. _`ti_sci_msg_resp_get_clock_num_parents`:

struct ti_sci_msg_resp_get_clock_num_parents
============================================

.. c:type:: struct ti_sci_msg_resp_get_clock_num_parents

    Response for get clk parents

.. _`ti_sci_msg_resp_get_clock_num_parents.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_get_clock_num_parents {
        struct ti_sci_msg_hdr hdr;
        u8 num_parents;
    }

.. _`ti_sci_msg_resp_get_clock_num_parents.members`:

Members
-------

hdr
    Generic header

num_parents
    Number of clock parents

.. _`ti_sci_msg_resp_get_clock_num_parents.description`:

Description
-----------

Response to TI_SCI_MSG_GET_NUM_CLOCK_PARENTS

.. _`ti_sci_msg_req_query_clock_freq`:

struct ti_sci_msg_req_query_clock_freq
======================================

.. c:type:: struct ti_sci_msg_req_query_clock_freq

    Request to query a frequency

.. _`ti_sci_msg_req_query_clock_freq.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_query_clock_freq {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u64 min_freq_hz;
        u64 target_freq_hz;
        u64 max_freq_hz;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_query_clock_freq.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

min_freq_hz
    The minimum allowable frequency in Hz. This is the minimum
    allowable programmed frequency and does not account for clock
    tolerances and jitter.

target_freq_hz
    The target clock frequency. A frequency will be found
    as close to this target frequency as possible.

max_freq_hz
    The maximum allowable frequency in Hz. This is the maximum
    allowable programmed frequency and does not account for clock
    tolerances and jitter.

clk_id
    Clock identifier for the device for this request.

.. _`ti_sci_msg_req_query_clock_freq.note`:

NOTE
----

Normally clock frequency management is automatically done by TISCI
entity. In case of specific requests, TISCI evaluates capability to achieve
requested frequency within provided range and responds with
result message.

Request type is TI_SCI_MSG_QUERY_CLOCK_FREQ, response is appropriate message,
or NACK in case of inability to satisfy request.

.. _`ti_sci_msg_resp_query_clock_freq`:

struct ti_sci_msg_resp_query_clock_freq
=======================================

.. c:type:: struct ti_sci_msg_resp_query_clock_freq

    Response to a clock frequency query

.. _`ti_sci_msg_resp_query_clock_freq.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_query_clock_freq {
        struct ti_sci_msg_hdr hdr;
        u64 freq_hz;
    }

.. _`ti_sci_msg_resp_query_clock_freq.members`:

Members
-------

hdr
    Generic Header

freq_hz
    Frequency that is the best match in Hz.

.. _`ti_sci_msg_resp_query_clock_freq.description`:

Description
-----------

Response to request type TI_SCI_MSG_QUERY_CLOCK_FREQ. NOTE: if the request
cannot be satisfied, the message will be of type NACK.

.. _`ti_sci_msg_req_set_clock_freq`:

struct ti_sci_msg_req_set_clock_freq
====================================

.. c:type:: struct ti_sci_msg_req_set_clock_freq

    Request to setup a clock frequency

.. _`ti_sci_msg_req_set_clock_freq.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_set_clock_freq {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u64 min_freq_hz;
        u64 target_freq_hz;
        u64 max_freq_hz;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_set_clock_freq.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

min_freq_hz
    The minimum allowable frequency in Hz. This is the minimum
    allowable programmed frequency and does not account for clock
    tolerances and jitter.

target_freq_hz
    The target clock frequency. The clock will be programmed
    at a rate as close to this target frequency as possible.

max_freq_hz
    The maximum allowable frequency in Hz. This is the maximum
    allowable programmed frequency and does not account for clock
    tolerances and jitter.

clk_id
    Clock identifier for the device for this request.

.. _`ti_sci_msg_req_set_clock_freq.note`:

NOTE
----

Normally clock frequency management is automatically done by TISCI
entity. In case of specific requests, TISCI evaluates capability to achieve
requested range and responds with success/failure message.

This sets the desired frequency for a clock within an allowable
range. This message will fail on an enabled clock unless
MSG_FLAG_CLOCK_ALLOW_FREQ_CHANGE is set for the clock. Additionally,
if other clocks have their frequency modified due to this message,
they also must have the MSG_FLAG_CLOCK_ALLOW_FREQ_CHANGE or be disabled.

Calling set frequency on a clock input to the SoC pseudo-device will
inform the PMMC of that clock's frequency. Setting a frequency of
zero will indicate the clock is disabled.

Calling set frequency on clock outputs from the SoC pseudo-device will
function similarly to setting the clock frequency on a device.

Request type is TI_SCI_MSG_SET_CLOCK_FREQ, response is a generic ACK/NACK
message.

.. _`ti_sci_msg_req_get_clock_freq`:

struct ti_sci_msg_req_get_clock_freq
====================================

.. c:type:: struct ti_sci_msg_req_get_clock_freq

    Request to get the clock frequency

.. _`ti_sci_msg_req_get_clock_freq.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_req_get_clock_freq {
        struct ti_sci_msg_hdr hdr;
        u32 dev_id;
        u8 clk_id;
    }

.. _`ti_sci_msg_req_get_clock_freq.members`:

Members
-------

hdr
    Generic Header

dev_id
    Device identifier this request is for

clk_id
    Clock identifier for the device for this request.

.. _`ti_sci_msg_req_get_clock_freq.note`:

NOTE
----

Normally clock frequency management is automatically done by TISCI
entity. In some cases, clock frequencies are configured by host.

Request type is TI_SCI_MSG_GET_CLOCK_FREQ, responded with clock frequency
that the clock is currently at.

.. _`ti_sci_msg_resp_get_clock_freq`:

struct ti_sci_msg_resp_get_clock_freq
=====================================

.. c:type:: struct ti_sci_msg_resp_get_clock_freq

    Response of clock frequency request

.. _`ti_sci_msg_resp_get_clock_freq.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_msg_resp_get_clock_freq {
        struct ti_sci_msg_hdr hdr;
        u64 freq_hz;
    }

.. _`ti_sci_msg_resp_get_clock_freq.members`:

Members
-------

hdr
    Generic Header

freq_hz
    Frequency that the clock is currently on, in Hz.

.. _`ti_sci_msg_resp_get_clock_freq.description`:

Description
-----------

Response to request type TI_SCI_MSG_GET_CLOCK_FREQ.

.. This file was automatic generated / don't edit.


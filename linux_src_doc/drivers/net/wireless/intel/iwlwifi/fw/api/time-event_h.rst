.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/time-event.h

.. _`iwl_time_event_policy`:

enum iwl_time_event_policy
==========================

.. c:type:: enum iwl_time_event_policy

    Time event policy values A notification (both event and fragment) includes a status indicating weather the FW was able to schedule the event or not. For fragment start/end notification the status is always success. There is no start/end fragment notification for monolithic events.

.. _`iwl_time_event_policy.definition`:

Definition
----------

.. code-block:: c

    enum iwl_time_event_policy {
        TE_V2_DEFAULT_POLICY,
        TE_V2_NOTIF_HOST_EVENT_START,
        TE_V2_NOTIF_HOST_EVENT_END,
        TE_V2_NOTIF_INTERNAL_EVENT_START,
        TE_V2_NOTIF_INTERNAL_EVENT_END,
        TE_V2_NOTIF_HOST_FRAG_START,
        TE_V2_NOTIF_HOST_FRAG_END,
        TE_V2_NOTIF_INTERNAL_FRAG_START,
        TE_V2_NOTIF_INTERNAL_FRAG_END,
        T2_V2_START_IMMEDIATELY,
        TE_V2_DEP_OTHER,
        TE_V2_DEP_TSF,
        TE_V2_EVENT_SOCIOPATHIC,
        TE_V2_ABSENCE
    };

.. _`iwl_time_event_policy.constants`:

Constants
---------

TE_V2_DEFAULT_POLICY
    independent, social, present, unoticable

TE_V2_NOTIF_HOST_EVENT_START
    request/receive notification on event start

TE_V2_NOTIF_HOST_EVENT_END
    request/receive notification on event end

TE_V2_NOTIF_INTERNAL_EVENT_START
    internal FW use

TE_V2_NOTIF_INTERNAL_EVENT_END
    internal FW use.

TE_V2_NOTIF_HOST_FRAG_START
    request/receive notification on frag start

TE_V2_NOTIF_HOST_FRAG_END
    request/receive notification on frag end

TE_V2_NOTIF_INTERNAL_FRAG_START
    internal FW use.

TE_V2_NOTIF_INTERNAL_FRAG_END
    internal FW use.

T2_V2_START_IMMEDIATELY
    start time event immediately

TE_V2_DEP_OTHER
    depends on another time event

TE_V2_DEP_TSF
    depends on a specific time

TE_V2_EVENT_SOCIOPATHIC
    can't co-exist with other events of tha same MAC

TE_V2_ABSENCE
    are we present or absent during the Time Event.

.. _`iwl_time_event_cmd`:

struct iwl_time_event_cmd
=========================

.. c:type:: struct iwl_time_event_cmd

    configuring Time Events with struct MAC_TIME_EVENT_DATA_API_S_VER_2 (see also with version 1. determined by IWL_UCODE_TLV_FLAGS) ( TIME_EVENT_CMD = 0x29 )

.. _`iwl_time_event_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_cmd {
        __le32 id_and_color;
        __le32 action;
        __le32 id;
        __le32 apply_time;
        __le32 max_delay;
        __le32 depends_on;
        __le32 interval;
        __le32 duration;
        u8 repeat;
        u8 max_frags;
        __le16 policy;
    }

.. _`iwl_time_event_cmd.members`:

Members
-------

id_and_color
    ID and color of the relevant MAC,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

action
    action to perform, one of \ :c:type:`enum iwl_ctxt_action <iwl_ctxt_action>`\ 

id
    this field has two meanings, depending on the action:
    If the action is ADD, then it means the type of event to add.
    For all other actions it is the unique event ID assigned when the
    event was added by the FW.

apply_time
    When to start the Time Event (in GP2)

max_delay
    maximum delay to event's start (apply time), in TU

depends_on
    the unique ID of the event we depend on (if any)

interval
    interval between repetitions, in TU

duration
    duration of event in TU

repeat
    how many repetitions to do, can be TE_REPEAT_ENDLESS

max_frags
    maximal number of fragments the Time Event can be divided to

policy
    defines whether uCode shall notify the host or other uCode modules
    on event and/or fragment start and/or end
    using one of TE_INDEPENDENT, TE_DEP_OTHER, TE_DEP_TSF
    TE_EVENT_SOCIOPATHIC
    using TE_ABSENCE and using TE_NOTIF\_\*,
    \ :c:type:`enum iwl_time_event_policy <iwl_time_event_policy>`\ 

.. _`iwl_time_event_resp`:

struct iwl_time_event_resp
==========================

.. c:type:: struct iwl_time_event_resp

    response structure to iwl_time_event_cmd

.. _`iwl_time_event_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_resp {
        __le32 status;
        __le32 id;
        __le32 unique_id;
        __le32 id_and_color;
    }

.. _`iwl_time_event_resp.members`:

Members
-------

status
    bit 0 indicates success, all others specify errors

id
    the Time Event type

unique_id
    the unique ID assigned (in ADD) or given (others) to the TE

id_and_color
    ID and color of the relevant MAC,
    \ :c:type:`enum iwl_ctxt_id_and_color <iwl_ctxt_id_and_color>`\ 

.. _`iwl_time_event_notif`:

struct iwl_time_event_notif
===========================

.. c:type:: struct iwl_time_event_notif

    notifications of time event start/stop ( TIME_EVENT_NOTIFICATION = 0x2a )

.. _`iwl_time_event_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_time_event_notif {
        __le32 timestamp;
        __le32 session_id;
        __le32 unique_id;
        __le32 id_and_color;
        __le32 action;
        __le32 status;
    }

.. _`iwl_time_event_notif.members`:

Members
-------

timestamp
    action timestamp in GP2

session_id
    session's unique id

unique_id
    unique id of the Time Event itself

id_and_color
    ID and color of the relevant MAC

action
    &enum iwl_time_event_policy

status
    true if scheduled, false otherwise (not executed)

.. This file was automatic generated / don't edit.


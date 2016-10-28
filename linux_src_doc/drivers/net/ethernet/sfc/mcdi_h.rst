.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/mcdi.h

.. _`efx_mcdi_state`:

enum efx_mcdi_state
===================

.. c:type:: enum efx_mcdi_state

    MCDI request handling state

.. _`efx_mcdi_state.definition`:

Definition
----------

.. code-block:: c

    enum efx_mcdi_state {
        MCDI_STATE_QUIESCENT,
        MCDI_STATE_RUNNING_SYNC,
        MCDI_STATE_RUNNING_ASYNC,
        MCDI_STATE_PROXY_WAIT,
        MCDI_STATE_COMPLETED
    };

.. _`efx_mcdi_state.constants`:

Constants
---------

MCDI_STATE_QUIESCENT
    No pending MCDI requests. If the caller holds the
    mcdi \ ``iface_lock``\  then they are able to move to \ ``MCDI_STATE_RUNNING``\ 

MCDI_STATE_RUNNING_SYNC
    There is a synchronous MCDI request pending.
    Only the thread that moved into this state is allowed to move out of it.

MCDI_STATE_RUNNING_ASYNC
    There is an asynchronous MCDI request pending.

MCDI_STATE_PROXY_WAIT
    An MCDI request has completed with a response that
    indicates we must wait for a proxy try again message.

MCDI_STATE_COMPLETED
    An MCDI request has completed, but the owning thread
    has not yet consumed the result. For all other threads, equivalent to
    \ ``MCDI_STATE_RUNNING``\ .

.. _`efx_mcdi_mode`:

enum efx_mcdi_mode
==================

.. c:type:: enum efx_mcdi_mode

    MCDI transaction mode

.. _`efx_mcdi_mode.definition`:

Definition
----------

.. code-block:: c

    enum efx_mcdi_mode {
        MCDI_MODE_POLL,
        MCDI_MODE_EVENTS,
        MCDI_MODE_FAIL
    };

.. _`efx_mcdi_mode.constants`:

Constants
---------

MCDI_MODE_POLL
    poll for MCDI completion, until timeout

MCDI_MODE_EVENTS
    wait for an mcdi_event.  On timeout, poll once

MCDI_MODE_FAIL
    we think MCDI is dead, so fail-fast all calls

.. _`efx_mcdi_iface`:

struct efx_mcdi_iface
=====================

.. c:type:: struct efx_mcdi_iface

    MCDI protocol context

.. _`efx_mcdi_iface.definition`:

Definition
----------

.. code-block:: c

    struct efx_mcdi_iface {
        struct efx_nic *efx;
        enum efx_mcdi_state state;
        enum efx_mcdi_mode mode;
        wait_queue_head_t wq;
        spinlock_t iface_lock;
        bool new_epoch;
        unsigned int credits;
        unsigned int seqno;
        int resprc;
        int resprc_raw;
        size_t resp_hdr_len;
        size_t resp_data_len;
        spinlock_t async_lock;
        struct list_head async_list;
        struct timer_list async_timer;
    #ifdef CONFIG_SFC_MCDI_LOGGING
        char *logging_buffer;
        bool logging_enabled;
    #endif
        unsigned int proxy_rx_handle;
        int proxy_rx_status;
        wait_queue_head_t proxy_rx_wq;
    }

.. _`efx_mcdi_iface.members`:

Members
-------

efx
    The associated NIC.

state
    Request handling state. Waited for by \ ``wq``\ .

mode
    Poll for mcdi completion, or wait for an mcdi_event.

wq
    Wait queue for threads waiting for \ ``state``\  != \ ``MCDI_STATE_RUNNING``\ 

iface_lock
    Serialises access to \ ``seqno``\ , \ ``credits``\  and response metadata

new_epoch
    Indicates start of day or start of MC reboot recovery

credits
    Number of spurious MCDI completion events allowed before we
    trigger a fatal error

seqno
    The next sequence number to use for mcdi requests.

resprc
    Response error/success code (Linux numbering)

resprc_raw
    *undescribed*

resp_hdr_len
    Response header length

resp_data_len
    Response data (SDU or error) length

async_lock
    Serialises access to \ ``async_list``\  while event processing is
    enabled

async_list
    Queue of asynchronous requests

async_timer
    Timer for asynchronous request timeout

logging_buffer
    buffer that may be used to build MCDI tracing messages

logging_enabled
    whether to trace MCDI

proxy_rx_handle
    Most recently received proxy authorisation handle

proxy_rx_status
    Status of most recent proxy authorisation

proxy_rx_wq
    Wait queue for updates to proxy_rx_handle

.. _`efx_mcdi_data`:

struct efx_mcdi_data
====================

.. c:type:: struct efx_mcdi_data

    extra state for NICs that implement MCDI

.. _`efx_mcdi_data.definition`:

Definition
----------

.. code-block:: c

    struct efx_mcdi_data {
        struct efx_mcdi_iface iface;
    #ifdef CONFIG_SFC_MCDI_MON
        struct efx_mcdi_mon hwmon;
    #endif
        u32 fn_flags;
    }

.. _`efx_mcdi_data.members`:

Members
-------

iface
    Interface/protocol state

hwmon
    Hardware monitor state

fn_flags
    Flags for this function, as returned by \ ``MC_CMD_DRV_ATTACH``\ .

.. This file was automatic generated / don't edit.


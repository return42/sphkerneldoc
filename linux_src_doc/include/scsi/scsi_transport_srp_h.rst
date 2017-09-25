.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/scsi_transport_srp.h

.. _`srp_rport_state`:

enum srp_rport_state
====================

.. c:type:: enum srp_rport_state

    SRP transport layer state

.. _`srp_rport_state.definition`:

Definition
----------

.. code-block:: c

    enum srp_rport_state {
        SRP_RPORT_RUNNING,
        SRP_RPORT_BLOCKED,
        SRP_RPORT_FAIL_FAST,
        SRP_RPORT_LOST
    };

.. _`srp_rport_state.constants`:

Constants
---------

SRP_RPORT_RUNNING
    Transport layer operational.

SRP_RPORT_BLOCKED
    Transport layer not operational; fast I/O fail timer
    is running and I/O has been blocked.

SRP_RPORT_FAIL_FAST
    Fast I/O fail timer has expired; fail I/O fast.

SRP_RPORT_LOST
    Port is being removed.

.. _`srp_rport`:

struct srp_rport
================

.. c:type:: struct srp_rport

    SRP initiator or target port

.. _`srp_rport.definition`:

Definition
----------

.. code-block:: c

    struct srp_rport {
        struct device dev;
        u8 port_id[16];
        u8 roles;
        void *lld_data;
        struct mutex mutex;
        enum srp_rport_state state;
        int reconnect_delay;
        int failed_reconnects;
        struct delayed_work reconnect_work;
        int fast_io_fail_tmo;
        int dev_loss_tmo;
        struct delayed_work fast_io_fail_work;
        struct delayed_work dev_loss_work;
    }

.. _`srp_rport.members`:

Members
-------

dev
    Device associated with this rport.

port_id
    16-byte port identifier.

roles
    Role of this port - initiator or target.

lld_data
    LLD private data.

mutex
    Protects against concurrent rport reconnect /
    fast_io_fail / dev_loss_tmo activity.

state
    rport state.

reconnect_delay
    Reconnect delay in seconds.

failed_reconnects
    Number of failed reconnect attempts.

reconnect_work
    Work structure used for scheduling reconnect attempts.

fast_io_fail_tmo
    Fast I/O fail timeout in seconds.

dev_loss_tmo
    Device loss timeout in seconds.

fast_io_fail_work
    Work structure used for scheduling fast I/O fail work.

dev_loss_work
    Work structure used for scheduling device loss work.

.. _`srp_function_template`:

struct srp_function_template
============================

.. c:type:: struct srp_function_template


.. _`srp_function_template.definition`:

Definition
----------

.. code-block:: c

    struct srp_function_template {
        bool has_rport_state;
        bool reset_timer_if_blocked;
        int *reconnect_delay;
        int *fast_io_fail_tmo;
        int *dev_loss_tmo;
        int (*reconnect)(struct srp_rport *rport);
        void (*terminate_rport_io)(struct srp_rport *rport);
        void (*rport_delete)(struct srp_rport *rport);
    }

.. _`srp_function_template.members`:

Members
-------

has_rport_state
    Whether or not to create the state, fast_io_fail_tmo and
    dev_loss_tmo sysfs attribute for an rport.

reset_timer_if_blocked
    Whether or \ :c:func:`srp_timed_out`\  should reset the command
    timer if the device on which it has been queued is blocked.

reconnect_delay
    If not NULL, points to the default reconnect_delay value.

fast_io_fail_tmo
    If not NULL, points to the default fast_io_fail_tmo value.

dev_loss_tmo
    If not NULL, points to the default dev_loss_tmo value.

reconnect
    Callback function for reconnecting to the target. See also
    \ :c:func:`srp_reconnect_rport`\ .

terminate_rport_io
    Callback function for terminating all outstanding I/O
    requests for an rport.

rport_delete
    Callback function that deletes an rport.

.. _`srp_chkready`:

srp_chkready
============

.. c:function:: int srp_chkready(struct srp_rport *rport)

    evaluate the transport layer state before I/O

    :param struct srp_rport \*rport:
        SRP target port pointer.

.. _`srp_chkready.description`:

Description
-----------

Returns a SCSI result code that can be returned by the LLD \ :c:func:`queuecommand`\ 
implementation. The role of this function is similar to that of
\ :c:func:`fc_remote_port_chkready`\ .

.. This file was automatic generated / don't edit.


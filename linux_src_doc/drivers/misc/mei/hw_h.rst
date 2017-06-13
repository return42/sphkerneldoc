.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw.h

.. _`mei_hbm_status`:

enum mei_hbm_status
===================

.. c:type:: enum mei_hbm_status

    mei host bus messages return values

.. _`mei_hbm_status.definition`:

Definition
----------

.. code-block:: c

    enum mei_hbm_status {
        MEI_HBMS_SUCCESS,
        MEI_HBMS_CLIENT_NOT_FOUND,
        MEI_HBMS_ALREADY_EXISTS,
        MEI_HBMS_REJECTED,
        MEI_HBMS_INVALID_PARAMETER,
        MEI_HBMS_NOT_ALLOWED,
        MEI_HBMS_ALREADY_STARTED,
        MEI_HBMS_NOT_STARTED,
        MEI_HBMS_MAX
    };

.. _`mei_hbm_status.constants`:

Constants
---------

MEI_HBMS_SUCCESS
    status success

MEI_HBMS_CLIENT_NOT_FOUND
    client not found

MEI_HBMS_ALREADY_EXISTS
    connection already established

MEI_HBMS_REJECTED
    connection is rejected

MEI_HBMS_INVALID_PARAMETER
    invalid parameter

MEI_HBMS_NOT_ALLOWED
    operation not allowed

MEI_HBMS_ALREADY_STARTED
    system is already started

MEI_HBMS_NOT_STARTED
    system not started

MEI_HBMS_MAX
    sentinel

.. _`mei_hbm_cl_cmd`:

struct mei_hbm_cl_cmd
=====================

.. c:type:: struct mei_hbm_cl_cmd

    client specific host bus command CONNECT, DISCONNECT, and FlOW CONTROL

.. _`mei_hbm_cl_cmd.definition`:

Definition
----------

.. code-block:: c

    struct mei_hbm_cl_cmd {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 data;
    }

.. _`mei_hbm_cl_cmd.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    address of the client in the driver

data
    generic data

.. _`hbm_host_enum_flags`:

enum hbm_host_enum_flags
========================

.. c:type:: enum hbm_host_enum_flags

    enumeration request flags (HBM version >= 2.0)

.. _`hbm_host_enum_flags.definition`:

Definition
----------

.. code-block:: c

    enum hbm_host_enum_flags {
        MEI_HBM_ENUM_F_ALLOW_ADD,
        MEI_HBM_ENUM_F_IMMEDIATE_ENUM
    };

.. _`hbm_host_enum_flags.constants`:

Constants
---------

MEI_HBM_ENUM_F_ALLOW_ADD
    allow dynamic clients add

MEI_HBM_ENUM_F_IMMEDIATE_ENUM
    allow FW to send answer immediately

.. _`hbm_host_enum_request`:

struct hbm_host_enum_request
============================

.. c:type:: struct hbm_host_enum_request

    enumeration request from host to fw

.. _`hbm_host_enum_request.definition`:

Definition
----------

.. code-block:: c

    struct hbm_host_enum_request {
        u8 hbm_cmd;
        u8 flags;
        u8 reserved;
    }

.. _`hbm_host_enum_request.members`:

Members
-------

hbm_cmd
    bus message command header

flags
    request flags

reserved
    reserved

.. _`hbm_add_client_request`:

struct hbm_add_client_request
=============================

.. c:type:: struct hbm_add_client_request

    request to add a client might be sent by fw after enumeration has already completed

.. _`hbm_add_client_request.definition`:

Definition
----------

.. code-block:: c

    struct hbm_add_client_request {
        u8 hbm_cmd;
        u8 me_addr;
        u8 reserved;
        struct mei_client_properties client_properties;
    }

.. _`hbm_add_client_request.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

reserved
    reserved

client_properties
    client properties

.. _`hbm_add_client_response`:

struct hbm_add_client_response
==============================

.. c:type:: struct hbm_add_client_response

    response to add a client sent by the host to report client addition status to fw

.. _`hbm_add_client_response.definition`:

Definition
----------

.. code-block:: c

    struct hbm_add_client_response {
        u8 hbm_cmd;
        u8 me_addr;
        u8 status;
        u8 reserved;
    }

.. _`hbm_add_client_response.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

status
    if HBMS_SUCCESS then the client can now accept connections.

reserved
    reserved

.. _`hbm_power_gate`:

struct hbm_power_gate
=====================

.. c:type:: struct hbm_power_gate

    power gate request/response

.. _`hbm_power_gate.definition`:

Definition
----------

.. code-block:: c

    struct hbm_power_gate {
        u8 hbm_cmd;
        u8 reserved;
    }

.. _`hbm_power_gate.members`:

Members
-------

hbm_cmd
    bus message command header

reserved
    reserved

.. _`hbm_client_connect_request`:

struct hbm_client_connect_request
=================================

.. c:type:: struct hbm_client_connect_request

    connect/disconnect request

.. _`hbm_client_connect_request.definition`:

Definition
----------

.. code-block:: c

    struct hbm_client_connect_request {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 reserved;
    }

.. _`hbm_client_connect_request.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    address of the client in the driver

reserved
    reserved

.. _`hbm_client_connect_response`:

struct hbm_client_connect_response
==================================

.. c:type:: struct hbm_client_connect_response

    connect/disconnect response

.. _`hbm_client_connect_response.definition`:

Definition
----------

.. code-block:: c

    struct hbm_client_connect_response {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 status;
    }

.. _`hbm_client_connect_response.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    address of the client in the driver

status
    status of the request

.. _`hbm_notification_request`:

struct hbm_notification_request
===============================

.. c:type:: struct hbm_notification_request

    start/stop notification request

.. _`hbm_notification_request.definition`:

Definition
----------

.. code-block:: c

    struct hbm_notification_request {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 start;
    }

.. _`hbm_notification_request.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    address of the client in the driver

start
    start = 1 or stop = 0 asynchronous notifications

.. _`hbm_notification_response`:

struct hbm_notification_response
================================

.. c:type:: struct hbm_notification_response

    start/stop notification response

.. _`hbm_notification_response.definition`:

Definition
----------

.. code-block:: c

    struct hbm_notification_response {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 status;
        u8 start;
        u8 reserved;
    }

.. _`hbm_notification_response.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    - address of the client in the driver

status
    (mei_hbm_status) response status for the request
    - MEI_HBMS_SUCCESS: successful stop/start
    - MEI_HBMS_CLIENT_NOT_FOUND: if the connection could not be found.
    - MEI_HBMS_ALREADY_STARTED: for start requests for a previously
    started notification.
    - MEI_HBMS_NOT_STARTED: for stop request for a connected client for whom
    asynchronous notifications are currently disabled.

start
    start = 1 or stop = 0 asynchronous notifications

reserved
    reserved

.. _`hbm_notification`:

struct hbm_notification
=======================

.. c:type:: struct hbm_notification

    notification event

.. _`hbm_notification.definition`:

Definition
----------

.. code-block:: c

    struct hbm_notification {
        u8 hbm_cmd;
        u8 me_addr;
        u8 host_addr;
        u8 reserved;
    }

.. _`hbm_notification.members`:

Members
-------

hbm_cmd
    bus message command header

me_addr
    address of the client in ME

host_addr
    address of the client in the driver

reserved
    reserved for alignment

.. This file was automatic generated / don't edit.


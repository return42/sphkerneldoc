.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/hbm.h

.. _`ishtp_hbm_cl_cmd`:

struct ishtp_hbm_cl_cmd
=======================

.. c:type:: struct ishtp_hbm_cl_cmd

    client specific host bus command CONNECT, DISCONNECT, and FlOW CONTROL

.. _`ishtp_hbm_cl_cmd.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_hbm_cl_cmd {
        uint8_t hbm_cmd;
        uint8_t fw_addr;
        uint8_t host_addr;
        uint8_t data;
    }

.. _`ishtp_hbm_cl_cmd.members`:

Members
-------

hbm_cmd
    *undescribed*

fw_addr
    *undescribed*

host_addr
    *undescribed*

data
    *undescribed*

.. _`ishtp_hbm_cl_cmd.description`:

Description
-----------

@hbm_cmd - bus message command header
\ ``fw_addr``\  - address of the fw client
\ ``host_addr``\  - address of the client in the driver
\ ``data``\ 

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
        uint8_t hbm_cmd;
        uint8_t fw_addr;
        uint8_t host_addr;
        uint8_t reserved;
    }

.. _`hbm_client_connect_request.members`:

Members
-------

hbm_cmd
    *undescribed*

fw_addr
    *undescribed*

host_addr
    *undescribed*

reserved
    *undescribed*

.. _`hbm_client_connect_request.description`:

Description
-----------

@hbm_cmd - bus message command header
\ ``fw_addr``\  - address of the fw client
\ ``host_addr``\  - address of the client in the driver
\ ``reserved``\ 

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
        uint8_t hbm_cmd;
        uint8_t fw_addr;
        uint8_t host_addr;
        uint8_t status;
    }

.. _`hbm_client_connect_response.members`:

Members
-------

hbm_cmd
    *undescribed*

fw_addr
    *undescribed*

host_addr
    *undescribed*

status
    *undescribed*

.. _`hbm_client_connect_response.description`:

Description
-----------

@hbm_cmd - bus message command header
\ ``fw_addr``\  - address of the fw client
\ ``host_addr``\  - address of the client in the driver
\ ``status``\  - status of the request

.. _`ishtp_hbm_state`:

enum ishtp_hbm_state
====================

.. c:type:: enum ishtp_hbm_state

    host bus message protocol state

.. _`ishtp_hbm_state.definition`:

Definition
----------

.. code-block:: c

    enum ishtp_hbm_state {
        ISHTP_HBM_IDLE,
        ISHTP_HBM_START,
        ISHTP_HBM_STARTED,
        ISHTP_HBM_ENUM_CLIENTS,
        ISHTP_HBM_CLIENT_PROPERTIES,
        ISHTP_HBM_WORKING,
        ISHTP_HBM_STOPPED
    };

.. _`ishtp_hbm_state.constants`:

Constants
---------

ISHTP_HBM_IDLE
    protocol not started

ISHTP_HBM_START
    start request message was sent

ISHTP_HBM_STARTED
    *undescribed*

ISHTP_HBM_ENUM_CLIENTS
    enumeration request was sent

ISHTP_HBM_CLIENT_PROPERTIES
    acquiring clients properties

ISHTP_HBM_WORKING
    *undescribed*

ISHTP_HBM_STOPPED
    *undescribed*

.. This file was automatic generated / don't edit.


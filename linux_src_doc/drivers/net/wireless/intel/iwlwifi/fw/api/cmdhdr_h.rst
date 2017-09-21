.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/cmdhdr.h

.. _`host-command-section`:

Host command section
====================

A host command is a command issued by the upper layer to the fw. There are
several versions of fw that have several APIs. The transport layer is
completely agnostic to these differences.
The transport does provide helper functionality (i.e. SYNC / ASYNC mode),

.. _`iwl_cmd_header`:

struct iwl_cmd_header
=====================

.. c:type:: struct iwl_cmd_header

    (short) command header format

.. _`iwl_cmd_header.definition`:

Definition
----------

.. code-block:: c

    struct iwl_cmd_header {
        u8 cmd;
        u8 group_id;
        __le16 sequence;
    }

.. _`iwl_cmd_header.members`:

Members
-------

cmd
    Command ID: REPLY_RXON, etc.

group_id
    group ID, for commands with groups

sequence
    Sequence number for the command.

    The driver sets up the sequence number to values of its choosing.
    uCode does not use this value, but passes it back to the driver
    when sending the response to each driver-originated command, so
    the driver can match the response to the command.  Since the values
    don't get used by uCode, the driver may set up an arbitrary format.

    There is one exception:  uCode sets bit 15 when it originates
    the response/notification, i.e. when the response/notification
    is not a direct response to a command sent by the driver.  For
    example, uCode issues REPLY_RX when it sends a received frame
    to the driver; it is not a direct response to any driver command.

    The Linux driver uses the following format:

    0:7         tfd index - position within TX queue
    8:12        TX queue id
    13:14       reserved
    15          unsolicited RX or uCode-originated notification

.. _`iwl_cmd_header.description`:

Description
-----------

This header format appears in the beginning of each command sent from the
driver, and each response/notification received from uCode.

.. _`iwl_cmd_header_wide`:

struct iwl_cmd_header_wide
==========================

.. c:type:: struct iwl_cmd_header_wide


.. _`iwl_cmd_header_wide.definition`:

Definition
----------

.. code-block:: c

    struct iwl_cmd_header_wide {
        u8 cmd;
        u8 group_id;
        __le16 sequence;
        __le16 length;
        u8 reserved;
        u8 version;
    }

.. _`iwl_cmd_header_wide.members`:

Members
-------

cmd
    command ID, like in \ :c:type:`struct iwl_cmd_header <iwl_cmd_header>`\ 

group_id
    group ID, like in \ :c:type:`struct iwl_cmd_header <iwl_cmd_header>`\ 

sequence
    sequence, like in \ :c:type:`struct iwl_cmd_header <iwl_cmd_header>`\ 

length
    length of the command

reserved
    reserved

version
    command version

.. _`iwl_cmd_header_wide.description`:

Description
-----------

This header format appears in the beginning of each command sent from the
driver, and each response/notification received from uCode.
this is the wide version that contains more information about the command
like length, version and command type

.. _`iwl_calib_res_notif_phy_db`:

struct iwl_calib_res_notif_phy_db
=================================

.. c:type:: struct iwl_calib_res_notif_phy_db

    Receive phy db chunk after calibrations

.. _`iwl_calib_res_notif_phy_db.definition`:

Definition
----------

.. code-block:: c

    struct iwl_calib_res_notif_phy_db {
        __le16 type;
        __le16 length;
        u8 data;
    }

.. _`iwl_calib_res_notif_phy_db.members`:

Members
-------

type
    type of the result - mostly ignored

length
    length of the data

data
    data, length in \ ``length``\ 

.. _`iwl_phy_db_cmd`:

struct iwl_phy_db_cmd
=====================

.. c:type:: struct iwl_phy_db_cmd

    configure operational ucode

.. _`iwl_phy_db_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_phy_db_cmd {
        __le16 type;
        __le16 length;
        u8 data;
    }

.. _`iwl_phy_db_cmd.members`:

Members
-------

type
    type of the data

length
    length of the data

data
    data, length in \ ``length``\ 

.. _`iwl_cmd_response`:

struct iwl_cmd_response
=======================

.. c:type:: struct iwl_cmd_response

    generic response struct for most commands

.. _`iwl_cmd_response.definition`:

Definition
----------

.. code-block:: c

    struct iwl_cmd_response {
        __le32 status;
    }

.. _`iwl_cmd_response.members`:

Members
-------

status
    status of the command asked, changes for each one

.. This file was automatic generated / don't edit.


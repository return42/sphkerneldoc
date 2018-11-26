.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/netconsole.c

.. _`netconsole_target`:

struct netconsole_target
========================

.. c:type:: struct netconsole_target

    Represents a configured netconsole target.

.. _`netconsole_target.definition`:

Definition
----------

.. code-block:: c

    struct netconsole_target {
        struct list_head list;
    #ifdef CONFIG_NETCONSOLE_DYNAMIC
        struct config_item item;
    #endif
        bool enabled;
        bool extended;
        struct netpoll np;
    }

.. _`netconsole_target.members`:

Members
-------

list
    Links this target into the target_list.

item
    Links us into the configfs subsystem hierarchy.

enabled
    On / off knob to enable / disable target.
    Visible from userspace (read-write).
    We maintain a strict 1:1 correspondence between this and
    whether the corresponding netpoll is active or inactive.
    Also, other parameters of a target may be modified at
    runtime only when it is disabled (enabled == 0).

extended
    *undescribed*

np
    The netpoll structure for this target.
    Contains the other userspace visible parameters:
    dev_name        (read-write)
    local_port      (read-write)
    remote_port     (read-write)
    local_ip        (read-write)
    remote_ip       (read-write)
    local_mac       (read-only)
    remote_mac      (read-write)

.. _`send_ext_msg_udp`:

send_ext_msg_udp
================

.. c:function:: void send_ext_msg_udp(struct netconsole_target *nt, const char *msg, int msg_len)

    send extended log message to target

    :param nt:
        target to send message to
    :type nt: struct netconsole_target \*

    :param msg:
        extended log message to send
    :type msg: const char \*

    :param msg_len:
        length of message
    :type msg_len: int

.. _`send_ext_msg_udp.description`:

Description
-----------

Transfer extended log \ ``msg``\  to \ ``nt``\ .  If \ ``msg``\  is longer than
MAX_PRINT_CHUNK, it'll be split and transmitted in multiple chunks with
ncfrag header field added to identify them.

.. This file was automatic generated / don't edit.


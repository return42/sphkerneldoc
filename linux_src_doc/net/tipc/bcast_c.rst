.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/bcast.c

.. _`tipc_bc_base`:

struct tipc_bc_base
===================

.. c:type:: struct tipc_bc_base

    base structure for keeping broadcast send state

.. _`tipc_bc_base.definition`:

Definition
----------

.. code-block:: c

    struct tipc_bc_base {
        struct tipc_link *link;
        struct sk_buff_head inputq;
        int dests[MAX_BEARERS];
        int primary_bearer;
    }

.. _`tipc_bc_base.members`:

Members
-------

link
    broadcast send link structure

inputq
    data input queue; will only carry SOCK_WAKEUP messages

primary_bearer
    a bearer having links to all broadcast destinations, if any

.. This file was automatic generated / don't edit.


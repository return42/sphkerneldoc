.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/can/core.h

.. _`can_proto`:

struct can_proto
================

.. c:type:: struct can_proto

    CAN protocol structure

.. _`can_proto.definition`:

Definition
----------

.. code-block:: c

    struct can_proto {
        int type;
        int protocol;
        const struct proto_ops *ops;
        struct proto *prot;
    }

.. _`can_proto.members`:

Members
-------

type
    type argument in \ :c:func:`socket`\  syscall, e.g. SOCK_DGRAM.

protocol
    protocol number in \ :c:func:`socket`\  syscall.

ops
    pointer to struct proto_ops for sock->ops.

prot
    pointer to struct proto structure.

.. This file was automatic generated / don't edit.


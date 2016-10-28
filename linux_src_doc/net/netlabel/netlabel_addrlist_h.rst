.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_addrlist.h

.. _`netlbl_af4list`:

struct netlbl_af4list
=====================

.. c:type:: struct netlbl_af4list

    NetLabel IPv4 address list

.. _`netlbl_af4list.definition`:

Definition
----------

.. code-block:: c

    struct netlbl_af4list {
        __be32 addr;
        __be32 mask;
        u32 valid;
        struct list_head list;
    }

.. _`netlbl_af4list.members`:

Members
-------

addr
    IPv4 address

mask
    IPv4 address mask

valid
    valid flag

list
    list structure, used internally

.. _`netlbl_af6list`:

struct netlbl_af6list
=====================

.. c:type:: struct netlbl_af6list

    NetLabel IPv6 address list

.. _`netlbl_af6list.definition`:

Definition
----------

.. code-block:: c

    struct netlbl_af6list {
        struct in6_addr addr;
        struct in6_addr mask;
        u32 valid;
        struct list_head list;
    }

.. _`netlbl_af6list.members`:

Members
-------

addr
    IPv6 address

mask
    IPv6 address mask

valid
    valid flag

list
    list structure, used internally

.. This file was automatic generated / don't edit.


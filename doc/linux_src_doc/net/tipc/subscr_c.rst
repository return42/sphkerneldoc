.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/subscr.c

.. _`tipc_subscriber`:

struct tipc_subscriber
======================

.. c:type:: struct tipc_subscriber

    TIPC network topology subscriber

.. _`tipc_subscriber.definition`:

Definition
----------

.. code-block:: c

    struct tipc_subscriber {
        struct kref kref;
        int conid;
        spinlock_t lock;
        struct list_head subscrp_list;
    }

.. _`tipc_subscriber.members`:

Members
-------

kref
    reference counter to tipc_subscription object

conid
    connection identifier to server connecting to subscriber

lock
    control access to subscriber

subscrp_list
    list of subscription objects for this subscriber

.. _`htohl`:

htohl
=====

.. c:function:: u32 htohl(u32 in, int swap)

    convert value to endianness used by destination

    :param u32 in:
        value to convert

    :param int swap:
        non-zero if endianness must be reversed

.. _`htohl.description`:

Description
-----------

Returns converted value

.. _`tipc_subscrp_check_overlap`:

tipc_subscrp_check_overlap
==========================

.. c:function:: int tipc_subscrp_check_overlap(struct tipc_name_seq *seq, u32 found_lower, u32 found_upper)

    test for subscription overlap with the given values

    :param struct tipc_name_seq \*seq:
        *undescribed*

    :param u32 found_lower:
        *undescribed*

    :param u32 found_upper:
        *undescribed*

.. _`tipc_subscrp_check_overlap.description`:

Description
-----------

Returns 1 if there is overlap, otherwise 0.

.. This file was automatic generated / don't edit.


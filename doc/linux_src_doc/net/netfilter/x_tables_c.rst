.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netfilter/x_tables.c

.. _`xt_check_entry_offsets`:

xt_check_entry_offsets
======================

.. c:function:: int xt_check_entry_offsets(const void *base, const char *elems, unsigned int target_offset, unsigned int next_offset)

    validate arp/ip/ip6t_entry

    :param const void \*base:
        pointer to arp/ip/ip6t_entry

    :param const char \*elems:
        pointer to first xt_entry_match, i.e. ip(6)t_entry->elems

    :param unsigned int target_offset:
        the arp/ip/ip6_t->target_offset

    :param unsigned int next_offset:
        the arp/ip/ip6_t->next_offset

.. _`xt_check_entry_offsets.description`:

Description
-----------

validates that target_offset and next_offset are sane and that all
match sizes (if any) align with the target offset.

This function does not validate the targets or matches themselves, it
only tests that all the offsets and sizes are correct, that all
match structures are aligned, and that the last structure ends where
the target structure begins.

Also see xt_compat_check_entry_offsets for CONFIG_COMPAT version.

The arp/ip/ip6t_entry structure \ ``base``\  must have passed following tests:
- it must point to a valid memory location
- base to base + next_offset must be accessible, i.e. not exceed allocated
length.

A well-formed entry looks like this:

ip(6)t_entry   match [mtdata]  match [mtdata] target [tgdata] ip(6)t_entry
e->elems[]-----'                              \|               \|
matchsize                      \|               \|
matchsize      \|               \|
\|               \|
target_offset---------------------------------'               \|
next_offset---------------------------------------------------'

elems[]: flexible array member at end of ip(6)/arpt_entry struct.
This is where matches (if any) and the target reside.

.. _`xt_check_entry_offsets.target_offset`:

target_offset
-------------

beginning of target.

.. _`xt_check_entry_offsets.next_offset`:

next_offset
-----------

start of the next rule; also: size of this rule.
Since targets have a minimum size, target_offset + minlen <= next_offset.

Every match stores its size, sum of sizes must not exceed target_offset.

.. _`xt_check_entry_offsets.return`:

Return
------

0 on success, negative errno on failure.

.. _`xt_copy_counters_from_user`:

xt_copy_counters_from_user
==========================

.. c:function:: void *xt_copy_counters_from_user(const void __user *user, unsigned int len, struct xt_counters_info *info, bool compat)

    copy counters and metadata from userspace

    :param const void __user \*user:
        src pointer to userspace memory

    :param unsigned int len:
        alleged size of userspace memory

    :param struct xt_counters_info \*info:
        where to store the xt_counters_info metadata

    :param bool compat:
        true if we setsockopt call is done by 32bit task on 64bit kernel

.. _`xt_copy_counters_from_user.description`:

Description
-----------

Copies counter meta data from \ ``user``\  and stores it in \ ``info``\ .

vmallocs memory to hold the counters, then copies the counter data
from \ ``user``\  to the new memory and returns a pointer to it.

If \ ``compat``\  is true, \ ``info``\  gets converted automatically to the 64bit
representation.

The metadata associated with the counters is stored in \ ``info``\ .

.. _`xt_copy_counters_from_user.return`:

Return
------

returns pointer that caller has to test via \ :c:func:`IS_ERR`\ .
If IS_ERR is false, caller has to vfree the pointer.

.. _`xt_hook_ops_alloc`:

xt_hook_ops_alloc
=================

.. c:function:: struct nf_hook_ops *xt_hook_ops_alloc(const struct xt_table *table, nf_hookfn *fn)

    set up hooks for a new table

    :param const struct xt_table \*table:
        table with metadata needed to set up hooks

    :param nf_hookfn \*fn:
        Hook function

.. _`xt_hook_ops_alloc.description`:

Description
-----------

This function will create the nf_hook_ops that the x_table needs
to hand to \ :c:func:`xt_hook_link_net`\ .

.. This file was automatic generated / don't edit.


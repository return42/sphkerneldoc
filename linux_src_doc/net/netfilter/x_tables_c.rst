.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netfilter/x_tables.c

.. _`xt_check_proc_name`:

xt_check_proc_name
==================

.. c:function:: int xt_check_proc_name(const char *name, unsigned int size)

    check that name is suitable for /proc file creation

    :param name:
        file name candidate
    :type name: const char \*

    :param size:
        length of buffer
    :type size: unsigned int

.. _`xt_check_proc_name.description`:

Description
-----------

some x_tables modules wish to create a file in /proc.
This function makes sure that the name is suitable for this
purpose, it checks that name is NUL terminated and isn't a 'special'
name, like "..".

returns negative number on error or 0 if name is useable.

.. _`xt_check_entry_offsets`:

xt_check_entry_offsets
======================

.. c:function:: int xt_check_entry_offsets(const void *base, const char *elems, unsigned int target_offset, unsigned int next_offset)

    validate arp/ip/ip6t_entry

    :param base:
        pointer to arp/ip/ip6t_entry
    :type base: const void \*

    :param elems:
        pointer to first xt_entry_match, i.e. ip(6)t_entry->elems
    :type elems: const char \*

    :param target_offset:
        the arp/ip/ip6_t->target_offset
    :type target_offset: unsigned int

    :param next_offset:
        the arp/ip/ip6_t->next_offset
    :type next_offset: unsigned int

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

.. _`xt_alloc_entry_offsets`:

xt_alloc_entry_offsets
======================

.. c:function:: unsigned int *xt_alloc_entry_offsets(unsigned int size)

    allocate array to store rule head offsets

    :param size:
        number of entries
    :type size: unsigned int

.. _`xt_alloc_entry_offsets.return`:

Return
------

NULL or kmalloc'd or vmalloc'd array

.. _`xt_find_jump_offset`:

xt_find_jump_offset
===================

.. c:function:: bool xt_find_jump_offset(const unsigned int *offsets, unsigned int target, unsigned int size)

    check if target is a valid jump offset

    :param offsets:
        array containing all valid rule start offsets of a rule blob
    :type offsets: const unsigned int \*

    :param target:
        the jump target to search for
    :type target: unsigned int

    :param size:
        entries in \ ``offset``\ 
    :type size: unsigned int

.. _`xt_copy_counters_from_user`:

xt_copy_counters_from_user
==========================

.. c:function:: void *xt_copy_counters_from_user(const void __user *user, unsigned int len, struct xt_counters_info *info, bool compat)

    copy counters and metadata from userspace

    :param user:
        src pointer to userspace memory
    :type user: const void __user \*

    :param len:
        alleged size of userspace memory
    :type len: unsigned int

    :param info:
        where to store the xt_counters_info metadata
    :type info: struct xt_counters_info \*

    :param compat:
        true if we setsockopt call is done by 32bit task on 64bit kernel
    :type compat: bool

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

    :param table:
        table with metadata needed to set up hooks
    :type table: const struct xt_table \*

    :param fn:
        Hook function
    :type fn: nf_hookfn \*

.. _`xt_hook_ops_alloc.description`:

Description
-----------

This function will create the nf_hook_ops that the x_table needs
to hand to \ :c:func:`xt_hook_link_net`\ .

.. _`xt_percpu_counter_alloc`:

xt_percpu_counter_alloc
=======================

.. c:function:: bool xt_percpu_counter_alloc(struct xt_percpu_counter_alloc_state *state, struct xt_counters *counter)

    allocate x_tables rule counter

    :param state:
        pointer to xt_percpu allocation state
    :type state: struct xt_percpu_counter_alloc_state \*

    :param counter:
        pointer to counter struct inside the ip(6)/arpt_entry struct
    :type counter: struct xt_counters \*

.. _`xt_percpu_counter_alloc.description`:

Description
-----------

On SMP, the packet counter [ ip(6)t_entry->counters.pcnt ] will then
contain the address of the real (percpu) counter.

Rule evaluation needs to use \ :c:func:`xt_get_this_cpu_counter`\  helper
to fetch the real percpu counter.

To speed up allocation and improve data locality, a 4kb block is
allocated.  Freeing any counter may free an entire block, so all
counters allocated using the same state must be freed at the same
time.

xt_percpu_counter_alloc_state contains the base address of the
allocated page and the current sub-offset.

returns false on error.

.. This file was automatic generated / don't edit.


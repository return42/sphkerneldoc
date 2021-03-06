.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpumask.h

.. _`cpumask_bits`:

cpumask_bits
============

.. c:function::  cpumask_bits( maskp)

    get the bits in a cpumask

    :param maskp:
        the struct cpumask \*
    :type maskp: 

.. _`cpumask_bits.description`:

Description
-----------

You should only assume nr_cpu_ids bits of this mask are valid.  This is
a macro so it's const-correct.

.. _`cpumask_pr_args`:

cpumask_pr_args
===============

.. c:function::  cpumask_pr_args( maskp)

    printf args to output a cpumask

    :param maskp:
        cpumask to be printed
    :type maskp: 

.. _`cpumask_pr_args.description`:

Description
-----------

Can be used to provide arguments for '%\*pb[l]' when printing a cpumask.

.. _`cpumask_first`:

cpumask_first
=============

.. c:function:: unsigned int cpumask_first(const struct cpumask *srcp)

    get the first cpu in a cpumask

    :param srcp:
        the cpumask pointer
    :type srcp: const struct cpumask \*

.. _`cpumask_first.description`:

Description
-----------

Returns >= nr_cpu_ids if no cpus set.

.. _`cpumask_last`:

cpumask_last
============

.. c:function:: unsigned int cpumask_last(const struct cpumask *srcp)

    get the last CPU in a cpumask

    :param srcp:
        - the cpumask pointer
    :type srcp: const struct cpumask \*

.. _`cpumask_last.description`:

Description
-----------

Returns      >= nr_cpumask_bits if no CPUs set.

.. _`cpumask_next_zero`:

cpumask_next_zero
=================

.. c:function:: unsigned int cpumask_next_zero(int n, const struct cpumask *srcp)

    get the next unset cpu in a cpumask

    :param n:
        the cpu prior to the place to search (ie. return will be > \ ``n``\ )
    :type n: int

    :param srcp:
        the cpumask pointer
    :type srcp: const struct cpumask \*

.. _`cpumask_next_zero.description`:

Description
-----------

Returns >= nr_cpu_ids if no further cpus unset.

.. _`for_each_cpu`:

for_each_cpu
============

.. c:function::  for_each_cpu( cpu,  mask)

    iterate over every cpu in a mask

    :param cpu:
        the (optionally unsigned) integer iterator
    :type cpu: 

    :param mask:
        the cpumask pointer
    :type mask: 

.. _`for_each_cpu.description`:

Description
-----------

After the loop, cpu is >= nr_cpu_ids.

.. _`for_each_cpu_not`:

for_each_cpu_not
================

.. c:function::  for_each_cpu_not( cpu,  mask)

    iterate over every cpu in a complemented mask

    :param cpu:
        the (optionally unsigned) integer iterator
    :type cpu: 

    :param mask:
        the cpumask pointer
    :type mask: 

.. _`for_each_cpu_not.description`:

Description
-----------

After the loop, cpu is >= nr_cpu_ids.

.. _`for_each_cpu_wrap`:

for_each_cpu_wrap
=================

.. c:function::  for_each_cpu_wrap( cpu,  mask,  start)

    iterate over every cpu in a mask, starting at a specified location

    :param cpu:
        the (optionally unsigned) integer iterator
    :type cpu: 

    :param mask:
        the cpumask poiter
    :type mask: 

    :param start:
        the start location
    :type start: 

.. _`for_each_cpu_wrap.description`:

Description
-----------

The implementation does not assume any bit in \ ``mask``\  is set (including \ ``start``\ ).

After the loop, cpu is >= nr_cpu_ids.

.. _`for_each_cpu_and`:

for_each_cpu_and
================

.. c:function::  for_each_cpu_and( cpu,  mask,  and)

    iterate over every cpu in both masks

    :param cpu:
        the (optionally unsigned) integer iterator
    :type cpu: 

    :param mask:
        the first cpumask pointer
    :type mask: 

    :param and:
        the second cpumask pointer
    :type and: 

.. _`for_each_cpu_and.description`:

Description
-----------

This saves a temporary CPU mask in many places.  It is equivalent to:
struct cpumask tmp;
cpumask_and(&tmp, \ :c:type:`struct mask <mask>`\ , \ :c:type:`struct and <and>`\ );
for_each_cpu(cpu, \ :c:type:`struct tmp <tmp>`\ )
...

After the loop, cpu is >= nr_cpu_ids.

.. _`cpumask_set_cpu`:

cpumask_set_cpu
===============

.. c:function:: void cpumask_set_cpu(unsigned int cpu, struct cpumask *dstp)

    set a cpu in a cpumask

    :param cpu:
        cpu number (< nr_cpu_ids)
    :type cpu: unsigned int

    :param dstp:
        the cpumask pointer
    :type dstp: struct cpumask \*

.. _`cpumask_clear_cpu`:

cpumask_clear_cpu
=================

.. c:function:: void cpumask_clear_cpu(int cpu, struct cpumask *dstp)

    clear a cpu in a cpumask

    :param cpu:
        cpu number (< nr_cpu_ids)
    :type cpu: int

    :param dstp:
        the cpumask pointer
    :type dstp: struct cpumask \*

.. _`cpumask_test_cpu`:

cpumask_test_cpu
================

.. c:function:: int cpumask_test_cpu(int cpu, const struct cpumask *cpumask)

    test for a cpu in a cpumask

    :param cpu:
        cpu number (< nr_cpu_ids)
    :type cpu: int

    :param cpumask:
        the cpumask pointer
    :type cpumask: const struct cpumask \*

.. _`cpumask_test_cpu.description`:

Description
-----------

Returns 1 if \ ``cpu``\  is set in \ ``cpumask``\ , else returns 0

.. _`cpumask_test_and_set_cpu`:

cpumask_test_and_set_cpu
========================

.. c:function:: int cpumask_test_and_set_cpu(int cpu, struct cpumask *cpumask)

    atomically test and set a cpu in a cpumask

    :param cpu:
        cpu number (< nr_cpu_ids)
    :type cpu: int

    :param cpumask:
        the cpumask pointer
    :type cpumask: struct cpumask \*

.. _`cpumask_test_and_set_cpu.description`:

Description
-----------

Returns 1 if \ ``cpu``\  is set in old bitmap of \ ``cpumask``\ , else returns 0

test_and_set_bit wrapper for cpumasks.

.. _`cpumask_test_and_clear_cpu`:

cpumask_test_and_clear_cpu
==========================

.. c:function:: int cpumask_test_and_clear_cpu(int cpu, struct cpumask *cpumask)

    atomically test and clear a cpu in a cpumask

    :param cpu:
        cpu number (< nr_cpu_ids)
    :type cpu: int

    :param cpumask:
        the cpumask pointer
    :type cpumask: struct cpumask \*

.. _`cpumask_test_and_clear_cpu.description`:

Description
-----------

Returns 1 if \ ``cpu``\  is set in old bitmap of \ ``cpumask``\ , else returns 0

test_and_clear_bit wrapper for cpumasks.

.. _`cpumask_setall`:

cpumask_setall
==============

.. c:function:: void cpumask_setall(struct cpumask *dstp)

    set all cpus (< nr_cpu_ids) in a cpumask

    :param dstp:
        the cpumask pointer
    :type dstp: struct cpumask \*

.. _`cpumask_clear`:

cpumask_clear
=============

.. c:function:: void cpumask_clear(struct cpumask *dstp)

    clear all cpus (< nr_cpu_ids) in a cpumask

    :param dstp:
        the cpumask pointer
    :type dstp: struct cpumask \*

.. _`cpumask_and`:

cpumask_and
===========

.. c:function:: int cpumask_and(struct cpumask *dstp, const struct cpumask *src1p, const struct cpumask *src2p)

    \*dstp = \*src1p & \*src2p

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_and.description`:

Description
-----------

If \*@dstp is empty, returns 0, else returns 1

.. _`cpumask_or`:

cpumask_or
==========

.. c:function:: void cpumask_or(struct cpumask *dstp, const struct cpumask *src1p, const struct cpumask *src2p)

    \*dstp = \*src1p \| \*src2p

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_xor`:

cpumask_xor
===========

.. c:function:: void cpumask_xor(struct cpumask *dstp, const struct cpumask *src1p, const struct cpumask *src2p)

    \*dstp = \*src1p ^ \*src2p

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_andnot`:

cpumask_andnot
==============

.. c:function:: int cpumask_andnot(struct cpumask *dstp, const struct cpumask *src1p, const struct cpumask *src2p)

    \*dstp = \*src1p & ~\*src2p

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_andnot.description`:

Description
-----------

If \*@dstp is empty, returns 0, else returns 1

.. _`cpumask_complement`:

cpumask_complement
==================

.. c:function:: void cpumask_complement(struct cpumask *dstp, const struct cpumask *srcp)

    \*dstp = ~\*srcp

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param srcp:
        the input to invert
    :type srcp: const struct cpumask \*

.. _`cpumask_equal`:

cpumask_equal
=============

.. c:function:: bool cpumask_equal(const struct cpumask *src1p, const struct cpumask *src2p)

    \*src1p == \*src2p

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_intersects`:

cpumask_intersects
==================

.. c:function:: bool cpumask_intersects(const struct cpumask *src1p, const struct cpumask *src2p)

    (\*src1p & \*src2p) != 0

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_subset`:

cpumask_subset
==============

.. c:function:: int cpumask_subset(const struct cpumask *src1p, const struct cpumask *src2p)

    (\*src1p & ~\*src2p) == 0

    :param src1p:
        the first input
    :type src1p: const struct cpumask \*

    :param src2p:
        the second input
    :type src2p: const struct cpumask \*

.. _`cpumask_subset.description`:

Description
-----------

Returns 1 if \*@src1p is a subset of \*@src2p, else returns 0

.. _`cpumask_empty`:

cpumask_empty
=============

.. c:function:: bool cpumask_empty(const struct cpumask *srcp)

    \*srcp == 0

    :param srcp:
        the cpumask to that all cpus < nr_cpu_ids are clear.
    :type srcp: const struct cpumask \*

.. _`cpumask_full`:

cpumask_full
============

.. c:function:: bool cpumask_full(const struct cpumask *srcp)

    \*srcp == 0xFFFFFFFF...

    :param srcp:
        the cpumask to that all cpus < nr_cpu_ids are set.
    :type srcp: const struct cpumask \*

.. _`cpumask_weight`:

cpumask_weight
==============

.. c:function:: unsigned int cpumask_weight(const struct cpumask *srcp)

    Count of bits in \*srcp

    :param srcp:
        the cpumask to count bits (< nr_cpu_ids) in.
    :type srcp: const struct cpumask \*

.. _`cpumask_shift_right`:

cpumask_shift_right
===================

.. c:function:: void cpumask_shift_right(struct cpumask *dstp, const struct cpumask *srcp, int n)

    \*dstp = \*srcp >> n

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param srcp:
        the input to shift
    :type srcp: const struct cpumask \*

    :param n:
        the number of bits to shift by
    :type n: int

.. _`cpumask_shift_left`:

cpumask_shift_left
==================

.. c:function:: void cpumask_shift_left(struct cpumask *dstp, const struct cpumask *srcp, int n)

    \*dstp = \*srcp << n

    :param dstp:
        the cpumask result
    :type dstp: struct cpumask \*

    :param srcp:
        the input to shift
    :type srcp: const struct cpumask \*

    :param n:
        the number of bits to shift by
    :type n: int

.. _`cpumask_copy`:

cpumask_copy
============

.. c:function:: void cpumask_copy(struct cpumask *dstp, const struct cpumask *srcp)

    \*dstp = \*srcp

    :param dstp:
        the result
    :type dstp: struct cpumask \*

    :param srcp:
        the input cpumask
    :type srcp: const struct cpumask \*

.. _`cpumask_any`:

cpumask_any
===========

.. c:function::  cpumask_any( srcp)

    pick a "random" cpu from \*srcp

    :param srcp:
        the input cpumask
    :type srcp: 

.. _`cpumask_any.description`:

Description
-----------

Returns >= nr_cpu_ids if no cpus set.

.. _`cpumask_first_and`:

cpumask_first_and
=================

.. c:function::  cpumask_first_and( src1p,  src2p)

    return the first cpu from \*srcp1 & \*srcp2

    :param src1p:
        the first input
    :type src1p: 

    :param src2p:
        the second input
    :type src2p: 

.. _`cpumask_first_and.description`:

Description
-----------

Returns >= nr_cpu_ids if no cpus set in both.  See also \ :c:func:`cpumask_next_and`\ .

.. _`cpumask_any_and`:

cpumask_any_and
===============

.. c:function::  cpumask_any_and( mask1,  mask2)

    pick a "random" cpu from \*mask1 & \*mask2

    :param mask1:
        the first input cpumask
    :type mask1: 

    :param mask2:
        the second input cpumask
    :type mask2: 

.. _`cpumask_any_and.description`:

Description
-----------

Returns >= nr_cpu_ids if no cpus set.

.. _`cpumask_of`:

cpumask_of
==========

.. c:function::  cpumask_of( cpu)

    the cpumask containing just a given cpu

    :param cpu:
        the cpu (<= nr_cpu_ids)
    :type cpu: 

.. _`cpumask_parse_user`:

cpumask_parse_user
==================

.. c:function:: int cpumask_parse_user(const char __user *buf, int len, struct cpumask *dstp)

    extract a cpumask from a user string

    :param buf:
        the buffer to extract from
    :type buf: const char __user \*

    :param len:
        the length of the buffer
    :type len: int

    :param dstp:
        the cpumask to set.
    :type dstp: struct cpumask \*

.. _`cpumask_parse_user.description`:

Description
-----------

Returns -errno, or 0 for success.

.. _`cpumask_parselist_user`:

cpumask_parselist_user
======================

.. c:function:: int cpumask_parselist_user(const char __user *buf, int len, struct cpumask *dstp)

    extract a cpumask from a user string

    :param buf:
        the buffer to extract from
    :type buf: const char __user \*

    :param len:
        the length of the buffer
    :type len: int

    :param dstp:
        the cpumask to set.
    :type dstp: struct cpumask \*

.. _`cpumask_parselist_user.description`:

Description
-----------

Returns -errno, or 0 for success.

.. _`cpumask_parse`:

cpumask_parse
=============

.. c:function:: int cpumask_parse(const char *buf, struct cpumask *dstp)

    extract a cpumask from a string

    :param buf:
        the buffer to extract from
    :type buf: const char \*

    :param dstp:
        the cpumask to set.
    :type dstp: struct cpumask \*

.. _`cpumask_parse.description`:

Description
-----------

Returns -errno, or 0 for success.

.. _`cpulist_parse`:

cpulist_parse
=============

.. c:function:: int cpulist_parse(const char *buf, struct cpumask *dstp)

    extract a cpumask from a user string of ranges

    :param buf:
        the buffer to extract from
    :type buf: const char \*

    :param dstp:
        the cpumask to set.
    :type dstp: struct cpumask \*

.. _`cpulist_parse.description`:

Description
-----------

Returns -errno, or 0 for success.

.. _`cpumask_size`:

cpumask_size
============

.. c:function:: unsigned int cpumask_size( void)

    size to allocate for a 'struct cpumask' in bytes

    :param void:
        no arguments
    :type void: 

.. _`to_cpumask`:

to_cpumask
==========

.. c:function::  to_cpumask( bitmap)

    convert an NR_CPUS bitmap to a struct cpumask \*

    :param bitmap:
        the bitmap
    :type bitmap: 

.. _`to_cpumask.description`:

Description
-----------

There are a few places where cpumask_var_t isn't appropriate and
static cpumasks must be used (eg. very early boot), yet we don't
expose the definition of 'struct cpumask'.

This does the conversion, and can be used as a constant initializer.

.. _`cpumap_print_to_pagebuf`:

cpumap_print_to_pagebuf
=======================

.. c:function:: ssize_t cpumap_print_to_pagebuf(bool list, char *buf, const struct cpumask *mask)

    copies the cpumask into the buffer either as comma-separated list of cpus or hex values of cpumask

    :param list:
        indicates whether the cpumap must be list
    :type list: bool

    :param buf:
        the buffer to copy into
    :type buf: char \*

    :param mask:
        the cpumask to copy
    :type mask: const struct cpumask \*

.. _`cpumap_print_to_pagebuf.description`:

Description
-----------

Returns the length of the (null-terminated) \ ``buf``\  string, zero if
nothing is copied.

.. This file was automatic generated / don't edit.


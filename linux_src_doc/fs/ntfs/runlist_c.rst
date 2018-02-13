.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/runlist.c

.. _`ntfs_rl_mm`:

ntfs_rl_mm
==========

.. c:function:: void ntfs_rl_mm(runlist_element *base, int dst, int src, int size)

    NTFS runlist handling code.  Part of the Linux-NTFS project.

    :param runlist_element \*base:
        *undescribed*

    :param int dst:
        *undescribed*

    :param int src:
        *undescribed*

    :param int size:
        *undescribed*

.. _`ntfs_rl_mm.description`:

Description
-----------

Copyright (c) 2001-2007 Anton Altaparmakov
Copyright (c) 2002-2005 Richard Russon

This program/include file is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program/include file is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (in the main directory of the Linux-NTFS
distribution in the file COPYING); if not, write to the Free Software
Foundation,Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _`ntfs_rl_mc`:

ntfs_rl_mc
==========

.. c:function:: void ntfs_rl_mc(runlist_element *dstbase, int dst, runlist_element *srcbase, int src, int size)

    runlist memory copy

    :param runlist_element \*dstbase:
        *undescribed*

    :param int dst:
        *undescribed*

    :param runlist_element \*srcbase:
        *undescribed*

    :param int src:
        *undescribed*

    :param int size:
        *undescribed*

.. _`ntfs_rl_mc.description`:

Description
-----------

It is up to the caller to serialize access to the runlists \ ``dstbase``\  and
\ ``srcbase``\ .

.. _`ntfs_rl_realloc`:

ntfs_rl_realloc
===============

.. c:function:: runlist_element *ntfs_rl_realloc(runlist_element *rl, int old_size, int new_size)

    Reallocate memory for runlists

    :param runlist_element \*rl:
        original runlist

    :param int old_size:
        number of runlist elements in the original runlist \ ``rl``\ 

    :param int new_size:
        number of runlist elements we need space for

.. _`ntfs_rl_realloc.description`:

Description
-----------

As the runlists grow, more memory will be required.  To prevent the
kernel having to allocate and reallocate large numbers of small bits of
memory, this function returns an entire page of memory.

It is up to the caller to serialize access to the runlist \ ``rl``\ .

N.B.  If the new allocation doesn't require a different number of pages in
memory, the function will return the original pointer.

On success, return a pointer to the newly allocated, or recycled, memory.
On error, return -errno. The following error codes are defined:
-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_rl_realloc_nofail`:

ntfs_rl_realloc_nofail
======================

.. c:function:: runlist_element *ntfs_rl_realloc_nofail(runlist_element *rl, int old_size, int new_size)

    Reallocate memory for runlists

    :param runlist_element \*rl:
        original runlist

    :param int old_size:
        number of runlist elements in the original runlist \ ``rl``\ 

    :param int new_size:
        number of runlist elements we need space for

.. _`ntfs_rl_realloc_nofail.description`:

Description
-----------

As the runlists grow, more memory will be required.  To prevent the
kernel having to allocate and reallocate large numbers of small bits of
memory, this function returns an entire page of memory.

This function guarantees that the allocation will succeed.  It will sleep
for as long as it takes to complete the allocation.

It is up to the caller to serialize access to the runlist \ ``rl``\ .

N.B.  If the new allocation doesn't require a different number of pages in
memory, the function will return the original pointer.

On success, return a pointer to the newly allocated, or recycled, memory.
On error, return -errno. The following error codes are defined:
-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_are_rl_mergeable`:

ntfs_are_rl_mergeable
=====================

.. c:function:: bool ntfs_are_rl_mergeable(runlist_element *dst, runlist_element *src)

    test if two runlists can be joined together

    :param runlist_element \*dst:
        original runlist

    :param runlist_element \*src:
        new runlist to test for mergeability with \ ``dst``\ 

.. _`ntfs_are_rl_mergeable.description`:

Description
-----------

Test if two runlists can be joined together. For this, their VCNs and LCNs
must be adjacent.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

.. _`ntfs_are_rl_mergeable.return`:

Return
------

true   Success, the runlists can be merged.
false  Failure, the runlists cannot be merged.

.. _`__ntfs_rl_merge`:

\__ntfs_rl_merge
================

.. c:function:: void __ntfs_rl_merge(runlist_element *dst, runlist_element *src)

    merge two runlists without testing if they can be merged

    :param runlist_element \*dst:
        original, destination runlist

    :param runlist_element \*src:
        new runlist to merge with \ ``dst``\ 

.. _`__ntfs_rl_merge.description`:

Description
-----------

Merge the two runlists, writing into the destination runlist \ ``dst``\ . The
caller must make sure the runlists can be merged or this will corrupt the
destination runlist.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

.. _`ntfs_rl_append`:

ntfs_rl_append
==============

.. c:function:: runlist_element *ntfs_rl_append(runlist_element *dst, int dsize, runlist_element *src, int ssize, int loc)

    append a runlist after a given element

    :param runlist_element \*dst:
        original runlist to be worked on

    :param int dsize:
        number of elements in \ ``dst``\  (including end marker)

    :param runlist_element \*src:
        runlist to be inserted into \ ``dst``\ 

    :param int ssize:
        number of elements in \ ``src``\  (excluding end marker)

    :param int loc:
        append the new runlist \ ``src``\  after this element in \ ``dst``\ 

.. _`ntfs_rl_append.description`:

Description
-----------

Append the runlist \ ``src``\  after element \ ``loc``\  in \ ``dst``\ .  Merge the right end of
the new runlist, if necessary. Adjust the size of the hole before the
appended runlist.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

On success, return a pointer to the new, combined, runlist. Note, both
runlists \ ``dst``\  and \ ``src``\  are deallocated before returning so you cannot use
the pointers for anything any more. (Strictly speaking the returned runlist
may be the same as \ ``dst``\  but this is irrelevant.)

On error, return -errno. Both runlists are left unmodified. The following

.. _`ntfs_rl_append.error-codes-are-defined`:

error codes are defined
-----------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_rl_insert`:

ntfs_rl_insert
==============

.. c:function:: runlist_element *ntfs_rl_insert(runlist_element *dst, int dsize, runlist_element *src, int ssize, int loc)

    insert a runlist into another

    :param runlist_element \*dst:
        original runlist to be worked on

    :param int dsize:
        number of elements in \ ``dst``\  (including end marker)

    :param runlist_element \*src:
        new runlist to be inserted

    :param int ssize:
        number of elements in \ ``src``\  (excluding end marker)

    :param int loc:
        insert the new runlist \ ``src``\  before this element in \ ``dst``\ 

.. _`ntfs_rl_insert.description`:

Description
-----------

Insert the runlist \ ``src``\  before element \ ``loc``\  in the runlist \ ``dst``\ . Merge the
left end of the new runlist, if necessary. Adjust the size of the hole
after the inserted runlist.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

On success, return a pointer to the new, combined, runlist. Note, both
runlists \ ``dst``\  and \ ``src``\  are deallocated before returning so you cannot use
the pointers for anything any more. (Strictly speaking the returned runlist
may be the same as \ ``dst``\  but this is irrelevant.)

On error, return -errno. Both runlists are left unmodified. The following

.. _`ntfs_rl_insert.error-codes-are-defined`:

error codes are defined
-----------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_rl_replace`:

ntfs_rl_replace
===============

.. c:function:: runlist_element *ntfs_rl_replace(runlist_element *dst, int dsize, runlist_element *src, int ssize, int loc)

    overwrite a runlist element with another runlist

    :param runlist_element \*dst:
        original runlist to be worked on

    :param int dsize:
        number of elements in \ ``dst``\  (including end marker)

    :param runlist_element \*src:
        new runlist to be inserted

    :param int ssize:
        number of elements in \ ``src``\  (excluding end marker)

    :param int loc:
        index in runlist \ ``dst``\  to overwrite with \ ``src``\ 

.. _`ntfs_rl_replace.description`:

Description
-----------

Replace the runlist element \ ``dst``\  at \ ``loc``\  with \ ``src``\ . Merge the left and
right ends of the inserted runlist, if necessary.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

On success, return a pointer to the new, combined, runlist. Note, both
runlists \ ``dst``\  and \ ``src``\  are deallocated before returning so you cannot use
the pointers for anything any more. (Strictly speaking the returned runlist
may be the same as \ ``dst``\  but this is irrelevant.)

On error, return -errno. Both runlists are left unmodified. The following

.. _`ntfs_rl_replace.error-codes-are-defined`:

error codes are defined
-----------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_rl_split`:

ntfs_rl_split
=============

.. c:function:: runlist_element *ntfs_rl_split(runlist_element *dst, int dsize, runlist_element *src, int ssize, int loc)

    insert a runlist into the centre of a hole

    :param runlist_element \*dst:
        original runlist to be worked on

    :param int dsize:
        number of elements in \ ``dst``\  (including end marker)

    :param runlist_element \*src:
        new runlist to be inserted

    :param int ssize:
        number of elements in \ ``src``\  (excluding end marker)

    :param int loc:
        index in runlist \ ``dst``\  at which to split and insert \ ``src``\ 

.. _`ntfs_rl_split.description`:

Description
-----------

Split the runlist \ ``dst``\  at \ ``loc``\  into two and insert \ ``new``\  in between the two
fragments. No merging of runlists is necessary. Adjust the size of the
holes either side.

It is up to the caller to serialize access to the runlists \ ``dst``\  and \ ``src``\ .

On success, return a pointer to the new, combined, runlist. Note, both
runlists \ ``dst``\  and \ ``src``\  are deallocated before returning so you cannot use
the pointers for anything any more. (Strictly speaking the returned runlist
may be the same as \ ``dst``\  but this is irrelevant.)

On error, return -errno. Both runlists are left unmodified. The following

.. _`ntfs_rl_split.error-codes-are-defined`:

error codes are defined
-----------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.

.. _`ntfs_runlists_merge`:

ntfs_runlists_merge
===================

.. c:function:: runlist_element *ntfs_runlists_merge(runlist_element *drl, runlist_element *srl)

    merge two runlists into one

    :param runlist_element \*drl:
        original runlist to be worked on

    :param runlist_element \*srl:
        new runlist to be merged into \ ``drl``\ 

.. _`ntfs_runlists_merge.description`:

Description
-----------

First we sanity check the two runlists \ ``srl``\  and \ ``drl``\  to make sure that they
are sensible and can be merged. The runlist \ ``srl``\  must be either after the
runlist \ ``drl``\  or completely within a hole (or unmapped region) in \ ``drl``\ .

It is up to the caller to serialize access to the runlists \ ``drl``\  and \ ``srl``\ .

.. _`ntfs_runlists_merge.merging-of-runlists-is-necessary-in-two-cases`:

Merging of runlists is necessary in two cases
---------------------------------------------

1. When attribute lists are used and a further extent is being mapped.
2. When new clusters are allocated to fill a hole or extend a file.

There are four possible ways \ ``srl``\  can be merged. It can:
- be inserted at the beginning of a hole,
- split the hole in two and be inserted between the two fragments,
- be appended at the end of a hole, or it can
- replace the whole hole.
It can also be appended to the end of the runlist, which is just a variant
of the insert case.

On success, return a pointer to the new, combined, runlist. Note, both
runlists \ ``drl``\  and \ ``srl``\  are deallocated before returning so you cannot use
the pointers for anything any more. (Strictly speaking the returned runlist
may be the same as \ ``dst``\  but this is irrelevant.)

On error, return -errno. Both runlists are left unmodified. The following

.. _`ntfs_runlists_merge.error-codes-are-defined`:

error codes are defined
-----------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EINVAL - Invalid parameters were passed in.
-ERANGE - The runlists overlap and cannot be merged.

.. _`ntfs_mapping_pairs_decompress`:

ntfs_mapping_pairs_decompress
=============================

.. c:function:: runlist_element *ntfs_mapping_pairs_decompress(const ntfs_volume *vol, const ATTR_RECORD *attr, runlist_element *old_rl)

    convert mapping pairs array to runlist

    :param const ntfs_volume \*vol:
        ntfs volume on which the attribute resides

    :param const ATTR_RECORD \*attr:
        attribute record whose mapping pairs array to decompress

    :param runlist_element \*old_rl:
        optional runlist in which to insert \ ``attr``\ 's runlist

.. _`ntfs_mapping_pairs_decompress.description`:

Description
-----------

It is up to the caller to serialize access to the runlist \ ``old_rl``\ .

Decompress the attribute \ ``attr``\ 's mapping pairs array into a runlist. On
success, return the decompressed runlist.

If \ ``old_rl``\  is not NULL, decompressed runlist is inserted into the
appropriate place in \ ``old_rl``\  and the resultant, combined runlist is
returned. The original \ ``old_rl``\  is deallocated.

On error, return -errno. \ ``old_rl``\  is left unmodified in that case.

.. _`ntfs_mapping_pairs_decompress.the-following-error-codes-are-defined`:

The following error codes are defined
-------------------------------------

-ENOMEM - Not enough memory to allocate runlist array.
-EIO    - Corrupt runlist.
-EINVAL - Invalid parameters were passed in.
-ERANGE - The two runlists overlap.

.. _`ntfs_mapping_pairs_decompress.fixme`:

FIXME
-----

For now we take the conceptionally simplest approach of creating the
new runlist disregarding the already existing one and then splicing the
two into one, if that is possible (we check for overlap and discard the new
runlist if overlap present before returning ERR_PTR(-ERANGE)).

.. _`ntfs_rl_vcn_to_lcn`:

ntfs_rl_vcn_to_lcn
==================

.. c:function:: LCN ntfs_rl_vcn_to_lcn(const runlist_element *rl, const VCN vcn)

    convert a vcn into a lcn given a runlist

    :param const runlist_element \*rl:
        runlist to use for conversion

    :param const VCN vcn:
        vcn to convert

.. _`ntfs_rl_vcn_to_lcn.description`:

Description
-----------

Convert the virtual cluster number \ ``vcn``\  of an attribute into a logical
cluster number (lcn) of a device using the runlist \ ``rl``\  to map vcns to their
corresponding lcns.

It is up to the caller to serialize access to the runlist \ ``rl``\ .

Since lcns must be >= 0, we use negative return codes with special meaning:

Return code          Meaning / Description
==================================================
LCN_HOLE            Hole / not allocated on disk.
LCN_RL_NOT_MAPPED   This is part of the runlist which has not been
inserted into the runlist yet.
LCN_ENOENT          There is no such vcn in the attribute.

.. _`ntfs_rl_vcn_to_lcn.locking`:

Locking
-------

- The caller must have locked the runlist (for reading or writing).
- This function does not touch the lock, nor does it modify the
runlist.

.. _`ntfs_rl_find_vcn_nolock`:

ntfs_rl_find_vcn_nolock
=======================

.. c:function:: runlist_element *ntfs_rl_find_vcn_nolock(runlist_element *rl, const VCN vcn)

    find a vcn in a runlist

    :param runlist_element \*rl:
        runlist to search

    :param const VCN vcn:
        vcn to find

.. _`ntfs_rl_find_vcn_nolock.description`:

Description
-----------

Find the virtual cluster number \ ``vcn``\  in the runlist \ ``rl``\  and return the
address of the runlist element containing the \ ``vcn``\  on success.

Return NULL if \ ``rl``\  is NULL or \ ``vcn``\  is in an unmapped part/out of bounds of
the runlist.

.. _`ntfs_rl_find_vcn_nolock.locking`:

Locking
-------

The runlist must be locked on entry.

.. _`ntfs_get_nr_significant_bytes`:

ntfs_get_nr_significant_bytes
=============================

.. c:function:: int ntfs_get_nr_significant_bytes(const s64 n)

    get number of bytes needed to store a number

    :param const s64 n:
        number for which to get the number of bytes for

.. _`ntfs_get_nr_significant_bytes.description`:

Description
-----------

Return the number of bytes required to store \ ``n``\  unambiguously as
a signed number.

This is used in the context of the mapping pairs array to determine how
many bytes will be needed in the array to store a given logical cluster
number (lcn) or a specific run length.

Return the number of bytes written.  This function cannot fail.

.. _`ntfs_get_size_for_mapping_pairs`:

ntfs_get_size_for_mapping_pairs
===============================

.. c:function:: int ntfs_get_size_for_mapping_pairs(const ntfs_volume *vol, const runlist_element *rl, const VCN first_vcn, const VCN last_vcn)

    get bytes needed for mapping pairs array

    :param const ntfs_volume \*vol:
        ntfs volume (needed for the ntfs version)

    :param const runlist_element \*rl:
        locked runlist to determine the size of the mapping pairs of

    :param const VCN first_vcn:
        first vcn which to include in the mapping pairs array

    :param const VCN last_vcn:
        last vcn which to include in the mapping pairs array

.. _`ntfs_get_size_for_mapping_pairs.description`:

Description
-----------

Walk the locked runlist \ ``rl``\  and calculate the size in bytes of the mapping
pairs array corresponding to the runlist \ ``rl``\ , starting at vcn \ ``first_vcn``\  and
finishing with vcn \ ``last_vcn``\ .

A \ ``last_vcn``\  of -1 means end of runlist and in that case the size of the
mapping pairs array corresponding to the runlist starting at vcn \ ``first_vcn``\ 
and finishing at the end of the runlist is determined.

This for example allows us to allocate a buffer of the right size when
building the mapping pairs array.

If \ ``rl``\  is NULL, just return 1 (for the single terminator byte).

Return the calculated size in bytes on success.  On error, return -errno.

.. _`ntfs_get_size_for_mapping_pairs.the-following-error-codes-are-defined`:

The following error codes are defined
-------------------------------------

-EINVAL - Run list contains unmapped elements.  Make sure to only pass
fully mapped runlists to this function.
-EIO    - The runlist is corrupt.

.. _`ntfs_get_size_for_mapping_pairs.locking`:

Locking
-------

\ ``rl``\  must be locked on entry (either for reading or writing), it
remains locked throughout, and is left locked upon return.

.. _`ntfs_write_significant_bytes`:

ntfs_write_significant_bytes
============================

.. c:function:: int ntfs_write_significant_bytes(s8 *dst, const s8 *dst_max, const s64 n)

    write the significant bytes of a number

    :param s8 \*dst:
        destination buffer to write to

    :param const s8 \*dst_max:
        pointer to last byte of destination buffer for bounds checking

    :param const s64 n:
        number whose significant bytes to write

.. _`ntfs_write_significant_bytes.description`:

Description
-----------

Store in \ ``dst``\ , the minimum bytes of the number \ ``n``\  which are required to
identify \ ``n``\  unambiguously as a signed number, taking care not to exceed
\ ``dest_max``\ , the maximum position within \ ``dst``\  to which we are allowed to
write.

This is used when building the mapping pairs array of a runlist to compress
a given logical cluster number (lcn) or a specific run length to the minimum
size possible.

Return the number of bytes written on success.  On error, i.e. the
destination buffer \ ``dst``\  is too small, return -ENOSPC.

.. _`ntfs_mapping_pairs_build`:

ntfs_mapping_pairs_build
========================

.. c:function:: int ntfs_mapping_pairs_build(const ntfs_volume *vol, s8 *dst, const int dst_len, const runlist_element *rl, const VCN first_vcn, const VCN last_vcn, VCN *const stop_vcn)

    build the mapping pairs array from a runlist

    :param const ntfs_volume \*vol:
        ntfs volume (needed for the ntfs version)

    :param s8 \*dst:
        destination buffer to which to write the mapping pairs array

    :param const int dst_len:
        size of destination buffer \ ``dst``\  in bytes

    :param const runlist_element \*rl:
        locked runlist for which to build the mapping pairs array

    :param const VCN first_vcn:
        first vcn which to include in the mapping pairs array

    :param const VCN last_vcn:
        last vcn which to include in the mapping pairs array

    :param VCN \*const stop_vcn:
        first vcn outside destination buffer on success or -ENOSPC

.. _`ntfs_mapping_pairs_build.description`:

Description
-----------

Create the mapping pairs array from the locked runlist \ ``rl``\ , starting at vcn
\ ``first_vcn``\  and finishing with vcn \ ``last_vcn``\  and save the array in \ ``dst``\ .
\ ``dst_len``\  is the size of \ ``dst``\  in bytes and it should be at least equal to the
value obtained by calling \ :c:func:`ntfs_get_size_for_mapping_pairs`\ .

A \ ``last_vcn``\  of -1 means end of runlist and in that case the mapping pairs
array corresponding to the runlist starting at vcn \ ``first_vcn``\  and finishing
at the end of the runlist is created.

If \ ``rl``\  is NULL, just write a single terminator byte to \ ``dst``\ .

On success or -ENOSPC error, if \ ``stop_vcn``\  is not NULL, \*@stop_vcn is set to
the first vcn outside the destination buffer.  Note that on error, \ ``dst``\  has
been filled with all the mapping pairs that will fit, thus it can be treated
as partial success, in that a new attribute extent needs to be created or
the next extent has to be used and the mapping pairs build has to be
continued with \ ``first_vcn``\  set to \*@stop_vcn.

Return 0 on success and -errno on error.  The following error codes are

.. _`ntfs_mapping_pairs_build.defined`:

defined
-------

-EINVAL - Run list contains unmapped elements.  Make sure to only pass
fully mapped runlists to this function.
-EIO    - The runlist is corrupt.
-ENOSPC - The destination buffer is too small.

.. _`ntfs_mapping_pairs_build.locking`:

Locking
-------

\ ``rl``\  must be locked on entry (either for reading or writing), it
remains locked throughout, and is left locked upon return.

.. _`ntfs_rl_truncate_nolock`:

ntfs_rl_truncate_nolock
=======================

.. c:function:: int ntfs_rl_truncate_nolock(const ntfs_volume *vol, runlist *const runlist, const s64 new_length)

    truncate a runlist starting at a specified vcn

    :param const ntfs_volume \*vol:
        ntfs volume (needed for error output)

    :param runlist \*const runlist:
        runlist to truncate

    :param const s64 new_length:
        the new length of the runlist in VCNs

.. _`ntfs_rl_truncate_nolock.description`:

Description
-----------

Truncate the runlist described by \ ``runlist``\  as well as the memory buffer
holding the runlist elements to a length of \ ``new_length``\  VCNs.

If \ ``new_length``\  lies within the runlist, the runlist elements with VCNs of
\ ``new_length``\  and above are discarded.  As a special case if \ ``new_length``\  is
zero, the runlist is discarded and set to NULL.

If \ ``new_length``\  lies beyond the runlist, a sparse runlist element is added to
the end of the runlist \ ``runlist``\  or if the last runlist element is a sparse
one already, this is extended.

Note, no checking is done for unmapped runlist elements.  It is assumed that
the caller has mapped any elements that need to be mapped already.

Return 0 on success and -errno on error.

.. _`ntfs_rl_truncate_nolock.locking`:

Locking
-------

The caller must hold \ ``runlist``\ ->lock for writing.

.. _`ntfs_rl_punch_nolock`:

ntfs_rl_punch_nolock
====================

.. c:function:: int ntfs_rl_punch_nolock(const ntfs_volume *vol, runlist *const runlist, const VCN start, const s64 length)

    punch a hole into a runlist

    :param const ntfs_volume \*vol:
        ntfs volume (needed for error output)

    :param runlist \*const runlist:
        runlist to punch a hole into

    :param const VCN start:
        starting VCN of the hole to be created

    :param const s64 length:
        size of the hole to be created in units of clusters

.. _`ntfs_rl_punch_nolock.description`:

Description
-----------

Punch a hole into the runlist \ ``runlist``\  starting at VCN \ ``start``\  and of size
\ ``length``\  clusters.

Return 0 on success and -errno on error, in which case \ ``runlist``\  has not been
modified.

If \ ``start``\  and/or \ ``start``\  + \ ``length``\  are outside the runlist return error code
-ENOENT.

If the runlist contains unmapped or error elements between \ ``start``\  and \ ``start``\ 
+ \ ``length``\  return error code -EINVAL.

.. _`ntfs_rl_punch_nolock.locking`:

Locking
-------

The caller must hold \ ``runlist``\ ->lock for writing.

.. This file was automatic generated / don't edit.


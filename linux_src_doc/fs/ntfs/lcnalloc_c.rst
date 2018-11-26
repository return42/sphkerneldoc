.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/lcnalloc.c

.. _`ntfs_cluster_free_from_rl_nolock`:

ntfs_cluster_free_from_rl_nolock
================================

.. c:function:: int ntfs_cluster_free_from_rl_nolock(ntfs_volume *vol, const runlist_element *rl)

    free clusters from runlist

    :param vol:
        mounted ntfs volume on which to free the clusters
    :type vol: ntfs_volume \*

    :param rl:
        runlist describing the clusters to free
    :type rl: const runlist_element \*

.. _`ntfs_cluster_free_from_rl_nolock.description`:

Description
-----------

Free all the clusters described by the runlist \ ``rl``\  on the volume \ ``vol``\ .  In
the case of an error being returned, at least some of the clusters were not
freed.

Return 0 on success and -errno on error.

.. _`ntfs_cluster_free_from_rl_nolock.locking`:

Locking
-------

- The volume lcn bitmap must be locked for writing on entry and is
left locked on return.

.. _`ntfs_cluster_alloc`:

ntfs_cluster_alloc
==================

.. c:function:: runlist_element *ntfs_cluster_alloc(ntfs_volume *vol, const VCN start_vcn, const s64 count, const LCN start_lcn, const NTFS_CLUSTER_ALLOCATION_ZONES zone, const bool is_extension)

    allocate clusters on an ntfs volume

    :param vol:
        mounted ntfs volume on which to allocate the clusters
    :type vol: ntfs_volume \*

    :param start_vcn:
        vcn to use for the first allocated cluster
    :type start_vcn: const VCN

    :param count:
        number of clusters to allocate
    :type count: const s64

    :param start_lcn:
        starting lcn at which to allocate the clusters (or -1 if none)
    :type start_lcn: const LCN

    :param zone:
        zone from which to allocate the clusters
    :type zone: const NTFS_CLUSTER_ALLOCATION_ZONES

    :param is_extension:
        if 'true', this is an attribute extension
    :type is_extension: const bool

.. _`ntfs_cluster_alloc.description`:

Description
-----------

Allocate \ ``count``\  clusters preferably starting at cluster \ ``start_lcn``\  or at the
current allocator position if \ ``start_lcn``\  is -1, on the mounted ntfs volume
\ ``vol``\ . \ ``zone``\  is either DATA_ZONE for allocation of normal clusters or
MFT_ZONE for allocation of clusters for the master file table, i.e. the
\ ``$MFT``\ /$DATA attribute.

\ ``start_vcn``\  specifies the vcn of the first allocated cluster.  This makes
merging the resulting runlist with the old runlist easier.

If \ ``is_extension``\  is 'true', the caller is allocating clusters to extend an
attribute and if it is 'false', the caller is allocating clusters to fill a
hole in an attribute.  Practically the difference is that if \ ``is_extension``\ 
is 'true' the returned runlist will be terminated with LCN_ENOENT and if
\ ``is_extension``\  is 'false' the runlist will be terminated with
LCN_RL_NOT_MAPPED.

You need to check the return value with \ :c:func:`IS_ERR`\ .  If this is false, the
function was successful and the return value is a runlist describing the
allocated cluster(s).  If \ :c:func:`IS_ERR`\  is true, the function failed and
\ :c:func:`PTR_ERR`\  gives you the error code.

Notes on the allocation algorithm
=================================

There are two data zones.  First is the area between the end of the mft zone
and the end of the volume, and second is the area between the start of the
volume and the start of the mft zone.  On unmodified/standard NTFS 1.x
volumes, the second data zone does not exist due to the mft zone being
expanded to cover the start of the volume in order to reserve space for the
mft bitmap attribute.

This is not the prettiest function but the complexity stems from the need of
implementing the mft vs data zoned approach and from the fact that we have
access to the lcn bitmap in portions of up to 8192 bytes at a time, so we
need to cope with crossing over boundaries of two buffers.  Further, the
fact that the allocator allows for caller supplied hints as to the location
of where allocation should begin and the fact that the allocator keeps track
of where in the data zones the next natural allocation should occur,
contribute to the complexity of the function.  But it should all be
worthwhile, because this allocator should: 1) be a full implementation of
the MFT zone approach used by Windows NT, 2) cause reduction in
fragmentation, and 3) be speedy in allocations (the code is not optimized
for speed, but the algorithm is, so further speed improvements are probably
possible).

.. _`ntfs_cluster_alloc.fixme`:

FIXME
-----

We should be monitoring cluster allocation and increment the MFT zone
size dynamically but this is something for the future.  We will just cause
heavier fragmentation by not doing it and I am not even sure Windows would
grow the MFT zone dynamically, so it might even be correct not to do this.
The overhead in doing dynamic MFT zone expansion would be very large and
unlikely worth the effort. (AIA)

.. _`ntfs_cluster_alloc.todo`:

TODO
----

I have added in double the required zone position pointer wrap around
logic which can be optimized to having only one of the two logic sets.
However, having the double logic will work fine, but if we have only one of
the sets and we get it wrong somewhere, then we get into trouble, so
removing the duplicate logic requires \_very\_ careful consideration of \_all_
possible code paths.  So at least for now, I am leaving the double logic -
better safe than sorry... (AIA)

.. _`ntfs_cluster_alloc.locking`:

Locking
-------

- The volume lcn bitmap must be unlocked on entry and is unlocked
on return.
- This function takes the volume lcn bitmap lock for writing and
modifies the bitmap contents.

.. _`__ntfs_cluster_free`:

\__ntfs_cluster_free
====================

.. c:function:: s64 __ntfs_cluster_free(ntfs_inode *ni, const VCN start_vcn, s64 count, ntfs_attr_search_ctx *ctx, const bool is_rollback)

    free clusters on an ntfs volume

    :param ni:
        ntfs inode whose runlist describes the clusters to free
    :type ni: ntfs_inode \*

    :param start_vcn:
        vcn in the runlist of \ ``ni``\  at which to start freeing clusters
    :type start_vcn: const VCN

    :param count:
        number of clusters to free or -1 for all clusters
    :type count: s64

    :param ctx:
        active attribute search context if present or NULL if not
    :type ctx: ntfs_attr_search_ctx \*

    :param is_rollback:
        true if this is a rollback operation
    :type is_rollback: const bool

.. _`__ntfs_cluster_free.description`:

Description
-----------

Free \ ``count``\  clusters starting at the cluster \ ``start_vcn``\  in the runlist
described by the vfs inode \ ``ni``\ .

If \ ``count``\  is -1, all clusters from \ ``start_vcn``\  to the end of the runlist are
deallocated.  Thus, to completely free all clusters in a runlist, use
\ ``start_vcn``\  = 0 and \ ``count``\  = -1.

If \ ``ctx``\  is specified, it is an active search context of \ ``ni``\  and its base mft
record.  This is needed when \__ntfs_cluster_free() encounters unmapped
runlist fragments and allows their mapping.  If you do not have the mft
record mapped, you can specify \ ``ctx``\  as NULL and \__ntfs_cluster_free() will
perform the necessary mapping and unmapping.

Note, \__ntfs_cluster_free() saves the state of \ ``ctx``\  on entry and restores it
before returning.  Thus, \ ``ctx``\  will be left pointing to the same attribute on
return as on entry.  However, the actual pointers in \ ``ctx``\  may point to
different memory locations on return, so you must remember to reset any
cached pointers from the \ ``ctx``\ , i.e. after the call to \__ntfs_cluster_free(),

.. _`__ntfs_cluster_free.you-will-probably-want-to-do`:

you will probably want to do
----------------------------

m = ctx->mrec;
a = ctx->attr;
Assuming you cache ctx->attr in a variable \ ``a``\  of type ATTR_RECORD \* and that
you cache ctx->mrec in a variable \ ``m``\  of type MFT_RECORD \*.

\ ``is_rollback``\  should always be 'false', it is for internal use to rollback
errors.  You probably want to use \ :c:func:`ntfs_cluster_free`\  instead.

Note, \__ntfs_cluster_free() does not modify the runlist, so you have to
remove from the runlist or mark sparse the freed runs later.

Return the number of deallocated clusters (not counting sparse ones) on
success and -errno on error.

.. _`__ntfs_cluster_free.warning`:

WARNING
-------

If \ ``ctx``\  is supplied, regardless of whether success or failure is
returned, you need to check IS_ERR(@ctx->mrec) and if 'true' the \ ``ctx``\ 
is no longer valid, i.e. you need to either call
\ :c:func:`ntfs_attr_reinit_search_ctx`\  or \ :c:func:`ntfs_attr_put_search_ctx`\  on it.
In that case PTR_ERR(@ctx->mrec) will give you the error code for
why the mapping of the old inode failed.

.. _`__ntfs_cluster_free.locking`:

Locking
-------

- The runlist described by \ ``ni``\  must be locked for writing on entry
and is locked on return.  Note the runlist may be modified when
needed runlist fragments need to be mapped.
- The volume lcn bitmap must be unlocked on entry and is unlocked
on return.
- This function takes the volume lcn bitmap lock for writing and
modifies the bitmap contents.
- If \ ``ctx``\  is NULL, the base mft record of \ ``ni``\  must not be mapped on
entry and it will be left unmapped on return.
- If \ ``ctx``\  is not NULL, the base mft record must be mapped on entry
and it will be left mapped on return.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/lcnalloc.h

.. _`ntfs_cluster_free`:

ntfs_cluster_free
=================

.. c:function:: s64 ntfs_cluster_free(ntfs_inode *ni, const VCN start_vcn, s64 count, ntfs_attr_search_ctx *ctx)

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

.. _`ntfs_cluster_free.description`:

Description
-----------

Free \ ``count``\  clusters starting at the cluster \ ``start_vcn``\  in the runlist
described by the ntfs inode \ ``ni``\ .

If \ ``count``\  is -1, all clusters from \ ``start_vcn``\  to the end of the runlist are
deallocated.  Thus, to completely free all clusters in a runlist, use
\ ``start_vcn``\  = 0 and \ ``count``\  = -1.

If \ ``ctx``\  is specified, it is an active search context of \ ``ni``\  and its base mft
record.  This is needed when \ :c:func:`ntfs_cluster_free`\  encounters unmapped runlist
fragments and allows their mapping.  If you do not have the mft record
mapped, you can specify \ ``ctx``\  as NULL and \ :c:func:`ntfs_cluster_free`\  will perform
the necessary mapping and unmapping.

Note, \ :c:func:`ntfs_cluster_free`\  saves the state of \ ``ctx``\  on entry and restores it
before returning.  Thus, \ ``ctx``\  will be left pointing to the same attribute on
return as on entry.  However, the actual pointers in \ ``ctx``\  may point to
different memory locations on return, so you must remember to reset any
cached pointers from the \ ``ctx``\ , i.e. after the call to \ :c:func:`ntfs_cluster_free`\ ,

.. _`ntfs_cluster_free.you-will-probably-want-to-do`:

you will probably want to do
----------------------------

m = ctx->mrec;
a = ctx->attr;
Assuming you cache ctx->attr in a variable \ ``a``\  of type ATTR_RECORD \* and that
you cache ctx->mrec in a variable \ ``m``\  of type MFT_RECORD \*.

Note, \ :c:func:`ntfs_cluster_free`\  does not modify the runlist, so you have to remove
from the runlist or mark sparse the freed runs later.

Return the number of deallocated clusters (not counting sparse ones) on
success and -errno on error.

.. _`ntfs_cluster_free.warning`:

WARNING
-------

If \ ``ctx``\  is supplied, regardless of whether success or failure is
returned, you need to check IS_ERR(@ctx->mrec) and if 'true' the \ ``ctx``\ 
is no longer valid, i.e. you need to either call
\ :c:func:`ntfs_attr_reinit_search_ctx`\  or \ :c:func:`ntfs_attr_put_search_ctx`\  on it.
In that case PTR_ERR(@ctx->mrec) will give you the error code for
why the mapping of the old inode failed.

.. _`ntfs_cluster_free.locking`:

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

.. _`ntfs_cluster_free_from_rl`:

ntfs_cluster_free_from_rl
=========================

.. c:function:: int ntfs_cluster_free_from_rl(ntfs_volume *vol, const runlist_element *rl)

    free clusters from runlist

    :param vol:
        mounted ntfs volume on which to free the clusters
    :type vol: ntfs_volume \*

    :param rl:
        runlist describing the clusters to free
    :type rl: const runlist_element \*

.. _`ntfs_cluster_free_from_rl.description`:

Description
-----------

Free all the clusters described by the runlist \ ``rl``\  on the volume \ ``vol``\ .  In
the case of an error being returned, at least some of the clusters were not
freed.

Return 0 on success and -errno on error.

.. _`ntfs_cluster_free_from_rl.locking`:

Locking
-------

- This function takes the volume lcn bitmap lock for writing and
modifies the bitmap contents.
- The caller must have locked the runlist \ ``rl``\  for reading or
writing.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/dir.c

.. _`gfs2_dir_write_data`:

gfs2_dir_write_data
===================

.. c:function:: int gfs2_dir_write_data(struct gfs2_inode *ip, const char *buf, u64 offset, unsigned int size)

    Write directory information to the inode

    :param struct gfs2_inode \*ip:
        The GFS2 inode

    :param const char \*buf:
        The buffer containing information to be written

    :param u64 offset:
        The file offset to start writing at

    :param unsigned int size:
        The amount of data to write

.. _`gfs2_dir_write_data.return`:

Return
------

The number of bytes correctly written or error code

.. _`gfs2_dir_read_data`:

gfs2_dir_read_data
==================

.. c:function:: int gfs2_dir_read_data(struct gfs2_inode *ip, __be64 *buf, unsigned int size)

    Read a data from a directory inode

    :param struct gfs2_inode \*ip:
        The GFS2 Inode

    :param __be64 \*buf:
        The buffer to place result into

    :param unsigned int size:
        Amount of data to transfer

.. _`gfs2_dir_read_data.return`:

Return
------

The amount of data actually copied or the error

.. _`gfs2_dir_get_hash_table`:

gfs2_dir_get_hash_table
=======================

.. c:function:: __be64 *gfs2_dir_get_hash_table(struct gfs2_inode *ip)

    Get pointer to the dir hash table

    :param struct gfs2_inode \*ip:
        The inode in question

.. _`gfs2_dir_get_hash_table.return`:

Return
------

The hash table or an error

.. _`gfs2_dir_hash_inval`:

gfs2_dir_hash_inval
===================

.. c:function:: void gfs2_dir_hash_inval(struct gfs2_inode *ip)

    Invalidate dir hash

    :param struct gfs2_inode \*ip:
        The directory inode

.. _`gfs2_dir_hash_inval.description`:

Description
-----------

Must be called with an exclusive glock, or during glock invalidation.

.. _`dirent_next`:

dirent_next
===========

.. c:function:: int dirent_next(struct gfs2_inode *dip, struct buffer_head *bh, struct gfs2_dirent **dent)

    Next dirent

    :param struct gfs2_inode \*dip:
        the directory

    :param struct buffer_head \*bh:
        The buffer

    :param struct gfs2_dirent \*\*dent:
        Pointer to list of dirents

.. _`dirent_next.return`:

Return
------

0 on success, error code otherwise

.. _`dirent_del`:

dirent_del
==========

.. c:function:: void dirent_del(struct gfs2_inode *dip, struct buffer_head *bh, struct gfs2_dirent *prev, struct gfs2_dirent *cur)

    Delete a dirent

    :param struct gfs2_inode \*dip:
        The GFS2 inode

    :param struct buffer_head \*bh:
        The buffer

    :param struct gfs2_dirent \*prev:
        The previous dirent

    :param struct gfs2_dirent \*cur:
        The current dirent

.. _`get_leaf_nr`:

get_leaf_nr
===========

.. c:function:: int get_leaf_nr(struct gfs2_inode *dip, u32 index, u64 *leaf_out)

    Get a leaf number associated with the index

    :param struct gfs2_inode \*dip:
        The GFS2 inode

    :param u32 index:
        *undescribed*

    :param u64 \*leaf_out:
        *undescribed*

.. _`get_leaf_nr.return`:

Return
------

0 on success, error code otherwise

.. _`dir_make_exhash`:

dir_make_exhash
===============

.. c:function:: int dir_make_exhash(struct inode *inode)

    Convert a stuffed directory into an ExHash directory

    :param struct inode \*inode:
        *undescribed*

.. _`dir_make_exhash.return`:

Return
------

0 on success, error code otherwise

.. _`dir_split_leaf`:

dir_split_leaf
==============

.. c:function:: int dir_split_leaf(struct inode *inode, const struct qstr *name)

    Split a leaf block into two

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*name:
        *undescribed*

.. _`dir_split_leaf.return`:

Return
------

0 on success, error code on failure

.. _`dir_double_exhash`:

dir_double_exhash
=================

.. c:function:: int dir_double_exhash(struct gfs2_inode *dip)

    Double size of ExHash table

    :param struct gfs2_inode \*dip:
        The GFS2 dinode

.. _`dir_double_exhash.return`:

Return
------

0 on success, error code on failure

.. _`compare_dents`:

compare_dents
=============

.. c:function:: int compare_dents(const void *a, const void *b)

    compare directory entries by hash value

    :param const void \*a:
        first dent

    :param const void \*b:
        second dent

.. _`compare_dents.description`:

Description
-----------

When comparing the hash entries of \ ``a``\  to \ ``b``\ :
gt: returns 1
lt: returns -1
eq: returns 0

.. _`do_filldir_main`:

do_filldir_main
===============

.. c:function:: int do_filldir_main(struct gfs2_inode *dip, struct dir_context *ctx, struct gfs2_dirent **darr, u32 entries, u32 sort_start, int *copied)

    read out directory entries

    :param struct gfs2_inode \*dip:
        The GFS2 inode

    :param struct dir_context \*ctx:
        what to feed the entries to

    :param struct gfs2_dirent \*\*darr:
        an array of struct gfs2_dirent pointers to read

    :param u32 entries:
        the number of entries in darr

    :param u32 sort_start:
        *undescribed*

    :param int \*copied:
        pointer to int that's non-zero if a entry has been copied out

.. _`do_filldir_main.description`:

Description
-----------

Jump through some hoops to make sure that if there are hash collsions,
they are read out at the beginning of a buffer.  We want to minimize
the possibility that they will fall into different readdir buffers or
that someone will want to seek to that location.

.. _`do_filldir_main.return`:

Return
------

errno, >0 if the actor tells you to stop

.. _`gfs2_dir_readahead`:

gfs2_dir_readahead
==================

.. c:function:: void gfs2_dir_readahead(struct inode *inode, unsigned hsize, u32 index, struct file_ra_state *f_ra)

    Issue read-ahead requests for leaf blocks.

    :param struct inode \*inode:
        *undescribed*

    :param unsigned hsize:
        *undescribed*

    :param u32 index:
        *undescribed*

    :param struct file_ra_state \*f_ra:
        *undescribed*

.. _`gfs2_dir_readahead.note`:

Note
----

we can't calculate each index like dir_e_read can because we don't
have the leaf, and therefore we don't have the depth, and therefore we
don't have the length. So we have to just read enough ahead to make up
for the loss of information.

.. _`dir_e_read`:

dir_e_read
==========

.. c:function:: int dir_e_read(struct inode *inode, struct dir_context *ctx, struct file_ra_state *f_ra)

    Reads the entries from a directory into a filldir buffer

    :param struct inode \*inode:
        *undescribed*

    :param struct dir_context \*ctx:
        actor to feed the entries to

    :param struct file_ra_state \*f_ra:
        *undescribed*

.. _`dir_e_read.return`:

Return
------

errno

.. _`gfs2_dir_search`:

gfs2_dir_search
===============

.. c:function:: struct inode *gfs2_dir_search(struct inode *dir, const struct qstr *name, bool fail_on_exist)

    Search a directory

    :param struct inode \*dir:
        *undescribed*

    :param const struct qstr \*name:
        The name we are looking up

    :param bool fail_on_exist:
        Fail if the name exists rather than looking it up

.. _`gfs2_dir_search.description`:

Description
-----------

This routine searches a directory for a file or another directory.
Assumes a glock is held on dip.

.. _`gfs2_dir_search.return`:

Return
------

errno

.. _`dir_new_leaf`:

dir_new_leaf
============

.. c:function:: int dir_new_leaf(struct inode *inode, const struct qstr *name)

    Add a new leaf onto hash chain

    :param struct inode \*inode:
        The directory

    :param const struct qstr \*name:
        The name we are adding

.. _`dir_new_leaf.description`:

Description
-----------

This adds a new dir leaf onto an existing leaf when there is not
enough space to add a new dir entry. This is a last resort after
we've expanded the hash table to max size and also split existing
leaf blocks, so it will only occur for very large directories.

The dist parameter is set to 1 for leaf blocks directly attached
to the hash table, 2 for one layer of indirection, 3 for two layers
etc. We are thus able to tell the difference between an old leaf
with dist set to zero (i.e. "don't know") and a new one where we
set this information for debug/fsck purposes.

.. _`dir_new_leaf.return`:

Return
------

0 on success, or -ve on error

.. _`gfs2_dir_add`:

gfs2_dir_add
============

.. c:function:: int gfs2_dir_add(struct inode *inode, const struct qstr *name, const struct gfs2_inode *nip, struct gfs2_diradd *da)

    Add new filename into directory

    :param struct inode \*inode:
        The directory inode

    :param const struct qstr \*name:
        The new name

    :param const struct gfs2_inode \*nip:
        The GFS2 inode to be linked in to the directory

    :param struct gfs2_diradd \*da:
        The directory addition info

.. _`gfs2_dir_add.description`:

Description
-----------

If the call to gfs2_diradd_alloc_required resulted in there being
no need to allocate any new directory blocks, then it will contain
a pointer to the directory entry and the bh in which it resides. We
can use that without having to repeat the search. If there was no
free space, then we must now create more space.

.. _`gfs2_dir_add.return`:

Return
------

0 on success, error code on failure

.. _`gfs2_dir_del`:

gfs2_dir_del
============

.. c:function:: int gfs2_dir_del(struct gfs2_inode *dip, const struct dentry *dentry)

    Delete a directory entry

    :param struct gfs2_inode \*dip:
        The GFS2 inode

    :param const struct dentry \*dentry:
        *undescribed*

.. _`gfs2_dir_del.return`:

Return
------

0 on success, error code on failure

.. _`gfs2_dir_mvino`:

gfs2_dir_mvino
==============

.. c:function:: int gfs2_dir_mvino(struct gfs2_inode *dip, const struct qstr *filename, const struct gfs2_inode *nip, unsigned int new_type)

    Change inode number of directory entry

    :param struct gfs2_inode \*dip:
        The GFS2 inode

    :param const struct qstr \*filename:
        *undescribed*

    :param const struct gfs2_inode \*nip:
        *undescribed*

    :param unsigned int new_type:
        *undescribed*

.. _`gfs2_dir_mvino.description`:

Description
-----------

This routine changes the inode number of a directory entry.  It's used
by rename to change ".." when a directory is moved.
Assumes a glock is held on dvp.

.. _`gfs2_dir_mvino.return`:

Return
------

errno

.. _`leaf_dealloc`:

leaf_dealloc
============

.. c:function:: int leaf_dealloc(struct gfs2_inode *dip, u32 index, u32 len, u64 leaf_no, struct buffer_head *leaf_bh, int last_dealloc)

    Deallocate a directory leaf

    :param struct gfs2_inode \*dip:
        the directory

    :param u32 index:
        the hash table offset in the directory

    :param u32 len:
        the number of pointers to this leaf

    :param u64 leaf_no:
        the leaf number

    :param struct buffer_head \*leaf_bh:
        buffer_head for the starting leaf

    :param int last_dealloc:
        *undescribed*

.. _`leaf_dealloc.last_dealloc`:

last_dealloc
------------

1 if this is the final dealloc for the leaf, else 0

.. _`leaf_dealloc.return`:

Return
------

errno

.. _`gfs2_dir_exhash_dealloc`:

gfs2_dir_exhash_dealloc
=======================

.. c:function:: int gfs2_dir_exhash_dealloc(struct gfs2_inode *dip)

    free all the leaf blocks in a directory

    :param struct gfs2_inode \*dip:
        the directory

.. _`gfs2_dir_exhash_dealloc.description`:

Description
-----------

Dealloc all on-disk directory leaves to FREEMETA state
Change on-disk inode type to "regular file"

.. _`gfs2_dir_exhash_dealloc.return`:

Return
------

errno

.. _`gfs2_diradd_alloc_required`:

gfs2_diradd_alloc_required
==========================

.. c:function:: int gfs2_diradd_alloc_required(struct inode *inode, const struct qstr *name, struct gfs2_diradd *da)

    find if adding entry will require an allocation

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*name:
        *undescribed*

    :param struct gfs2_diradd \*da:
        The structure to return dir alloc info

.. _`gfs2_diradd_alloc_required.return`:

Return
------

0 if ok, -ve on error

.. This file was automatic generated / don't edit.


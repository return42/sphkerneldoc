.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/xattr.c

.. _`ea_calc_size`:

ea_calc_size
============

.. c:function:: int ea_calc_size(struct gfs2_sbd *sdp, unsigned int nsize, size_t dsize, unsigned int *size)

    returns the acutal number of bytes the request will take up (not counting any unstuffed data blocks)

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param unsigned int nsize:
        *undescribed*

    :param size_t dsize:
        *undescribed*

    :param unsigned int \*size:
        *undescribed*

.. _`ea_calc_size.return`:

Return
------

1 if the EA should be stuffed

.. _`ea_dealloc_unstuffed`:

ea_dealloc_unstuffed
====================

.. c:function:: int ea_dealloc_unstuffed(struct gfs2_inode *ip, struct buffer_head *bh, struct gfs2_ea_header *ea, struct gfs2_ea_header *prev, void *private)

    :param struct gfs2_inode \*ip:
        *undescribed*

    :param struct buffer_head \*bh:
        *undescribed*

    :param struct gfs2_ea_header \*ea:
        *undescribed*

    :param struct gfs2_ea_header \*prev:
        *undescribed*

    :param void \*private:
        *undescribed*

.. _`ea_dealloc_unstuffed.description`:

Description
-----------

Take advantage of the fact that all unstuffed blocks are
allocated from the same RG.  But watch, this may not always
be true.

.. _`ea_dealloc_unstuffed.return`:

Return
------

errno

.. _`gfs2_listxattr`:

gfs2_listxattr
==============

.. c:function:: ssize_t gfs2_listxattr(struct dentry *dentry, char *buffer, size_t size)

    List gfs2 extended attributes

    :param struct dentry \*dentry:
        The dentry whose inode we are interested in

    :param char \*buffer:
        The buffer to write the results

    :param size_t size:
        The size of the buffer

.. _`gfs2_listxattr.return`:

Return
------

actual size of data on success, -errno on error

.. _`gfs2_iter_unstuffed`:

gfs2_iter_unstuffed
===================

.. c:function:: int gfs2_iter_unstuffed(struct gfs2_inode *ip, struct gfs2_ea_header *ea, const char *din, char *dout)

    copies the unstuffed xattr data to/from the request buffer

    :param struct gfs2_inode \*ip:
        The GFS2 inode

    :param struct gfs2_ea_header \*ea:
        The extended attribute header structure

    :param const char \*din:
        The data to be copied in

    :param char \*dout:
        The data to be copied out (one of din,dout will be NULL)

.. _`gfs2_iter_unstuffed.return`:

Return
------

errno

.. _`__gfs2_xattr_get`:

\__gfs2_xattr_get
=================

.. c:function:: int __gfs2_xattr_get(struct inode *inode, const char *name, void *buffer, size_t size, int type)

    Get a GFS2 extended attribute

    :param struct inode \*inode:
        The inode

    :param const char \*name:
        The name of the extended attribute

    :param void \*buffer:
        The buffer to write the result into

    :param size_t size:
        The size of the buffer

    :param int type:
        The type of extended attribute

.. _`__gfs2_xattr_get.return`:

Return
------

actual size of data on success, -errno on error

.. _`ea_alloc_blk`:

ea_alloc_blk
============

.. c:function:: int ea_alloc_blk(struct gfs2_inode *ip, struct buffer_head **bhp)

    allocates a new block for extended attributes.

    :param struct gfs2_inode \*ip:
        A pointer to the inode that's getting extended attributes

    :param struct buffer_head \*\*bhp:
        Pointer to pointer to a struct buffer_head

.. _`ea_alloc_blk.return`:

Return
------

errno

.. _`ea_write`:

ea_write
========

.. c:function:: int ea_write(struct gfs2_inode *ip, struct gfs2_ea_header *ea, struct gfs2_ea_request *er)

    writes the request info to an ea, creating new blocks if necessary

    :param struct gfs2_inode \*ip:
        inode that is being modified

    :param struct gfs2_ea_header \*ea:
        the location of the new ea in a block

    :param struct gfs2_ea_request \*er:
        the write request

.. _`ea_write.note`:

Note
----

does not update ea_rec_len or the GFS2_EAFLAG_LAST bin of ea_flags

returns : errno

.. _`ea_init`:

ea_init
=======

.. c:function:: int ea_init(struct gfs2_inode *ip, int type, const char *name, const void *data, size_t size)

    initializes a new eattr block

    :param struct gfs2_inode \*ip:
        *undescribed*

    :param int type:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param const void \*data:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`ea_init.return`:

Return
------

errno

.. _`gfs2_xattr_remove`:

gfs2_xattr_remove
=================

.. c:function:: int gfs2_xattr_remove(struct gfs2_inode *ip, int type, const char *name)

    Remove a GFS2 extended attribute

    :param struct gfs2_inode \*ip:
        The inode

    :param int type:
        The type of the extended attribute

    :param const char \*name:
        The name of the extended attribute

.. _`gfs2_xattr_remove.description`:

Description
-----------

This is not called directly by the VFS since we use the (common)
scheme of making a "set with NULL data" mean a remove request. Note
that this is different from a set with zero length data.

.. _`gfs2_xattr_remove.return`:

Return
------

0, or errno on failure

.. _`__gfs2_xattr_set`:

\__gfs2_xattr_set
=================

.. c:function:: int __gfs2_xattr_set(struct inode *inode, const char *name, const void *value, size_t size, int flags, int type)

    Set (or remove) a GFS2 extended attribute

    :param struct inode \*inode:
        *undescribed*

    :param const char \*name:
        The name of the extended attribute

    :param const void \*value:
        The value of the extended attribute (NULL for remove)

    :param size_t size:
        The size of the \ ``value``\  argument

    :param int flags:
        Create or Replace

    :param int type:
        The type of the extended attribute

.. _`__gfs2_xattr_set.description`:

Description
-----------

See \ :c:func:`gfs2_xattr_remove`\  for details of the removal of xattrs.

.. _`__gfs2_xattr_set.return`:

Return
------

0 or errno on failure

.. _`gfs2_ea_dealloc`:

gfs2_ea_dealloc
===============

.. c:function:: int gfs2_ea_dealloc(struct gfs2_inode *ip)

    deallocate the extended attribute fork

    :param struct gfs2_inode \*ip:
        the inode

.. _`gfs2_ea_dealloc.return`:

Return
------

errno

.. This file was automatic generated / don't edit.


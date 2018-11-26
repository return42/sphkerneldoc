.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/xattr.c

.. _`ea_calc_size`:

ea_calc_size
============

.. c:function:: int ea_calc_size(struct gfs2_sbd *sdp, unsigned int nsize, size_t dsize, unsigned int *size)

    returns the acutal number of bytes the request will take up (not counting any unstuffed data blocks)

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param nsize:
        *undescribed*
    :type nsize: unsigned int

    :param dsize:
        *undescribed*
    :type dsize: size_t

    :param size:
        *undescribed*
    :type size: unsigned int \*

.. _`ea_calc_size.return`:

Return
------

1 if the EA should be stuffed

.. _`ea_dealloc_unstuffed`:

ea_dealloc_unstuffed
====================

.. c:function:: int ea_dealloc_unstuffed(struct gfs2_inode *ip, struct buffer_head *bh, struct gfs2_ea_header *ea, struct gfs2_ea_header *prev, void *private)

    :param ip:
        *undescribed*
    :type ip: struct gfs2_inode \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*

    :param ea:
        *undescribed*
    :type ea: struct gfs2_ea_header \*

    :param prev:
        *undescribed*
    :type prev: struct gfs2_ea_header \*

    :param private:
        *undescribed*
    :type private: void \*

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

    :param dentry:
        The dentry whose inode we are interested in
    :type dentry: struct dentry \*

    :param buffer:
        The buffer to write the results
    :type buffer: char \*

    :param size:
        The size of the buffer
    :type size: size_t

.. _`gfs2_listxattr.return`:

Return
------

actual size of data on success, -errno on error

.. _`gfs2_iter_unstuffed`:

gfs2_iter_unstuffed
===================

.. c:function:: int gfs2_iter_unstuffed(struct gfs2_inode *ip, struct gfs2_ea_header *ea, const char *din, char *dout)

    copies the unstuffed xattr data to/from the request buffer

    :param ip:
        The GFS2 inode
    :type ip: struct gfs2_inode \*

    :param ea:
        The extended attribute header structure
    :type ea: struct gfs2_ea_header \*

    :param din:
        The data to be copied in
    :type din: const char \*

    :param dout:
        The data to be copied out (one of din,dout will be NULL)
    :type dout: char \*

.. _`gfs2_iter_unstuffed.return`:

Return
------

errno

.. _`__gfs2_xattr_get`:

\__gfs2_xattr_get
=================

.. c:function:: int __gfs2_xattr_get(struct inode *inode, const char *name, void *buffer, size_t size, int type)

    Get a GFS2 extended attribute

    :param inode:
        The inode
    :type inode: struct inode \*

    :param name:
        The name of the extended attribute
    :type name: const char \*

    :param buffer:
        The buffer to write the result into
    :type buffer: void \*

    :param size:
        The size of the buffer
    :type size: size_t

    :param type:
        The type of extended attribute
    :type type: int

.. _`__gfs2_xattr_get.return`:

Return
------

actual size of data on success, -errno on error

.. _`ea_alloc_blk`:

ea_alloc_blk
============

.. c:function:: int ea_alloc_blk(struct gfs2_inode *ip, struct buffer_head **bhp)

    allocates a new block for extended attributes.

    :param ip:
        A pointer to the inode that's getting extended attributes
    :type ip: struct gfs2_inode \*

    :param bhp:
        Pointer to pointer to a struct buffer_head
    :type bhp: struct buffer_head \*\*

.. _`ea_alloc_blk.return`:

Return
------

errno

.. _`ea_write`:

ea_write
========

.. c:function:: int ea_write(struct gfs2_inode *ip, struct gfs2_ea_header *ea, struct gfs2_ea_request *er)

    writes the request info to an ea, creating new blocks if necessary

    :param ip:
        inode that is being modified
    :type ip: struct gfs2_inode \*

    :param ea:
        the location of the new ea in a block
    :type ea: struct gfs2_ea_header \*

    :param er:
        the write request
    :type er: struct gfs2_ea_request \*

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

    :param ip:
        *undescribed*
    :type ip: struct gfs2_inode \*

    :param type:
        *undescribed*
    :type type: int

    :param name:
        *undescribed*
    :type name: const char \*

    :param data:
        *undescribed*
    :type data: const void \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`ea_init.return`:

Return
------

errno

.. _`gfs2_xattr_remove`:

gfs2_xattr_remove
=================

.. c:function:: int gfs2_xattr_remove(struct gfs2_inode *ip, int type, const char *name)

    Remove a GFS2 extended attribute

    :param ip:
        The inode
    :type ip: struct gfs2_inode \*

    :param type:
        The type of the extended attribute
    :type type: int

    :param name:
        The name of the extended attribute
    :type name: const char \*

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

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param name:
        The name of the extended attribute
    :type name: const char \*

    :param value:
        The value of the extended attribute (NULL for remove)
    :type value: const void \*

    :param size:
        The size of the \ ``value``\  argument
    :type size: size_t

    :param flags:
        Create or Replace
    :type flags: int

    :param type:
        The type of the extended attribute
    :type type: int

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

    :param ip:
        the inode
    :type ip: struct gfs2_inode \*

.. _`gfs2_ea_dealloc.return`:

Return
------

errno

.. This file was automatic generated / don't edit.


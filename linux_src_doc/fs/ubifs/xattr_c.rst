.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/xattr.c

.. _`create_xattr`:

create_xattr
============

.. c:function:: int create_xattr(struct ubifs_info *c, struct inode *host, const struct fscrypt_name *nm, const void *value, int size)

    create an extended attribute.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct inode \*host:
        host inode

    :param const struct fscrypt_name \*nm:
        extended attribute name

    :param const void \*value:
        extended attribute value

    :param int size:
        size of extended attribute value

.. _`create_xattr.description`:

Description
-----------

This is a helper function which creates an extended attribute of name \ ``nm``\ 
and value \ ``value``\  for inode \ ``host``\ . The host inode is also updated on flash
because the ctime and extended attribute accounting data changes. This
function returns zero in case of success and a negative error code in case
of failure.

.. _`change_xattr`:

change_xattr
============

.. c:function:: int change_xattr(struct ubifs_info *c, struct inode *host, struct inode *inode, const void *value, int size)

    change an extended attribute.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct inode \*host:
        host inode

    :param struct inode \*inode:
        extended attribute inode

    :param const void \*value:
        extended attribute value

    :param int size:
        size of extended attribute value

.. _`change_xattr.description`:

Description
-----------

This helper function changes the value of extended attribute \ ``inode``\  with new
data from \ ``value``\ . Returns zero in case of success and a negative error code
in case of failure.

.. _`ubifs_evict_xattr_inode`:

ubifs_evict_xattr_inode
=======================

.. c:function:: void ubifs_evict_xattr_inode(struct ubifs_info *c, ino_t xattr_inum)

    Evict an xattr inode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t xattr_inum:
        xattr inode number

.. _`ubifs_evict_xattr_inode.description`:

Description
-----------

When an inode that hosts xattrs is being removed we have to make sure
that cached inodes of the xattrs also get removed from the inode cache
otherwise we'd waste memory. This function looks up an inode from the
inode cache and clears the link counter such that \ :c:func:`iput`\  will evict
the inode.

.. This file was automatic generated / don't edit.


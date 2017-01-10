.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/xattr_security.c

.. _`ll_initxattrs`:

ll_initxattrs
=============

.. c:function:: int ll_initxattrs(struct inode *inode, const struct xattr *xattr_array, void *fs_info)

    that takes care of setting xattrs

    :param struct inode \*inode:
        *undescribed*

    :param const struct xattr \*xattr_array:
        *undescribed*

    :param void \*fs_info:
        *undescribed*

.. _`ll_initxattrs.description`:

Description
-----------

Get security context of \ ``inode``\  from \ ``xattr_array``\ ,
and put it in 'security.xxx' xattr of dentry
stored in \ ``fs_info``\ .

\retval 0        success
\retval -ENOMEM  if no memory could be allocated for xattr name
\retval < 0      failure to set xattr

.. _`ll_init_security`:

ll_init_security
================

.. c:function:: int ll_init_security(struct dentry *dentry, struct inode *inode, struct inode *dir)

    :param struct dentry \*dentry:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

    :param struct inode \*dir:
        *undescribed*

.. _`ll_init_security.description`:

Description
-----------

Get security context of \ ``inode``\  in \ ``dir``\ ,
and put it in 'security.xxx' xattr of \ ``dentry``\ .

\retval 0        success, or SELinux is disabled
\retval -ENOMEM  if no memory could be allocated for xattr name
\retval < 0      failure to get security context or set xattr

.. This file was automatic generated / don't edit.


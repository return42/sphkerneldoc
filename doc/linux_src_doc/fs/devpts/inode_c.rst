.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/devpts/inode.c

.. _`devpts_pty_new`:

devpts_pty_new
==============

.. c:function:: struct dentry *devpts_pty_new(struct pts_fs_info *fsi, int index, void *priv)

    - create a new inode in /dev/pts/

    :param struct pts_fs_info \*fsi:
        *undescribed*

    :param int index:
        used as a name of the node

    :param void \*priv:
        what's given back by devpts_get_priv

.. _`devpts_pty_new.description`:

Description
-----------

The created inode is returned. Remove it from /dev/pts/ by devpts_pty_kill.

.. _`devpts_get_priv`:

devpts_get_priv
===============

.. c:function:: void *devpts_get_priv(struct dentry *dentry)

    - get private data for a slave

    :param struct dentry \*dentry:
        *undescribed*

.. _`devpts_get_priv.description`:

Description
-----------

Returns whatever was passed as priv in devpts_pty_new for a given inode.

.. _`devpts_pty_kill`:

devpts_pty_kill
===============

.. c:function:: void devpts_pty_kill(struct dentry *dentry)

    - remove inode form /dev/pts/

    :param struct dentry \*dentry:
        *undescribed*

.. _`devpts_pty_kill.description`:

Description
-----------

This is an inverse operation of devpts_pty_new.

.. This file was automatic generated / don't edit.


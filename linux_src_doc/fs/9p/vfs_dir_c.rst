.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_dir.c

.. _`p9_rdir`:

struct p9_rdir
==============

.. c:type:: struct p9_rdir

    readdir accounting

.. _`p9_rdir.definition`:

Definition
----------

.. code-block:: c

    struct p9_rdir {
        int head;
        int tail;
        uint8_t buf[];
    }

.. _`p9_rdir.members`:

Members
-------

head
    start offset of current dirread buffer

tail
    end offset of current dirread buffer

buf
    dirread buffer

.. _`p9_rdir.description`:

Description
-----------

private structure for keeping track of readdir
allocated on demand

.. _`dt_type`:

dt_type
=======

.. c:function:: int dt_type(struct p9_wstat *mistat)

    return file type

    :param mistat:
        mistat structure
    :type mistat: struct p9_wstat \*

.. _`v9fs_alloc_rdir_buf`:

v9fs_alloc_rdir_buf
===================

.. c:function:: struct p9_rdir *v9fs_alloc_rdir_buf(struct file *filp, int buflen)

    Allocate buffer used for read and readdir

    :param filp:
        opened file structure
    :type filp: struct file \*

    :param buflen:
        Length in bytes of buffer to allocate
    :type buflen: int

.. _`v9fs_dir_readdir`:

v9fs_dir_readdir
================

.. c:function:: int v9fs_dir_readdir(struct file *file, struct dir_context *ctx)

    iterate through a directory

    :param file:
        opened file structure
    :type file: struct file \*

    :param ctx:
        actor we feed the entries to
    :type ctx: struct dir_context \*

.. _`v9fs_dir_readdir_dotl`:

v9fs_dir_readdir_dotl
=====================

.. c:function:: int v9fs_dir_readdir_dotl(struct file *file, struct dir_context *ctx)

    iterate through a directory

    :param file:
        opened file structure
    :type file: struct file \*

    :param ctx:
        actor we feed the entries to
    :type ctx: struct dir_context \*

.. _`v9fs_dir_release`:

v9fs_dir_release
================

.. c:function:: int v9fs_dir_release(struct inode *inode, struct file *filp)

    close a directory

    :param inode:
        inode of the directory
    :type inode: struct inode \*

    :param filp:
        file pointer to a directory
    :type filp: struct file \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_appraise.c

.. _`ima_inode_post_setattr`:

ima_inode_post_setattr
======================

.. c:function:: void ima_inode_post_setattr(struct dentry *dentry)

    reflect file metadata changes

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

.. _`ima_inode_post_setattr.description`:

Description
-----------

Changes to a dentry's metadata might result in needing to appraise.

This function is called from \ :c:func:`notify_change`\ , which expects the caller
to lock the inode's i_mutex.

.. This file was automatic generated / don't edit.


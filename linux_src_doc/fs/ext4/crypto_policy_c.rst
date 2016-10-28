.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/crypto_policy.c

.. _`ext4_inherit_context`:

ext4_inherit_context
====================

.. c:function:: int ext4_inherit_context(struct inode *parent, struct inode *child)

    Sets a child context from its parent

    :param struct inode \*parent:
        Parent inode from which the context is inherited.

    :param struct inode \*child:
        Child inode that inherits the context from \ ``parent``\ .

.. _`ext4_inherit_context.return`:

Return
------

Zero on success, non-zero otherwise

.. This file was automatic generated / don't edit.


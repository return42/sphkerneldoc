.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/policy.c

.. _`fscrypt_inherit_context`:

fscrypt_inherit_context
=======================

.. c:function:: int fscrypt_inherit_context(struct inode *parent, struct inode *child, void *fs_data, bool preload)

    Sets a child context from its parent

    :param struct inode \*parent:
        Parent inode from which the context is inherited.

    :param struct inode \*child:
        Child inode that inherits the context from \ ``parent``\ .

    :param void \*fs_data:
        private data given by FS.

    :param bool preload:
        preload child i_crypt_info

.. _`fscrypt_inherit_context.return`:

Return
------

Zero on success, non-zero otherwise

.. This file was automatic generated / don't edit.


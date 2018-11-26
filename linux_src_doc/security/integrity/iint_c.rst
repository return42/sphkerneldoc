.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/iint.c

.. _`integrity_inode_get`:

integrity_inode_get
===================

.. c:function:: struct integrity_iint_cache *integrity_inode_get(struct inode *inode)

    find or allocate an iint associated with an inode

    :param inode:
        pointer to the inode
    :type inode: struct inode \*

.. _`integrity_inode_get.description`:

Description
-----------

Caller must lock i_mutex

.. _`integrity_inode_free`:

integrity_inode_free
====================

.. c:function:: void integrity_inode_free(struct inode *inode)

    called on security_inode_free

    :param inode:
        pointer to the inode
    :type inode: struct inode \*

.. _`integrity_inode_free.description`:

Description
-----------

Free the integrity information(iint) associated with an inode.

.. This file was automatic generated / don't edit.


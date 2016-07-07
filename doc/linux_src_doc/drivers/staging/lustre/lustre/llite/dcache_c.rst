.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/dcache.c

.. _`ll_ddelete`:

ll_ddelete
==========

.. c:function:: int ll_ddelete(const struct dentry *de)

    :param const struct dentry \*de:
        *undescribed*

.. _`ll_ddelete.whether-or-not-it-should-cache-it`:

whether or not it should cache it
---------------------------------

- return 1 to delete the dentry immediately
- return 0 to cache the dentry
Should NOT be called with the dcache lock, see fs/dcache.c

.. This file was automatic generated / don't edit.


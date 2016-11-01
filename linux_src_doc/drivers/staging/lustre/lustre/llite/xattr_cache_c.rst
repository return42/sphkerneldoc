.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/xattr_cache.c

.. _`ll_xattr_cache_init`:

ll_xattr_cache_init
===================

.. c:function:: void ll_xattr_cache_init(struct ll_inode_info *lli)

    :param struct ll_inode_info \*lli:
        *undescribed*

.. _`ll_xattr_cache_init.description`:

Description
-----------

This initializes the xattr list and marks cache presence.

.. _`ll_xattr_cache_find`:

ll_xattr_cache_find
===================

.. c:function:: int ll_xattr_cache_find(struct list_head *cache, const char *xattr_name, struct ll_xattr_entry **xattr)

    :param struct list_head \*cache:
        *undescribed*

    :param const char \*xattr_name:
        *undescribed*

    :param struct ll_xattr_entry \*\*xattr:
        *undescribed*

.. _`ll_xattr_cache_find.description`:

Description
-----------

Find in \ ``cache``\  and return \ ``xattr_name``\  attribute in \ ``xattr``\ ,
for the NULL \ ``xattr_name``\  return the first cached \ ``xattr``\ .

\retval 0        success
\retval -ENODATA if not found

.. _`ll_xattr_cache_add`:

ll_xattr_cache_add
==================

.. c:function:: int ll_xattr_cache_add(struct list_head *cache, const char *xattr_name, const char *xattr_val, unsigned xattr_val_len)

    :param struct list_head \*cache:
        *undescribed*

    :param const char \*xattr_name:
        *undescribed*

    :param const char \*xattr_val:
        *undescribed*

    :param unsigned xattr_val_len:
        *undescribed*

.. _`ll_xattr_cache_add.description`:

Description
-----------

Add \ ``xattr_name``\  attr with \ ``xattr_val``\  value and \ ``xattr_val_len``\  length,

\retval 0       success
\retval -ENOMEM if no memory could be allocated for the cached attr
\retval -EPROTO if duplicate xattr is being added

.. _`ll_xattr_cache_del`:

ll_xattr_cache_del
==================

.. c:function:: int ll_xattr_cache_del(struct list_head *cache, const char *xattr_name)

    :param struct list_head \*cache:
        *undescribed*

    :param const char \*xattr_name:
        *undescribed*

.. _`ll_xattr_cache_del.description`:

Description
-----------

Remove \ ``xattr_name``\  attribute from \ ``cache``\ .

\retval 0        success
\retval -ENODATA if \ ``xattr_name``\  is not cached

.. _`ll_xattr_cache_list`:

ll_xattr_cache_list
===================

.. c:function:: int ll_xattr_cache_list(struct list_head *cache, char *xld_buffer, int xld_size)

    :param struct list_head \*cache:
        *undescribed*

    :param char \*xld_buffer:
        *undescribed*

    :param int xld_size:
        *undescribed*

.. _`ll_xattr_cache_list.description`:

Description
-----------

Walk over cached attributes in \ ``cache``\  and
fill in \ ``xld_buffer``\  or only calculate buffer
size if \ ``xld_buffer``\  is NULL.

\retval >= 0     buffer list size
\retval -ENODATA if the list cannot fit \ ``xld_size``\  buffer

.. _`ll_xattr_cache_valid`:

ll_xattr_cache_valid
====================

.. c:function:: int ll_xattr_cache_valid(struct ll_inode_info *lli)

    :param struct ll_inode_info \*lli:
        *undescribed*

.. _`ll_xattr_cache_valid.description`:

Description
-----------

\retval 0 \ ``cache``\  is not initialized
\retval 1 \ ``cache``\  is initialized

.. _`ll_xattr_cache_destroy_locked`:

ll_xattr_cache_destroy_locked
=============================

.. c:function:: int ll_xattr_cache_destroy_locked(struct ll_inode_info *lli)

    :param struct ll_inode_info \*lli:
        *undescribed*

.. _`ll_xattr_cache_destroy_locked.description`:

Description
-----------

Free all xattr memory. \ ``lli``\  is the inode info pointer.

\retval 0 no error occurred

.. _`ll_xattr_find_get_lock`:

ll_xattr_find_get_lock
======================

.. c:function:: int ll_xattr_find_get_lock(struct inode *inode, struct lookup_intent *oit, struct ptlrpc_request **req)

    :param struct inode \*inode:
        *undescribed*

    :param struct lookup_intent \*oit:
        *undescribed*

    :param struct ptlrpc_request \*\*req:
        *undescribed*

.. _`ll_xattr_find_get_lock.description`:

Description
-----------

Find or request an LDLM lock with xattr data.
Since LDLM does not provide API for atomic match_or_enqueue,
the function handles it with a separate enq lock.
If successful, the function exits with the list lock held.

\retval 0       no error occurred
\retval -ENOMEM not enough memory

.. _`ll_xattr_cache_refill`:

ll_xattr_cache_refill
=====================

.. c:function:: int ll_xattr_cache_refill(struct inode *inode, struct lookup_intent *oit)

    :param struct inode \*inode:
        *undescribed*

    :param struct lookup_intent \*oit:
        *undescribed*

.. _`ll_xattr_cache_refill.description`:

Description
-----------

Fetch and cache the whole of xattrs for \ ``inode``\ , acquiring
a read or a write xattr lock depending on operation in \ ``oit``\ .
Intent is dropped on exit unless the operation is setxattr.

\retval 0       no error occurred
\retval -EPROTO network protocol error
\retval -ENOMEM not enough memory for the cache

.. _`ll_xattr_cache_get`:

ll_xattr_cache_get
==================

.. c:function:: int ll_xattr_cache_get(struct inode *inode, const char *name, char *buffer, size_t size, __u64 valid)

    through cache.

    :param struct inode \*inode:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param char \*buffer:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param __u64 valid:
        *undescribed*

.. _`ll_xattr_cache_get.description`:

Description
-----------

Get the xattr value (@valid has OBD_MD_FLXATTR set) of \ ``name``\  or
list xattr names (@valid has OBD_MD_FLXATTRLS set) for \ ``inode``\ .
The resulting value/list is stored in \ ``buffer``\  if the former
is not larger than \ ``size``\ .

\retval 0        no error occurred
\retval -EPROTO  network protocol error
\retval -ENOMEM  not enough memory for the cache
\retval -ERANGE  the buffer is not large enough
\retval -ENODATA no such attr or the list is empty

.. This file was automatic generated / don't edit.


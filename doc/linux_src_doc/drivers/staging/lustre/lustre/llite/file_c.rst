.. -*- coding: utf-8; mode: rst -*-

======
file.c
======


.. _`ll_prepare_close`:

ll_prepare_close
================

.. c:function:: void ll_prepare_close (struct inode *inode, struct md_op_data *op_data, struct obd_client_handle *och)

    :param struct inode \*inode:

        *undescribed*

    :param struct md_op_data \*op_data:

        *undescribed*

    :param struct obd_client_handle \*och:

        *undescribed*



.. _`ll_prepare_close.description`:

Description
-----------

the CLOSE rpc.



.. _`ll_ioepoch_open`:

ll_ioepoch_open
===============

.. c:function:: void ll_ioepoch_open (struct ll_inode_info *lli, __u64 ioepoch)

    :param struct ll_inode_info \*lli:

        *undescribed*

    :param __u64 ioepoch:

        *undescribed*



.. _`ll_ioepoch_open.description`:

Description
-----------

not believe attributes if a few ioepoch holders exist. Attributes for
previous ioepoch if new one is opened are also skipped by MDS.



.. _`ll_lease_open`:

ll_lease_open
=============

.. c:function:: struct obd_client_handle *ll_lease_open (struct inode *inode, struct file *file, fmode_t fmode, __u64 open_flags)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*file:

        *undescribed*

    :param fmode_t fmode:

        *undescribed*

    :param __u64 open_flags:

        *undescribed*



.. _`ll_lease_close`:

ll_lease_close
==============

.. c:function:: int ll_lease_close (struct obd_client_handle *och, struct inode *inode, bool *lease_broken)

    :param struct obd_client_handle \*och:

        *undescribed*

    :param struct inode \*inode:

        *undescribed*

    :param bool \*lease_broken:

        *undescribed*



.. _`ll_lease_close.description`:

Description
-----------

It will check if the lease has ever broken.



.. _`ll_inode_getattr`:

ll_inode_getattr
================

.. c:function:: int ll_inode_getattr (struct inode *inode, struct obdo *obdo, __u64 ioepoch, int sync)

    :param struct inode \*inode:

        *undescribed*

    :param struct obdo \*obdo:

        *undescribed*

    :param __u64 ioepoch:

        *undescribed*

    :param int sync:

        *undescribed*



.. _`ll_inode_getattr.description`:

Description
-----------

If ``sync`` != 0, perform the getattr under the server-side lock.



.. _`ll_release_openhandle`:

ll_release_openhandle
=====================

.. c:function:: int ll_release_openhandle (struct inode *inode, struct lookup_intent *it)

    :param struct inode \*inode:

        *undescribed*

    :param struct lookup_intent \*it:

        *undescribed*



.. _`ll_release_openhandle.description`:

Description
-----------


\param inode  [in]     inode in question
\param it     [in,out] intent which contains open info and result

\retval 0     success
\retval <0    failure



.. _`ll_do_fiemap`:

ll_do_fiemap
============

.. c:function:: int ll_do_fiemap (struct inode *inode, struct ll_user_fiemap *fiemap, size_t num_bytes)

    :param struct inode \*inode:

        *undescribed*

    :param struct ll_user_fiemap \*fiemap:

        *undescribed*

    :param size_t num_bytes:

        *undescribed*



.. _`ll_do_fiemap.description`:

Description
-----------

Make the FIEMAP get_info call and returns the result.



.. _`cl_sync_file_range`:

cl_sync_file_range
==================

.. c:function:: int cl_sync_file_range (struct inode *inode, loff_t start, loff_t end, enum cl_fsync_mode mode, int ignore_layout)

    :param struct inode \*inode:

        *undescribed*

    :param loff_t start:

        *undescribed*

    :param loff_t end:

        *undescribed*

    :param enum cl_fsync_mode mode:

        *undescribed*

    :param int ignore_layout:

        *undescribed*



.. _`cl_sync_file_range.description`:

Description
-----------

if ``mode`` is not CL_FSYNC_LOCAL, it will send OST_SYNC RPCs to OST.

Return how many pages have been written.



.. _`ll_have_md_lock`:

ll_have_md_lock
===============

.. c:function:: int ll_have_md_lock (struct inode *inode, __u64 *bits, enum ldlm_mode l_req_mode)

    :param struct inode \*inode:

        *undescribed*

    :param __u64 \*bits:

        *undescribed*

    :param enum ldlm_mode l_req_mode:

        *undescribed*



.. _`ll_have_md_lock.description`:

Description
-----------

- bits can be in different locks
- if found clear the common lock bits in \*bits
- the bits not found, are kept in \*bits
\param inode [IN]
\param bits [IN] searched lock bits [IN]
\param l_req_mode [IN] searched lock mode
\retval boolean, true iff all bits are found



.. _`ll_layout_lock_set`:

ll_layout_lock_set
==================

.. c:function:: int ll_layout_lock_set (struct lustre_handle *lockh, enum ldlm_mode mode, struct inode *inode, __u32 *gen, bool reconf)

    :param struct lustre_handle \*lockh:

        *undescribed*

    :param enum ldlm_mode mode:

        *undescribed*

    :param struct inode \*inode:

        *undescribed*

    :param __u32 \*gen:

        *undescribed*

    :param bool reconf:

        *undescribed*



.. _`ll_layout_lock_set.description`:

Description
-----------

in this function.



.. _`ll_layout_refresh`:

ll_layout_refresh
=================

.. c:function:: int ll_layout_refresh (struct inode *inode, __u32 *gen)

    :param struct inode \*inode:

        *undescribed*

    :param __u32 \*gen:

        *undescribed*



.. _`ll_layout_refresh.description`:

Description
-----------

or enqueues it if it doesn't have one in cache.

This function will not hold layout lock so it may be revoked any time after
this function returns. Any operations depend on layout should be redone
in that case.

This function should be called before :c:func:`lov_io_init` to get an uptodate
layout version, the caller should save the version number and after IO
is finished, this function should be called again to verify that layout
is not changed during IO time.



.. _`ll_layout_restore`:

ll_layout_restore
=================

.. c:function:: int ll_layout_restore (struct inode *inode)

    :param struct inode \*inode:

        *undescribed*


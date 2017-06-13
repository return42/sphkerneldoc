.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/misc.h

.. _`ubifs_zn_dirty`:

ubifs_zn_dirty
==============

.. c:function:: int ubifs_zn_dirty(const struct ubifs_znode *znode)

    check if znode is dirty.

    :param const struct ubifs_znode \*znode:
        znode to check

.. _`ubifs_zn_dirty.description`:

Description
-----------

This helper function returns \ ``1``\  if \ ``znode``\  is dirty and \ ``0``\  otherwise.

.. _`ubifs_zn_obsolete`:

ubifs_zn_obsolete
=================

.. c:function:: int ubifs_zn_obsolete(const struct ubifs_znode *znode)

    check if znode is obsolete.

    :param const struct ubifs_znode \*znode:
        znode to check

.. _`ubifs_zn_obsolete.description`:

Description
-----------

This helper function returns \ ``1``\  if \ ``znode``\  is obsolete and \ ``0``\  otherwise.

.. _`ubifs_zn_cow`:

ubifs_zn_cow
============

.. c:function:: int ubifs_zn_cow(const struct ubifs_znode *znode)

    check if znode has to be copied on write.

    :param const struct ubifs_znode \*znode:
        znode to check

.. _`ubifs_zn_cow.description`:

Description
-----------

This helper function returns \ ``1``\  if \ ``znode``\  is has COW flag set and \ ``0``\ 
otherwise.

.. _`ubifs_wake_up_bgt`:

ubifs_wake_up_bgt
=================

.. c:function:: void ubifs_wake_up_bgt(struct ubifs_info *c)

    wake up background thread.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_tnc_find_child`:

ubifs_tnc_find_child
====================

.. c:function:: struct ubifs_znode *ubifs_tnc_find_child(struct ubifs_znode *znode, int start)

    find next child in znode.

    :param struct ubifs_znode \*znode:
        znode to search at

    :param int start:
        the zbranch index to start at

.. _`ubifs_tnc_find_child.description`:

Description
-----------

This helper function looks for znode child starting at index \ ``start``\ . Returns
the child or \ ``NULL``\  if no children were found.

.. _`ubifs_inode`:

ubifs_inode
===========

.. c:function:: struct ubifs_inode *ubifs_inode(const struct inode *inode)

    get UBIFS inode information by VFS 'struct inode' object.

    :param const struct inode \*inode:
        the VFS 'struct inode' pointer

.. _`ubifs_compr_present`:

ubifs_compr_present
===================

.. c:function:: int ubifs_compr_present(int compr_type)

    check if compressor was compiled in.

    :param int compr_type:
        compressor type to check

.. _`ubifs_compr_present.description`:

Description
-----------

This function returns \ ``1``\  of compressor of type \ ``compr_type``\  is present, and
\ ``0``\  if not.

.. _`ubifs_compr_name`:

ubifs_compr_name
================

.. c:function:: const char *ubifs_compr_name(int compr_type)

    get compressor name string by its type.

    :param int compr_type:
        compressor type

.. _`ubifs_compr_name.description`:

Description
-----------

This function returns compressor type string.

.. _`ubifs_wbuf_sync`:

ubifs_wbuf_sync
===============

.. c:function:: int ubifs_wbuf_sync(struct ubifs_wbuf *wbuf)

    synchronize write-buffer.

    :param struct ubifs_wbuf \*wbuf:
        write-buffer to synchronize

.. _`ubifs_wbuf_sync.description`:

Description
-----------

This is the same as as 'ubifs_wbuf_sync_nolock()' but it does not assume
that the write-buffer is already locked.

.. _`ubifs_encode_dev`:

ubifs_encode_dev
================

.. c:function:: int ubifs_encode_dev(union ubifs_dev_desc *dev, dev_t rdev)

    encode device node IDs.

    :param union ubifs_dev_desc \*dev:
        UBIFS device node information

    :param dev_t rdev:
        device IDs to encode

.. _`ubifs_encode_dev.description`:

Description
-----------

This is a helper function which encodes major/minor numbers of a device node
into UBIFS device node description. We use standard Linux "new" and "huge"
encodings.

.. _`ubifs_add_dirt`:

ubifs_add_dirt
==============

.. c:function:: int ubifs_add_dirt(struct ubifs_info *c, int lnum, int dirty)

    add dirty space to LEB properties.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB to add dirty space for

    :param int dirty:
        dirty space to add

.. _`ubifs_add_dirt.description`:

Description
-----------

This is a helper function which increased amount of dirty LEB space. Returns
zero in case of success and a negative error code in case of failure.

.. _`ubifs_return_leb`:

ubifs_return_leb
================

.. c:function:: int ubifs_return_leb(struct ubifs_info *c, int lnum)

    return LEB to lprops.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB to return

.. _`ubifs_return_leb.description`:

Description
-----------

This helper function cleans the "taken" flag of a logical eraseblock in the
lprops. Returns zero in case of success and a negative error code in case of
failure.

.. _`ubifs_idx_node_sz`:

ubifs_idx_node_sz
=================

.. c:function:: int ubifs_idx_node_sz(const struct ubifs_info *c, int child_cnt)

    return index node size.

    :param const struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int child_cnt:
        number of children of this index node

.. _`ubifs_idx_branch`:

ubifs_idx_branch
================

.. c:function:: struct ubifs_branch *ubifs_idx_branch(const struct ubifs_info *c, const struct ubifs_idx_node *idx, int bnum)

    return pointer to an index branch.

    :param const struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_idx_node \*idx:
        index node

    :param int bnum:
        branch number

.. _`ubifs_idx_key`:

ubifs_idx_key
=============

.. c:function:: void *ubifs_idx_key(const struct ubifs_info *c, const struct ubifs_idx_node *idx)

    return pointer to an index key.

    :param const struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_idx_node \*idx:
        index node

.. _`ubifs_tnc_lookup`:

ubifs_tnc_lookup
================

.. c:function:: int ubifs_tnc_lookup(struct ubifs_info *c, const union ubifs_key *key, void *node)

    look up a file-system node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        node key to lookup

    :param void \*node:
        the node is returned here

.. _`ubifs_tnc_lookup.description`:

Description
-----------

This function look up and reads node with key \ ``key``\ . The caller has to make
sure the \ ``node``\  buffer is large enough to fit the node. Returns zero in case
of success, \ ``-ENOENT``\  if the node was not found, and a negative error code in
case of failure.

.. _`ubifs_get_lprops`:

ubifs_get_lprops
================

.. c:function:: void ubifs_get_lprops(struct ubifs_info *c)

    get reference to LEB properties.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_get_lprops.description`:

Description
-----------

This function locks lprops. Lprops have to be unlocked by
'ubifs_release_lprops()'.

.. _`ubifs_release_lprops`:

ubifs_release_lprops
====================

.. c:function:: void ubifs_release_lprops(struct ubifs_info *c)

    release lprops lock.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_release_lprops.description`:

Description
-----------

This function has to be called after each 'ubifs_get_lprops()' call to
unlock lprops.

.. _`ubifs_next_log_lnum`:

ubifs_next_log_lnum
===================

.. c:function:: int ubifs_next_log_lnum(const struct ubifs_info *c, int lnum)

    switch to the next log LEB.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        current log LEB

.. _`ubifs_next_log_lnum.description`:

Description
-----------

This helper function returns the log LEB number which goes next after LEB
'lnum'.

.. This file was automatic generated / don't edit.


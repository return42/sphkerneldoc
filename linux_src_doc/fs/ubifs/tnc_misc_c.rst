.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/tnc_misc.c

.. _`ubifs_tnc_levelorder_next`:

ubifs_tnc_levelorder_next
=========================

.. c:function:: struct ubifs_znode *ubifs_tnc_levelorder_next(const struct ubifs_info *c, struct ubifs_znode *zr, struct ubifs_znode *znode)

    next TNC tree element in levelorder traversal.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param zr:
        root of the subtree to traverse
    :type zr: struct ubifs_znode \*

    :param znode:
        previous znode
    :type znode: struct ubifs_znode \*

.. _`ubifs_tnc_levelorder_next.description`:

Description
-----------

This function implements levelorder TNC traversal. The LNC is ignored.
Returns the next element or \ ``NULL``\  if \ ``znode``\  is already the last one.

.. _`ubifs_search_zbranch`:

ubifs_search_zbranch
====================

.. c:function:: int ubifs_search_zbranch(const struct ubifs_info *c, const struct ubifs_znode *znode, const union ubifs_key *key, int *n)

    search znode branch.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param znode:
        znode to search in
    :type znode: const struct ubifs_znode \*

    :param key:
        key to search for
    :type key: const union ubifs_key \*

    :param n:
        znode branch slot number is returned here
    :type n: int \*

.. _`ubifs_search_zbranch.description`:

Description
-----------

This is a helper function which search branch with key \ ``key``\  in \ ``znode``\  using
binary search. The result of the search may be:
o exact match, then \ ``1``\  is returned, and the slot number of the branch is
stored in \ ``n``\ ;
o no exact match, then \ ``0``\  is returned and the slot number of the left
closest branch is returned in \ ``n``\ ; the slot if all keys in this znode are
greater than \ ``key``\ , then \ ``-1``\  is returned in \ ``n``\ .

.. _`ubifs_tnc_postorder_first`:

ubifs_tnc_postorder_first
=========================

.. c:function:: struct ubifs_znode *ubifs_tnc_postorder_first(struct ubifs_znode *znode)

    find first znode to do postorder tree traversal.

    :param znode:
        znode to start at (root of the sub-tree to traverse)
    :type znode: struct ubifs_znode \*

.. _`ubifs_tnc_postorder_first.description`:

Description
-----------

Find the lowest leftmost znode in a subtree of the TNC tree. The LNC is
ignored.

.. _`ubifs_tnc_postorder_next`:

ubifs_tnc_postorder_next
========================

.. c:function:: struct ubifs_znode *ubifs_tnc_postorder_next(const struct ubifs_info *c, struct ubifs_znode *znode)

    next TNC tree element in postorder traversal.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param znode:
        previous znode
    :type znode: struct ubifs_znode \*

.. _`ubifs_tnc_postorder_next.description`:

Description
-----------

This function implements postorder TNC traversal. The LNC is ignored.
Returns the next element or \ ``NULL``\  if \ ``znode``\  is already the last one.

.. _`ubifs_destroy_tnc_subtree`:

ubifs_destroy_tnc_subtree
=========================

.. c:function:: long ubifs_destroy_tnc_subtree(const struct ubifs_info *c, struct ubifs_znode *znode)

    destroy all znodes connected to a subtree.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param znode:
        znode defining subtree to destroy
    :type znode: struct ubifs_znode \*

.. _`ubifs_destroy_tnc_subtree.description`:

Description
-----------

This function destroys subtree of the TNC tree. Returns number of clean
znodes in the subtree.

.. _`read_znode`:

read_znode
==========

.. c:function:: int read_znode(struct ubifs_info *c, struct ubifs_zbranch *zzbr, struct ubifs_znode *znode)

    read an indexing node from flash and fill znode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param zzbr:
        the zbranch describing the node to read
    :type zzbr: struct ubifs_zbranch \*

    :param znode:
        znode to read to
    :type znode: struct ubifs_znode \*

.. _`read_znode.description`:

Description
-----------

This function reads an indexing node from the flash media and fills znode
with the read data. Returns zero in case of success and a negative error
code in case of failure. The read indexing node is validated and if anything
is wrong with it, this function prints complaint messages and returns
\ ``-EINVAL``\ .

.. _`ubifs_load_znode`:

ubifs_load_znode
================

.. c:function:: struct ubifs_znode *ubifs_load_znode(struct ubifs_info *c, struct ubifs_zbranch *zbr, struct ubifs_znode *parent, int iip)

    load znode to TNC cache.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param zbr:
        znode branch
    :type zbr: struct ubifs_zbranch \*

    :param parent:
        znode's parent
    :type parent: struct ubifs_znode \*

    :param iip:
        index in parent
    :type iip: int

.. _`ubifs_load_znode.description`:

Description
-----------

This function loads znode pointed to by \ ``zbr``\  into the TNC cache and
returns pointer to it in case of success and a negative error code in case
of failure.

.. _`ubifs_tnc_read_node`:

ubifs_tnc_read_node
===================

.. c:function:: int ubifs_tnc_read_node(struct ubifs_info *c, struct ubifs_zbranch *zbr, void *node)

    read a leaf node from the flash media.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param zbr:
        key and position of the node
    :type zbr: struct ubifs_zbranch \*

    :param node:
        node is returned here
    :type node: void \*

.. _`ubifs_tnc_read_node.description`:

Description
-----------

This function reads a node defined by \ ``zbr``\  from the flash media. Returns
zero in case of success or a negative negative error code in case of
failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/tnc_misc.c

.. _`ubifs_tnc_levelorder_next`:

ubifs_tnc_levelorder_next
=========================

.. c:function:: struct ubifs_znode *ubifs_tnc_levelorder_next(struct ubifs_znode *zr, struct ubifs_znode *znode)

    next TNC tree element in levelorder traversal.

    :param struct ubifs_znode \*zr:
        root of the subtree to traverse

    :param struct ubifs_znode \*znode:
        previous znode

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

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const struct ubifs_znode \*znode:
        znode to search in

    :param const union ubifs_key \*key:
        key to search for

    :param int \*n:
        znode branch slot number is returned here

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

    :param struct ubifs_znode \*znode:
        znode to start at (root of the sub-tree to traverse)

.. _`ubifs_tnc_postorder_first.description`:

Description
-----------

Find the lowest leftmost znode in a subtree of the TNC tree. The LNC is
ignored.

.. _`ubifs_tnc_postorder_next`:

ubifs_tnc_postorder_next
========================

.. c:function:: struct ubifs_znode *ubifs_tnc_postorder_next(struct ubifs_znode *znode)

    next TNC tree element in postorder traversal.

    :param struct ubifs_znode \*znode:
        previous znode

.. _`ubifs_tnc_postorder_next.description`:

Description
-----------

This function implements postorder TNC traversal. The LNC is ignored.
Returns the next element or \ ``NULL``\  if \ ``znode``\  is already the last one.

.. _`ubifs_destroy_tnc_subtree`:

ubifs_destroy_tnc_subtree
=========================

.. c:function:: long ubifs_destroy_tnc_subtree(struct ubifs_znode *znode)

    destroy all znodes connected to a subtree.

    :param struct ubifs_znode \*znode:
        znode defining subtree to destroy

.. _`ubifs_destroy_tnc_subtree.description`:

Description
-----------

This function destroys subtree of the TNC tree. Returns number of clean
znodes in the subtree.

.. _`read_znode`:

read_znode
==========

.. c:function:: int read_znode(struct ubifs_info *c, int lnum, int offs, int len, struct ubifs_znode *znode)

    read an indexing node from flash and fill znode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB of the indexing node to read

    :param int offs:
        node offset

    :param int len:
        node length

    :param struct ubifs_znode \*znode:
        znode to read to

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

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        znode branch

    :param struct ubifs_znode \*parent:
        znode's parent

    :param int iip:
        index in parent

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

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        key and position of the node

    :param void \*node:
        node is returned here

.. _`ubifs_tnc_read_node.description`:

Description
-----------

This function reads a node defined by \ ``zbr``\  from the flash media. Returns
zero in case of success or a negative negative error code in case of
failure.

.. This file was automatic generated / don't edit.


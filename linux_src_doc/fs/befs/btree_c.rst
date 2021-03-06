.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/befs/btree.c

.. _`befs_bt_read_super`:

befs_bt_read_super
==================

.. c:function:: int befs_bt_read_super(struct super_block *sb, const befs_data_stream *ds, befs_btree_super *sup)

    read in btree superblock convert to cpu byteorder

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream to read from
    :type ds: const befs_data_stream \*

    :param sup:
        Buffer in which to place the btree superblock
    :type sup: befs_btree_super \*

.. _`befs_bt_read_super.description`:

Description
-----------

Calls befs_read_datastream to read in the btree superblock and
makes sure it is in cpu byteorder, byteswapping if necessary.

.. _`befs_bt_read_super.return`:

Return
------

BEFS_OK on success and if \*@sup contains the btree superblock in cpu
byte order. Otherwise return BEFS_ERR on error.

.. _`befs_bt_read_node`:

befs_bt_read_node
=================

.. c:function:: int befs_bt_read_node(struct super_block *sb, const befs_data_stream *ds, struct befs_btree_node *node, befs_off_t node_off)

    read in btree node and convert to cpu byteorder

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream to read from
    :type ds: const befs_data_stream \*

    :param node:
        Buffer in which to place the btree node
    :type node: struct befs_btree_node \*

    :param node_off:
        Starting offset (in bytes) of the node in \ ``ds``\ 
    :type node_off: befs_off_t

.. _`befs_bt_read_node.description`:

Description
-----------

Calls befs_read_datastream to read in the indicated btree node and
makes sure its header fields are in cpu byteorder, byteswapping if
necessary.

.. _`befs_bt_read_node.note`:

Note
----

node->bh must be NULL when this function is called the first time.
Don't forget brelse(node->bh) after last call.

On success, returns BEFS_OK and \*@node contains the btree node that
starts at \ ``node_off``\ , with the node->head fields in cpu byte order.

On failure, BEFS_ERR is returned.

.. _`befs_btree_find`:

befs_btree_find
===============

.. c:function:: int befs_btree_find(struct super_block *sb, const befs_data_stream *ds, const char *key, befs_off_t *value)

    Find a key in a befs B+tree

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream containing btree
    :type ds: const befs_data_stream \*

    :param key:
        Key string to lookup in btree
    :type key: const char \*

    :param value:
        Value stored with \ ``key``\ 
    :type value: befs_off_t \*

.. _`befs_btree_find.description`:

Description
-----------

On success, returns BEFS_OK and sets \*@value to the value stored
with \ ``key``\  (usually the disk block number of an inode).

On failure, returns BEFS_ERR or BEFS_BT_NOT_FOUND.

.. _`befs_btree_find.algorithm`:

Algorithm
---------

Read the superblock and rootnode of the b+tree.
Drill down through the interior nodes using \ :c:func:`befs_find_key`\ .
Once at the correct leaf node, use \ :c:func:`befs_find_key`\  again to get the
actual value stored with the key.

.. _`befs_find_key`:

befs_find_key
=============

.. c:function:: int befs_find_key(struct super_block *sb, struct befs_btree_node *node, const char *findkey, befs_off_t *value)

    Search for a key within a node

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param node:
        Node to find the key within
    :type node: struct befs_btree_node \*

    :param findkey:
        Keystring to search for
    :type findkey: const char \*

    :param value:
        If key is found, the value stored with the key is put here
    :type value: befs_off_t \*

.. _`befs_find_key.description`:

Description
-----------

Finds exact match if one exists, and returns BEFS_BT_MATCH.
If there is no match and node's value array is too small for key, return
BEFS_BT_OVERFLOW.
If no match and node should countain this key, return BEFS_BT_NOT_FOUND.

Uses binary search instead of a linear.

.. _`befs_btree_read`:

befs_btree_read
===============

.. c:function:: int befs_btree_read(struct super_block *sb, const befs_data_stream *ds, loff_t key_no, size_t bufsize, char *keybuf, size_t *keysize, befs_off_t *value)

    Traverse leafnodes of a btree

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream containing btree
    :type ds: const befs_data_stream \*

    :param key_no:
        Key number (alphabetical order) of key to read
    :type key_no: loff_t

    :param bufsize:
        Size of the buffer to return key in
    :type bufsize: size_t

    :param keybuf:
        Pointer to a buffer to put the key in
    :type keybuf: char \*

    :param keysize:
        Length of the returned key
    :type keysize: size_t \*

    :param value:
        Value stored with the returned key
    :type value: befs_off_t \*

.. _`befs_btree_read.description`:

Description
-----------

Here's how it works: Key_no is the index of the key/value pair to
return in keybuf/value.
Bufsize is the size of keybuf (BEFS_NAME_LEN+1 is a good size). Keysize is
the number of characters in the key (just a convenience).

.. _`befs_btree_read.algorithm`:

Algorithm
---------

Get the first leafnode of the tree. See if the requested key is in that
node. If not, follow the node->right link to the next leafnode. Repeat
until the (key_no)th key is found or the tree is out of keys.

.. _`befs_btree_seekleaf`:

befs_btree_seekleaf
===================

.. c:function:: int befs_btree_seekleaf(struct super_block *sb, const befs_data_stream *ds, befs_btree_super *bt_super, struct befs_btree_node *this_node, befs_off_t *node_off)

    Find the first leafnode in the btree

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream containing btree
    :type ds: const befs_data_stream \*

    :param bt_super:
        Pointer to the superblock of the btree
    :type bt_super: befs_btree_super \*

    :param this_node:
        Buffer to return the leafnode in
    :type this_node: struct befs_btree_node \*

    :param node_off:
        Pointer to offset of current node within datastream. Modified
        by the function.
    :type node_off: befs_off_t \*

.. _`befs_btree_seekleaf.description`:

Description
-----------

Helper function for btree traverse. Moves the current position to the
start of the first leaf node.

Also checks for an empty tree. If there are no keys, returns BEFS_BT_EMPTY.

.. _`befs_leafnode`:

befs_leafnode
=============

.. c:function:: int befs_leafnode(struct befs_btree_node *node)

    Determine if the btree node is a leaf node or an interior node

    :param node:
        Pointer to node structure to test
    :type node: struct befs_btree_node \*

.. _`befs_leafnode.description`:

Description
-----------

Return 1 if leaf, 0 if interior

.. _`befs_bt_keylen_index`:

befs_bt_keylen_index
====================

.. c:function:: fs16 *befs_bt_keylen_index(struct befs_btree_node *node)

    Finds start of keylen index in a node

    :param node:
        Pointer to the node structure to find the keylen index within
    :type node: struct befs_btree_node \*

.. _`befs_bt_keylen_index.description`:

Description
-----------

Returns a pointer to the start of the key length index array
of the B+tree node \*@node

"The length of all the keys in the node is added to the size of the
header and then rounded up to a multiple of four to get the beginning
of the key length index" (p.88, practical filesystem design).

Except that rounding up to 8 works, and rounding up to 4 doesn't.

.. _`befs_bt_valarray`:

befs_bt_valarray
================

.. c:function:: fs64 *befs_bt_valarray(struct befs_btree_node *node)

    Finds the start of value array in a node

    :param node:
        Pointer to the node structure to find the value array within
    :type node: struct befs_btree_node \*

.. _`befs_bt_valarray.description`:

Description
-----------

Returns a pointer to the start of the value array
of the node pointed to by the node header

.. _`befs_bt_keydata`:

befs_bt_keydata
===============

.. c:function:: char *befs_bt_keydata(struct befs_btree_node *node)

    Finds start of keydata array in a node

    :param node:
        Pointer to the node structure to find the keydata array within
    :type node: struct befs_btree_node \*

.. _`befs_bt_keydata.description`:

Description
-----------

Returns a pointer to the start of the keydata array
of the node pointed to by the node header

.. _`befs_bt_get_key`:

befs_bt_get_key
===============

.. c:function:: char *befs_bt_get_key(struct super_block *sb, struct befs_btree_node *node, int index, u16 *keylen)

    returns a pointer to the start of a key

    :param sb:
        filesystem superblock
    :type sb: struct super_block \*

    :param node:
        node in which to look for the key
    :type node: struct befs_btree_node \*

    :param index:
        the index of the key to get
    :type index: int

    :param keylen:
        modified to be the length of the key at \ ``index``\ 
    :type keylen: u16 \*

.. _`befs_bt_get_key.description`:

Description
-----------

Returns a valid pointer into \ ``node``\  on success.
Returns NULL on failure (bad input) and sets \*@keylen = 0

.. _`befs_compare_strings`:

befs_compare_strings
====================

.. c:function:: int befs_compare_strings(const void *key1, int keylen1, const void *key2, int keylen2)

    compare two strings

    :param key1:
        pointer to the first key to be compared
    :type key1: const void \*

    :param keylen1:
        length in bytes of key1
    :type keylen1: int

    :param key2:
        pointer to the second key to be compared
    :type key2: const void \*

    :param keylen2:
        length in bytes of key2
    :type keylen2: int

.. _`befs_compare_strings.description`:

Description
-----------

Returns 0 if \ ``key1``\  and \ ``key2``\  are equal.
Returns >0 if \ ``key1``\  is greater.
Returns <0 if \ ``key2``\  is greater.

.. This file was automatic generated / don't edit.


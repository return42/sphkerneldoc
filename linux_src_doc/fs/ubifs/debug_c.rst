.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/debug.c

.. _`ubifs_dump_index`:

ubifs_dump_index
================

.. c:function:: void ubifs_dump_index(struct ubifs_info *c)

    dump the on-flash index.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_dump_index.description`:

Description
-----------

This function dumps whole UBIFS indexing B-tree, unlike 'ubifs_dump_tnc()'
which dumps only in-memory znodes and does not read znodes which from flash.

.. _`dbg_save_space_info`:

dbg_save_space_info
===================

.. c:function:: void dbg_save_space_info(struct ubifs_info *c)

    save information about flash space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_save_space_info.description`:

Description
-----------

This function saves information about UBIFS free space, dirty space, etc, in
order to check it later.

.. _`dbg_check_space_info`:

dbg_check_space_info
====================

.. c:function:: int dbg_check_space_info(struct ubifs_info *c)

    check flash space information.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_check_space_info.description`:

Description
-----------

This function compares current flash space information with the information
which was saved when the 'dbg_save_space_info()' function was called.
Returns zero if the information has not changed, and \ ``-EINVAL``\  it it has
changed.

.. _`dbg_check_synced_i_size`:

dbg_check_synced_i_size
=======================

.. c:function:: int dbg_check_synced_i_size(const struct ubifs_info *c, struct inode *inode)

    check synchronized inode size.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct inode \*inode:
        inode to check

.. _`dbg_check_synced_i_size.description`:

Description
-----------

If inode is clean, synchronized inode size has to be equivalent to current
inode size. This function has to be called only for locked inodes (@i_mutex
has to be locked). Returns \ ``0``\  if synchronized inode size if correct, and
\ ``-EINVAL``\  if not.

.. _`dbg_check_key_order`:

dbg_check_key_order
===================

.. c:function:: int dbg_check_key_order(struct ubifs_info *c, struct ubifs_zbranch *zbr1, struct ubifs_zbranch *zbr2)

    make sure that colliding keys are properly ordered.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr1:
        first zbranch

    :param struct ubifs_zbranch \*zbr2:
        following zbranch

.. _`dbg_check_key_order.description`:

Description
-----------

In UBIFS indexing B-tree colliding keys has to be sorted in binary order of
names of the direntries/xentries which are referred by the keys. This
function reads direntries/xentries referred by \ ``zbr1``\  and \ ``zbr2``\  and makes
sure the name of direntry/xentry referred by \ ``zbr1``\  is less than
direntry/xentry referred by \ ``zbr2``\ . Returns zero if this is true, \ ``1``\  if not,
and a negative error code in case of failure.

.. _`dbg_check_znode`:

dbg_check_znode
===============

.. c:function:: int dbg_check_znode(struct ubifs_info *c, struct ubifs_zbranch *zbr)

    check if znode is all right.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        zbranch which points to this znode

.. _`dbg_check_znode.description`:

Description
-----------

This function makes sure that znode referred to by \ ``zbr``\  is all right.
Returns zero if it is, and \ ``-EINVAL``\  if it is not.

.. _`dbg_check_tnc`:

dbg_check_tnc
=============

.. c:function:: int dbg_check_tnc(struct ubifs_info *c, int extra)

    check TNC tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int extra:
        do extra checks that are possible at start commit

.. _`dbg_check_tnc.description`:

Description
-----------

This function traverses whole TNC tree and checks every znode. Returns zero
if everything is all right and \ ``-EINVAL``\  if something is wrong with TNC.

.. _`dbg_walk_index`:

dbg_walk_index
==============

.. c:function:: int dbg_walk_index(struct ubifs_info *c, dbg_leaf_callback leaf_cb, dbg_znode_callback znode_cb, void *priv)

    walk the on-flash index.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param dbg_leaf_callback leaf_cb:
        called for each leaf node

    :param dbg_znode_callback znode_cb:
        called for each indexing node

    :param void \*priv:
        private data which is passed to callbacks

.. _`dbg_walk_index.description`:

Description
-----------

This function walks the UBIFS index and calls the \ ``leaf_cb``\  for each leaf
node and \ ``znode_cb``\  for each indexing node. Returns zero in case of success
and a negative error code in case of failure.

It would be better if this function removed every znode it pulled to into
the TNC, so that the behavior more closely matched the non-debugging
behavior.

.. _`add_size`:

add_size
========

.. c:function:: int add_size(struct ubifs_info *c, struct ubifs_znode *znode, void *priv)

    add znode size to partially calculated index size.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to add size for

    :param void \*priv:
        partially calculated index size

.. _`add_size.description`:

Description
-----------

This is a helper function for 'dbg_check_idx_size()' which is called for
every indexing node and adds its size to the 'long long' variable pointed to
by \ ``priv``\ .

.. _`dbg_check_idx_size`:

dbg_check_idx_size
==================

.. c:function:: int dbg_check_idx_size(struct ubifs_info *c, long long idx_size)

    check index size.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param long long idx_size:
        size to check

.. _`dbg_check_idx_size.description`:

Description
-----------

This function walks the UBIFS index, calculates its size and checks that the
size is equivalent to \ ``idx_size``\ . Returns zero in case of success and a
negative error code in case of failure.

.. _`fsck_inode`:

struct fsck_inode
=================

.. c:type:: struct fsck_inode

    information about an inode used when checking the file-system.

.. _`fsck_inode.definition`:

Definition
----------

.. code-block:: c

    struct fsck_inode {
        struct rb_node rb;
        ino_t inum;
        umode_t mode;
        unsigned int nlink;
        unsigned int xattr_cnt;
        int references;
        int calc_cnt;
        long long size;
        unsigned int xattr_sz;
        long long calc_sz;
        long long calc_xcnt;
        long long calc_xsz;
        unsigned int xattr_nms;
        long long calc_xnms;
    }

.. _`fsck_inode.members`:

Members
-------

rb
    link in the RB-tree of inodes

inum
    inode number

mode
    inode type, permissions, etc

nlink
    inode link count

xattr_cnt
    count of extended attributes

references
    how many directory/xattr entries refer this inode (calculated
    while walking the index)

calc_cnt
    for directory inode count of child directories

size
    inode size (read from on-flash inode)

xattr_sz
    summary size of all extended attributes (read from on-flash
    inode)

calc_sz
    for directories calculated directory size

calc_xcnt
    count of extended attributes

calc_xsz
    calculated summary size of all extended attributes

xattr_nms
    sum of lengths of all extended attribute names belonging to this
    inode (read from on-flash inode)

calc_xnms
    calculated sum of lengths of all extended attribute names

.. _`fsck_data`:

struct fsck_data
================

.. c:type:: struct fsck_data

    private FS checking information.

.. _`fsck_data.definition`:

Definition
----------

.. code-block:: c

    struct fsck_data {
        struct rb_root inodes;
    }

.. _`fsck_data.members`:

Members
-------

inodes
    RB-tree of all inodes (contains \ ``struct``\  fsck_inode objects)

.. _`add_inode`:

add_inode
=========

.. c:function:: struct fsck_inode *add_inode(struct ubifs_info *c, struct fsck_data *fsckd, struct ubifs_ino_node *ino)

    add inode information to RB-tree of inodes.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct fsck_data \*fsckd:
        FS checking information

    :param struct ubifs_ino_node \*ino:
        raw UBIFS inode to add

.. _`add_inode.description`:

Description
-----------

This is a helper function for 'check_leaf()' which adds information about
inode \ ``ino``\  to the RB-tree of inodes. Returns inode information pointer in
case of success and a negative error code in case of failure.

.. _`search_inode`:

search_inode
============

.. c:function:: struct fsck_inode *search_inode(struct fsck_data *fsckd, ino_t inum)

    search inode in the RB-tree of inodes.

    :param struct fsck_data \*fsckd:
        FS checking information

    :param ino_t inum:
        inode number to search

.. _`search_inode.description`:

Description
-----------

This is a helper function for 'check_leaf()' which searches inode \ ``inum``\  in
the RB-tree of inodes and returns an inode information pointer or \ ``NULL``\  if
the inode was not found.

.. _`read_add_inode`:

read_add_inode
==============

.. c:function:: struct fsck_inode *read_add_inode(struct ubifs_info *c, struct fsck_data *fsckd, ino_t inum)

    read inode node and add it to RB-tree of inodes.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct fsck_data \*fsckd:
        FS checking information

    :param ino_t inum:
        inode number to read

.. _`read_add_inode.description`:

Description
-----------

This is a helper function for 'check_leaf()' which finds inode node \ ``inum``\  in
the index, reads it, and adds it to the RB-tree of inodes. Returns inode
information pointer in case of success and a negative error code in case of
failure.

.. _`check_leaf`:

check_leaf
==========

.. c:function:: int check_leaf(struct ubifs_info *c, struct ubifs_zbranch *zbr, void *priv)

    check leaf node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        zbranch of the leaf node to check

    :param void \*priv:
        FS checking information

.. _`check_leaf.description`:

Description
-----------

This is a helper function for 'dbg_check_filesystem()' which is called for
every single leaf node while walking the indexing tree. It checks that the
leaf node referred from the indexing tree exists, has correct CRC, and does
some other basic validation. This function is also responsible for building
an RB-tree of inodes - it adds all inodes into the RB-tree. It also
calculates reference count, size, etc for each inode in order to later
compare them to the information stored inside the inodes and detect possible
inconsistencies. Returns zero in case of success and a negative error code
in case of failure.

.. _`free_inodes`:

free_inodes
===========

.. c:function:: void free_inodes(struct fsck_data *fsckd)

    free RB-tree of inodes.

    :param struct fsck_data \*fsckd:
        FS checking information

.. _`check_inodes`:

check_inodes
============

.. c:function:: int check_inodes(struct ubifs_info *c, struct fsck_data *fsckd)

    checks all inodes.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct fsck_data \*fsckd:
        FS checking information

.. _`check_inodes.description`:

Description
-----------

This is a helper function for 'dbg_check_filesystem()' which walks the
RB-tree of inodes after the index scan has been finished, and checks that
inode nlink, size, etc are correct. Returns zero if inodes are fine,
\ ``-EINVAL``\  if not, and a negative error code in case of failure.

.. _`dbg_check_filesystem`:

dbg_check_filesystem
====================

.. c:function:: int dbg_check_filesystem(struct ubifs_info *c)

    check the file-system.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_check_filesystem.description`:

Description
-----------

This function checks the file system, namely:
o makes sure that all leaf nodes exist and their CRCs are correct;
o makes sure inode nlink, size, xattr size/count are correct (for all
inodes).

The function reads whole indexing tree and all nodes, so it is pretty
heavy-weight. Returns zero if the file-system is consistent, \ ``-EINVAL``\  if
not, and a negative error code in case of failure.

.. _`dbg_check_data_nodes_order`:

dbg_check_data_nodes_order
==========================

.. c:function:: int dbg_check_data_nodes_order(struct ubifs_info *c, struct list_head *head)

    check that list of data nodes is sorted.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct list_head \*head:
        the list of nodes ('struct ubifs_scan_node' objects)

.. _`dbg_check_data_nodes_order.description`:

Description
-----------

This function returns zero if the list of data nodes is sorted correctly,
and \ ``-EINVAL``\  if not.

.. _`dbg_check_nondata_nodes_order`:

dbg_check_nondata_nodes_order
=============================

.. c:function:: int dbg_check_nondata_nodes_order(struct ubifs_info *c, struct list_head *head)

    check that list of data nodes is sorted.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct list_head \*head:
        the list of nodes ('struct ubifs_scan_node' objects)

.. _`dbg_check_nondata_nodes_order.description`:

Description
-----------

This function returns zero if the list of non-data nodes is sorted correctly,
and \ ``-EINVAL``\  if not.

.. _`provide_user_output`:

provide_user_output
===================

.. c:function:: int provide_user_output(int val, char __user *u, size_t count, loff_t *ppos)

    provide output to the user reading a debugfs file.

    :param int val:
        boolean value for the answer

    :param char __user \*u:
        the buffer to store the answer at

    :param size_t count:
        size of the buffer

    :param loff_t \*ppos:
        position in the \ ``u``\  output buffer

.. _`provide_user_output.description`:

Description
-----------

This is a simple helper function which stores \ ``val``\  boolean value in the user
buffer when the user reads one of UBIFS debugfs files. Returns amount of
bytes written to \ ``u``\  in case of success and a negative error code in case of
failure.

.. _`interpret_user_input`:

interpret_user_input
====================

.. c:function:: int interpret_user_input(const char __user *u, size_t count)

    interpret user debugfs file input.

    :param const char __user \*u:
        user-provided buffer with the input

    :param size_t count:
        buffer size

.. _`interpret_user_input.description`:

Description
-----------

This is a helper function which interpret user input to a boolean UBIFS
debugfs file. Returns \ ``0``\  or \ ``1``\  in case of success and a negative error code
in case of failure.

.. _`dbg_debugfs_init_fs`:

dbg_debugfs_init_fs
===================

.. c:function:: int dbg_debugfs_init_fs(struct ubifs_info *c)

    initialize debugfs for UBIFS instance.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_debugfs_init_fs.description`:

Description
-----------

This function creates all debugfs files for this instance of UBIFS. Returns
zero in case of success and a negative error code in case of failure.

Note, the only reason we have not merged this function with the
'ubifs_debugging_init()' function is because it is better to initialize
debugfs interfaces at the very end of the mount process, and remove them at
the very beginning of the mount process.

.. _`dbg_debugfs_exit_fs`:

dbg_debugfs_exit_fs
===================

.. c:function:: void dbg_debugfs_exit_fs(struct ubifs_info *c)

    remove all debugfs files.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_debugfs_init`:

dbg_debugfs_init
================

.. c:function:: int dbg_debugfs_init( void)

    initialize debugfs file-system.

    :param  void:
        no arguments

.. _`dbg_debugfs_init.description`:

Description
-----------

UBIFS uses debugfs file-system to expose various debugging knobs to
user-space. This function creates "ubifs" directory in the debugfs
file-system. Returns zero in case of success and a negative error code in
case of failure.

.. _`dbg_debugfs_exit`:

dbg_debugfs_exit
================

.. c:function:: void dbg_debugfs_exit( void)

    remove the "ubifs" directory from debugfs file-system.

    :param  void:
        no arguments

.. _`ubifs_debugging_init`:

ubifs_debugging_init
====================

.. c:function:: int ubifs_debugging_init(struct ubifs_info *c)

    initialize UBIFS debugging.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_debugging_init.description`:

Description
-----------

This function initializes debugging-related data for the file system.
Returns zero in case of success and a negative error code in case of
failure.

.. _`ubifs_debugging_exit`:

ubifs_debugging_exit
====================

.. c:function:: void ubifs_debugging_exit(struct ubifs_info *c)

    free debugging data.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. This file was automatic generated / don't edit.


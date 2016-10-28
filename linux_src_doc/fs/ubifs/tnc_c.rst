.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/tnc.c

.. _`insert_old_idx`:

insert_old_idx
==============

.. c:function:: int insert_old_idx(struct ubifs_info *c, int lnum, int offs)

    record an index node obsoleted since the last commit start.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number of obsoleted index node

    :param int offs:
        offset of obsoleted index node

.. _`insert_old_idx.description`:

Description
-----------

Returns \ ``0``\  on success, and a negative error code on failure.

For recovery, there must always be a complete intact version of the index on
flash at all times. That is called the "old index". It is the index as at the
time of the last successful commit. Many of the index nodes in the old index
may be dirty, but they must not be erased until the next successful commit
(at which point that index becomes the old index).

That means that the garbage collection and the in-the-gaps method of
committing must be able to determine if an index node is in the old index.
Most of the old index nodes can be found by looking up the TNC using the
'\ :c:func:`lookup_znode`\ ' function. However, some of the old index nodes may have
been deleted from the current index or may have been changed so much that
they cannot be easily found. In those cases, an entry is added to an RB-tree.
That is what this function does. The RB-tree is ordered by LEB number and
offset because they uniquely identify the old index node.

.. _`insert_old_idx_znode`:

insert_old_idx_znode
====================

.. c:function:: int insert_old_idx_znode(struct ubifs_info *c, struct ubifs_znode *znode)

    record a znode obsoleted since last commit start.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode of obsoleted index node

.. _`insert_old_idx_znode.description`:

Description
-----------

Returns \ ``0``\  on success, and a negative error code on failure.

.. _`ins_clr_old_idx_znode`:

ins_clr_old_idx_znode
=====================

.. c:function:: int ins_clr_old_idx_znode(struct ubifs_info *c, struct ubifs_znode *znode)

    record a znode obsoleted since last commit start.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode of obsoleted index node

.. _`ins_clr_old_idx_znode.description`:

Description
-----------

Returns \ ``0``\  on success, and a negative error code on failure.

.. _`destroy_old_idx`:

destroy_old_idx
===============

.. c:function:: void destroy_old_idx(struct ubifs_info *c)

    destroy the old_idx RB-tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`destroy_old_idx.description`:

Description
-----------

During start commit, the old_idx RB-tree is used to avoid overwriting index
nodes that were in the index last commit but have since been deleted.  This
is necessary for recovery i.e. the old index must be kept intact until the
new index is successfully written.  The old-idx RB-tree is used for the
in-the-gaps method of writing index nodes and is destroyed every commit.

.. _`copy_znode`:

copy_znode
==========

.. c:function:: struct ubifs_znode *copy_znode(struct ubifs_info *c, struct ubifs_znode *znode)

    copy a dirty znode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to copy

.. _`copy_znode.description`:

Description
-----------

A dirty znode being committed may not be changed, so it is copied.

.. _`add_idx_dirt`:

add_idx_dirt
============

.. c:function:: int add_idx_dirt(struct ubifs_info *c, int lnum, int dirt)

    add dirt due to a dirty znode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number of index node

    :param int dirt:
        size of index node

.. _`add_idx_dirt.description`:

Description
-----------

This function updates lprops dirty space and the new size of the index.

.. _`dirty_cow_znode`:

dirty_cow_znode
===============

.. c:function:: struct ubifs_znode *dirty_cow_znode(struct ubifs_info *c, struct ubifs_zbranch *zbr)

    ensure a znode is not being committed.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        branch of znode to check

.. _`dirty_cow_znode.description`:

Description
-----------

Returns dirtied znode on success or negative error code on failure.

.. _`lnc_add`:

lnc_add
=======

.. c:function:: int lnc_add(struct ubifs_info *c, struct ubifs_zbranch *zbr, const void *node)

    add a leaf node to the leaf node cache.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        zbranch of leaf node

    :param const void \*node:
        leaf node

.. _`lnc_add.description`:

Description
-----------

Leaf nodes are non-index nodes directory entry nodes or data nodes. The
purpose of the leaf node cache is to save re-reading the same leaf node over
and over again. Most things are cached by VFS, however the file system must
cache directory entries for readdir and for resolving hash collisions. The
present implementation of the leaf node cache is extremely simple, and
allows for error returns that are not used but that may be needed if a more
complex implementation is created.

Note, this function does not add the \ ``node``\  object to LNC directly, but
allocates a copy of the object and adds the copy to LNC. The reason for this
is that \ ``node``\  has been allocated outside of the TNC subsystem and will be
used with \ ``c``\ ->tnc_mutex unlock upon return from the TNC subsystem. But LNC
may be changed at any time, e.g. freed by the shrinker.

.. _`lnc_free`:

lnc_free
========

.. c:function:: void lnc_free(struct ubifs_zbranch *zbr)

    remove a leaf node from the leaf node cache.

    :param struct ubifs_zbranch \*zbr:
        zbranch of leaf node

.. _`tnc_read_node_nm`:

tnc_read_node_nm
================

.. c:function:: int tnc_read_node_nm(struct ubifs_info *c, struct ubifs_zbranch *zbr, void *node)

    read a "hashed" leaf node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        key and position of the node

    :param void \*node:
        node is returned here

.. _`tnc_read_node_nm.description`:

Description
-----------

This function reads a "hashed" node defined by \ ``zbr``\  from the leaf node cache
(in it is there) or from the hash media, in which case the node is also
added to LNC. Returns zero in case of success or a negative negative error
code in case of failure.

.. _`try_read_node`:

try_read_node
=============

.. c:function:: int try_read_node(const struct ubifs_info *c, void *buf, int type, int len, int lnum, int offs)

    read a node if it is a node.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to read to

    :param int type:
        node type

    :param int len:
        node length (not aligned)

    :param int lnum:
        LEB number of node to read

    :param int offs:
        offset of node to read

.. _`try_read_node.description`:

Description
-----------

This function tries to read a node of known type and length, checks it and
stores it in \ ``buf``\ . This function returns \ ``1``\  if a node is present and \ ``0``\  if
a node is not present. A negative error code is returned for I/O errors.
This function performs that same function as ubifs_read_node except that
it does not require that there is actually a node present and instead
the return code indicates if a node was read.

Note, this function does not check CRC of data nodes if \ ``c``\ ->no_chk_data_crc
is true (it is controlled by corresponding mount option). However, if
\ ``c``\ ->mounting or \ ``c``\ ->remounting_rw is true (we are mounting or re-mounting to
R/W mode), \ ``c``\ ->no_chk_data_crc is ignored and CRC is checked. This is
because during mounting or re-mounting from R/O mode to R/W mode we may read
journal nodes (when replying the journal or doing the recovery) and the
journal nodes may potentially be corrupted, so checking is required.

.. _`fallible_read_node`:

fallible_read_node
==================

.. c:function:: int fallible_read_node(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_zbranch *zbr, void *node)

    try to read a leaf node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key of node to read

    :param struct ubifs_zbranch \*zbr:
        position of node

    :param void \*node:
        node returned

.. _`fallible_read_node.description`:

Description
-----------

This function tries to read a node and returns \ ``1``\  if the node is read, \ ``0``\ 
if the node is not present, and a negative error code in the case of error.

.. _`matches_name`:

matches_name
============

.. c:function:: int matches_name(struct ubifs_info *c, struct ubifs_zbranch *zbr, const struct qstr *nm)

    determine if a direntry or xattr entry matches a given name.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        zbranch of dent

    :param const struct qstr \*nm:
        name to match

.. _`matches_name.description`:

Description
-----------

This function checks if xentry/direntry referred by zbranch \ ``zbr``\  matches name
\ ``nm``\ . Returns \ ``NAME_MATCHES``\  if it does, \ ``NAME_LESS``\  if the name referred by
\ ``zbr``\  is less than \ ``nm``\ , and \ ``NAME_GREATER``\  if it is greater than \ ``nm``\ . In case
of failure, a negative error code is returned.

.. _`get_znode`:

get_znode
=========

.. c:function:: struct ubifs_znode *get_znode(struct ubifs_info *c, struct ubifs_znode *znode, int n)

    get a TNC znode that may not be loaded yet.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        parent znode

    :param int n:
        znode branch slot number

.. _`get_znode.description`:

Description
-----------

This function returns the znode or a negative error code.

.. _`tnc_next`:

tnc_next
========

.. c:function:: int tnc_next(struct ubifs_info *c, struct ubifs_znode **zn, int *n)

    find next TNC entry.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*\*zn:
        znode is passed and returned here

    :param int \*n:
        znode branch slot number is passed and returned here

.. _`tnc_next.description`:

Description
-----------

This function returns \ ``0``\  if the next TNC entry is found, \ ``-ENOENT``\  if there is
no next entry, or a negative error code otherwise.

.. _`tnc_prev`:

tnc_prev
========

.. c:function:: int tnc_prev(struct ubifs_info *c, struct ubifs_znode **zn, int *n)

    find previous TNC entry.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*\*zn:
        znode is returned here

    :param int \*n:
        znode branch slot number is passed and returned here

.. _`tnc_prev.description`:

Description
-----------

This function returns \ ``0``\  if the previous TNC entry is found, \ ``-ENOENT``\  if
there is no next entry, or a negative error code otherwise.

.. _`resolve_collision`:

resolve_collision
=================

.. c:function:: int resolve_collision(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_znode **zn, int *n, const struct qstr *nm)

    resolve a collision.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key of a directory or extended attribute entry

    :param struct ubifs_znode \*\*zn:
        znode is returned here

    :param int \*n:
        zbranch number is passed and returned here

    :param const struct qstr \*nm:
        name of the entry

.. _`resolve_collision.description`:

Description
-----------

This function is called for "hashed" keys to make sure that the found key
really corresponds to the looked up node (directory or extended attribute
entry). It returns \ ``1``\  and sets \ ``zn``\  and \ ``n``\  if the collision is resolved.
\ ``0``\  is returned if \ ``nm``\  is not found and \ ``zn``\  and \ ``n``\  are set to the previous
entry, i.e. to the entry after which \ ``nm``\  could follow if it were in TNC.
This means that \ ``n``\  may be set to \ ``-1``\  if the leftmost key in \ ``zn``\  is the
previous one. A negative error code is returned on failures.

.. _`fallible_matches_name`:

fallible_matches_name
=====================

.. c:function:: int fallible_matches_name(struct ubifs_info *c, struct ubifs_zbranch *zbr, const struct qstr *nm)

    determine if a dent matches a given name.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zbr:
        zbranch of dent

    :param const struct qstr \*nm:
        name to match

.. _`fallible_matches_name.description`:

Description
-----------

This is a "fallible" version of '\ :c:func:`matches_name`\ ' function which does not
panic if the direntry/xentry referred by \ ``zbr``\  does not exist on the media.

This function checks if xentry/direntry referred by zbranch \ ``zbr``\  matches name
\ ``nm``\ . Returns \ ``NAME_MATCHES``\  it does, \ ``NAME_LESS``\  if the name referred by \ ``zbr``\ 
is less than \ ``nm``\ , \ ``NAME_GREATER``\  if it is greater than \ ``nm``\ , and \ ``NOT_ON_MEDIA``\ 
if xentry/direntry referred by \ ``zbr``\  does not exist on the media. A negative
error code is returned in case of failure.

.. _`fallible_resolve_collision`:

fallible_resolve_collision
==========================

.. c:function:: int fallible_resolve_collision(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_znode **zn, int *n, const struct qstr *nm, int adding)

    resolve a collision even if nodes are missing.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key

    :param struct ubifs_znode \*\*zn:
        znode is returned here

    :param int \*n:
        branch number is passed and returned here

    :param const struct qstr \*nm:
        name of directory entry

    :param int adding:
        indicates caller is adding a key to the TNC

.. _`fallible_resolve_collision.description`:

Description
-----------

This is a "fallible" version of the '\ :c:func:`resolve_collision`\ ' function which
does not panic if one of the nodes referred to by TNC does not exist on the
media. This may happen when replaying the journal if a deleted node was
Garbage-collected and the commit was not done. A branch that refers to a node
that is not present is called a dangling branch. The following are the return

.. _`fallible_resolve_collision.codes-for-this-function`:

codes for this function
-----------------------

o if \ ``nm``\  was found, \ ``1``\  is returned and \ ``zn``\  and \ ``n``\  are set to the found
branch;
o if we are \ ``adding``\  and \ ``nm``\  was not found, \ ``0``\  is returned;
o if we are not \ ``adding``\  and \ ``nm``\  was not found, but a dangling branch was
found, then \ ``1``\  is returned and \ ``zn``\  and \ ``n``\  are set to the dangling branch;
o a negative error code is returned in case of failure.

.. _`matches_position`:

matches_position
================

.. c:function:: int matches_position(struct ubifs_zbranch *zbr, int lnum, int offs)

    determine if a zbranch matches a given position.

    :param struct ubifs_zbranch \*zbr:
        zbranch of dent

    :param int lnum:
        LEB number of dent to match

    :param int offs:
        offset of dent to match

.. _`matches_position.description`:

Description
-----------

This function returns \ ``1``\  if \ ``lnum``\ :\ ``offs``\  matches, and \ ``0``\  otherwise.

.. _`resolve_collision_directly`:

resolve_collision_directly
==========================

.. c:function:: int resolve_collision_directly(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_znode **zn, int *n, int lnum, int offs)

    resolve a collision directly.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key of directory entry

    :param struct ubifs_znode \*\*zn:
        znode is passed and returned here

    :param int \*n:
        zbranch number is passed and returned here

    :param int lnum:
        LEB number of dent node to match

    :param int offs:
        offset of dent node to match

.. _`resolve_collision_directly.description`:

Description
-----------

This function is used for "hashed" keys to make sure the found directory or
extended attribute entry node is what was looked for. It is used when the
flash address of the right node is known (\ ``lnum``\ :\ ``offs``\ ) which makes it much
easier to resolve collisions (no need to read entries and match full
names). This function returns \ ``1``\  and sets \ ``zn``\  and \ ``n``\  if the collision is
resolved, \ ``0``\  if \ ``lnum``\ :\ ``offs``\  is not found and \ ``zn``\  and \ ``n``\  are set to the
previous directory entry. Otherwise a negative error code is returned.

.. _`dirty_cow_bottom_up`:

dirty_cow_bottom_up
===================

.. c:function:: struct ubifs_znode *dirty_cow_bottom_up(struct ubifs_info *c, struct ubifs_znode *znode)

    dirty a znode and its ancestors.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to dirty

.. _`dirty_cow_bottom_up.description`:

Description
-----------

If we do not have a unique key that resides in a znode, then we cannot
dirty that znode from the top down (i.e. by using lookup_level0_dirty)
This function records the path back to the last dirty ancestor, and then
dirties the znodes on that path.

.. _`ubifs_lookup_level0`:

ubifs_lookup_level0
===================

.. c:function:: int ubifs_lookup_level0(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_znode **zn, int *n)

    search for zero-level znode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to lookup

    :param struct ubifs_znode \*\*zn:
        znode is returned here

    :param int \*n:
        znode branch slot number is returned here

.. _`ubifs_lookup_level0.description`:

Description
-----------

This function looks up the TNC tree and search for zero-level znode which
refers key \ ``key``\ . The found zero-level znode is returned in \ ``zn``\ . There are 3

.. _`ubifs_lookup_level0.cases`:

cases
-----

o exact match, i.e. the found zero-level znode contains key \ ``key``\ , then \ ``1``\ 
is returned and slot number of the matched branch is stored in \ ``n``\ ;
o not exact match, which means that zero-level znode does not contain
\ ``key``\ , then \ ``0``\  is returned and slot number of the closest branch is stored
in \ ``n``\ ;
o \ ``key``\  is so small that it is even less than the lowest key of the
leftmost zero-level node, then \ ``0``\  is returned and \ ``0``\  is stored in \ ``n``\ .

Note, when the TNC tree is traversed, some znodes may be absent, then this
function reads corresponding indexing nodes and inserts them to TNC. In
case of failure, a negative error code is returned.

.. _`lookup_level0_dirty`:

lookup_level0_dirty
===================

.. c:function:: int lookup_level0_dirty(struct ubifs_info *c, const union ubifs_key *key, struct ubifs_znode **zn, int *n)

    search for zero-level znode dirtying.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to lookup

    :param struct ubifs_znode \*\*zn:
        znode is returned here

    :param int \*n:
        znode branch slot number is returned here

.. _`lookup_level0_dirty.description`:

Description
-----------

This function looks up the TNC tree and search for zero-level znode which
refers key \ ``key``\ . The found zero-level znode is returned in \ ``zn``\ . There are 3

.. _`lookup_level0_dirty.cases`:

cases
-----

o exact match, i.e. the found zero-level znode contains key \ ``key``\ , then \ ``1``\ 
is returned and slot number of the matched branch is stored in \ ``n``\ ;
o not exact match, which means that zero-level znode does not contain \ ``key``\ 
then \ ``0``\  is returned and slot number of the closed branch is stored in
\ ``n``\ ;
o \ ``key``\  is so small that it is even less than the lowest key of the
leftmost zero-level node, then \ ``0``\  is returned and \ ``-1``\  is stored in \ ``n``\ .

Additionally all znodes in the path from the root to the located zero-level
znode are marked as dirty.

Note, when the TNC tree is traversed, some znodes may be absent, then this
function reads corresponding indexing nodes and inserts them to TNC. In
case of failure, a negative error code is returned.

.. _`maybe_leb_gced`:

maybe_leb_gced
==============

.. c:function:: int maybe_leb_gced(struct ubifs_info *c, int lnum, int gc_seq1)

    determine if a LEB may have been garbage collected.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param int gc_seq1:
        garbage collection sequence number

.. _`maybe_leb_gced.description`:

Description
-----------

This function determines if \ ``lnum``\  may have been garbage collected since
sequence number \ ``gc_seq1``\ . If it may have been then \ ``1``\  is returned, otherwise
\ ``0``\  is returned.

.. _`ubifs_tnc_locate`:

ubifs_tnc_locate
================

.. c:function:: int ubifs_tnc_locate(struct ubifs_info *c, const union ubifs_key *key, void *node, int *lnum, int *offs)

    look up a file-system node and return it and its location.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        node key to lookup

    :param void \*node:
        the node is returned here

    :param int \*lnum:
        LEB number is returned here

    :param int \*offs:
        offset is returned here

.. _`ubifs_tnc_locate.description`:

Description
-----------

This function looks up and reads node with key \ ``key``\ . The caller has to make
sure the \ ``node``\  buffer is large enough to fit the node. Returns zero in case
of success, \ ``-ENOENT``\  if the node was not found, and a negative error code in
case of failure. The node location can be returned in \ ``lnum``\  and \ ``offs``\ .

.. _`ubifs_tnc_get_bu_keys`:

ubifs_tnc_get_bu_keys
=====================

.. c:function:: int ubifs_tnc_get_bu_keys(struct ubifs_info *c, struct bu_info *bu)

    lookup keys for bulk-read.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct bu_info \*bu:
        bulk-read parameters and results

.. _`ubifs_tnc_get_bu_keys.description`:

Description
-----------

Lookup consecutive data node keys for the same inode that reside
consecutively in the same LEB. This function returns zero in case of success
and a negative error code in case of failure.

Note, if the bulk-read buffer length (\ ``bu``\ ->buf_len) is known, this function
makes sure bulk-read nodes fit the buffer. Otherwise, this function prepares
maximum possible amount of nodes for bulk-read.

.. _`read_wbuf`:

read_wbuf
=========

.. c:function:: int read_wbuf(struct ubifs_wbuf *wbuf, void *buf, int len, int lnum, int offs)

    bulk-read from a LEB with a wbuf.

    :param struct ubifs_wbuf \*wbuf:
        wbuf that may overlap the read

    :param void \*buf:
        buffer into which to read

    :param int len:
        read length

    :param int lnum:
        LEB number from which to read

    :param int offs:
        offset from which to read

.. _`read_wbuf.description`:

Description
-----------

This functions returns \ ``0``\  on success or a negative error code on failure.

.. _`validate_data_node`:

validate_data_node
==================

.. c:function:: int validate_data_node(struct ubifs_info *c, void *buf, struct ubifs_zbranch *zbr)

    validate data nodes for bulk-read.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer containing data node to validate

    :param struct ubifs_zbranch \*zbr:
        zbranch of data node to validate

.. _`validate_data_node.description`:

Description
-----------

This functions returns \ ``0``\  on success or a negative error code on failure.

.. _`ubifs_tnc_bulk_read`:

ubifs_tnc_bulk_read
===================

.. c:function:: int ubifs_tnc_bulk_read(struct ubifs_info *c, struct bu_info *bu)

    read a number of data nodes in one go.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct bu_info \*bu:
        bulk-read parameters and results

.. _`ubifs_tnc_bulk_read.description`:

Description
-----------

This functions reads and validates the data nodes that were identified by the
'\ :c:func:`ubifs_tnc_get_bu_keys`\ ' function. This functions returns \ ``0``\  on success,
-EAGAIN to indicate a race with GC, or another negative error code on
failure.

.. _`do_lookup_nm`:

do_lookup_nm
============

.. c:function:: int do_lookup_nm(struct ubifs_info *c, const union ubifs_key *key, void *node, const struct qstr *nm)

    look up a "hashed" node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        node key to lookup

    :param void \*node:
        the node is returned here

    :param const struct qstr \*nm:
        node name

.. _`do_lookup_nm.description`:

Description
-----------

This function look up and reads a node which contains name hash in the key.
Since the hash may have collisions, there may be many nodes with the same
key, so we have to sequentially look to all of them until the needed one is
found. This function returns zero in case of success, \ ``-ENOENT``\  if the node
was not found, and a negative error code in case of failure.

.. _`ubifs_tnc_lookup_nm`:

ubifs_tnc_lookup_nm
===================

.. c:function:: int ubifs_tnc_lookup_nm(struct ubifs_info *c, const union ubifs_key *key, void *node, const struct qstr *nm)

    look up a "hashed" node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        node key to lookup

    :param void \*node:
        the node is returned here

    :param const struct qstr \*nm:
        node name

.. _`ubifs_tnc_lookup_nm.description`:

Description
-----------

This function look up and reads a node which contains name hash in the key.
Since the hash may have collisions, there may be many nodes with the same
key, so we have to sequentially look to all of them until the needed one is
found. This function returns zero in case of success, \ ``-ENOENT``\  if the node
was not found, and a negative error code in case of failure.

.. _`correct_parent_keys`:

correct_parent_keys
===================

.. c:function:: void correct_parent_keys(const struct ubifs_info *c, struct ubifs_znode *znode)

    correct parent znodes' keys.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to correct parent znodes for

.. _`correct_parent_keys.description`:

Description
-----------

This is a helper function for '\ :c:func:`tnc_insert`\ '. When the key of the leftmost
zbranch changes, keys of parent znodes have to be corrected. This helper
function is called in such situations and corrects the keys if needed.

.. _`insert_zbranch`:

insert_zbranch
==============

.. c:function:: void insert_zbranch(struct ubifs_znode *znode, const struct ubifs_zbranch *zbr, int n)

    insert a zbranch into a znode.

    :param struct ubifs_znode \*znode:
        znode into which to insert

    :param const struct ubifs_zbranch \*zbr:
        zbranch to insert

    :param int n:
        slot number to insert to

.. _`insert_zbranch.description`:

Description
-----------

This is a helper function for '\ :c:func:`tnc_insert`\ '. UBIFS does not allow "gaps" in
znode's array of zbranches and keeps zbranches consolidated, so when a new
zbranch has to be inserted to the \ ``znode``\ ->zbranches[]' array at the \ ``n``\ -th
slot, zbranches starting from \ ``n``\  have to be moved right.

.. _`tnc_insert`:

tnc_insert
==========

.. c:function:: int tnc_insert(struct ubifs_info *c, struct ubifs_znode *znode, struct ubifs_zbranch *zbr, int n)

    insert a node into TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to insert into

    :param struct ubifs_zbranch \*zbr:
        branch to insert

    :param int n:
        slot number to insert new zbranch to

.. _`tnc_insert.description`:

Description
-----------

This function inserts a new node described by \ ``zbr``\  into znode \ ``znode``\ . If
znode does not have a free slot for new zbranch, it is split. Parent znodes
are splat as well if needed. Returns zero in case of success or a negative
error code in case of failure.

.. _`ubifs_tnc_add`:

ubifs_tnc_add
=============

.. c:function:: int ubifs_tnc_add(struct ubifs_info *c, const union ubifs_key *key, int lnum, int offs, int len)

    add a node to TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to add

    :param int lnum:
        LEB number of node

    :param int offs:
        node offset

    :param int len:
        node length

.. _`ubifs_tnc_add.description`:

Description
-----------

This function adds a node with key \ ``key``\  to TNC. The node may be new or it may
obsolete some existing one. Returns \ ``0``\  on success or negative error code on
failure.

.. _`ubifs_tnc_replace`:

ubifs_tnc_replace
=================

.. c:function:: int ubifs_tnc_replace(struct ubifs_info *c, const union ubifs_key *key, int old_lnum, int old_offs, int lnum, int offs, int len)

    replace a node in the TNC only if the old node is found.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to add

    :param int old_lnum:
        LEB number of old node

    :param int old_offs:
        old node offset

    :param int lnum:
        LEB number of node

    :param int offs:
        node offset

    :param int len:
        node length

.. _`ubifs_tnc_replace.description`:

Description
-----------

This function replaces a node with key \ ``key``\  in the TNC only if the old node
is found.  This function is called by garbage collection when node are moved.
Returns \ ``0``\  on success or negative error code on failure.

.. _`ubifs_tnc_add_nm`:

ubifs_tnc_add_nm
================

.. c:function:: int ubifs_tnc_add_nm(struct ubifs_info *c, const union ubifs_key *key, int lnum, int offs, int len, const struct qstr *nm)

    add a "hashed" node to TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to add

    :param int lnum:
        LEB number of node

    :param int offs:
        node offset

    :param int len:
        node length

    :param const struct qstr \*nm:
        node name

.. _`ubifs_tnc_add_nm.description`:

Description
-----------

This is the same as '\ :c:func:`ubifs_tnc_add`\ ' but it should be used with keys which
may have collisions, like directory entry keys.

.. _`tnc_delete`:

tnc_delete
==========

.. c:function:: int tnc_delete(struct ubifs_info *c, struct ubifs_znode *znode, int n)

    delete a znode form TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode to delete from

    :param int n:
        zbranch slot number to delete

.. _`tnc_delete.description`:

Description
-----------

This function deletes a leaf node from \ ``n``\ -th slot of \ ``znode``\ . Returns zero in
case of success and a negative error code in case of failure.

.. _`ubifs_tnc_remove`:

ubifs_tnc_remove
================

.. c:function:: int ubifs_tnc_remove(struct ubifs_info *c, const union ubifs_key *key)

    remove an index entry of a node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key of node

.. _`ubifs_tnc_remove.description`:

Description
-----------

Returns \ ``0``\  on success or negative error code on failure.

.. _`ubifs_tnc_remove_nm`:

ubifs_tnc_remove_nm
===================

.. c:function:: int ubifs_tnc_remove_nm(struct ubifs_info *c, const union ubifs_key *key, const struct qstr *nm)

    remove an index entry for a "hashed" node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key of node

    :param const struct qstr \*nm:
        directory entry name

.. _`ubifs_tnc_remove_nm.description`:

Description
-----------

Returns \ ``0``\  on success or negative error code on failure.

.. _`key_in_range`:

key_in_range
============

.. c:function:: int key_in_range(struct ubifs_info *c, union ubifs_key *key, union ubifs_key *from_key, union ubifs_key *to_key)

    determine if a key falls within a range of keys.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to check

    :param union ubifs_key \*from_key:
        lowest key in range

    :param union ubifs_key \*to_key:
        highest key in range

.. _`key_in_range.description`:

Description
-----------

This function returns \ ``1``\  if the key is in range and \ ``0``\  otherwise.

.. _`ubifs_tnc_remove_range`:

ubifs_tnc_remove_range
======================

.. c:function:: int ubifs_tnc_remove_range(struct ubifs_info *c, union ubifs_key *from_key, union ubifs_key *to_key)

    remove index entries in range.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*from_key:
        lowest key to remove

    :param union ubifs_key \*to_key:
        highest key to remove

.. _`ubifs_tnc_remove_range.description`:

Description
-----------

This function removes index entries starting at \ ``from_key``\  and ending at
\ ``to_key``\ .  This function returns zero in case of success and a negative error
code in case of failure.

.. _`ubifs_tnc_remove_ino`:

ubifs_tnc_remove_ino
====================

.. c:function:: int ubifs_tnc_remove_ino(struct ubifs_info *c, ino_t inum)

    remove an inode from TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        inode number to remove

.. _`ubifs_tnc_remove_ino.description`:

Description
-----------

This function remove inode \ ``inum``\  and all the extended attributes associated
with the anode from TNC and returns zero in case of success or a negative
error code in case of failure.

.. _`ubifs_tnc_next_ent`:

ubifs_tnc_next_ent
==================

.. c:function:: struct ubifs_dent_node *ubifs_tnc_next_ent(struct ubifs_info *c, union ubifs_key *key, const struct qstr *nm)

    walk directory or extended attribute entries.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key of last entry

    :param const struct qstr \*nm:
        name of last entry found or \ ``NULL``\ 

.. _`ubifs_tnc_next_ent.description`:

Description
-----------

This function finds and reads the next directory or extended attribute entry
after the given key (\ ``key``\ ) if there is one. \ ``nm``\  is used to resolve
collisions.

If the name of the current entry is not known and only the key is known,
\ ``nm``\ ->name has to be \ ``NULL``\ . In this case the semantics of this function is a
little bit different and it returns the entry corresponding to this key, not
the next one. If the key was not found, the closest "right" entry is
returned.

If the fist entry has to be found, \ ``key``\  has to contain the lowest possible
key value for this inode and \ ``name``\  has to be \ ``NULL``\ .

This function returns the found directory or extended attribute entry node
in case of success, \ ``-ENOENT``\  is returned if no entry was found, and a
negative error code is returned in case of failure.

.. _`tnc_destroy_cnext`:

tnc_destroy_cnext
=================

.. c:function:: void tnc_destroy_cnext(struct ubifs_info *c)

    destroy left-over obsolete znodes from a failed commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`tnc_destroy_cnext.description`:

Description
-----------

Destroy left-over obsolete znodes from a failed commit.

.. _`ubifs_tnc_close`:

ubifs_tnc_close
===============

.. c:function:: void ubifs_tnc_close(struct ubifs_info *c)

    close TNC subsystem and free all related resources.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`left_znode`:

left_znode
==========

.. c:function:: struct ubifs_znode *left_znode(struct ubifs_info *c, struct ubifs_znode *znode)

    get the znode to the left.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode

.. _`left_znode.description`:

Description
-----------

This function returns a pointer to the znode to the left of \ ``znode``\  or NULL if
there is not one. A negative error code is returned on failure.

.. _`right_znode`:

right_znode
===========

.. c:function:: struct ubifs_znode *right_znode(struct ubifs_info *c, struct ubifs_znode *znode)

    get the znode to the right.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_znode \*znode:
        znode

.. _`right_znode.description`:

Description
-----------

This function returns a pointer to the znode to the right of \ ``znode``\  or NULL
if there is not one. A negative error code is returned on failure.

.. _`lookup_znode`:

lookup_znode
============

.. c:function:: struct ubifs_znode *lookup_znode(struct ubifs_info *c, union ubifs_key *key, int level, int lnum, int offs)

    find a particular indexing node from TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        index node key to lookup

    :param int level:
        index node level

    :param int lnum:
        index node LEB number

    :param int offs:
        index node offset

.. _`lookup_znode.description`:

Description
-----------

This function searches an indexing node by its first key \ ``key``\  and its
address \ ``lnum``\ :\ ``offs``\ . It looks up the indexing tree by pulling all indexing
nodes it traverses to TNC. This function is called for indexing nodes which
were found on the media by scanning, for example when garbage-collecting or
when doing in-the-gaps commit. This means that the indexing node which is
looked for does not have to have exactly the same leftmost key \ ``key``\ , because
the leftmost key may have been changed, in which case TNC will contain a
dirty znode which still refers the same \ ``lnum``\ :\ ``offs``\ . This function is clever
enough to recognize such indexing nodes.

Note, if a znode was deleted or changed too much, then this function will
not find it. For situations like this UBIFS has the old index RB-tree
(indexed by \ ``lnum``\ :\ ``offs``\ ).

This function returns a pointer to the znode found or \ ``NULL``\  if it is not
found. A negative error code is returned on failure.

.. _`is_idx_node_in_tnc`:

is_idx_node_in_tnc
==================

.. c:function:: int is_idx_node_in_tnc(struct ubifs_info *c, union ubifs_key *key, int level, int lnum, int offs)

    determine if an index node is in the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key of index node

    :param int level:
        index node level

    :param int lnum:
        LEB number of index node

    :param int offs:
        offset of index node

.. _`is_idx_node_in_tnc.description`:

Description
-----------

This function returns \ ``0``\  if the index node is not referred to in the TNC, \ ``1``\ 
if the index node is referred to in the TNC and the corresponding znode is
dirty, \ ``2``\  if an index node is referred to in the TNC and the corresponding
znode is clean, and a negative error code in case of failure.

Note, the \ ``key``\  argument has to be the key of the first child. Also note,
this function relies on the fact that 0:0 is never a valid LEB number and
offset for a main-area node.

.. _`is_leaf_node_in_tnc`:

is_leaf_node_in_tnc
===================

.. c:function:: int is_leaf_node_in_tnc(struct ubifs_info *c, union ubifs_key *key, int lnum, int offs)

    determine if a non-indexing not is in the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        node key

    :param int lnum:
        node LEB number

    :param int offs:
        node offset

.. _`is_leaf_node_in_tnc.description`:

Description
-----------

This function returns \ ``1``\  if the node is referred to in the TNC, \ ``0``\  if it is
not, and a negative error code in case of failure.

Note, this function relies on the fact that 0:0 is never a valid LEB number
and offset for a main-area node.

.. _`ubifs_tnc_has_node`:

ubifs_tnc_has_node
==================

.. c:function:: int ubifs_tnc_has_node(struct ubifs_info *c, union ubifs_key *key, int level, int lnum, int offs, int is_idx)

    determine whether a node is in the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        node key

    :param int level:
        index node level (if it is an index node)

    :param int lnum:
        node LEB number

    :param int offs:
        node offset

    :param int is_idx:
        non-zero if the node is an index node

.. _`ubifs_tnc_has_node.description`:

Description
-----------

This function returns \ ``1``\  if the node is in the TNC, \ ``0``\  if it is not, and a
negative error code in case of failure. For index nodes, \ ``key``\  has to be the
key of the first child. An index node is considered to be in the TNC only if
the corresponding znode is clean or has not been loaded.

.. _`ubifs_dirty_idx_node`:

ubifs_dirty_idx_node
====================

.. c:function:: int ubifs_dirty_idx_node(struct ubifs_info *c, union ubifs_key *key, int level, int lnum, int offs)

    dirty an index node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        index node key

    :param int level:
        index node level

    :param int lnum:
        index node LEB number

    :param int offs:
        index node offset

.. _`ubifs_dirty_idx_node.description`:

Description
-----------

This function loads and dirties an index node so that it can be garbage
collected. The \ ``key``\  argument has to be the key of the first child. This
function relies on the fact that 0:0 is never a valid LEB number and offset
for a main-area node. Returns \ ``0``\  on success and a negative error code on
failure.

.. _`dbg_check_inode_size`:

dbg_check_inode_size
====================

.. c:function:: int dbg_check_inode_size(struct ubifs_info *c, const struct inode *inode, loff_t size)

    check if inode size is correct.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const struct inode \*inode:
        *undescribed*

    :param loff_t size:
        inode size

.. _`dbg_check_inode_size.description`:

Description
-----------

This function makes sure that the inode size (\ ``size``\ ) is correct and it does
not have any pages beyond \ ``size``\ . Returns zero if the inode is OK, \ ``-EINVAL``\ 
if it has a data page beyond \ ``size``\ , and other negative error code in case of
other errors.

.. This file was automatic generated / don't edit.


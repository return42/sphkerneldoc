.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/lpt.c

.. _`do_calc_lpt_geom`:

do_calc_lpt_geom
================

.. c:function:: void do_calc_lpt_geom(struct ubifs_info *c)

    calculate sizes for the LPT area.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`do_calc_lpt_geom.description`:

Description
-----------

Calculate the sizes of LPT bit fields, nodes, and tree, based on the
properties of the flash and whether LPT is "big" (c->big_lpt).

.. _`ubifs_calc_lpt_geom`:

ubifs_calc_lpt_geom
===================

.. c:function:: int ubifs_calc_lpt_geom(struct ubifs_info *c)

    calculate and check sizes for the LPT area.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_calc_lpt_geom.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`calc_dflt_lpt_geom`:

calc_dflt_lpt_geom
==================

.. c:function:: int calc_dflt_lpt_geom(struct ubifs_info *c, int *main_lebs, int *big_lpt)

    calculate default LPT geometry.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int \*main_lebs:
        number of main area LEBs is passed and returned here

    :param int \*big_lpt:
        whether the LPT area is "big" is returned here

.. _`calc_dflt_lpt_geom.description`:

Description
-----------

The size of the LPT area depends on parameters that themselves are dependent
on the size of the LPT area. This function, successively recalculates the LPT
area geometry until the parameters and resultant geometry are consistent.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`pack_bits`:

pack_bits
=========

.. c:function:: void pack_bits(uint8_t **addr, int *pos, uint32_t val, int nrbits)

    pack bit fields end-to-end.

    :param uint8_t \*\*addr:
        address at which to pack (passed and next address returned)

    :param int \*pos:
        bit position at which to pack (passed and next position returned)

    :param uint32_t val:
        value to pack

    :param int nrbits:
        number of bits of value to pack (1-32)

.. _`ubifs_unpack_bits`:

ubifs_unpack_bits
=================

.. c:function:: uint32_t ubifs_unpack_bits(uint8_t **addr, int *pos, int nrbits)

    unpack bit fields.

    :param uint8_t \*\*addr:
        address at which to unpack (passed and next address returned)

    :param int \*pos:
        bit position at which to unpack (passed and next position returned)

    :param int nrbits:
        number of bits of value to unpack (1-32)

.. _`ubifs_unpack_bits.description`:

Description
-----------

This functions returns the value unpacked.

.. _`ubifs_pack_pnode`:

ubifs_pack_pnode
================

.. c:function:: void ubifs_pack_pnode(struct ubifs_info *c, void *buf, struct ubifs_pnode *pnode)

    pack all the bit fields of a pnode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer into which to pack

    :param struct ubifs_pnode \*pnode:
        pnode to pack

.. _`ubifs_pack_nnode`:

ubifs_pack_nnode
================

.. c:function:: void ubifs_pack_nnode(struct ubifs_info *c, void *buf, struct ubifs_nnode *nnode)

    pack all the bit fields of a nnode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer into which to pack

    :param struct ubifs_nnode \*nnode:
        nnode to pack

.. _`ubifs_pack_ltab`:

ubifs_pack_ltab
===============

.. c:function:: void ubifs_pack_ltab(struct ubifs_info *c, void *buf, struct ubifs_lpt_lprops *ltab)

    pack the LPT's own lprops table.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer into which to pack

    :param struct ubifs_lpt_lprops \*ltab:
        LPT's own lprops table to pack

.. _`ubifs_pack_lsave`:

ubifs_pack_lsave
================

.. c:function:: void ubifs_pack_lsave(struct ubifs_info *c, void *buf, int *lsave)

    pack the LPT's save table.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer into which to pack

    :param int \*lsave:
        LPT's save table to pack

.. _`ubifs_add_lpt_dirt`:

ubifs_add_lpt_dirt
==================

.. c:function:: void ubifs_add_lpt_dirt(struct ubifs_info *c, int lnum, int dirty)

    add dirty space to LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number to which to add dirty space

    :param int dirty:
        amount of dirty space to add

.. _`set_ltab`:

set_ltab
========

.. c:function:: void set_ltab(struct ubifs_info *c, int lnum, int free, int dirty)

    set LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param int free:
        amount of free space

    :param int dirty:
        amount of dirty space

.. _`ubifs_add_nnode_dirt`:

ubifs_add_nnode_dirt
====================

.. c:function:: void ubifs_add_nnode_dirt(struct ubifs_info *c, struct ubifs_nnode *nnode)

    add dirty space to LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*nnode:
        nnode for which to add dirt

.. _`add_pnode_dirt`:

add_pnode_dirt
==============

.. c:function:: void add_pnode_dirt(struct ubifs_info *c, struct ubifs_pnode *pnode)

    add dirty space to LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode for which to add dirt

.. _`calc_nnode_num`:

calc_nnode_num
==============

.. c:function:: int calc_nnode_num(int row, int col)

    calculate nnode number.

    :param int row:
        the row in the tree (root is zero)

    :param int col:
        the column in the row (leftmost is zero)

.. _`calc_nnode_num.description`:

Description
-----------

The nnode number is a number that uniquely identifies a nnode and can be used
easily to traverse the tree from the root to that nnode.

This function calculates and returns the nnode number for the nnode at \ ``row``\ 
and \ ``col``\ .

.. _`calc_nnode_num_from_parent`:

calc_nnode_num_from_parent
==========================

.. c:function:: int calc_nnode_num_from_parent(const struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    calculate nnode number.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode

    :param int iip:
        index in parent

.. _`calc_nnode_num_from_parent.description`:

Description
-----------

The nnode number is a number that uniquely identifies a nnode and can be used
easily to traverse the tree from the root to that nnode.

This function calculates and returns the nnode number based on the parent's
nnode number and the index in parent.

.. _`calc_pnode_num_from_parent`:

calc_pnode_num_from_parent
==========================

.. c:function:: int calc_pnode_num_from_parent(const struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    calculate pnode number.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode

    :param int iip:
        index in parent

.. _`calc_pnode_num_from_parent.description`:

Description
-----------

The pnode number is a number that uniquely identifies a pnode and can be used
easily to traverse the tree from the root to that pnode.

This function calculates and returns the pnode number based on the parent's
nnode number and the index in parent.

.. _`ubifs_create_dflt_lpt`:

ubifs_create_dflt_lpt
=====================

.. c:function:: int ubifs_create_dflt_lpt(struct ubifs_info *c, int *main_lebs, int lpt_first, int *lpt_lebs, int *big_lpt)

    create default LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int \*main_lebs:
        number of main area LEBs is passed and returned here

    :param int lpt_first:
        LEB number of first LPT LEB

    :param int \*lpt_lebs:
        number of LEBs for LPT is passed and returned here

    :param int \*big_lpt:
        use big LPT model is passed and returned here

.. _`ubifs_create_dflt_lpt.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`update_cats`:

update_cats
===========

.. c:function:: void update_cats(struct ubifs_info *c, struct ubifs_pnode *pnode)

    add LEB properties of a pnode to LEB category lists and heaps.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode

.. _`update_cats.description`:

Description
-----------

When a pnode is loaded into memory, the LEB properties it contains are added,
by this function, to the LEB category lists and heaps.

.. _`replace_cats`:

replace_cats
============

.. c:function:: void replace_cats(struct ubifs_info *c, struct ubifs_pnode *old_pnode, struct ubifs_pnode *new_pnode)

    add LEB properties of a pnode to LEB category lists and heaps.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*old_pnode:
        pnode copied

    :param struct ubifs_pnode \*new_pnode:
        pnode copy

.. _`replace_cats.description`:

Description
-----------

During commit it is sometimes necessary to copy a pnode
(see dirty_cow_pnode).  When that happens, references in
category lists and heaps must be replaced.  This function does that.

.. _`check_lpt_crc`:

check_lpt_crc
=============

.. c:function:: int check_lpt_crc(const struct ubifs_info *c, void *buf, int len)

    check LPT node crc is correct.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer containing node

    :param int len:
        length of node

.. _`check_lpt_crc.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`check_lpt_type`:

check_lpt_type
==============

.. c:function:: int check_lpt_type(const struct ubifs_info *c, uint8_t **addr, int *pos, int type)

    check LPT node type is correct.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param uint8_t \*\*addr:
        address of type bit field is passed and returned updated here

    :param int \*pos:
        position of type bit field is passed and returned updated here

    :param int type:
        expected type

.. _`check_lpt_type.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`unpack_pnode`:

unpack_pnode
============

.. c:function:: int unpack_pnode(const struct ubifs_info *c, void *buf, struct ubifs_pnode *pnode)

    unpack a pnode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer containing packed pnode to unpack

    :param struct ubifs_pnode \*pnode:
        pnode structure to fill

.. _`unpack_pnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_unpack_nnode`:

ubifs_unpack_nnode
==================

.. c:function:: int ubifs_unpack_nnode(const struct ubifs_info *c, void *buf, struct ubifs_nnode *nnode)

    unpack a nnode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer containing packed nnode to unpack

    :param struct ubifs_nnode \*nnode:
        nnode structure to fill

.. _`ubifs_unpack_nnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`unpack_ltab`:

unpack_ltab
===========

.. c:function:: int unpack_ltab(const struct ubifs_info *c, void *buf)

    unpack the LPT's own lprops table.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer from which to unpack

.. _`unpack_ltab.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`unpack_lsave`:

unpack_lsave
============

.. c:function:: int unpack_lsave(const struct ubifs_info *c, void *buf)

    unpack the LPT's save table.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer from which to unpack

.. _`unpack_lsave.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`validate_nnode`:

validate_nnode
==============

.. c:function:: int validate_nnode(const struct ubifs_info *c, struct ubifs_nnode *nnode, struct ubifs_nnode *parent, int iip)

    validate a nnode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*nnode:
        nnode to validate

    :param struct ubifs_nnode \*parent:
        parent nnode (or NULL for the root nnode)

    :param int iip:
        index in parent

.. _`validate_nnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`validate_pnode`:

validate_pnode
==============

.. c:function:: int validate_pnode(const struct ubifs_info *c, struct ubifs_pnode *pnode, struct ubifs_nnode *parent, int iip)

    validate a pnode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode to validate

    :param struct ubifs_nnode \*parent:
        parent nnode

    :param int iip:
        index in parent

.. _`validate_pnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`set_pnode_lnum`:

set_pnode_lnum
==============

.. c:function:: void set_pnode_lnum(const struct ubifs_info *c, struct ubifs_pnode *pnode)

    set LEB numbers on a pnode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode to update

.. _`set_pnode_lnum.description`:

Description
-----------

This function calculates the LEB numbers for the LEB properties it contains
based on the pnode number.

.. _`ubifs_read_nnode`:

ubifs_read_nnode
================

.. c:function:: int ubifs_read_nnode(struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    read a nnode from flash and link it to the tree in memory.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode (or NULL for the root)

    :param int iip:
        index in parent

.. _`ubifs_read_nnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`read_pnode`:

read_pnode
==========

.. c:function:: int read_pnode(struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    read a pnode from flash and link it to the tree in memory.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode

    :param int iip:
        index in parent

.. _`read_pnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`read_ltab`:

read_ltab
=========

.. c:function:: int read_ltab(struct ubifs_info *c)

    read LPT's own lprops table.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`read_ltab.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`read_lsave`:

read_lsave
==========

.. c:function:: int read_lsave(struct ubifs_info *c)

    read LPT's save table.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`read_lsave.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_get_nnode`:

ubifs_get_nnode
===============

.. c:function:: struct ubifs_nnode *ubifs_get_nnode(struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    get a nnode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode (or NULL for the root)

    :param int iip:
        index in parent

.. _`ubifs_get_nnode.description`:

Description
-----------

This function returns a pointer to the nnode on success or a negative error
code on failure.

.. _`ubifs_get_pnode`:

ubifs_get_pnode
===============

.. c:function:: struct ubifs_pnode *ubifs_get_pnode(struct ubifs_info *c, struct ubifs_nnode *parent, int iip)

    get a pnode.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*parent:
        parent nnode

    :param int iip:
        index in parent

.. _`ubifs_get_pnode.description`:

Description
-----------

This function returns a pointer to the pnode on success or a negative error
code on failure.

.. _`ubifs_lpt_lookup`:

ubifs_lpt_lookup
================

.. c:function:: struct ubifs_lprops *ubifs_lpt_lookup(struct ubifs_info *c, int lnum)

    lookup LEB properties in the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number to lookup

.. _`ubifs_lpt_lookup.description`:

Description
-----------

This function returns a pointer to the LEB properties on success or a
negative error code on failure.

.. _`dirty_cow_nnode`:

dirty_cow_nnode
===============

.. c:function:: struct ubifs_nnode *dirty_cow_nnode(struct ubifs_info *c, struct ubifs_nnode *nnode)

    ensure a nnode is not being committed.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*nnode:
        nnode to check

.. _`dirty_cow_nnode.description`:

Description
-----------

Returns dirtied nnode on success or negative error code on failure.

.. _`dirty_cow_pnode`:

dirty_cow_pnode
===============

.. c:function:: struct ubifs_pnode *dirty_cow_pnode(struct ubifs_info *c, struct ubifs_pnode *pnode)

    ensure a pnode is not being committed.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode to check

.. _`dirty_cow_pnode.description`:

Description
-----------

Returns dirtied pnode on success or negative error code on failure.

.. _`ubifs_lpt_lookup_dirty`:

ubifs_lpt_lookup_dirty
======================

.. c:function:: struct ubifs_lprops *ubifs_lpt_lookup_dirty(struct ubifs_info *c, int lnum)

    lookup LEB properties in the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number to lookup

.. _`ubifs_lpt_lookup_dirty.description`:

Description
-----------

This function returns a pointer to the LEB properties on success or a
negative error code on failure.

.. _`lpt_init_rd`:

lpt_init_rd
===========

.. c:function:: int lpt_init_rd(struct ubifs_info *c)

    initialize the LPT for reading.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`lpt_init_rd.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`lpt_init_wr`:

lpt_init_wr
===========

.. c:function:: int lpt_init_wr(struct ubifs_info *c)

    initialize the LPT for writing.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`lpt_init_wr.description`:

Description
-----------

'lpt_init_rd()' must have been called already.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_lpt_init`:

ubifs_lpt_init
==============

.. c:function:: int ubifs_lpt_init(struct ubifs_info *c, int rd, int wr)

    initialize the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int rd:
        whether to initialize lpt for reading

    :param int wr:
        whether to initialize lpt for writing

.. _`ubifs_lpt_init.description`:

Description
-----------

For mounting 'rw', \ ``rd``\  and \ ``wr``\  are both true. For mounting 'ro', \ ``rd``\  is true
and \ ``wr``\  is false. For mounting from 'ro' to 'rw', \ ``rd``\  is false and \ ``wr``\  is
true.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`lpt_scan_node`:

struct lpt_scan_node
====================

.. c:type:: struct lpt_scan_node

    somewhere to put nodes while we scan LPT.

.. _`lpt_scan_node.definition`:

Definition
----------

.. code-block:: c

    struct lpt_scan_node {
        union {unnamed_union};
        int in_tree;
        union ptr;
    }

.. _`lpt_scan_node.members`:

Members
-------

{unnamed_union}
    anonymous


in_tree
    is the node in the tree in memory

ptr
    *undescribed*

ptr.nnode
    pointer to the nnode (if it is an nnode) which may be here or in
    the tree

ptr.pnode
    ditto for pnode

ptr.cnode
    ditto for cnode

.. _`scan_get_nnode`:

scan_get_nnode
==============

.. c:function:: struct ubifs_nnode *scan_get_nnode(struct ubifs_info *c, struct lpt_scan_node *path, struct ubifs_nnode *parent, int iip)

    for the scan, get a nnode from either the tree or flash.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param struct lpt_scan_node \*path:
        where to put the nnode

    :param struct ubifs_nnode \*parent:
        parent of the nnode

    :param int iip:
        index in parent of the nnode

.. _`scan_get_nnode.description`:

Description
-----------

This function returns a pointer to the nnode on success or a negative error
code on failure.

.. _`scan_get_pnode`:

scan_get_pnode
==============

.. c:function:: struct ubifs_pnode *scan_get_pnode(struct ubifs_info *c, struct lpt_scan_node *path, struct ubifs_nnode *parent, int iip)

    for the scan, get a pnode from either the tree or flash.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param struct lpt_scan_node \*path:
        where to put the pnode

    :param struct ubifs_nnode \*parent:
        parent of the pnode

    :param int iip:
        index in parent of the pnode

.. _`scan_get_pnode.description`:

Description
-----------

This function returns a pointer to the pnode on success or a negative error
code on failure.

.. _`ubifs_lpt_scan_nolock`:

ubifs_lpt_scan_nolock
=====================

.. c:function:: int ubifs_lpt_scan_nolock(struct ubifs_info *c, int start_lnum, int end_lnum, ubifs_lpt_scan_callback scan_cb, void *data)

    scan the LPT.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int start_lnum:
        LEB number from which to start scanning

    :param int end_lnum:
        LEB number at which to stop scanning

    :param ubifs_lpt_scan_callback scan_cb:
        callback function called for each lprops

    :param void \*data:
        data to be passed to the callback function

.. _`ubifs_lpt_scan_nolock.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_chk_pnode`:

dbg_chk_pnode
=============

.. c:function:: int dbg_chk_pnode(struct ubifs_info *c, struct ubifs_pnode *pnode, int col)

    check a pnode.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode to check

    :param int col:
        pnode column

.. _`dbg_chk_pnode.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_check_lpt_nodes`:

dbg_check_lpt_nodes
===================

.. c:function:: int dbg_check_lpt_nodes(struct ubifs_info *c, struct ubifs_cnode *cnode, int row, int col)

    check nnodes and pnodes.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param struct ubifs_cnode \*cnode:
        next cnode (nnode or pnode) to check

    :param int row:
        row of cnode (root is zero)

    :param int col:
        column of cnode (leftmost is zero)

.. _`dbg_check_lpt_nodes.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. This file was automatic generated / don't edit.


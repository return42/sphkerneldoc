.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/replay.c

.. _`replay_entry`:

struct replay_entry
===================

.. c:type:: struct replay_entry

    replay list entry.

.. _`replay_entry.definition`:

Definition
----------

.. code-block:: c

    struct replay_entry {
        int lnum;
        int offs;
        int len;
        unsigned int deletion:1;
        unsigned long long sqnum;
        struct list_head list;
        union ubifs_key key;
        union {unnamed_union};
    }

.. _`replay_entry.members`:

Members
-------

lnum
    logical eraseblock number of the node

offs
    node offset

len
    node length

deletion
    non-zero if this entry corresponds to a node deletion

sqnum
    node sequence number

list
    links the replay list

key
    node key

{unnamed_union}
    anonymous


.. _`replay_entry.description`:

Description
-----------

The replay process first scans all buds and builds the replay list, then
sorts the replay list in nodes sequence number order, and then inserts all
the replay entries to the TNC.

.. _`bud_entry`:

struct bud_entry
================

.. c:type:: struct bud_entry

    entry in the list of buds to replay.

.. _`bud_entry.definition`:

Definition
----------

.. code-block:: c

    struct bud_entry {
        struct list_head list;
        struct ubifs_bud *bud;
        unsigned long long sqnum;
        int free;
        int dirty;
    }

.. _`bud_entry.members`:

Members
-------

list
    next bud in the list

bud
    bud description object

sqnum
    reference node sequence number

free
    free bytes in the bud

dirty
    dirty bytes in the bud

.. _`set_bud_lprops`:

set_bud_lprops
==============

.. c:function:: int set_bud_lprops(struct ubifs_info *c, struct bud_entry *b)

    set free and dirty space used by a bud.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct bud_entry \*b:
        bud entry which describes the bud

.. _`set_bud_lprops.description`:

Description
-----------

This function makes sure the LEB properties of bud \ ``b``\  are set correctly
after the replay. Returns zero in case of success and a negative error code
in case of failure.

.. _`set_buds_lprops`:

set_buds_lprops
===============

.. c:function:: int set_buds_lprops(struct ubifs_info *c)

    set free and dirty space for all replayed buds.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`set_buds_lprops.description`:

Description
-----------

This function sets LEB properties for all replayed buds. Returns zero in
case of success and a negative error code in case of failure.

.. _`trun_remove_range`:

trun_remove_range
=================

.. c:function:: int trun_remove_range(struct ubifs_info *c, struct replay_entry *r)

    apply a replay entry for a truncation to the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct replay_entry \*r:
        replay entry of truncation

.. _`apply_replay_entry`:

apply_replay_entry
==================

.. c:function:: int apply_replay_entry(struct ubifs_info *c, struct replay_entry *r)

    apply a replay entry to the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct replay_entry \*r:
        replay entry to apply

.. _`apply_replay_entry.description`:

Description
-----------

Apply a replay entry to the TNC.

.. _`replay_entries_cmp`:

replay_entries_cmp
==================

.. c:function:: int replay_entries_cmp(void *priv, struct list_head *a, struct list_head *b)

    compare 2 replay entries.

    :param void \*priv:
        UBIFS file-system description object

    :param struct list_head \*a:
        second replay entry

    :param struct list_head \*b:
        *undescribed*

.. _`replay_entries_cmp.description`:

Description
-----------

This is a comparios function for '\ :c:func:`list_sort`\ ' which compares 2 replay
entries \ ``a``\  and \ ``b``\  by comparing their sequence numer.  Returns \ ``1``\  if \ ``a``\  has
greater sequence number and \ ``-1``\  otherwise.

.. _`apply_replay_list`:

apply_replay_list
=================

.. c:function:: int apply_replay_list(struct ubifs_info *c)

    apply the replay list to the TNC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`apply_replay_list.description`:

Description
-----------

Apply all entries in the replay list to the TNC. Returns zero in case of
success and a negative error code in case of failure.

.. _`destroy_replay_list`:

destroy_replay_list
===================

.. c:function:: void destroy_replay_list(struct ubifs_info *c)

    destroy the replay.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`destroy_replay_list.description`:

Description
-----------

Destroy the replay list.

.. _`insert_node`:

insert_node
===========

.. c:function:: int insert_node(struct ubifs_info *c, int lnum, int offs, int len, union ubifs_key *key, unsigned long long sqnum, int deletion, int *used, loff_t old_size, loff_t new_size)

    insert a node to the replay list

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        node logical eraseblock number

    :param int offs:
        node offset

    :param int len:
        node length

    :param union ubifs_key \*key:
        node key

    :param unsigned long long sqnum:
        sequence number

    :param int deletion:
        non-zero if this is a deletion

    :param int \*used:
        number of bytes in use in a LEB

    :param loff_t old_size:
        truncation old size

    :param loff_t new_size:
        truncation new size

.. _`insert_node.description`:

Description
-----------

This function inserts a scanned non-direntry node to the replay list. The
replay list contains \ ``struct``\  replay_entry elements, and we sort this list in
sequence number order before applying it. The replay list is applied at the
very end of the replay process. Since the list is sorted in sequence number
order, the older modifications are applied first. This function returns zero
in case of success and a negative error code in case of failure.

.. _`insert_dent`:

insert_dent
===========

.. c:function:: int insert_dent(struct ubifs_info *c, int lnum, int offs, int len, union ubifs_key *key, const char *name, int nlen, unsigned long long sqnum, int deletion, int *used)

    insert a directory entry node into the replay list.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        node logical eraseblock number

    :param int offs:
        node offset

    :param int len:
        node length

    :param union ubifs_key \*key:
        node key

    :param const char \*name:
        directory entry name

    :param int nlen:
        directory entry name length

    :param unsigned long long sqnum:
        sequence number

    :param int deletion:
        non-zero if this is a deletion

    :param int \*used:
        number of bytes in use in a LEB

.. _`insert_dent.description`:

Description
-----------

This function inserts a scanned directory entry node or an extended
attribute entry to the replay list. Returns zero in case of success and a
negative error code in case of failure.

.. _`ubifs_validate_entry`:

ubifs_validate_entry
====================

.. c:function:: int ubifs_validate_entry(struct ubifs_info *c, const struct ubifs_dent_node *dent)

    validate directory or extended attribute entry node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const struct ubifs_dent_node \*dent:
        the node to validate

.. _`ubifs_validate_entry.description`:

Description
-----------

This function validates directory or extended attribute entry node \ ``dent``\ .
Returns zero if the node is all right and a \ ``-EINVAL``\  if not.

.. _`is_last_bud`:

is_last_bud
===========

.. c:function:: int is_last_bud(struct ubifs_info *c, struct ubifs_bud *bud)

    check if the bud is the last in the journal head.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_bud \*bud:
        bud description object

.. _`is_last_bud.description`:

Description
-----------

This function checks if bud \ ``bud``\  is the last bud in its journal head. This
information is then used by '\ :c:func:`replay_bud`\ ' to decide whether the bud can
have corruptions or not. Indeed, only last buds can be corrupted by power
cuts. Returns \ ``1``\  if this is the last bud, and \ ``0``\  if not.

.. _`replay_bud`:

replay_bud
==========

.. c:function:: int replay_bud(struct ubifs_info *c, struct bud_entry *b)

    replay a bud logical eraseblock.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct bud_entry \*b:
        bud entry which describes the bud

.. _`replay_bud.description`:

Description
-----------

This function replays bud \ ``bud``\ , recovers it if needed, and adds all nodes
from this bud to the replay list. Returns zero in case of success and a
negative error code in case of failure.

.. _`replay_buds`:

replay_buds
===========

.. c:function:: int replay_buds(struct ubifs_info *c)

    replay all buds.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`replay_buds.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`destroy_bud_list`:

destroy_bud_list
================

.. c:function:: void destroy_bud_list(struct ubifs_info *c)

    destroy the list of buds to replay.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`add_replay_bud`:

add_replay_bud
==============

.. c:function:: int add_replay_bud(struct ubifs_info *c, int lnum, int offs, int jhead, unsigned long long sqnum)

    add a bud to the list of buds to replay.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        bud logical eraseblock number to replay

    :param int offs:
        bud start offset

    :param int jhead:
        journal head to which this bud belongs

    :param unsigned long long sqnum:
        reference node sequence number

.. _`add_replay_bud.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`validate_ref`:

validate_ref
============

.. c:function:: int validate_ref(struct ubifs_info *c, const struct ubifs_ref_node *ref)

    validate a reference node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param const struct ubifs_ref_node \*ref:
        the reference node to validate

.. _`validate_ref.description`:

Description
-----------

This function returns \ ``1``\  if a bud reference already exists for the LEB. \ ``0``\  is
returned if the reference node is new, otherwise \ ``-EINVAL``\  is returned if
validation failed.

.. _`replay_log_leb`:

replay_log_leb
==============

.. c:function:: int replay_log_leb(struct ubifs_info *c, int lnum, int offs, void *sbuf)

    replay a log logical eraseblock.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        log logical eraseblock to replay

    :param int offs:
        offset to start replaying from

    :param void \*sbuf:
        scan buffer

.. _`replay_log_leb.description`:

Description
-----------

This function replays a log LEB and returns zero in case of success, \ ``1``\  if
this is the last LEB in the log, and a negative error code in case of
failure.

.. _`take_ihead`:

take_ihead
==========

.. c:function:: int take_ihead(struct ubifs_info *c)

    update the status of the index head in lprops to 'taken'.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`take_ihead.description`:

Description
-----------

This function returns the amount of free space in the index head LEB or a
negative error code.

.. _`ubifs_replay_journal`:

ubifs_replay_journal
====================

.. c:function:: int ubifs_replay_journal(struct ubifs_info *c)

    replay journal.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_replay_journal.description`:

Description
-----------

This function scans the journal, replays and cleans it up. It makes sure all
memory data structures related to uncommitted journal are built (dirty TNC
tree, tree of buds, modified lprops, etc).

.. This file was automatic generated / don't edit.


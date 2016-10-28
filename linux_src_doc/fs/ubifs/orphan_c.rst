.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/orphan.c

.. _`ubifs_add_orphan`:

ubifs_add_orphan
================

.. c:function:: int ubifs_add_orphan(struct ubifs_info *c, ino_t inum)

    add an orphan.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        orphan inode number

.. _`ubifs_add_orphan.description`:

Description
-----------

Add an orphan. This function is called when an inodes link count drops to
zero.

.. _`ubifs_delete_orphan`:

ubifs_delete_orphan
===================

.. c:function:: void ubifs_delete_orphan(struct ubifs_info *c, ino_t inum)

    delete an orphan.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        orphan inode number

.. _`ubifs_delete_orphan.description`:

Description
-----------

Delete an orphan. This function is called when an inode is deleted.

.. _`ubifs_orphan_start_commit`:

ubifs_orphan_start_commit
=========================

.. c:function:: int ubifs_orphan_start_commit(struct ubifs_info *c)

    start commit of orphans.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_orphan_start_commit.description`:

Description
-----------

Start commit of orphans.

.. _`avail_orphs`:

avail_orphs
===========

.. c:function:: int avail_orphs(struct ubifs_info *c)

    calculate available space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`avail_orphs.description`:

Description
-----------

This function returns the number of orphans that can be written in the
available space.

.. _`tot_avail_orphs`:

tot_avail_orphs
===============

.. c:function:: int tot_avail_orphs(struct ubifs_info *c)

    calculate total space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`tot_avail_orphs.description`:

Description
-----------

This function returns the number of orphans that can be written in half
the total space. That leaves half the space for adding new orphans.

.. _`do_write_orph_node`:

do_write_orph_node
==================

.. c:function:: int do_write_orph_node(struct ubifs_info *c, int len, int atomic)

    write a node to the orphan head.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int len:
        length of node

    :param int atomic:
        write atomically

.. _`do_write_orph_node.description`:

Description
-----------

This function writes a node to the orphan head from the orphan buffer. If
\ ``atomic``\  is not zero, then the write is done atomically. On success, \ ``0``\  is
returned, otherwise a negative error code is returned.

.. _`write_orph_node`:

write_orph_node
===============

.. c:function:: int write_orph_node(struct ubifs_info *c, int atomic)

    write an orphan node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int atomic:
        write atomically

.. _`write_orph_node.description`:

Description
-----------

This function builds an orphan node from the cnext list and writes it to the
orphan head. On success, \ ``0``\  is returned, otherwise a negative error code
is returned.

.. _`write_orph_nodes`:

write_orph_nodes
================

.. c:function:: int write_orph_nodes(struct ubifs_info *c, int atomic)

    write orphan nodes until there are no more to commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int atomic:
        write atomically

.. _`write_orph_nodes.description`:

Description
-----------

This function writes orphan nodes for all the orphans to commit. On success,
\ ``0``\  is returned, otherwise a negative error code is returned.

.. _`consolidate`:

consolidate
===========

.. c:function:: int consolidate(struct ubifs_info *c)

    consolidate the orphan area.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`consolidate.description`:

Description
-----------

This function enables consolidation by putting all the orphans into the list
to commit. The list is in the order that the orphans were added, and the
LEBs are written atomically in order, so at no time can orphans be lost by
an unclean unmount.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`commit_orphans`:

commit_orphans
==============

.. c:function:: int commit_orphans(struct ubifs_info *c)

    commit orphans.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`commit_orphans.description`:

Description
-----------

This function commits orphans to flash. On success, \ ``0``\  is returned,
otherwise a negative error code is returned.

.. _`erase_deleted`:

erase_deleted
=============

.. c:function:: void erase_deleted(struct ubifs_info *c)

    erase the orphans marked for deletion.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`erase_deleted.description`:

Description
-----------

During commit, the orphans being committed cannot be deleted, so they are
marked for deletion and deleted by this function. Also, the recovery
adds killed orphans to the deletion list, and therefore they are deleted
here too.

.. _`ubifs_orphan_end_commit`:

ubifs_orphan_end_commit
=======================

.. c:function:: int ubifs_orphan_end_commit(struct ubifs_info *c)

    end commit of orphans.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_orphan_end_commit.description`:

Description
-----------

End commit of orphans.

.. _`ubifs_clear_orphans`:

ubifs_clear_orphans
===================

.. c:function:: int ubifs_clear_orphans(struct ubifs_info *c)

    erase all LEBs used for orphans.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_clear_orphans.description`:

Description
-----------

If recovery is not required, then the orphans from the previous session
are not needed. This function locates the LEBs used to record
orphans, and un-maps them.

.. _`insert_dead_orphan`:

insert_dead_orphan
==================

.. c:function:: int insert_dead_orphan(struct ubifs_info *c, ino_t inum)

    insert an orphan.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        orphan inode number

.. _`insert_dead_orphan.description`:

Description
-----------

This function is a helper to the '\ :c:func:`do_kill_orphans`\ ' function. The orphan
must be kept until the next commit, so it is added to the rb-tree and the
deletion list.

.. _`do_kill_orphans`:

do_kill_orphans
===============

.. c:function:: int do_kill_orphans(struct ubifs_info *c, struct ubifs_scan_leb *sleb, unsigned long long *last_cmt_no, int *outofdate, int *last_flagged)

    remove orphan inodes from the index.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_scan_leb \*sleb:
        scanned LEB

    :param unsigned long long \*last_cmt_no:
        cmt_no of last orphan node read is passed and returned here

    :param int \*outofdate:
        whether the LEB is out of date is returned here

    :param int \*last_flagged:
        whether the end orphan node is encountered

.. _`do_kill_orphans.description`:

Description
-----------

This function is a helper to the '\ :c:func:`kill_orphans`\ ' function. It goes through
every orphan node in a LEB and for every inode number recorded, removes
all keys for that inode from the TNC.

.. _`kill_orphans`:

kill_orphans
============

.. c:function:: int kill_orphans(struct ubifs_info *c)

    remove all orphan inodes from the index.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`kill_orphans.description`:

Description
-----------

If recovery is required, then orphan inodes recorded during the previous
session (which ended with an unclean unmount) must be deleted from the index.
This is done by updating the TNC, but since the index is not updated until
the next commit, the LEBs where the orphan information is recorded are not
erased until the next commit.

.. _`ubifs_mount_orphans`:

ubifs_mount_orphans
===================

.. c:function:: int ubifs_mount_orphans(struct ubifs_info *c, int unclean, int read_only)

    delete orphan inodes and erase LEBs that recorded them.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int unclean:
        indicates recovery from unclean unmount

    :param int read_only:
        indicates read only mount

.. _`ubifs_mount_orphans.description`:

Description
-----------

This function is called when mounting to erase orphans from the previous
session. If UBIFS was not unmounted cleanly, then the inodes recorded as
orphans are deleted.

.. This file was automatic generated / don't edit.


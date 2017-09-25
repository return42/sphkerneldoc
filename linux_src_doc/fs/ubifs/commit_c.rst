.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/commit.c

.. _`do_commit`:

do_commit
=========

.. c:function:: int do_commit(struct ubifs_info *c)

    commit the journal.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`do_commit.description`:

Description
-----------

This function implements UBIFS commit. It has to be called with commit lock
locked. Returns zero in case of success and a negative error code in case of
failure.

.. _`run_bg_commit`:

run_bg_commit
=============

.. c:function:: int run_bg_commit(struct ubifs_info *c)

    run background commit if it is needed.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`run_bg_commit.description`:

Description
-----------

This function runs background commit if it is needed. Returns zero in case
of success and a negative error code in case of failure.

.. _`ubifs_bg_thread`:

ubifs_bg_thread
===============

.. c:function:: int ubifs_bg_thread(void *info)

    UBIFS background thread function.

    :param void \*info:
        points to the file-system description object

.. _`ubifs_bg_thread.description`:

Description
-----------

This function implements various file-system background activities:
o when a write-buffer timer expires it synchronizes the appropriate
write-buffer;
o when the journal is about to be full, it starts in-advance commit.

Note, other stuff like background garbage collection may be added here in
future.

.. _`ubifs_commit_required`:

ubifs_commit_required
=====================

.. c:function:: void ubifs_commit_required(struct ubifs_info *c)

    set commit state to "required".

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_commit_required.description`:

Description
-----------

This function is called if a commit is required but cannot be done from the
calling function, so it is just flagged instead.

.. _`ubifs_request_bg_commit`:

ubifs_request_bg_commit
=======================

.. c:function:: void ubifs_request_bg_commit(struct ubifs_info *c)

    notify the background thread to do a commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_request_bg_commit.description`:

Description
-----------

This function is called if the journal is full enough to make a commit
worthwhile, so background thread is kicked to start it.

.. _`wait_for_commit`:

wait_for_commit
===============

.. c:function:: int wait_for_commit(struct ubifs_info *c)

    wait for commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`wait_for_commit.description`:

Description
-----------

This function sleeps until the commit operation is no longer running.

.. _`ubifs_run_commit`:

ubifs_run_commit
================

.. c:function:: int ubifs_run_commit(struct ubifs_info *c)

    run or wait for commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_run_commit.description`:

Description
-----------

This function runs commit and returns zero in case of success and a negative
error code in case of failure.

.. _`ubifs_gc_should_commit`:

ubifs_gc_should_commit
======================

.. c:function:: int ubifs_gc_should_commit(struct ubifs_info *c)

    determine if it is time for GC to run commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_gc_should_commit.description`:

Description
-----------

This function is called by garbage collection to determine if commit should
be run. If commit state is \ ``COMMIT_BACKGROUND``\ , which means that the journal
is full enough to start commit, this function returns true. It is not
absolutely necessary to commit yet, but it feels like this should be better
then to keep doing GC. This function returns \ ``1``\  if GC has to initiate commit
and \ ``0``\  if not.

.. _`idx_node`:

struct idx_node
===============

.. c:type:: struct idx_node

    hold index nodes during index tree traversal.

.. _`idx_node.definition`:

Definition
----------

.. code-block:: c

    struct idx_node {
        struct list_head list;
        int iip;
        union ubifs_key upper_key;
        struct ubifs_idx_node idx __aligned(8);
    }

.. _`idx_node.members`:

Members
-------

list
    list

iip
    index in parent (slot number of this indexing node in the parent
    indexing node)

upper_key
    all keys in this indexing node have to be less or equivalent to
    this key

idx
    index node (8-byte aligned because all node structures must be 8-byte
    aligned)

.. _`dbg_old_index_check_init`:

dbg_old_index_check_init
========================

.. c:function:: int dbg_old_index_check_init(struct ubifs_info *c, struct ubifs_zbranch *zroot)

    get information for the next old index check.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zroot:
        root of the index

.. _`dbg_old_index_check_init.description`:

Description
-----------

This function records information about the index that will be needed for the
next old index check i.e. 'dbg_check_old_index()'.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_check_old_index`:

dbg_check_old_index
===================

.. c:function:: int dbg_check_old_index(struct ubifs_info *c, struct ubifs_zbranch *zroot)

    check the old copy of the index.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_zbranch \*zroot:
        root of the new index

.. _`dbg_check_old_index.description`:

Description
-----------

In order to be able to recover from an unclean unmount, a complete copy of
the index must exist on flash. This is the "old" index. The commit process
must write the "new" index to flash without overwriting or destroying any
part of the old index. This function is run at commit end in order to check
that the old index does indeed exist completely intact.

This function returns \ ``0``\  on success and a negative error code on failure.

.. This file was automatic generated / don't edit.


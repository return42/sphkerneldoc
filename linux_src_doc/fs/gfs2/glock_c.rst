.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/glock.c

.. _`wake_up_glock`:

wake_up_glock
=============

.. c:function:: void wake_up_glock(struct gfs2_glock *gl)

    Wake up waiters on a glock

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

.. _`gfs2_glock_hold`:

gfs2_glock_hold
===============

.. c:function:: void gfs2_glock_hold(struct gfs2_glock *gl)

    increment reference count on glock

    :param gl:
        The glock to hold
    :type gl: struct gfs2_glock \*

.. _`demote_ok`:

demote_ok
=========

.. c:function:: int demote_ok(const struct gfs2_glock *gl)

    Check to see if it's ok to unlock a glock

    :param gl:
        the glock
    :type gl: const struct gfs2_glock \*

.. _`demote_ok.return`:

Return
------

1 if it's ok

.. _`gfs2_glock_put`:

gfs2_glock_put
==============

.. c:function:: void gfs2_glock_put(struct gfs2_glock *gl)

    Decrement reference count on glock

    :param gl:
        The glock to put
    :type gl: struct gfs2_glock \*

.. _`may_grant`:

may_grant
=========

.. c:function:: int may_grant(const struct gfs2_glock *gl, const struct gfs2_holder *gh)

    check if its ok to grant a new lock

    :param gl:
        The glock
    :type gl: const struct gfs2_glock \*

    :param gh:
        The lock request which we wish to grant
    :type gh: const struct gfs2_holder \*

.. _`may_grant.return`:

Return
------

true if its ok to grant the lock

.. _`do_error`:

do_error
========

.. c:function:: void do_error(struct gfs2_glock *gl, const int ret)

    Something unexpected has happened during a lock request

    :param gl:
        *undescribed*
    :type gl: struct gfs2_glock \*

    :param ret:
        *undescribed*
    :type ret: const int

.. _`do_promote`:

do_promote
==========

.. c:function:: int do_promote(struct gfs2_glock *gl)

    promote as many requests as possible on the current queue

    :param gl:
        The glock
    :type gl: struct gfs2_glock \*

.. _`do_promote.return`:

Return
------

1 if there is a blocked holder at the head of the list, or 2
if a type specific operation is underway.

.. _`find_first_waiter`:

find_first_waiter
=================

.. c:function:: struct gfs2_holder *find_first_waiter(const struct gfs2_glock *gl)

    find the first gh that's waiting for the glock

    :param gl:
        the glock
    :type gl: const struct gfs2_glock \*

.. _`state_change`:

state_change
============

.. c:function:: void state_change(struct gfs2_glock *gl, unsigned int new_state)

    record that the glock is now in a different state

    :param gl:
        the glock
        \ ``new_state``\  the new state
    :type gl: struct gfs2_glock \*

    :param new_state:
        *undescribed*
    :type new_state: unsigned int

.. _`finish_xmote`:

finish_xmote
============

.. c:function:: void finish_xmote(struct gfs2_glock *gl, unsigned int ret)

    The DLM has replied to one of our lock requests

    :param gl:
        The glock
    :type gl: struct gfs2_glock \*

    :param ret:
        The status from the DLM
    :type ret: unsigned int

.. _`do_xmote`:

do_xmote
========

.. c:function:: void do_xmote(struct gfs2_glock *gl, struct gfs2_holder *gh, unsigned int target)

    Calls the DLM to change the state of a lock

    :param gl:
        The lock state
    :type gl: struct gfs2_glock \*

    :param gh:
        The holder (only for promotes)
    :type gh: struct gfs2_holder \*

    :param target:
        The target lock state
    :type target: unsigned int

.. _`find_first_holder`:

find_first_holder
=================

.. c:function:: struct gfs2_holder *find_first_holder(const struct gfs2_glock *gl)

    find the first "holder" gh

    :param gl:
        the glock
    :type gl: const struct gfs2_glock \*

.. _`run_queue`:

run_queue
=========

.. c:function:: void run_queue(struct gfs2_glock *gl, const int nonblock)

    do all outstanding tasks related to a glock

    :param gl:
        The glock in question
    :type gl: struct gfs2_glock \*

    :param nonblock:
        True if we must not block in run_queue
    :type nonblock: const int

.. _`gfs2_glock_get`:

gfs2_glock_get
==============

.. c:function:: int gfs2_glock_get(struct gfs2_sbd *sdp, u64 number, const struct gfs2_glock_operations *glops, int create, struct gfs2_glock **glp)

    Get a glock, or create one if one doesn't exist

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param number:
        the lock number
    :type number: u64

    :param glops:
        The glock_operations to use
    :type glops: const struct gfs2_glock_operations \*

    :param create:
        If 0, don't create the glock if it doesn't exist
    :type create: int

    :param glp:
        the glock is returned here
    :type glp: struct gfs2_glock \*\*

.. _`gfs2_glock_get.description`:

Description
-----------

This does not lock a glock, just finds/creates structures for one.

.. _`gfs2_glock_get.return`:

Return
------

errno

.. _`gfs2_holder_init`:

gfs2_holder_init
================

.. c:function:: void gfs2_holder_init(struct gfs2_glock *gl, unsigned int state, u16 flags, struct gfs2_holder *gh)

    initialize a struct gfs2_holder in the default way

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param state:
        the state we're requesting
    :type state: unsigned int

    :param flags:
        the modifier flags
    :type flags: u16

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_holder_reinit`:

gfs2_holder_reinit
==================

.. c:function:: void gfs2_holder_reinit(unsigned int state, u16 flags, struct gfs2_holder *gh)

    reinitialize a struct gfs2_holder so we can requeue it

    :param state:
        the state we're requesting
    :type state: unsigned int

    :param flags:
        the modifier flags
    :type flags: u16

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_holder_reinit.description`:

Description
-----------

Don't mess with the glock.

.. _`gfs2_holder_uninit`:

gfs2_holder_uninit
==================

.. c:function:: void gfs2_holder_uninit(struct gfs2_holder *gh)

    uninitialize a holder structure (drop glock reference)

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_wait`:

gfs2_glock_wait
===============

.. c:function:: int gfs2_glock_wait(struct gfs2_holder *gh)

    wait on a glock acquisition

    :param gh:
        the glock holder
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_wait.return`:

Return
------

0 on success

.. _`handle_callback`:

handle_callback
===============

.. c:function:: void handle_callback(struct gfs2_glock *gl, unsigned int state, unsigned long delay, bool remote)

    process a demote request

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param state:
        the state the caller wants us to change to
    :type state: unsigned int

    :param delay:
        *undescribed*
    :type delay: unsigned long

    :param remote:
        *undescribed*
    :type remote: bool

.. _`handle_callback.description`:

Description
-----------

There are only two requests that we are going to see in actual

.. _`handle_callback.practise`:

practise
--------

LM_ST_SHARED and LM_ST_UNLOCKED

.. _`add_to_queue`:

add_to_queue
============

.. c:function:: void add_to_queue(struct gfs2_holder *gh)

    Add a holder to the wait queue (but look for recursion)

    :param gh:
        the holder structure to add
    :type gh: struct gfs2_holder \*

.. _`add_to_queue.description`:

Description
-----------

Eventually we should move the recursive locking trap to a
debugging option or something like that. This is the fast
path and needs to have the minimum number of distractions.

.. _`gfs2_glock_nq`:

gfs2_glock_nq
=============

.. c:function:: int gfs2_glock_nq(struct gfs2_holder *gh)

    enqueue a struct gfs2_holder onto a glock (acquire a glock)

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_nq.description`:

Description
-----------

if (gh->gh_flags & GL_ASYNC), this never returns an error

.. _`gfs2_glock_nq.return`:

Return
------

0, GLR_TRYFAILED, or errno on failure

.. _`gfs2_glock_poll`:

gfs2_glock_poll
===============

.. c:function:: int gfs2_glock_poll(struct gfs2_holder *gh)

    poll to see if an async request has been completed

    :param gh:
        the holder
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_poll.return`:

Return
------

1 if the request is ready to be \ :c:func:`gfs2_glock_wait`\ ed on

.. _`gfs2_glock_dq`:

gfs2_glock_dq
=============

.. c:function:: void gfs2_glock_dq(struct gfs2_holder *gh)

    dequeue a struct gfs2_holder from a glock (release a glock)

    :param gh:
        the glock holder
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_dq_uninit`:

gfs2_glock_dq_uninit
====================

.. c:function:: void gfs2_glock_dq_uninit(struct gfs2_holder *gh)

    dequeue a holder from a glock and initialize it

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_nq_num`:

gfs2_glock_nq_num
=================

.. c:function:: int gfs2_glock_nq_num(struct gfs2_sbd *sdp, u64 number, const struct gfs2_glock_operations *glops, unsigned int state, u16 flags, struct gfs2_holder *gh)

    acquire a glock based on lock number

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param number:
        the lock number
    :type number: u64

    :param glops:
        the glock operations for the type of glock
    :type glops: const struct gfs2_glock_operations \*

    :param state:
        the state to acquire the glock in
    :type state: unsigned int

    :param flags:
        modifier flags for the acquisition
    :type flags: u16

    :param gh:
        the struct gfs2_holder
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_nq_num.return`:

Return
------

errno

.. _`glock_compare`:

glock_compare
=============

.. c:function:: int glock_compare(const void *arg_a, const void *arg_b)

    Compare two struct gfs2_glock structures for sorting

    :param arg_a:
        the first structure
    :type arg_a: const void \*

    :param arg_b:
        the second structure
    :type arg_b: const void \*

.. _`nq_m_sync`:

nq_m_sync
=========

.. c:function:: int nq_m_sync(unsigned int num_gh, struct gfs2_holder *ghs, struct gfs2_holder **p)

    synchonously acquire more than one glock in deadlock free order

    :param num_gh:
        the number of structures
    :type num_gh: unsigned int

    :param ghs:
        an array of struct gfs2_holder structures
    :type ghs: struct gfs2_holder \*

    :param p:
        *undescribed*
    :type p: struct gfs2_holder \*\*

.. _`nq_m_sync.return`:

Return
------

0 on success (all glocks acquired),
errno on failure (no glocks acquired)

.. _`gfs2_glock_nq_m`:

gfs2_glock_nq_m
===============

.. c:function:: int gfs2_glock_nq_m(unsigned int num_gh, struct gfs2_holder *ghs)

    acquire multiple glocks

    :param num_gh:
        the number of structures
    :type num_gh: unsigned int

    :param ghs:
        an array of struct gfs2_holder structures
    :type ghs: struct gfs2_holder \*

.. _`gfs2_glock_nq_m.return`:

Return
------

0 on success (all glocks acquired),
errno on failure (no glocks acquired)

.. _`gfs2_glock_dq_m`:

gfs2_glock_dq_m
===============

.. c:function:: void gfs2_glock_dq_m(unsigned int num_gh, struct gfs2_holder *ghs)

    release multiple glocks

    :param num_gh:
        the number of structures
    :type num_gh: unsigned int

    :param ghs:
        an array of struct gfs2_holder structures
    :type ghs: struct gfs2_holder \*

.. _`gfs2_should_freeze`:

gfs2_should_freeze
==================

.. c:function:: int gfs2_should_freeze(const struct gfs2_glock *gl)

    Figure out if glock should be frozen

    :param gl:
        The glock in question
    :type gl: const struct gfs2_glock \*

.. _`gfs2_should_freeze.description`:

Description
-----------

Glocks are not frozen if (a) the result of the dlm operation is
an error, (b) the locking operation was an unlock operation or
(c) if there is a "noexp" flagged request anywhere in the queue

.. _`gfs2_should_freeze.return`:

Return
------

1 if freezing should occur, 0 otherwise

.. _`gfs2_glock_complete`:

gfs2_glock_complete
===================

.. c:function:: void gfs2_glock_complete(struct gfs2_glock *gl, int ret)

    Callback used by locking

    :param gl:
        Pointer to the glock
    :type gl: struct gfs2_glock \*

    :param ret:
        The return value from the dlm
    :type ret: int

.. _`gfs2_glock_complete.description`:

Description
-----------

The gl_reply field is under the gl_lockref.lock lock so that it is ok
to use a bitfield shared with other glock state fields.

.. _`gfs2_dispose_glock_lru`:

gfs2_dispose_glock_lru
======================

.. c:function:: void gfs2_dispose_glock_lru(struct list_head *list)

    Demote a list of glocks

    :param list:
        The list to dispose of
    :type list: struct list_head \*

.. _`gfs2_dispose_glock_lru.description`:

Description
-----------

Disposing of glocks may involve disk accesses, so that here we sort
the glocks by number (i.e. disk location of the inodes) so that if
there are any such accesses, they'll be sent in order (mostly).

Must be called under the lru_lock, but may drop and retake this
lock. While the lru_lock is dropped, entries may vanish from the
list, but no new entries will appear on the list (since it is
private)

.. _`gfs2_scan_glock_lru`:

gfs2_scan_glock_lru
===================

.. c:function:: long gfs2_scan_glock_lru(int nr)

    Scan the LRU looking for locks to demote

    :param nr:
        The number of entries to scan
    :type nr: int

.. _`gfs2_scan_glock_lru.description`:

Description
-----------

This function selects the entries on the LRU which are able to
be demoted, and then kicks off the process by calling
\ :c:func:`gfs2_dispose_glock_lru`\  above.

.. _`glock_hash_walk`:

glock_hash_walk
===============

.. c:function:: void glock_hash_walk(glock_examiner examiner, const struct gfs2_sbd *sdp)

    Call a function for glock in a hash bucket

    :param examiner:
        the function
    :type examiner: glock_examiner

    :param sdp:
        the filesystem
    :type sdp: const struct gfs2_sbd \*

.. _`glock_hash_walk.description`:

Description
-----------

Note that the function can be called multiple times on the same
object.  So the user must ensure that the function can cope with
that.

.. _`thaw_glock`:

thaw_glock
==========

.. c:function:: void thaw_glock(struct gfs2_glock *gl)

    thaw out a glock which has an unprocessed reply waiting

    :param gl:
        The glock to thaw
    :type gl: struct gfs2_glock \*

.. _`clear_glock`:

clear_glock
===========

.. c:function:: void clear_glock(struct gfs2_glock *gl)

    look at a glock and see if we can free it from glock cache

    :param gl:
        the glock to look at
    :type gl: struct gfs2_glock \*

.. _`gfs2_glock_thaw`:

gfs2_glock_thaw
===============

.. c:function:: void gfs2_glock_thaw(struct gfs2_sbd *sdp)

    Thaw any frozen glocks

    :param sdp:
        The super block
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_gl_hash_clear`:

gfs2_gl_hash_clear
==================

.. c:function:: void gfs2_gl_hash_clear(struct gfs2_sbd *sdp)

    Empty out the glock hash table

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_gl_hash_clear.description`:

Description
-----------

Called when unmounting the filesystem.

.. _`dump_holder`:

dump_holder
===========

.. c:function:: void dump_holder(struct seq_file *seq, const struct gfs2_holder *gh)

    print information about a glock holder

    :param seq:
        the seq_file struct
    :type seq: struct seq_file \*

    :param gh:
        the glock holder
    :type gh: const struct gfs2_holder \*

.. _`gfs2_dump_glock`:

gfs2_dump_glock
===============

.. c:function:: void gfs2_dump_glock(struct seq_file *seq, const struct gfs2_glock *gl)

    print information about a glock

    :param seq:
        The seq_file struct
    :type seq: struct seq_file \*

    :param gl:
        the glock
    :type gl: const struct gfs2_glock \*

.. _`gfs2_dump_glock.the-file-format-is-as-follows`:

The file format is as follows
-----------------------------

One line per object, capital letters are used to indicate objects
G = glock, I = Inode, R = rgrp, H = holder. Glocks are not indented,
other objects are indented by a single space and follow the glock to
which they are related. Fields are indicated by lower case letters
followed by a colon and the field value, except for strings which are in
[] so that its possible to see if they are composed of spaces for
example. The field's are n = number (id of the object), f = flags,
t = type, s = state, r = refcount, e = error, p = pid.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/wl.c

.. _`wl_tree_add`:

wl_tree_add
===========

.. c:function:: void wl_tree_add(struct ubi_wl_entry *e, struct rb_root *root)

    add a wear-leveling entry to a WL RB-tree.

    :param struct ubi_wl_entry \*e:
        the wear-leveling entry to add

    :param struct rb_root \*root:
        the root of the tree

.. _`wl_tree_add.description`:

Description
-----------

Note, we use (erase counter, physical eraseblock number) pairs as keys in
the \ ``ubi``\ ->used and \ ``ubi``\ ->free RB-trees.

.. _`wl_entry_destroy`:

wl_entry_destroy
================

.. c:function:: void wl_entry_destroy(struct ubi_device *ubi, struct ubi_wl_entry *e)

    destroy a wear-leveling entry.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the wear-leveling entry to add

.. _`wl_entry_destroy.description`:

Description
-----------

This function destroys a wear leveling entry and removes
the reference from the lookup table.

.. _`do_work`:

do_work
=======

.. c:function:: int do_work(struct ubi_device *ubi)

    do one pending work.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`do_work.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`in_wl_tree`:

in_wl_tree
==========

.. c:function:: int in_wl_tree(struct ubi_wl_entry *e, struct rb_root *root)

    check if wear-leveling entry is present in a WL RB-tree.

    :param struct ubi_wl_entry \*e:
        the wear-leveling entry to check

    :param struct rb_root \*root:
        the root of the tree

.. _`in_wl_tree.description`:

Description
-----------

This function returns non-zero if \ ``e``\  is in the \ ``root``\  RB-tree and zero if it
is not.

.. _`prot_queue_add`:

prot_queue_add
==============

.. c:function:: void prot_queue_add(struct ubi_device *ubi, struct ubi_wl_entry *e)

    add physical eraseblock to the protection queue.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the physical eraseblock to add

.. _`prot_queue_add.description`:

Description
-----------

This function adds \ ``e``\  to the tail of the protection queue \ ``ubi``\ ->pq, where
\ ``e``\  will stay for \ ``UBI_PROT_QUEUE_LEN``\  erase operations and will be
temporarily protected from the wear-leveling worker. Note, \ ``wl``\ ->lock has to
be locked.

.. _`find_wl_entry`:

find_wl_entry
=============

.. c:function:: struct ubi_wl_entry *find_wl_entry(struct ubi_device *ubi, struct rb_root *root, int diff)

    find wear-leveling entry closest to certain erase counter.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct rb_root \*root:
        the RB-tree where to look for

    :param int diff:
        maximum possible difference from the smallest erase counter

.. _`find_wl_entry.description`:

Description
-----------

This function looks for a wear leveling entry with erase counter closest to
min + \ ``diff``\ , where min is the smallest erase counter.

.. _`find_mean_wl_entry`:

find_mean_wl_entry
==================

.. c:function:: struct ubi_wl_entry *find_mean_wl_entry(struct ubi_device *ubi, struct rb_root *root)

    find wear-leveling entry with medium erase counter.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct rb_root \*root:
        the RB-tree where to look for

.. _`find_mean_wl_entry.description`:

Description
-----------

This function looks for a wear leveling entry with medium erase counter,
but not greater or equivalent than the lowest erase counter plus
\ ``WL_FREE_MAX_DIFF``\ /2.

.. _`wl_get_wle`:

wl_get_wle
==========

.. c:function:: struct ubi_wl_entry *wl_get_wle(struct ubi_device *ubi)

    get a mean wl entry to be used by \ :c:func:`ubi_wl_get_peb`\  or \ :c:func:`refill_wl_user_pool`\ .

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`wl_get_wle.description`:

Description
-----------

This function returns a a wear leveling entry in case of success and
NULL in case of failure.

.. _`prot_queue_del`:

prot_queue_del
==============

.. c:function:: int prot_queue_del(struct ubi_device *ubi, int pnum)

    remove a physical eraseblock from the protection queue.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int pnum:
        the physical eraseblock to remove

.. _`prot_queue_del.description`:

Description
-----------

This function deletes PEB \ ``pnum``\  from the protection queue and returns zero
in case of success and \ ``-ENODEV``\  if the PEB was not found.

.. _`sync_erase`:

sync_erase
==========

.. c:function:: int sync_erase(struct ubi_device *ubi, struct ubi_wl_entry *e, int torture)

    synchronously erase a physical eraseblock.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the the physical eraseblock to erase

    :param int torture:
        if the physical eraseblock has to be tortured

.. _`sync_erase.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`serve_prot_queue`:

serve_prot_queue
================

.. c:function:: void serve_prot_queue(struct ubi_device *ubi)

    check if it is time to stop protecting PEBs.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`serve_prot_queue.description`:

Description
-----------

This function is called after each erase operation and removes PEBs from the
tail of the protection queue. These PEBs have been protected for long enough
and should be moved to the used tree.

.. _`__schedule_ubi_work`:

__schedule_ubi_work
===================

.. c:function:: void __schedule_ubi_work(struct ubi_device *ubi, struct ubi_work *wrk)

    schedule a work.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_work \*wrk:
        the work to schedule

.. _`__schedule_ubi_work.description`:

Description
-----------

This function adds a work defined by \ ``wrk``\  to the tail of the pending works
list. Can only be used if ubi->work_sem is already held in read mode!

.. _`schedule_ubi_work`:

schedule_ubi_work
=================

.. c:function:: void schedule_ubi_work(struct ubi_device *ubi, struct ubi_work *wrk)

    schedule a work.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_work \*wrk:
        the work to schedule

.. _`schedule_ubi_work.description`:

Description
-----------

This function adds a work defined by \ ``wrk``\  to the tail of the pending works
list.

.. _`schedule_erase`:

schedule_erase
==============

.. c:function:: int schedule_erase(struct ubi_device *ubi, struct ubi_wl_entry *e, int vol_id, int lnum, int torture, bool nested)

    schedule an erase work.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the WL entry of the physical eraseblock to erase

    :param int vol_id:
        the volume ID that last used this PEB

    :param int lnum:
        the last used logical eraseblock number for the PEB

    :param int torture:
        if the physical eraseblock has to be tortured

    :param bool nested:
        *undescribed*

.. _`schedule_erase.description`:

Description
-----------

This function returns zero in case of success and a \ ``-ENOMEM``\  in case of
failure.

.. _`do_sync_erase`:

do_sync_erase
=============

.. c:function:: int do_sync_erase(struct ubi_device *ubi, struct ubi_wl_entry *e, int vol_id, int lnum, int torture)

    run the erase worker synchronously.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the WL entry of the physical eraseblock to erase

    :param int vol_id:
        the volume ID that last used this PEB

    :param int lnum:
        the last used logical eraseblock number for the PEB

    :param int torture:
        if the physical eraseblock has to be tortured

.. _`wear_leveling_worker`:

wear_leveling_worker
====================

.. c:function:: int wear_leveling_worker(struct ubi_device *ubi, struct ubi_work *wrk, int shutdown)

    wear-leveling worker function.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_work \*wrk:
        the work object

    :param int shutdown:
        non-zero if the worker has to free memory and exit
        because the WL-subsystem is shutting down

.. _`wear_leveling_worker.description`:

Description
-----------

This function copies a more worn out physical eraseblock to a less worn out
one. Returns zero in case of success and a negative error code in case of
failure.

.. _`ensure_wear_leveling`:

ensure_wear_leveling
====================

.. c:function:: int ensure_wear_leveling(struct ubi_device *ubi, int nested)

    schedule wear-leveling if it is needed.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int nested:
        set to non-zero if this function is called from UBI worker

.. _`ensure_wear_leveling.description`:

Description
-----------

This function checks if it is time to start wear-leveling and schedules it
if yes. This function returns zero in case of success and a negative error
code in case of failure.

.. _`__erase_worker`:

__erase_worker
==============

.. c:function:: int __erase_worker(struct ubi_device *ubi, struct ubi_work *wl_wrk)

    physical eraseblock erase worker function.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_work \*wl_wrk:
        the work object

.. _`__erase_worker.description`:

Description
-----------

This function erases a physical eraseblock and perform torture testing if
needed. It also takes care about marking the physical eraseblock bad if
needed. Returns zero in case of success and a negative error code in case of
failure.

.. _`ubi_wl_put_peb`:

ubi_wl_put_peb
==============

.. c:function:: int ubi_wl_put_peb(struct ubi_device *ubi, int vol_id, int lnum, int pnum, int torture)

    return a PEB to the wear-leveling sub-system.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        the volume ID that last used this PEB

    :param int lnum:
        the last used logical eraseblock number for the PEB

    :param int pnum:
        physical eraseblock to return

    :param int torture:
        if this physical eraseblock has to be tortured

.. _`ubi_wl_put_peb.description`:

Description
-----------

This function is called to return physical eraseblock \ ``pnum``\  to the pool of
free physical eraseblocks. The \ ``torture``\  flag has to be set if an I/O error
occurred to this \ ``pnum``\  and it has to be tested. This function returns zero
in case of success, and a negative error code in case of failure.

.. _`ubi_wl_scrub_peb`:

ubi_wl_scrub_peb
================

.. c:function:: int ubi_wl_scrub_peb(struct ubi_device *ubi, int pnum)

    schedule a physical eraseblock for scrubbing.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int pnum:
        the physical eraseblock to schedule

.. _`ubi_wl_scrub_peb.description`:

Description
-----------

If a bit-flip in a physical eraseblock is detected, this physical eraseblock
needs scrubbing. This function schedules a physical eraseblock for
scrubbing which is done in background. This function returns zero in case of
success and a negative error code in case of failure.

.. _`ubi_wl_flush`:

ubi_wl_flush
============

.. c:function:: int ubi_wl_flush(struct ubi_device *ubi, int vol_id, int lnum)

    flush all pending works.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        the volume id to flush for

    :param int lnum:
        the logical eraseblock number to flush for

.. _`ubi_wl_flush.description`:

Description
-----------

This function executes all pending works for a particular volume id /
logical eraseblock number pair. If either value is set to \ ``UBI_ALL``\ , then it
acts as a wildcard for all of the corresponding volume numbers or logical
eraseblock numbers. It returns zero in case of success and a negative error
code in case of failure.

.. _`tree_destroy`:

tree_destroy
============

.. c:function:: void tree_destroy(struct ubi_device *ubi, struct rb_root *root)

    destroy an RB-tree.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct rb_root \*root:
        the root of the tree to destroy

.. _`ubi_thread`:

ubi_thread
==========

.. c:function:: int ubi_thread(void *u)

    UBI background thread.

    :param void \*u:
        the UBI device description object pointer

.. _`shutdown_work`:

shutdown_work
=============

.. c:function:: void shutdown_work(struct ubi_device *ubi)

    shutdown all pending works.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`erase_aeb`:

erase_aeb
=========

.. c:function:: int erase_aeb(struct ubi_device *ubi, struct ubi_ainf_peb *aeb, bool sync)

    erase a PEB given in UBI attach info PEB

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_ainf_peb \*aeb:
        UBI attach info PEB

    :param bool sync:
        If true, erase synchronously. Otherwise schedule for erasure

.. _`ubi_wl_init`:

ubi_wl_init
===========

.. c:function:: int ubi_wl_init(struct ubi_device *ubi, struct ubi_attach_info *ai)

    initialize the WL sub-system using attaching information.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

.. _`ubi_wl_init.description`:

Description
-----------

This function returns zero in case of success, and a negative error code in
case of failure.

.. _`protection_queue_destroy`:

protection_queue_destroy
========================

.. c:function:: void protection_queue_destroy(struct ubi_device *ubi)

    destroy the protection queue.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`ubi_wl_close`:

ubi_wl_close
============

.. c:function:: void ubi_wl_close(struct ubi_device *ubi)

    close the wear-leveling sub-system.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`self_check_ec`:

self_check_ec
=============

.. c:function:: int self_check_ec(struct ubi_device *ubi, int pnum, int ec)

    make sure that the erase counter of a PEB is correct.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int pnum:
        the physical eraseblock number to check

    :param int ec:
        the erase counter to check

.. _`self_check_ec.description`:

Description
-----------

This function returns zero if the erase counter of physical eraseblock \ ``pnum``\ 
is equivalent to \ ``ec``\ , and a negative error code if not or if an error
occurred.

.. _`self_check_in_wl_tree`:

self_check_in_wl_tree
=====================

.. c:function:: int self_check_in_wl_tree(const struct ubi_device *ubi, struct ubi_wl_entry *e, struct rb_root *root)

    check that wear-leveling entry is in WL RB-tree.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the wear-leveling entry to check

    :param struct rb_root \*root:
        the root of the tree

.. _`self_check_in_wl_tree.description`:

Description
-----------

This function returns zero if \ ``e``\  is in the \ ``root``\  RB-tree and \ ``-EINVAL``\  if it
is not.

.. _`self_check_in_pq`:

self_check_in_pq
================

.. c:function:: int self_check_in_pq(const struct ubi_device *ubi, struct ubi_wl_entry *e)

    check if wear-leveling entry is in the protection queue.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_wl_entry \*e:
        the wear-leveling entry to check

.. _`self_check_in_pq.description`:

Description
-----------

This function returns zero if \ ``e``\  is in \ ``ubi``\ ->pq and \ ``-EINVAL``\  if it is not.

.. _`produce_free_peb`:

produce_free_peb
================

.. c:function:: int produce_free_peb(struct ubi_device *ubi)

    produce a free physical eraseblock.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`produce_free_peb.description`:

Description
-----------

This function tries to make a free PEB by means of synchronous execution of
pending works. This may be needed if, for example the background thread is
disabled. Returns zero in case of success and a negative error code in case
of failure.

.. _`ubi_wl_get_peb`:

ubi_wl_get_peb
==============

.. c:function:: int ubi_wl_get_peb(struct ubi_device *ubi)

    get a physical eraseblock.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`ubi_wl_get_peb.description`:

Description
-----------

This function returns a physical eraseblock in case of success and a
negative error code in case of failure.
Returns with ubi->fm_eba_sem held in read mode!

.. This file was automatic generated / don't edit.


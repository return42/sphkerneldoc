.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/fastmap-wl.c

.. _`update_fastmap_work_fn`:

update_fastmap_work_fn
======================

.. c:function:: void update_fastmap_work_fn(struct work_struct *wrk)

    calls ubi_update_fastmap from a work queue

    :param wrk:
        the work description object
    :type wrk: struct work_struct \*

.. _`find_anchor_wl_entry`:

find_anchor_wl_entry
====================

.. c:function:: struct ubi_wl_entry *find_anchor_wl_entry(struct rb_root *root)

    find wear-leveling entry to used as anchor PEB.

    :param root:
        the RB-tree where to look for
    :type root: struct rb_root \*

.. _`return_unused_pool_pebs`:

return_unused_pool_pebs
=======================

.. c:function:: void return_unused_pool_pebs(struct ubi_device *ubi, struct ubi_fm_pool *pool)

    returns unused PEB to the free tree.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param pool:
        fastmap pool description object
    :type pool: struct ubi_fm_pool \*

.. _`ubi_wl_get_fm_peb`:

ubi_wl_get_fm_peb
=================

.. c:function:: struct ubi_wl_entry *ubi_wl_get_fm_peb(struct ubi_device *ubi, int anchor)

    find a physical erase block with a given maximal number.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param anchor:
        This PEB will be used as anchor PEB by fastmap
    :type anchor: int

.. _`ubi_wl_get_fm_peb.description`:

Description
-----------

The function returns a physical erase block with a given maximal number
and removes it from the wl subsystem.
Must be called with wl_lock held!

.. _`ubi_refill_pools`:

ubi_refill_pools
================

.. c:function:: void ubi_refill_pools(struct ubi_device *ubi)

    refills all fastmap PEB pools.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`produce_free_peb`:

produce_free_peb
================

.. c:function:: int produce_free_peb(struct ubi_device *ubi)

    produce a free physical eraseblock.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

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

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_wl_get_peb.description`:

Description
-----------

This function returns a physical eraseblock in case of success and a
negative error code in case of failure.
Returns with ubi->fm_eba_sem held in read mode!

.. _`ubi_ensure_anchor_pebs`:

ubi_ensure_anchor_pebs
======================

.. c:function:: int ubi_ensure_anchor_pebs(struct ubi_device *ubi)

    schedule wear-leveling to produce an anchor PEB.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_wl_put_fm_peb`:

ubi_wl_put_fm_peb
=================

.. c:function:: int ubi_wl_put_fm_peb(struct ubi_device *ubi, struct ubi_wl_entry *fm_e, int lnum, int torture)

    returns a PEB used in a fastmap to the wear-leveling sub-system.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param fm_e:
        physical eraseblock to return
    :type fm_e: struct ubi_wl_entry \*

    :param lnum:
        the last used logical eraseblock number for the PEB
    :type lnum: int

    :param torture:
        if this physical eraseblock has to be tortured
    :type torture: int

.. _`ubi_wl_put_fm_peb.see`:

see
---

\ :c:func:`ubi_wl_put_peb`\ 

.. _`ubi_is_erase_work`:

ubi_is_erase_work
=================

.. c:function:: int ubi_is_erase_work(struct ubi_work *wrk)

    checks whether a work is erase work.

    :param wrk:
        The work object to be checked
    :type wrk: struct ubi_work \*

.. _`may_reserve_for_fm`:

may_reserve_for_fm
==================

.. c:function:: struct ubi_wl_entry *may_reserve_for_fm(struct ubi_device *ubi, struct ubi_wl_entry *e, struct rb_root *root)

    tests whether a PEB shall be reserved for fastmap. See \ :c:func:`find_mean_wl_entry`\ 

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param e:
        physical eraseblock to return
    :type e: struct ubi_wl_entry \*

    :param root:
        RB tree to test against.
    :type root: struct rb_root \*

.. This file was automatic generated / don't edit.


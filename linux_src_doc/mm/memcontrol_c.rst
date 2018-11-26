.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memcontrol.c

.. _`mem_cgroup_css_from_page`:

mem_cgroup_css_from_page
========================

.. c:function:: struct cgroup_subsys_state *mem_cgroup_css_from_page(struct page *page)

    css of the memcg associated with a page

    :param page:
        page of interest
    :type page: struct page \*

.. _`mem_cgroup_css_from_page.description`:

Description
-----------

If memcg is bound to the default hierarchy, css of the memcg associated
with \ ``page``\  is returned.  The returned css remains associated with \ ``page``\ 
until it is released.

If memcg is bound to a traditional hierarchy, the css of root_mem_cgroup
is returned.

.. _`page_cgroup_ino`:

page_cgroup_ino
===============

.. c:function:: ino_t page_cgroup_ino(struct page *page)

    return inode number of the memcg a page is charged to

    :param page:
        the page
    :type page: struct page \*

.. _`page_cgroup_ino.description`:

Description
-----------

Look up the closest online ancestor of the memory cgroup \ ``page``\  is charged to
and return its inode number or 0 if \ ``page``\  is not charged to any cgroup. It
is safe to call this function without holding a reference to \ ``page``\ .

Note, this function is inherently racy, because there is nothing to prevent
the cgroup inode from getting torn down and potentially reallocated a moment
after \ :c:func:`page_cgroup_ino`\  returns, so it only should be used by callers that
do not care (such as procfs interfaces).

.. _`get_mem_cgroup_from_mm`:

get_mem_cgroup_from_mm
======================

.. c:function:: struct mem_cgroup *get_mem_cgroup_from_mm(struct mm_struct *mm)

    Obtain a reference on given mm_struct's memcg.

    :param mm:
        mm from which memcg should be extracted. It can be NULL.
    :type mm: struct mm_struct \*

.. _`get_mem_cgroup_from_mm.description`:

Description
-----------

Obtain a reference on mm->memcg and returns it if successful. Otherwise
root_mem_cgroup is returned. However if mem_cgroup is disabled, NULL is
returned.

.. _`get_mem_cgroup_from_page`:

get_mem_cgroup_from_page
========================

.. c:function:: struct mem_cgroup *get_mem_cgroup_from_page(struct page *page)

    Obtain a reference on given page's memcg.

    :param page:
        page from which memcg should be extracted.
    :type page: struct page \*

.. _`get_mem_cgroup_from_page.description`:

Description
-----------

Obtain a reference on page->memcg and returns it if successful. Otherwise
root_mem_cgroup is returned.

.. _`get_mem_cgroup_from_current`:

get_mem_cgroup_from_current
===========================

.. c:function:: struct mem_cgroup *get_mem_cgroup_from_current( void)

    >active_memcg is non-NULL, do not fallback to current->mm->memcg.

    :param void:
        no arguments
    :type void: 

.. _`mem_cgroup_iter`:

mem_cgroup_iter
===============

.. c:function:: struct mem_cgroup *mem_cgroup_iter(struct mem_cgroup *root, struct mem_cgroup *prev, struct mem_cgroup_reclaim_cookie *reclaim)

    iterate over memory cgroup hierarchy

    :param root:
        hierarchy root
    :type root: struct mem_cgroup \*

    :param prev:
        previously returned memcg, NULL on first invocation
    :type prev: struct mem_cgroup \*

    :param reclaim:
        cookie for shared reclaim walks, NULL for full walks
    :type reclaim: struct mem_cgroup_reclaim_cookie \*

.. _`mem_cgroup_iter.description`:

Description
-----------

Returns references to children of the hierarchy below \ ``root``\ , or
\ ``root``\  itself, or \ ``NULL``\  after a full round-trip.

Caller must pass the return value in \ ``prev``\  on subsequent
invocations for reference counting, or use \ :c:func:`mem_cgroup_iter_break`\ 
to cancel a hierarchy walk before the round-trip is complete.

Reclaimers can specify a node and a priority level in \ ``reclaim``\  to
divide up the memcgs in the hierarchy among all concurrent
reclaimers operating on the same node and priority.

.. _`mem_cgroup_iter_break`:

mem_cgroup_iter_break
=====================

.. c:function:: void mem_cgroup_iter_break(struct mem_cgroup *root, struct mem_cgroup *prev)

    abort a hierarchy walk prematurely

    :param root:
        hierarchy root
    :type root: struct mem_cgroup \*

    :param prev:
        last visited hierarchy member as returned by \ :c:func:`mem_cgroup_iter`\ 
    :type prev: struct mem_cgroup \*

.. _`mem_cgroup_scan_tasks`:

mem_cgroup_scan_tasks
=====================

.. c:function:: int mem_cgroup_scan_tasks(struct mem_cgroup *memcg, int (*fn)(struct task_struct *, void *), void *arg)

    iterate over tasks of a memory cgroup hierarchy

    :param memcg:
        hierarchy root
    :type memcg: struct mem_cgroup \*

    :param int (\*fn)(struct task_struct \*, void \*):
        function to call for each task

    :param arg:
        argument passed to \ ``fn``\ 
    :type arg: void \*

.. _`mem_cgroup_scan_tasks.description`:

Description
-----------

This function iterates over tasks attached to \ ``memcg``\  or to any of its
descendants and calls \ ``fn``\  for each task. If \ ``fn``\  returns a non-zero
value, the function breaks the iteration loop and returns the value.
Otherwise, it will iterate over all tasks and return 0.

This function must not be called for the root memory cgroup.

.. _`mem_cgroup_page_lruvec`:

mem_cgroup_page_lruvec
======================

.. c:function:: struct lruvec *mem_cgroup_page_lruvec(struct page *page, struct pglist_data *pgdat)

    return lruvec for isolating/putting an LRU page

    :param page:
        the page
    :type page: struct page \*

    :param pgdat:
        pgdat of the page
    :type pgdat: struct pglist_data \*

.. _`mem_cgroup_page_lruvec.description`:

Description
-----------

This function is only safe when following the LRU page isolation

.. _`mem_cgroup_page_lruvec.and-putback-protocol`:

and putback protocol
--------------------

the LRU lock must be held, and the page must
either be \ :c:func:`PageLRU`\  or the caller must have isolated/allocated it.

.. _`mem_cgroup_update_lru_size`:

mem_cgroup_update_lru_size
==========================

.. c:function:: void mem_cgroup_update_lru_size(struct lruvec *lruvec, enum lru_list lru, int zid, int nr_pages)

    account for adding or removing an lru page

    :param lruvec:
        mem_cgroup per zone lru vector
    :type lruvec: struct lruvec \*

    :param lru:
        index of lru list the page is sitting on
    :type lru: enum lru_list

    :param zid:
        zone id of the accounted pages
    :type zid: int

    :param nr_pages:
        positive when adding or negative when removing
    :type nr_pages: int

.. _`mem_cgroup_update_lru_size.description`:

Description
-----------

This function must be called under lru_lock, just before a page is added
to or just after a page is removed from an lru list (that ordering being
so as to allow it to check that lru_size 0 is consistent with list_empty).

.. _`mem_cgroup_margin`:

mem_cgroup_margin
=================

.. c:function:: unsigned long mem_cgroup_margin(struct mem_cgroup *memcg)

    calculate chargeable space of a memory cgroup

    :param memcg:
        the memory cgroup
    :type memcg: struct mem_cgroup \*

.. _`mem_cgroup_margin.description`:

Description
-----------

Returns the maximum amount of memory \ ``mem``\  can be charged with, in
pages.

.. _`mem_cgroup_print_oom_info`:

mem_cgroup_print_oom_info
=========================

.. c:function:: void mem_cgroup_print_oom_info(struct mem_cgroup *memcg, struct task_struct *p)

    Print OOM information relevant to memory controller.

    :param memcg:
        The memory cgroup that went over limit
    :type memcg: struct mem_cgroup \*

    :param p:
        Task that is going to be killed
    :type p: struct task_struct \*

.. _`mem_cgroup_print_oom_info.note`:

NOTE
----

\ ``memcg``\  and \ ``p``\ 's mem_cgroup can be different when hierarchy is
enabled

.. _`test_mem_cgroup_node_reclaimable`:

test_mem_cgroup_node_reclaimable
================================

.. c:function:: bool test_mem_cgroup_node_reclaimable(struct mem_cgroup *memcg, int nid, bool noswap)

    :param memcg:
        the target memcg
    :type memcg: struct mem_cgroup \*

    :param nid:
        the node ID to be checked.
    :type nid: int

    :param noswap:
        specify true here if the user wants flle only information.
    :type noswap: bool

.. _`test_mem_cgroup_node_reclaimable.description`:

Description
-----------

This function returns whether the specified memcg contains any
reclaimable pages on a node. Returns true if there are any reclaimable
pages in the node.

.. _`mem_cgroup_oom_synchronize`:

mem_cgroup_oom_synchronize
==========================

.. c:function:: bool mem_cgroup_oom_synchronize(bool handle)

    complete memcg OOM handling

    :param handle:
        actually kill/wait or just clean up the OOM state
    :type handle: bool

.. _`mem_cgroup_oom_synchronize.description`:

Description
-----------

This has to be called at the end of a page fault if the memcg OOM
handler was enabled.

Memcg supports userspace OOM handling where failed allocations must
sleep on a waitqueue until the userspace task resolves the
situation.  Sleeping directly in the charge context with all kinds
of locks held is not a good idea, instead we remember an OOM state
in the task and \ :c:func:`mem_cgroup_oom_synchronize`\  has to be called at
the end of the page fault to complete the OOM handling.

Returns \ ``true``\  if an ongoing memcg OOM situation was detected and
completed, \ ``false``\  otherwise.

.. _`mem_cgroup_get_oom_group`:

mem_cgroup_get_oom_group
========================

.. c:function:: struct mem_cgroup *mem_cgroup_get_oom_group(struct task_struct *victim, struct mem_cgroup *oom_domain)

    get a memory cgroup to clean up after OOM

    :param victim:
        task to be killed by the OOM killer
    :type victim: struct task_struct \*

    :param oom_domain:
        memcg in case of memcg OOM, NULL in case of system-wide OOM
    :type oom_domain: struct mem_cgroup \*

.. _`mem_cgroup_get_oom_group.description`:

Description
-----------

Returns a pointer to a memory cgroup, which has to be cleaned up
by killing all belonging OOM-killable tasks.

Caller has to call \ :c:func:`mem_cgroup_put`\  on the returned non-NULL memcg.

.. _`lock_page_memcg`:

lock_page_memcg
===============

.. c:function:: struct mem_cgroup *lock_page_memcg(struct page *page)

    lock a page->mem_cgroup binding

    :param page:
        the page
    :type page: struct page \*

.. _`lock_page_memcg.description`:

Description
-----------

This function protects unlocked LRU pages from being moved to
another cgroup.

It ensures lifetime of the returned memcg. Caller is responsible
for the lifetime of the page; \__unlock_page_memcg() is available
when \ ``page``\  might get freed inside the locked section.

.. _`__unlock_page_memcg`:

\__unlock_page_memcg
====================

.. c:function:: void __unlock_page_memcg(struct mem_cgroup *memcg)

    unlock and unpin a memcg

    :param memcg:
        the memcg
    :type memcg: struct mem_cgroup \*

.. _`__unlock_page_memcg.description`:

Description
-----------

Unlock and unpin a memcg returned by \ :c:func:`lock_page_memcg`\ .

.. _`unlock_page_memcg`:

unlock_page_memcg
=================

.. c:function:: void unlock_page_memcg(struct page *page)

    unlock a page->mem_cgroup binding

    :param page:
        the page
    :type page: struct page \*

.. _`consume_stock`:

consume_stock
=============

.. c:function:: bool consume_stock(struct mem_cgroup *memcg, unsigned int nr_pages)

    Try to consume stocked charge on this cpu.

    :param memcg:
        memcg to consume from.
    :type memcg: struct mem_cgroup \*

    :param nr_pages:
        how many pages to charge.
    :type nr_pages: unsigned int

.. _`consume_stock.description`:

Description
-----------

The charges will only happen if \ ``memcg``\  matches the current cpu's memcg
stock, and at least \ ``nr_pages``\  are available in that stock.  Failure to
service an allocation will refill the stock.

returns true if successful, false otherwise.

.. _`memcg_kmem_get_cache`:

memcg_kmem_get_cache
====================

.. c:function:: struct kmem_cache *memcg_kmem_get_cache(struct kmem_cache *cachep)

    select the correct per-memcg cache for allocation

    :param cachep:
        the original global kmem cache
    :type cachep: struct kmem_cache \*

.. _`memcg_kmem_get_cache.description`:

Description
-----------

Return the kmem_cache we're supposed to use for a slab allocation.
We try to use the current memcg's version of the cache.

If the cache does not exist yet, if we are the first user of it, we
create it asynchronously in a workqueue and let the current allocation
go through with the original cache.

This function takes a reference to the cache it returns to assure it
won't get destroyed while we are working with it. Once the caller is
done with it, \ :c:func:`memcg_kmem_put_cache`\  must be called to release the
reference.

.. _`memcg_kmem_put_cache`:

memcg_kmem_put_cache
====================

.. c:function:: void memcg_kmem_put_cache(struct kmem_cache *cachep)

    drop reference taken by memcg_kmem_get_cache

    :param cachep:
        the cache returned by memcg_kmem_get_cache
    :type cachep: struct kmem_cache \*

.. _`memcg_kmem_charge_memcg`:

memcg_kmem_charge_memcg
=======================

.. c:function:: int memcg_kmem_charge_memcg(struct page *page, gfp_t gfp, int order, struct mem_cgroup *memcg)

    charge a kmem page

    :param page:
        page to charge
    :type page: struct page \*

    :param gfp:
        reclaim mode
    :type gfp: gfp_t

    :param order:
        allocation order
    :type order: int

    :param memcg:
        memory cgroup to charge
    :type memcg: struct mem_cgroup \*

.. _`memcg_kmem_charge_memcg.description`:

Description
-----------

Returns 0 on success, an error code on failure.

.. _`memcg_kmem_charge`:

memcg_kmem_charge
=================

.. c:function:: int memcg_kmem_charge(struct page *page, gfp_t gfp, int order)

    charge a kmem page to the current memory cgroup

    :param page:
        page to charge
    :type page: struct page \*

    :param gfp:
        reclaim mode
    :type gfp: gfp_t

    :param order:
        allocation order
    :type order: int

.. _`memcg_kmem_charge.description`:

Description
-----------

Returns 0 on success, an error code on failure.

.. _`memcg_kmem_uncharge`:

memcg_kmem_uncharge
===================

.. c:function:: void memcg_kmem_uncharge(struct page *page, int order)

    uncharge a kmem page

    :param page:
        page to uncharge
    :type page: struct page \*

    :param order:
        allocation order
    :type order: int

.. _`mem_cgroup_move_swap_account`:

mem_cgroup_move_swap_account
============================

.. c:function:: int mem_cgroup_move_swap_account(swp_entry_t entry, struct mem_cgroup *from, struct mem_cgroup *to)

    move swap charge and swap_cgroup's record.

    :param entry:
        swap entry to be moved
    :type entry: swp_entry_t

    :param from:
        mem_cgroup which the entry is moved from
    :type from: struct mem_cgroup \*

    :param to:
        mem_cgroup which the entry is moved to
    :type to: struct mem_cgroup \*

.. _`mem_cgroup_move_swap_account.description`:

Description
-----------

It succeeds only when the swap_cgroup's record for this entry is the same
as the mem_cgroup's id of \ ``from``\ .

Returns 0 on success, -EINVAL on failure.

The caller must have charged to \ ``to``\ , IOW, called \ :c:func:`page_counter_charge`\  about
both res and memsw, and called \ :c:func:`css_get`\ .

.. _`mem_cgroup_wb_stats`:

mem_cgroup_wb_stats
===================

.. c:function:: void mem_cgroup_wb_stats(struct bdi_writeback *wb, unsigned long *pfilepages, unsigned long *pheadroom, unsigned long *pdirty, unsigned long *pwriteback)

    retrieve writeback related stats from its memcg

    :param wb:
        bdi_writeback in question
    :type wb: struct bdi_writeback \*

    :param pfilepages:
        out parameter for number of file pages
    :type pfilepages: unsigned long \*

    :param pheadroom:
        out parameter for number of allocatable pages according to memcg
    :type pheadroom: unsigned long \*

    :param pdirty:
        out parameter for number of dirty pages
    :type pdirty: unsigned long \*

    :param pwriteback:
        out parameter for number of pages under writeback
    :type pwriteback: unsigned long \*

.. _`mem_cgroup_wb_stats.description`:

Description
-----------

Determine the numbers of file, headroom, dirty, and writeback pages in
\ ``wb``\ 's memcg.  File, dirty and writeback are self-explanatory.  Headroom
is a bit more involved.

A memcg's headroom is "min(max, high) - used".  In the hierarchy, the
headroom is calculated as the lowest headroom of itself and the
ancestors.  Note that this doesn't consider the actual amount of
available memory in the system.  The caller should further cap
\*@pheadroom accordingly.

.. _`mem_cgroup_from_id`:

mem_cgroup_from_id
==================

.. c:function:: struct mem_cgroup *mem_cgroup_from_id(unsigned short id)

    look up a memcg from a memcg id

    :param id:
        the memcg id to look up
    :type id: unsigned short

.. _`mem_cgroup_from_id.description`:

Description
-----------

Caller must hold \ :c:func:`rcu_read_lock`\ .

.. _`mem_cgroup_css_reset`:

mem_cgroup_css_reset
====================

.. c:function:: void mem_cgroup_css_reset(struct cgroup_subsys_state *css)

    reset the states of a mem_cgroup

    :param css:
        the target css
    :type css: struct cgroup_subsys_state \*

.. _`mem_cgroup_css_reset.description`:

Description
-----------

Reset the states of the mem_cgroup associated with \ ``css``\ .  This is
invoked when the userland requests disabling on the default hierarchy
but the memcg is pinned through dependency.  The memcg should stop
applying policies and should revert to the vanilla state as it may be
made visible again.

The current implementation only resets the essential configurations.
This needs to be expanded to cover all the visible parts.

.. _`mem_cgroup_move_account`:

mem_cgroup_move_account
=======================

.. c:function:: int mem_cgroup_move_account(struct page *page, bool compound, struct mem_cgroup *from, struct mem_cgroup *to)

    move account of the page

    :param page:
        the page
    :type page: struct page \*

    :param compound:
        charge the page as compound or small page
    :type compound: bool

    :param from:
        mem_cgroup which the page is moved from.
    :type from: struct mem_cgroup \*

    :param to:
        mem_cgroup which the page is moved to. \ ``from``\  != \ ``to``\ .
    :type to: struct mem_cgroup \*

.. _`mem_cgroup_move_account.description`:

Description
-----------

The caller must make sure the page is not on LRU (isolate_page() is useful.)

This function doesn't do "charge" to new cgroup and doesn't do "uncharge"
from old cgroup.

.. _`get_mctgt_type`:

get_mctgt_type
==============

.. c:function:: enum mc_target_type get_mctgt_type(struct vm_area_struct *vma, unsigned long addr, pte_t ptent, union mc_target *target)

    get target type of moving charge

    :param vma:
        the vma the pte to be checked belongs
    :type vma: struct vm_area_struct \*

    :param addr:
        the address corresponding to the pte to be checked
    :type addr: unsigned long

    :param ptent:
        the pte to be checked
    :type ptent: pte_t

    :param target:
        the pointer the target page or swap ent will be stored(can be NULL)
    :type target: union mc_target \*

.. _`get_mctgt_type.description`:

Description
-----------

Returns
0(MC_TARGET_NONE): if the pte is not a target for move charge.
1(MC_TARGET_PAGE): if the page corresponding to this pte is a target for
move charge. if \ ``target``\  is not NULL, the page is stored in target->page
with extra refcnt got(Callers should handle it).
2(MC_TARGET_SWAP): if the swap entry corresponding to this pte is a
target for charge migration. if \ ``target``\  is not NULL, the entry is stored
in target->ent.
3(MC_TARGET_DEVICE): like MC_TARGET_PAGE  but page is MEMORY_DEVICE_PUBLIC
or MEMORY_DEVICE_PRIVATE (so ZONE_DEVICE page and thus not on the lru).
For now we such page is charge like a regular page would be as for all
intent and purposes it is just special memory taking the place of a
regular page.

See Documentations/vm/hmm.txt and include/linux/hmm.h

Called with pte lock held.

.. _`mem_cgroup_protected`:

mem_cgroup_protected
====================

.. c:function:: enum mem_cgroup_protection mem_cgroup_protected(struct mem_cgroup *root, struct mem_cgroup *memcg)

    check if memory consumption is in the normal range

    :param root:
        the top ancestor of the sub-tree being checked
    :type root: struct mem_cgroup \*

    :param memcg:
        the memory cgroup to check
    :type memcg: struct mem_cgroup \*

.. _`mem_cgroup_protected.warning`:

WARNING
-------

This function is not stateless! It can only be used as part
of a top-down tree iteration, not for isolated queries.

.. _`mem_cgroup_protected.memcg_prot_none`:

MEMCG_PROT_NONE
---------------

cgroup memory is not protected

.. _`mem_cgroup_protected.memcg_prot_low`:

MEMCG_PROT_LOW
--------------

cgroup memory is protected as long there is
an unprotected supply of reclaimable memory from other cgroups.

.. _`mem_cgroup_protected.memcg_prot_min`:

MEMCG_PROT_MIN
--------------

cgroup memory is protected

\ ``root``\  is exclusive; it is never protected when looked at directly

To provide a proper hierarchical behavior, effective memory.min/low values
are used. Below is the description of how effective memory.low is calculated.
Effective memory.min values is calculated in the same way.

Effective memory.low is always equal or less than the original memory.low.
If there is no memory.low overcommittment (which is always true for
top-level memory cgroups), these two values are equal.
Otherwise, it's a part of parent's effective memory.low,
calculated as a cgroup's memory.low usage divided by sum of sibling's
memory.low usages, where memory.low usage is the size of actually
protected memory.

low_usage
elow = min( memory.low, parent->elow \* ------------------ ),
siblings_low_usage

\| memory.current, if memory.current < memory.low
low_usage = \|


Such definition of the effective memory.low provides the expected

.. _`mem_cgroup_protected.hierarchical-behavior`:

hierarchical behavior
---------------------

parent's memory.low value is limiting
children, unprotected memory is reclaimed first and cgroups,
which are not using their guarantee do not affect actual memory
distribution.

For example, if there are memcgs A, A/B, A/C, A/D and A/E:

A      A/memory.low = 2G, A/memory.current = 6G
//\\
BC  DE   B/memory.low = 3G  B/memory.current = 2G
C/memory.low = 1G  C/memory.current = 2G
D/memory.low = 0   D/memory.current = 2G
E/memory.low = 10G E/memory.current = 0

and the memory pressure is applied, the following memory distribution
is expected (approximately):

A/memory.current = 2G

B/memory.current = 1.3G
C/memory.current = 0.6G
D/memory.current = 0
E/memory.current = 0

These calculations require constant tracking of the actual low usages
(see \ :c:func:`propagate_protected_usage`\ ), as well as recursive calculation of
effective memory.low values. But as we do call \ :c:func:`mem_cgroup_protected`\ 
path for each memory cgroup top-down from the reclaim,
it's possible to optimize this part, and save calculated elow
for next usage. This part is intentionally racy, but it's ok,
as memory.low is a best-effort mechanism.

.. _`mem_cgroup_try_charge`:

mem_cgroup_try_charge
=====================

.. c:function:: int mem_cgroup_try_charge(struct page *page, struct mm_struct *mm, gfp_t gfp_mask, struct mem_cgroup **memcgp, bool compound)

    try charging a page

    :param page:
        page to charge
    :type page: struct page \*

    :param mm:
        mm context of the victim
    :type mm: struct mm_struct \*

    :param gfp_mask:
        reclaim mode
    :type gfp_mask: gfp_t

    :param memcgp:
        charged memcg return
    :type memcgp: struct mem_cgroup \*\*

    :param compound:
        charge the page as compound or small page
    :type compound: bool

.. _`mem_cgroup_try_charge.description`:

Description
-----------

Try to charge \ ``page``\  to the memcg that \ ``mm``\  belongs to, reclaiming
pages according to \ ``gfp_mask``\  if necessary.

Returns 0 on success, with \*@memcgp pointing to the charged memcg.
Otherwise, an error code is returned.

After page->mapping has been set up, the caller must finalize the
charge with \ :c:func:`mem_cgroup_commit_charge`\ .  Or abort the transaction
with \ :c:func:`mem_cgroup_cancel_charge`\  in case page instantiation fails.

.. _`mem_cgroup_commit_charge`:

mem_cgroup_commit_charge
========================

.. c:function:: void mem_cgroup_commit_charge(struct page *page, struct mem_cgroup *memcg, bool lrucare, bool compound)

    commit a page charge

    :param page:
        page to charge
    :type page: struct page \*

    :param memcg:
        memcg to charge the page to
    :type memcg: struct mem_cgroup \*

    :param lrucare:
        page might be on LRU already
    :type lrucare: bool

    :param compound:
        charge the page as compound or small page
    :type compound: bool

.. _`mem_cgroup_commit_charge.description`:

Description
-----------

Finalize a charge transaction started by \ :c:func:`mem_cgroup_try_charge`\ ,
after page->mapping has been set up.  This must happen atomically
as part of the page instantiation, i.e. under the page table lock
for anonymous pages, under the page lock for page and swap cache.

In addition, the page must not be on the LRU during the commit, to
prevent racing with task migration.  If it might be, use \ ``lrucare``\ .

Use \ :c:func:`mem_cgroup_cancel_charge`\  to cancel the transaction instead.

.. _`mem_cgroup_cancel_charge`:

mem_cgroup_cancel_charge
========================

.. c:function:: void mem_cgroup_cancel_charge(struct page *page, struct mem_cgroup *memcg, bool compound)

    cancel a page charge

    :param page:
        page to charge
    :type page: struct page \*

    :param memcg:
        memcg to charge the page to
    :type memcg: struct mem_cgroup \*

    :param compound:
        charge the page as compound or small page
    :type compound: bool

.. _`mem_cgroup_cancel_charge.description`:

Description
-----------

Cancel a charge transaction started by \ :c:func:`mem_cgroup_try_charge`\ .

.. _`mem_cgroup_uncharge`:

mem_cgroup_uncharge
===================

.. c:function:: void mem_cgroup_uncharge(struct page *page)

    uncharge a page

    :param page:
        page to uncharge
    :type page: struct page \*

.. _`mem_cgroup_uncharge.description`:

Description
-----------

Uncharge a page previously charged with \ :c:func:`mem_cgroup_try_charge`\  and
\ :c:func:`mem_cgroup_commit_charge`\ .

.. _`mem_cgroup_uncharge_list`:

mem_cgroup_uncharge_list
========================

.. c:function:: void mem_cgroup_uncharge_list(struct list_head *page_list)

    uncharge a list of page

    :param page_list:
        list of pages to uncharge
    :type page_list: struct list_head \*

.. _`mem_cgroup_uncharge_list.description`:

Description
-----------

Uncharge a list of pages previously charged with
\ :c:func:`mem_cgroup_try_charge`\  and \ :c:func:`mem_cgroup_commit_charge`\ .

.. _`mem_cgroup_migrate`:

mem_cgroup_migrate
==================

.. c:function:: void mem_cgroup_migrate(struct page *oldpage, struct page *newpage)

    charge a page's replacement

    :param oldpage:
        currently circulating page
    :type oldpage: struct page \*

    :param newpage:
        replacement page
    :type newpage: struct page \*

.. _`mem_cgroup_migrate.description`:

Description
-----------

Charge \ ``newpage``\  as a replacement page for \ ``oldpage``\ . \ ``oldpage``\  will
be uncharged upon free.

Both pages must be locked, \ ``newpage->mapping``\  must be set up.

.. _`mem_cgroup_charge_skmem`:

mem_cgroup_charge_skmem
=======================

.. c:function:: bool mem_cgroup_charge_skmem(struct mem_cgroup *memcg, unsigned int nr_pages)

    charge socket memory

    :param memcg:
        memcg to charge
    :type memcg: struct mem_cgroup \*

    :param nr_pages:
        number of pages to charge
    :type nr_pages: unsigned int

.. _`mem_cgroup_charge_skmem.description`:

Description
-----------

Charges \ ``nr_pages``\  to \ ``memcg``\ . Returns \ ``true``\  if the charge fit within
\ ``memcg``\ 's configured limit, \ ``false``\  if the charge had to be forced.

.. _`mem_cgroup_uncharge_skmem`:

mem_cgroup_uncharge_skmem
=========================

.. c:function:: void mem_cgroup_uncharge_skmem(struct mem_cgroup *memcg, unsigned int nr_pages)

    uncharge socket memory

    :param memcg:
        memcg to uncharge
    :type memcg: struct mem_cgroup \*

    :param nr_pages:
        number of pages to uncharge
    :type nr_pages: unsigned int

.. _`mem_cgroup_swapout`:

mem_cgroup_swapout
==================

.. c:function:: void mem_cgroup_swapout(struct page *page, swp_entry_t entry)

    transfer a memsw charge to swap

    :param page:
        page whose memsw charge to transfer
    :type page: struct page \*

    :param entry:
        swap entry to move the charge to
    :type entry: swp_entry_t

.. _`mem_cgroup_swapout.description`:

Description
-----------

Transfer the memsw charge of \ ``page``\  to \ ``entry``\ .

.. _`mem_cgroup_try_charge_swap`:

mem_cgroup_try_charge_swap
==========================

.. c:function:: int mem_cgroup_try_charge_swap(struct page *page, swp_entry_t entry)

    try charging swap space for a page

    :param page:
        page being added to swap
    :type page: struct page \*

    :param entry:
        swap entry to charge
    :type entry: swp_entry_t

.. _`mem_cgroup_try_charge_swap.description`:

Description
-----------

Try to charge \ ``page``\ 's memcg for the swap space at \ ``entry``\ .

Returns 0 on success, -ENOMEM on failure.

.. _`mem_cgroup_uncharge_swap`:

mem_cgroup_uncharge_swap
========================

.. c:function:: void mem_cgroup_uncharge_swap(swp_entry_t entry, unsigned int nr_pages)

    uncharge swap space

    :param entry:
        swap entry to uncharge
    :type entry: swp_entry_t

    :param nr_pages:
        the amount of swap space to uncharge
    :type nr_pages: unsigned int

.. This file was automatic generated / don't edit.


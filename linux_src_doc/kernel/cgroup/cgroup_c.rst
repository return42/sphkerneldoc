.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/cgroup.c

.. _`cgroup_ssid_enabled`:

cgroup_ssid_enabled
===================

.. c:function:: bool cgroup_ssid_enabled(int ssid)

    cgroup subsys enabled test by subsys ID

    :param int ssid:
        subsys ID of interest

.. _`cgroup_ssid_enabled.description`:

Description
-----------

\ :c:func:`cgroup_subsys_enabled`\  can only be used with literal subsys names which
is fine for individual subsystems but unsuitable for cgroup core.  This
is slower \ :c:func:`static_key_enabled`\  based test indexed by \ ``ssid``\ .

.. _`cgroup_on_dfl`:

cgroup_on_dfl
=============

.. c:function:: bool cgroup_on_dfl(const struct cgroup *cgrp)

    test whether a cgroup is on the default hierarchy

    :param const struct cgroup \*cgrp:
        the cgroup of interest

.. _`cgroup_on_dfl.description`:

Description
-----------

The default hierarchy is the v2 interface of cgroup and this function
can be used to test whether a cgroup is on the default hierarchy for
cases where a subsystem should behave differnetly depending on the
interface version.

The set of behaviors which change on the default hierarchy are still
being determined and the mount option is prefixed with \__DEVEL__.

.. _`cgroup_on_dfl.list-of-changed-behaviors`:

List of changed behaviors
-------------------------


- Mount options "noprefix", "xattr", "clone_children", "release_agent"
and "name" are disallowed.

- When mounting an existing superblock, mount options should match.

- Remount is disallowed.

- rename(2) is disallowed.

- "tasks" is removed.  Everything should be at process granularity.  Use
"cgroup.procs" instead.

- "cgroup.procs" is not sorted.  pids will be unique unless they got
recycled inbetween reads.

- "release_agent" and "notify_on_release" are removed.  Replacement
notification mechanism will be implemented.

- "cgroup.clone_children" is removed.

- "cgroup.subtree_populated" is available.  Its value is 0 if the cgroup
and its descendants contain no task; otherwise, 1.  The file also
generates kernfs notification which can be monitored through poll and
[di]notify when the value of the file changes.

- cpuset: tasks will be kept in empty cpusets when hotplug happens and
take masks of ancestors with non-empty cpus/mems, instead of being
moved to an ancestor.

- cpuset: a task can be moved into an empty cpuset, and again it takes
masks of ancestors.

- memcg: use_hierarchy is on by default and the cgroup file for the flag
is not created.

- blkcg: blk-throttle becomes properly hierarchical.

- debug: disallowed on the default hierarchy.

.. _`cgroup_css`:

cgroup_css
==========

.. c:function:: struct cgroup_subsys_state *cgroup_css(struct cgroup *cgrp, struct cgroup_subsys *ss)

    obtain a cgroup's css for the specified subsystem

    :param struct cgroup \*cgrp:
        the cgroup of interest

    :param struct cgroup_subsys \*ss:
        the subsystem of interest (%NULL returns \ ``cgrp``\ ->self)

.. _`cgroup_css.description`:

Description
-----------

Return \ ``cgrp``\ 's css (cgroup_subsys_state) associated with \ ``ss``\ .  This
function must be called either under cgroup_mutex or \ :c:func:`rcu_read_lock`\  and
the caller is responsible for pinning the returned css if it wants to
keep accessing it outside the said locks.  This function may return
\ ``NULL``\  if \ ``cgrp``\  doesn't have \ ``subsys_id``\  enabled.

.. _`cgroup_tryget_css`:

cgroup_tryget_css
=================

.. c:function:: struct cgroup_subsys_state *cgroup_tryget_css(struct cgroup *cgrp, struct cgroup_subsys *ss)

    try to get a cgroup's css for the specified subsystem

    :param struct cgroup \*cgrp:
        the cgroup of interest

    :param struct cgroup_subsys \*ss:
        the subsystem of interest

.. _`cgroup_tryget_css.description`:

Description
-----------

Find and get \ ``cgrp``\ 's css assocaited with \ ``ss``\ .  If the css doesn't exist
or is offline, \ ``NULL``\  is returned.

.. _`cgroup_e_css`:

cgroup_e_css
============

.. c:function:: struct cgroup_subsys_state *cgroup_e_css(struct cgroup *cgrp, struct cgroup_subsys *ss)

    obtain a cgroup's effective css for the specified subsystem

    :param struct cgroup \*cgrp:
        the cgroup of interest

    :param struct cgroup_subsys \*ss:
        the subsystem of interest (%NULL returns \ ``cgrp``\ ->self)

.. _`cgroup_e_css.description`:

Description
-----------

Similar to \ :c:func:`cgroup_css`\  but returns the effective css, which is defined
as the matching css of the nearest ancestor including self which has \ ``ss``\ 
enabled.  If \ ``ss``\  is associated with the hierarchy \ ``cgrp``\  is on, this
function is guaranteed to return non-NULL css.

.. _`cgroup_get_e_css`:

cgroup_get_e_css
================

.. c:function:: struct cgroup_subsys_state *cgroup_get_e_css(struct cgroup *cgrp, struct cgroup_subsys *ss)

    get a cgroup's effective css for the specified subsystem

    :param struct cgroup \*cgrp:
        the cgroup of interest

    :param struct cgroup_subsys \*ss:
        the subsystem of interest

.. _`cgroup_get_e_css.description`:

Description
-----------

Find and get the effective css of \ ``cgrp``\  for \ ``ss``\ .  The effective css is
defined as the matching css of the nearest ancestor including self which
has \ ``ss``\  enabled.  If \ ``ss``\  is not mounted on the hierarchy \ ``cgrp``\  is on,
the root css is returned, so this function always returns a valid css.
The returned css must be put using \ :c:func:`css_put`\ .

.. _`for_each_css`:

for_each_css
============

.. c:function::  for_each_css( css,  ssid,  cgrp)

    iterate all css's of a cgroup

    :param  css:
        the iteration cursor

    :param  ssid:
        the index of the subsystem, CGROUP_SUBSYS_COUNT after reaching the end

    :param  cgrp:
        the target cgroup to iterate css's of

.. _`for_each_css.description`:

Description
-----------

Should be called under cgroup_[tree_]mutex.

.. _`for_each_e_css`:

for_each_e_css
==============

.. c:function::  for_each_e_css( css,  ssid,  cgrp)

    iterate all effective css's of a cgroup

    :param  css:
        the iteration cursor

    :param  ssid:
        the index of the subsystem, CGROUP_SUBSYS_COUNT after reaching the end

    :param  cgrp:
        the target cgroup to iterate css's of

.. _`for_each_e_css.description`:

Description
-----------

Should be called under cgroup_[tree_]mutex.

.. _`do_each_subsys_mask`:

do_each_subsys_mask
===================

.. c:function::  do_each_subsys_mask( ss,  ssid,  ss_mask)

    filter for_each_subsys with a bitmask

    :param  ss:
        the iteration cursor

    :param  ssid:
        the index of \ ``ss``\ , CGROUP_SUBSYS_COUNT after reaching the end

    :param  ss_mask:
        the bitmask

.. _`do_each_subsys_mask.description`:

Description
-----------

The block will only run for cases where the ssid-th bit (1 << ssid) of
\ ``ss_mask``\  is set.

.. _`css_set_populated`:

css_set_populated
=================

.. c:function:: bool css_set_populated(struct css_set *cset)

    does a css_set contain any tasks?

    :param struct css_set \*cset:
        target css_set

.. _`css_set_populated.description`:

Description
-----------

\ :c:func:`css_set_populated`\  should be the same as !!cset->nr_tasks at steady
state. However, \ :c:func:`css_set_populated`\  can be called while a task is being
added to or removed from the linked list before the nr_tasks is
properly updated. Hence, we can't just look at ->nr_tasks here.

.. _`cgroup_update_populated`:

cgroup_update_populated
=======================

.. c:function:: void cgroup_update_populated(struct cgroup *cgrp, bool populated)

    update the populated count of a cgroup

    :param struct cgroup \*cgrp:
        the target cgroup

    :param bool populated:
        inc or dec populated count

.. _`cgroup_update_populated.description`:

Description
-----------

One of the css_sets associated with \ ``cgrp``\  is either getting its first
task or losing the last.  Update \ ``cgrp``\ ->nr_populated\_\* accordingly.  The
count is propagated towards root so that a given cgroup's
nr_populated_children is zero iff none of its descendants contain any
tasks.

\ ``cgrp``\ 's interface file "cgroup.populated" is zero if both
\ ``cgrp``\ ->nr_populated_csets and \ ``cgrp``\ ->nr_populated_children are zero and
1 otherwise.  When the sum changes from or to zero, userland is notified
that the content of the interface file has changed.  This can be used to
detect when \ ``cgrp``\  and its descendants become populated or empty.

.. _`css_set_update_populated`:

css_set_update_populated
========================

.. c:function:: void css_set_update_populated(struct css_set *cset, bool populated)

    update populated state of a css_set

    :param struct css_set \*cset:
        target css_set

    :param bool populated:
        whether \ ``cset``\  is populated or depopulated

.. _`css_set_update_populated.description`:

Description
-----------

\ ``cset``\  is either getting the first task or losing the last.  Update the
populated counters of all associated cgroups accordingly.

.. _`css_set_move_task`:

css_set_move_task
=================

.. c:function:: void css_set_move_task(struct task_struct *task, struct css_set *from_cset, struct css_set *to_cset, bool use_mg_tasks)

    move a task from one css_set to another

    :param struct task_struct \*task:
        task being moved

    :param struct css_set \*from_cset:
        css_set \ ``task``\  currently belongs to (may be NULL)

    :param struct css_set \*to_cset:
        new css_set \ ``task``\  is being moved to (may be NULL)

    :param bool use_mg_tasks:
        move to \ ``to_cset``\ ->mg_tasks instead of ->tasks

.. _`css_set_move_task.description`:

Description
-----------

Move \ ``task``\  from \ ``from_cset``\  to \ ``to_cset``\ .  If \ ``task``\  didn't belong to any
css_set, \ ``from_cset``\  can be NULL.  If \ ``task``\  is being disassociated
instead of moved, \ ``to_cset``\  can be NULL.

This function automatically handles populated counter updates and
css_task_iter adjustments but the caller is responsible for managing
\ ``from_cset``\  and \ ``to_cset``\ 's reference counts.

.. _`compare_css_sets`:

compare_css_sets
================

.. c:function:: bool compare_css_sets(struct css_set *cset, struct css_set *old_cset, struct cgroup *new_cgrp, struct cgroup_subsys_state  *template)

    helper function for \ :c:func:`find_existing_css_set`\ .

    :param struct css_set \*cset:
        candidate css_set being tested

    :param struct css_set \*old_cset:
        existing css_set for a task

    :param struct cgroup \*new_cgrp:
        cgroup that's being entered by the task

    :param struct cgroup_subsys_state  \*template:
        desired set of css pointers in css_set (pre-calculated)

.. _`compare_css_sets.description`:

Description
-----------

Returns true if "cset" matches "old_cset" except for the hierarchy
which "new_cgrp" belongs to, for which it should match "new_cgrp".

.. _`find_existing_css_set`:

find_existing_css_set
=====================

.. c:function:: struct css_set *find_existing_css_set(struct css_set *old_cset, struct cgroup *cgrp, struct cgroup_subsys_state  *template)

    init css array and find the matching css_set

    :param struct css_set \*old_cset:
        the css_set that we're using before the cgroup transition

    :param struct cgroup \*cgrp:
        the cgroup that we're moving into

    :param struct cgroup_subsys_state  \*template:
        out param for the new set of csses, should be clear on entry

.. _`allocate_cgrp_cset_links`:

allocate_cgrp_cset_links
========================

.. c:function:: int allocate_cgrp_cset_links(int count, struct list_head *tmp_links)

    allocate cgrp_cset_links

    :param int count:
        the number of links to allocate

    :param struct list_head \*tmp_links:
        list_head the allocated links are put on

.. _`allocate_cgrp_cset_links.description`:

Description
-----------

Allocate \ ``count``\  cgrp_cset_link structures and chain them on \ ``tmp_links``\ 
through ->cset_link.  Returns 0 on success or -errno.

.. _`link_css_set`:

link_css_set
============

.. c:function:: void link_css_set(struct list_head *tmp_links, struct css_set *cset, struct cgroup *cgrp)

    a helper function to link a css_set to a cgroup

    :param struct list_head \*tmp_links:
        cgrp_cset_link objects allocated by \ :c:func:`allocate_cgrp_cset_links`\ 

    :param struct css_set \*cset:
        the css_set to be linked

    :param struct cgroup \*cgrp:
        the destination cgroup

.. _`find_css_set`:

find_css_set
============

.. c:function:: struct css_set *find_css_set(struct css_set *old_cset, struct cgroup *cgrp)

    return a new css_set with one cgroup updated

    :param struct css_set \*old_cset:
        the baseline css_set

    :param struct cgroup \*cgrp:
        the cgroup to be updated

.. _`find_css_set.description`:

Description
-----------

Return a new css_set that's equivalent to \ ``old_cset``\ , but with \ ``cgrp``\ 
substituted into the appropriate hierarchy.

.. _`cgroup_file_mode`:

cgroup_file_mode
================

.. c:function:: umode_t cgroup_file_mode(const struct cftype *cft)

    deduce file mode of a control file

    :param const struct cftype \*cft:
        the control file in question

.. _`cgroup_file_mode.description`:

Description
-----------

S_IRUGO for read, S_IWUSR for write.

.. _`cgroup_calc_subtree_ss_mask`:

cgroup_calc_subtree_ss_mask
===========================

.. c:function:: u16 cgroup_calc_subtree_ss_mask(u16 subtree_control, u16 this_ss_mask)

    calculate subtree_ss_mask

    :param u16 subtree_control:
        the new subtree_control mask to consider

    :param u16 this_ss_mask:
        available subsystems

.. _`cgroup_calc_subtree_ss_mask.description`:

Description
-----------

On the default hierarchy, a subsystem may request other subsystems to be
enabled together through its ->depends_on mask.  In such cases, more
subsystems than specified in "cgroup.subtree_control" may be enabled.

This function calculates which subsystems need to be enabled if
\ ``subtree_control``\  is to be applied while restricted to \ ``this_ss_mask``\ .

.. _`cgroup_kn_unlock`:

cgroup_kn_unlock
================

.. c:function:: void cgroup_kn_unlock(struct kernfs_node *kn)

    unlocking helper for cgroup kernfs methods

    :param struct kernfs_node \*kn:
        the kernfs_node being serviced

.. _`cgroup_kn_unlock.description`:

Description
-----------

This helper undoes \ :c:func:`cgroup_kn_lock_live`\  and should be invoked before
the method finishes if locking succeeded.  Note that once this function
returns the cgroup returned by \ :c:func:`cgroup_kn_lock_live`\  may become
inaccessible any time.  If the caller intends to continue to access the
cgroup, it should pin it before invoking this function.

.. _`cgroup_kn_lock_live`:

cgroup_kn_lock_live
===================

.. c:function:: struct cgroup *cgroup_kn_lock_live(struct kernfs_node *kn, bool drain_offline)

    locking helper for cgroup kernfs methods

    :param struct kernfs_node \*kn:
        the kernfs_node being serviced

    :param bool drain_offline:
        perform offline draining on the cgroup

.. _`cgroup_kn_lock_live.description`:

Description
-----------

This helper is to be used by a cgroup kernfs method currently servicing
\ ``kn``\ .  It breaks the active protection, performs cgroup locking and
verifies that the associated cgroup is alive.  Returns the cgroup if
alive; otherwise, \ ``NULL``\ .  A successful return should be undone by a
matching \ :c:func:`cgroup_kn_unlock`\  invocation.  If \ ``drain_offline``\  is \ ``true``\ , the
cgroup is drained of offlining csses before return.

Any cgroup kernfs method implementation which requires locking the
associated cgroup should use this helper.  It avoids nesting cgroup
locking under kernfs active protection and allows all kernfs operations
including self-removal.

.. _`css_clear_dir`:

css_clear_dir
=============

.. c:function:: void css_clear_dir(struct cgroup_subsys_state *css)

    remove subsys files in a cgroup directory

    :param struct cgroup_subsys_state \*css:
        taget css

.. _`css_populate_dir`:

css_populate_dir
================

.. c:function:: int css_populate_dir(struct cgroup_subsys_state *css)

    create subsys files in a cgroup directory

    :param struct cgroup_subsys_state \*css:
        target css

.. _`css_populate_dir.description`:

Description
-----------

On failure, no file is added.

.. _`task_cgroup_path`:

task_cgroup_path
================

.. c:function:: int task_cgroup_path(struct task_struct *task, char *buf, size_t buflen)

    cgroup path of a task in the first cgroup hierarchy

    :param struct task_struct \*task:
        target task

    :param char \*buf:
        the buffer to write the path into

    :param size_t buflen:
        the length of the buffer

.. _`task_cgroup_path.description`:

Description
-----------

Determine \ ``task``\ 's cgroup on the first (the one with the lowest non-zero
hierarchy_id) cgroup hierarchy and copy its path into \ ``buf``\ .  This
function grabs cgroup_mutex and shouldn't be used inside locks used by
cgroup controller callbacks.

Return value is the same as \ :c:func:`kernfs_path`\ .

.. _`cgroup_migrate_add_task`:

cgroup_migrate_add_task
=======================

.. c:function:: void cgroup_migrate_add_task(struct task_struct *task, struct cgroup_mgctx *mgctx)

    add a migration target task to a migration context

    :param struct task_struct \*task:
        target task

    :param struct cgroup_mgctx \*mgctx:
        target migration context

.. _`cgroup_migrate_add_task.description`:

Description
-----------

Add \ ``task``\ , which is a migration target, to \ ``mgctx``\ ->tset.  This function
becomes noop if \ ``task``\  doesn't need to be migrated.  \ ``task``\ 's css_set
should have been added as a migration source and \ ``task``\ ->cg_list will be
moved from the css_set's tasks list to mg_tasks one.

.. _`cgroup_taskset_first`:

cgroup_taskset_first
====================

.. c:function:: struct task_struct *cgroup_taskset_first(struct cgroup_taskset *tset, struct cgroup_subsys_state **dst_cssp)

    reset taskset and return the first task

    :param struct cgroup_taskset \*tset:
        taskset of interest

    :param struct cgroup_subsys_state \*\*dst_cssp:
        output variable for the destination css

.. _`cgroup_taskset_first.description`:

Description
-----------

\ ``tset``\  iteration is initialized and the first task is returned.

.. _`cgroup_taskset_next`:

cgroup_taskset_next
===================

.. c:function:: struct task_struct *cgroup_taskset_next(struct cgroup_taskset *tset, struct cgroup_subsys_state **dst_cssp)

    iterate to the next task in taskset

    :param struct cgroup_taskset \*tset:
        taskset of interest

    :param struct cgroup_subsys_state \*\*dst_cssp:
        output variable for the destination css

.. _`cgroup_taskset_next.description`:

Description
-----------

Return the next task in \ ``tset``\ .  Iteration must have been initialized
with \ :c:func:`cgroup_taskset_first`\ .

.. _`cgroup_migrate_execute`:

cgroup_migrate_execute
======================

.. c:function:: int cgroup_migrate_execute(struct cgroup_mgctx *mgctx)

    migrate a taskset

    :param struct cgroup_mgctx \*mgctx:
        migration context

.. _`cgroup_migrate_execute.description`:

Description
-----------

Migrate tasks in \ ``mgctx``\  as setup by migration preparation functions.
This function fails iff one of the ->can_attach callbacks fails and
guarantees that either all or none of the tasks in \ ``mgctx``\  are migrated.
\ ``mgctx``\  is consumed regardless of success.

.. _`cgroup_migrate_vet_dst`:

cgroup_migrate_vet_dst
======================

.. c:function:: int cgroup_migrate_vet_dst(struct cgroup *dst_cgrp)

    verify whether a cgroup can be migration destination

    :param struct cgroup \*dst_cgrp:
        destination cgroup to test

.. _`cgroup_migrate_vet_dst.description`:

Description
-----------

On the default hierarchy, except for the mixable, (possible) thread root
and threaded cgroups, subtree_control must be zero for migration
destination cgroups with tasks so that child cgroups don't compete
against tasks.

.. _`cgroup_migrate_finish`:

cgroup_migrate_finish
=====================

.. c:function:: void cgroup_migrate_finish(struct cgroup_mgctx *mgctx)

    cleanup after attach

    :param struct cgroup_mgctx \*mgctx:
        migration context

.. _`cgroup_migrate_finish.description`:

Description
-----------

Undo \ :c:func:`cgroup_migrate_add_src`\  and \ :c:func:`cgroup_migrate_prepare_dst`\ .  See
those functions for details.

.. _`cgroup_migrate_add_src`:

cgroup_migrate_add_src
======================

.. c:function:: void cgroup_migrate_add_src(struct css_set *src_cset, struct cgroup *dst_cgrp, struct cgroup_mgctx *mgctx)

    add a migration source css_set

    :param struct css_set \*src_cset:
        the source css_set to add

    :param struct cgroup \*dst_cgrp:
        the destination cgroup

    :param struct cgroup_mgctx \*mgctx:
        migration context

.. _`cgroup_migrate_add_src.description`:

Description
-----------

Tasks belonging to \ ``src_cset``\  are about to be migrated to \ ``dst_cgrp``\ .  Pin
\ ``src_cset``\  and add it to \ ``mgctx``\ ->src_csets, which should later be cleaned
up by \ :c:func:`cgroup_migrate_finish`\ .

This function may be called without holding cgroup_threadgroup_rwsem
even if the target is a process.  Threads may be created and destroyed
but as long as cgroup_mutex is not dropped, no new css_set can be put
into play and the preloaded css_sets are guaranteed to cover all
migrations.

.. _`cgroup_migrate_prepare_dst`:

cgroup_migrate_prepare_dst
==========================

.. c:function:: int cgroup_migrate_prepare_dst(struct cgroup_mgctx *mgctx)

    prepare destination css_sets for migration

    :param struct cgroup_mgctx \*mgctx:
        migration context

.. _`cgroup_migrate_prepare_dst.description`:

Description
-----------

Tasks are about to be moved and all the source css_sets have been
preloaded to \ ``mgctx``\ ->preloaded_src_csets.  This function looks up and
pins all destination css_sets, links each to its source, and append them
to \ ``mgctx``\ ->preloaded_dst_csets.

This function must be called after \ :c:func:`cgroup_migrate_add_src`\  has been
called on each migration source css_set.  After migration is performed
using \ :c:func:`cgroup_migrate`\ , \ :c:func:`cgroup_migrate_finish`\  must be called on
\ ``mgctx``\ .

.. _`cgroup_migrate`:

cgroup_migrate
==============

.. c:function:: int cgroup_migrate(struct task_struct *leader, bool threadgroup, struct cgroup_mgctx *mgctx)

    migrate a process or task to a cgroup

    :param struct task_struct \*leader:
        the leader of the process or the task to migrate

    :param bool threadgroup:
        whether \ ``leader``\  points to the whole process or a single task

    :param struct cgroup_mgctx \*mgctx:
        migration context

.. _`cgroup_migrate.description`:

Description
-----------

Migrate a process or task denoted by \ ``leader``\ .  If migrating a process,
the caller must be holding cgroup_threadgroup_rwsem.  The caller is also
responsible for invoking \ :c:func:`cgroup_migrate_add_src`\  and
\ :c:func:`cgroup_migrate_prepare_dst`\  on the targets before invoking this
function and following up with \ :c:func:`cgroup_migrate_finish`\ .

As long as a controller's ->can_attach() doesn't fail, this function is
guaranteed to succeed.  This means that, excluding ->can_attach()
failure, when migrating multiple targets, the success or failure can be
decided for all targets by invoking \ :c:func:`group_migrate_prepare_dst`\  before
actually starting migrating.

.. _`cgroup_attach_task`:

cgroup_attach_task
==================

.. c:function:: int cgroup_attach_task(struct cgroup *dst_cgrp, struct task_struct *leader, bool threadgroup)

    attach a task or a whole threadgroup to a cgroup

    :param struct cgroup \*dst_cgrp:
        the cgroup to attach to

    :param struct task_struct \*leader:
        the task or the leader of the threadgroup to be attached

    :param bool threadgroup:
        attach the whole threadgroup?

.. _`cgroup_attach_task.description`:

Description
-----------

Call holding cgroup_mutex and cgroup_threadgroup_rwsem.

.. _`cgroup_update_dfl_csses`:

cgroup_update_dfl_csses
=======================

.. c:function:: int cgroup_update_dfl_csses(struct cgroup *cgrp)

    update css assoc of a subtree in default hierarchy

    :param struct cgroup \*cgrp:
        root of the subtree to update csses for

.. _`cgroup_update_dfl_csses.description`:

Description
-----------

\ ``cgrp``\ 's control masks have changed and its subtree's css associations
need to be updated accordingly.  This function looks up all css_sets
which are attached to the subtree, creates the matching updated css_sets
and migrates the tasks to the new ones.

.. _`cgroup_lock_and_drain_offline`:

cgroup_lock_and_drain_offline
=============================

.. c:function:: void cgroup_lock_and_drain_offline(struct cgroup *cgrp)

    lock cgroup_mutex and drain offlined csses

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_lock_and_drain_offline.description`:

Description
-----------

Because css offlining is asynchronous, userland may try to re-enable a
controller while the previous css is still around.  This function grabs
cgroup_mutex and drains the previous css instances of \ ``cgrp``\ 's subtree.

.. _`cgroup_save_control`:

cgroup_save_control
===================

.. c:function:: void cgroup_save_control(struct cgroup *cgrp)

    save control masks of a subtree

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_save_control.description`:

Description
-----------

Save ->subtree_control and ->subtree_ss_mask to the respective old_
prefixed fields for \ ``cgrp``\ 's subtree including \ ``cgrp``\  itself.

.. _`cgroup_propagate_control`:

cgroup_propagate_control
========================

.. c:function:: void cgroup_propagate_control(struct cgroup *cgrp)

    refresh control masks of a subtree

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_propagate_control.description`:

Description
-----------

For \ ``cgrp``\  and its subtree, ensure ->subtree_ss_mask matches
->subtree_control and propagate controller availability through the
subtree so that descendants don't have unavailable controllers enabled.

.. _`cgroup_restore_control`:

cgroup_restore_control
======================

.. c:function:: void cgroup_restore_control(struct cgroup *cgrp)

    restore control masks of a subtree

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_restore_control.description`:

Description
-----------

Restore ->subtree_control and ->subtree_ss_mask from the respective old_
prefixed fields for \ ``cgrp``\ 's subtree including \ ``cgrp``\  itself.

.. _`cgroup_apply_control_enable`:

cgroup_apply_control_enable
===========================

.. c:function:: int cgroup_apply_control_enable(struct cgroup *cgrp)

    enable or show csses according to control

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_apply_control_enable.description`:

Description
-----------

Walk \ ``cgrp``\ 's subtree and create new csses or make the existing ones
visible.  A css is created invisible if it's being implicitly enabled
through dependency.  An invisible css is made visible when the userland
explicitly enables it.

Returns 0 on success, -errno on failure.  On failure, csses which have
been processed already aren't cleaned up.  The caller is responsible for
cleaning up with \ :c:func:`cgroup_apply_control_disable`\ .

.. _`cgroup_apply_control_disable`:

cgroup_apply_control_disable
============================

.. c:function:: void cgroup_apply_control_disable(struct cgroup *cgrp)

    kill or hide csses according to control

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_apply_control_disable.description`:

Description
-----------

Walk \ ``cgrp``\ 's subtree and kill and hide csses so that they match
\ :c:func:`cgroup_ss_mask`\  and \ :c:func:`cgroup_visible_mask`\ .

A css is hidden when the userland requests it to be disabled while other
subsystems are still depending on it.  The css must not actively control
resources and be in the vanilla state if it's made visible again later.
Controllers which may be depended upon should provide ->css_reset() for
this purpose.

.. _`cgroup_apply_control`:

cgroup_apply_control
====================

.. c:function:: int cgroup_apply_control(struct cgroup *cgrp)

    apply control mask updates to the subtree

    :param struct cgroup \*cgrp:
        root of the target subtree

.. _`cgroup_apply_control.description`:

Description
-----------

subsystems can be enabled and disabled in a subtree using the following
steps.

1. Call \ :c:func:`cgroup_save_control`\  to stash the current state.
2. Update ->subtree_control masks in the subtree as desired.
3. Call \ :c:func:`cgroup_apply_control`\  to apply the changes.
4. Optionally perform other related operations.
5. Call \ :c:func:`cgroup_finalize_control`\  to finish up.

This function implements step 3 and propagates the mask changes
throughout \ ``cgrp``\ 's subtree, updates csses accordingly and perform
process migrations.

.. _`cgroup_finalize_control`:

cgroup_finalize_control
=======================

.. c:function:: void cgroup_finalize_control(struct cgroup *cgrp, int ret)

    finalize control mask update

    :param struct cgroup \*cgrp:
        root of the target subtree

    :param int ret:
        the result of the update

.. _`cgroup_finalize_control.description`:

Description
-----------

Finalize control mask update.  See \ :c:func:`cgroup_apply_control`\  for more info.

.. _`cgroup_enable_threaded`:

cgroup_enable_threaded
======================

.. c:function:: int cgroup_enable_threaded(struct cgroup *cgrp)

    make \ ``cgrp``\  threaded

    :param struct cgroup \*cgrp:
        the target cgroup

.. _`cgroup_enable_threaded.description`:

Description
-----------

Called when "threaded" is written to the cgroup.type interface file and
tries to make \ ``cgrp``\  threaded and join the parent's resource domain.
This function is never called on the root cgroup as cgroup.type doesn't
exist on it.

.. _`cgroup_addrm_files`:

cgroup_addrm_files
==================

.. c:function:: int cgroup_addrm_files(struct cgroup_subsys_state *css, struct cgroup *cgrp, struct cftype cfts, bool is_add)

    add or remove files to a cgroup directory

    :param struct cgroup_subsys_state \*css:
        the target css

    :param struct cgroup \*cgrp:
        the target cgroup (usually css->cgroup)

    :param struct cftype cfts:
        array of cftypes to be added

    :param bool is_add:
        whether to add or remove

.. _`cgroup_addrm_files.description`:

Description
-----------

Depending on \ ``is_add``\ , add or remove files defined by \ ``cfts``\  on \ ``cgrp``\ .
For removals, this function never fails.

.. _`cgroup_rm_cftypes`:

cgroup_rm_cftypes
=================

.. c:function:: int cgroup_rm_cftypes(struct cftype *cfts)

    remove an array of cftypes from a subsystem

    :param struct cftype \*cfts:
        zero-length name terminated array of cftypes

.. _`cgroup_rm_cftypes.description`:

Description
-----------

Unregister \ ``cfts``\ .  Files described by \ ``cfts``\  are removed from all
existing cgroups and all future cgroups won't have them either.  This
function can be called anytime whether \ ``cfts``\ ' subsys is attached or not.

Returns 0 on successful unregistration, -ENOENT if \ ``cfts``\  is not
registered.

.. _`cgroup_add_cftypes`:

cgroup_add_cftypes
==================

.. c:function:: int cgroup_add_cftypes(struct cgroup_subsys *ss, struct cftype *cfts)

    add an array of cftypes to a subsystem

    :param struct cgroup_subsys \*ss:
        target cgroup subsystem

    :param struct cftype \*cfts:
        zero-length name terminated array of cftypes

.. _`cgroup_add_cftypes.description`:

Description
-----------

Register \ ``cfts``\  to \ ``ss``\ .  Files described by \ ``cfts``\  are created for all
existing cgroups to which \ ``ss``\  is attached and all future cgroups will
have them too.  This function can be called anytime whether \ ``ss``\  is
attached or not.

Returns 0 on successful registration, -errno on failure.  Note that this
function currently returns 0 as long as \ ``cfts``\  registration is successful
even if some file creation attempts on existing cgroups fail.

.. _`cgroup_add_dfl_cftypes`:

cgroup_add_dfl_cftypes
======================

.. c:function:: int cgroup_add_dfl_cftypes(struct cgroup_subsys *ss, struct cftype *cfts)

    add an array of cftypes for default hierarchy

    :param struct cgroup_subsys \*ss:
        target cgroup subsystem

    :param struct cftype \*cfts:
        zero-length name terminated array of cftypes

.. _`cgroup_add_dfl_cftypes.description`:

Description
-----------

Similar to \ :c:func:`cgroup_add_cftypes`\  but the added files are only used for
the default hierarchy.

.. _`cgroup_add_legacy_cftypes`:

cgroup_add_legacy_cftypes
=========================

.. c:function:: int cgroup_add_legacy_cftypes(struct cgroup_subsys *ss, struct cftype *cfts)

    add an array of cftypes for legacy hierarchies

    :param struct cgroup_subsys \*ss:
        target cgroup subsystem

    :param struct cftype \*cfts:
        zero-length name terminated array of cftypes

.. _`cgroup_add_legacy_cftypes.description`:

Description
-----------

Similar to \ :c:func:`cgroup_add_cftypes`\  but the added files are only used for
the legacy hierarchies.

.. _`cgroup_file_notify`:

cgroup_file_notify
==================

.. c:function:: void cgroup_file_notify(struct cgroup_file *cfile)

    generate a file modified event for a cgroup_file

    :param struct cgroup_file \*cfile:
        target cgroup_file

.. _`cgroup_file_notify.description`:

Description
-----------

\ ``cfile``\  must have been obtained by setting cftype->file_offset.

.. _`css_next_child`:

css_next_child
==============

.. c:function:: struct cgroup_subsys_state *css_next_child(struct cgroup_subsys_state *pos, struct cgroup_subsys_state *parent)

    find the next child of a given css

    :param struct cgroup_subsys_state \*pos:
        the current position (%NULL to initiate traversal)

    :param struct cgroup_subsys_state \*parent:
        css whose children to walk

.. _`css_next_child.description`:

Description
-----------

This function returns the next child of \ ``parent``\  and should be called
under either cgroup_mutex or RCU read lock.  The only requirement is
that \ ``parent``\  and \ ``pos``\  are accessible.  The next sibling is guaranteed to
be returned regardless of their states.

If a subsystem synchronizes ->css_online() and the start of iteration, a
css which finished ->css_online() is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->css_online() or already finished
->css_offline() may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

.. _`css_next_descendant_pre`:

css_next_descendant_pre
=======================

.. c:function:: struct cgroup_subsys_state *css_next_descendant_pre(struct cgroup_subsys_state *pos, struct cgroup_subsys_state *root)

    find the next descendant for pre-order walk

    :param struct cgroup_subsys_state \*pos:
        the current position (%NULL to initiate traversal)

    :param struct cgroup_subsys_state \*root:
        css whose descendants to walk

.. _`css_next_descendant_pre.description`:

Description
-----------

To be used by \ :c:func:`css_for_each_descendant_pre`\ .  Find the next descendant
to visit for pre-order traversal of \ ``root``\ 's descendants.  \ ``root``\  is
included in the iteration and the first node to be visited.

While this function requires cgroup_mutex or RCU read locking, it
doesn't require the whole traversal to be contained in a single critical
section.  This function will return the correct next descendant as long
as both \ ``pos``\  and \ ``root``\  are accessible and \ ``pos``\  is a descendant of \ ``root``\ .

If a subsystem synchronizes ->css_online() and the start of iteration, a
css which finished ->css_online() is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->css_online() or already finished
->css_offline() may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

.. _`css_rightmost_descendant`:

css_rightmost_descendant
========================

.. c:function:: struct cgroup_subsys_state *css_rightmost_descendant(struct cgroup_subsys_state *pos)

    return the rightmost descendant of a css

    :param struct cgroup_subsys_state \*pos:
        css of interest

.. _`css_rightmost_descendant.description`:

Description
-----------

Return the rightmost descendant of \ ``pos``\ .  If there's no descendant, \ ``pos``\ 
is returned.  This can be used during pre-order traversal to skip
subtree of \ ``pos``\ .

While this function requires cgroup_mutex or RCU read locking, it
doesn't require the whole traversal to be contained in a single critical
section.  This function will return the correct rightmost descendant as
long as \ ``pos``\  is accessible.

.. _`css_next_descendant_post`:

css_next_descendant_post
========================

.. c:function:: struct cgroup_subsys_state *css_next_descendant_post(struct cgroup_subsys_state *pos, struct cgroup_subsys_state *root)

    find the next descendant for post-order walk

    :param struct cgroup_subsys_state \*pos:
        the current position (%NULL to initiate traversal)

    :param struct cgroup_subsys_state \*root:
        css whose descendants to walk

.. _`css_next_descendant_post.description`:

Description
-----------

To be used by \ :c:func:`css_for_each_descendant_post`\ .  Find the next descendant
to visit for post-order traversal of \ ``root``\ 's descendants.  \ ``root``\  is
included in the iteration and the last node to be visited.

While this function requires cgroup_mutex or RCU read locking, it
doesn't require the whole traversal to be contained in a single critical
section.  This function will return the correct next descendant as long
as both \ ``pos``\  and \ ``cgroup``\  are accessible and \ ``pos``\  is a descendant of
\ ``cgroup``\ .

If a subsystem synchronizes ->css_online() and the start of iteration, a
css which finished ->css_online() is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->css_online() or already finished
->css_offline() may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

.. _`css_has_online_children`:

css_has_online_children
=======================

.. c:function:: bool css_has_online_children(struct cgroup_subsys_state *css)

    does a css have online children

    :param struct cgroup_subsys_state \*css:
        the target css

.. _`css_has_online_children.description`:

Description
-----------

Returns \ ``true``\  if \ ``css``\  has any online children; otherwise, \ ``false``\ .  This
function can be called from any context but the caller is responsible
for synchronizing against on/offlining as necessary.

.. _`css_task_iter_advance_css_set`:

css_task_iter_advance_css_set
=============================

.. c:function:: void css_task_iter_advance_css_set(struct css_task_iter *it)

    advance a task itererator to the next css_set

    :param struct css_task_iter \*it:
        the iterator to advance

.. _`css_task_iter_advance_css_set.description`:

Description
-----------

Advance \ ``it``\  to the next css_set to walk.

.. _`css_task_iter_start`:

css_task_iter_start
===================

.. c:function:: void css_task_iter_start(struct cgroup_subsys_state *css, unsigned int flags, struct css_task_iter *it)

    initiate task iteration

    :param struct cgroup_subsys_state \*css:
        the css to walk tasks of

    :param unsigned int flags:
        CSS_TASK_ITER\_\* flags

    :param struct css_task_iter \*it:
        the task iterator to use

.. _`css_task_iter_start.description`:

Description
-----------

Initiate iteration through the tasks of \ ``css``\ .  The caller can call
\ :c:func:`css_task_iter_next`\  to walk through the tasks until the function
returns NULL.  On completion of iteration, \ :c:func:`css_task_iter_end`\  must be
called.

.. _`css_task_iter_next`:

css_task_iter_next
==================

.. c:function:: struct task_struct *css_task_iter_next(struct css_task_iter *it)

    return the next task for the iterator

    :param struct css_task_iter \*it:
        the task iterator being iterated

.. _`css_task_iter_next.description`:

Description
-----------

The "next" function for task iteration.  \ ``it``\  should have been
initialized via \ :c:func:`css_task_iter_start`\ .  Returns NULL when the iteration
reaches the end.

.. _`css_task_iter_end`:

css_task_iter_end
=================

.. c:function:: void css_task_iter_end(struct css_task_iter *it)

    finish task iteration

    :param struct css_task_iter \*it:
        the task iterator to finish

.. _`css_task_iter_end.description`:

Description
-----------

Finish task iteration started by \ :c:func:`css_task_iter_start`\ .

.. _`css_create`:

css_create
==========

.. c:function:: struct cgroup_subsys_state *css_create(struct cgroup *cgrp, struct cgroup_subsys *ss)

    create a cgroup_subsys_state

    :param struct cgroup \*cgrp:
        the cgroup new css will be associated with

    :param struct cgroup_subsys \*ss:
        the subsys of new css

.. _`css_create.description`:

Description
-----------

Create a new css associated with \ ``cgrp``\  - \ ``ss``\  pair.  On success, the new
css is online and installed in \ ``cgrp``\ .  This function doesn't create the
interface files.  Returns 0 on success, -errno on failure.

.. _`kill_css`:

kill_css
========

.. c:function:: void kill_css(struct cgroup_subsys_state *css)

    destroy a css

    :param struct cgroup_subsys_state \*css:
        css to destroy

.. _`kill_css.description`:

Description
-----------

This function initiates destruction of \ ``css``\  by removing cgroup interface
files and putting its base reference.  ->css_offline() will be invoked
asynchronously once \ :c:func:`css_tryget_online`\  is guaranteed to fail and when
the reference count reaches zero, \ ``css``\  will be released.

.. _`cgroup_destroy_locked`:

cgroup_destroy_locked
=====================

.. c:function:: int cgroup_destroy_locked(struct cgroup *cgrp)

    the first stage of cgroup destruction

    :param struct cgroup \*cgrp:
        cgroup to be destroyed

.. _`cgroup_destroy_locked.description`:

Description
-----------

css's make use of percpu refcnts whose killing latency shouldn't be
exposed to userland and are RCU protected.  Also, cgroup core needs to
guarantee that \ :c:func:`css_tryget_online`\  won't succeed by the time
->css_offline() is invoked.  To satisfy all the requirements,
destruction is implemented in the following two steps.

s1. Verify \ ``cgrp``\  can be destroyed and mark it dying.  Remove all
userland visible parts and start killing the percpu refcnts of
css's.  Set up so that the next stage will be kicked off once all
the percpu refcnts are confirmed to be killed.

s2. Invoke ->css_offline(), mark the cgroup dead and proceed with the
rest of destruction.  Once all cgroup references are gone, the
cgroup is RCU-freed.

This function implements s1.  After this step, \ ``cgrp``\  is gone as far as
the userland is concerned and a new cgroup with the same name may be
created.  As cgroup doesn't care about the names internally, this
doesn't cause any problem.

.. _`cgroup_init_early`:

cgroup_init_early
=================

.. c:function:: int cgroup_init_early( void)

    cgroup initialization at system boot

    :param  void:
        no arguments

.. _`cgroup_init_early.description`:

Description
-----------

Initialize cgroups at system boot, and initialize any
subsystems that request early init.

.. _`cgroup_init`:

cgroup_init
===========

.. c:function:: int cgroup_init( void)

    cgroup initialization

    :param  void:
        no arguments

.. _`cgroup_init.description`:

Description
-----------

Register cgroup filesystem and /proc file, and initialize
any subsystems that didn't request early init.

.. _`cgroup_fork`:

cgroup_fork
===========

.. c:function:: void cgroup_fork(struct task_struct *child)

    initialize cgroup related fields during \ :c:func:`copy_process`\ 

    :param struct task_struct \*child:
        pointer to task_struct of forking parent process.

.. _`cgroup_fork.description`:

Description
-----------

A task is associated with the init_css_set until \ :c:func:`cgroup_post_fork`\ 
attaches it to the parent's css_set.  Empty cg_list indicates that
\ ``child``\  isn't holding reference to its css_set.

.. _`cgroup_can_fork`:

cgroup_can_fork
===============

.. c:function:: int cgroup_can_fork(struct task_struct *child)

    called on a new task before the process is exposed

    :param struct task_struct \*child:
        the task in question.

.. _`cgroup_can_fork.description`:

Description
-----------

This calls the subsystem \ :c:func:`can_fork`\  callbacks. If the \ :c:func:`can_fork`\  callback
returns an error, the fork aborts with that error code. This allows for
a cgroup subsystem to conditionally allow or deny new forks.

.. _`cgroup_cancel_fork`:

cgroup_cancel_fork
==================

.. c:function:: void cgroup_cancel_fork(struct task_struct *child)

    called if a fork failed after \ :c:func:`cgroup_can_fork`\ 

    :param struct task_struct \*child:
        the task in question

.. _`cgroup_cancel_fork.description`:

Description
-----------

This calls the \ :c:func:`cancel_fork`\  callbacks if a fork failed \*after\*
\ :c:func:`cgroup_can_fork`\  succeded.

.. _`cgroup_post_fork`:

cgroup_post_fork
================

.. c:function:: void cgroup_post_fork(struct task_struct *child)

    called on a new task after adding it to the task list

    :param struct task_struct \*child:
        the task in question

.. _`cgroup_post_fork.description`:

Description
-----------

Adds the task to the list running through its css_set if necessary and
call the subsystem \ :c:func:`fork`\  callbacks.  Has to be after the task is
visible on the task list in case we race with the first call to
\ :c:func:`cgroup_task_iter_start`\  - to guarantee that the new task ends up on its
list.

.. _`cgroup_exit`:

cgroup_exit
===========

.. c:function:: void cgroup_exit(struct task_struct *tsk)

    detach cgroup from exiting task

    :param struct task_struct \*tsk:
        pointer to task_struct of exiting process

.. _`cgroup_exit.description`:

Description
-----------

Detach cgroup from \ ``tsk``\  and release it.

Note that cgroups marked notify_on_release force every task in
them to take the global cgroup_mutex mutex when exiting.
This could impact scaling on very large systems.  Be reluctant to
use notify_on_release cgroups where very high task exit scaling
is required on large systems.

We set the exiting tasks cgroup to the root cgroup (top_cgroup).  We
call \ :c:func:`cgroup_exit`\  while the task is still competent to handle
\ :c:func:`notify_on_release`\ , then leave the task attached to the root cgroup in
each hierarchy for the remainder of its exit.  No need to bother with
init_css_set refcnting.  init_css_set never goes away and we can't race
with migration path - PF_EXITING is visible to migration path.

.. _`css_tryget_online_from_dir`:

css_tryget_online_from_dir
==========================

.. c:function:: struct cgroup_subsys_state *css_tryget_online_from_dir(struct dentry *dentry, struct cgroup_subsys *ss)

    get corresponding css from a cgroup dentry

    :param struct dentry \*dentry:
        directory dentry of interest

    :param struct cgroup_subsys \*ss:
        subsystem of interest

.. _`css_tryget_online_from_dir.description`:

Description
-----------

If \ ``dentry``\  is a directory for a cgroup which has \ ``ss``\  enabled on it, try
to get the corresponding css and return it.  If such css doesn't exist
or can't be pinned, an ERR_PTR value is returned.

.. _`css_from_id`:

css_from_id
===========

.. c:function:: struct cgroup_subsys_state *css_from_id(int id, struct cgroup_subsys *ss)

    lookup css by id

    :param int id:
        the cgroup id

    :param struct cgroup_subsys \*ss:
        cgroup subsys to be looked into

.. _`css_from_id.description`:

Description
-----------

Returns the css if there's valid one with \ ``id``\ , otherwise returns NULL.
Should be called under \ :c:func:`rcu_read_lock`\ .

.. _`cgroup_get_from_path`:

cgroup_get_from_path
====================

.. c:function:: struct cgroup *cgroup_get_from_path(const char *path)

    lookup and get a cgroup from its default hierarchy path

    :param const char \*path:
        path on the default hierarchy

.. _`cgroup_get_from_path.description`:

Description
-----------

Find the cgroup at \ ``path``\  on the default hierarchy, increment its
reference count and return it.  Returns pointer to the found cgroup on
success, ERR_PTR(-ENOENT) if \ ``path``\  doens't exist and ERR_PTR(-ENOTDIR)
if \ ``path``\  points to a non-directory.

.. _`cgroup_get_from_fd`:

cgroup_get_from_fd
==================

.. c:function:: struct cgroup *cgroup_get_from_fd(int fd)

    get a cgroup pointer from a fd

    :param int fd:
        fd obtained by open(cgroup2_dir)

.. _`cgroup_get_from_fd.description`:

Description
-----------

Find the cgroup from a fd which should be obtained
by opening a cgroup directory.  Returns a pointer to the
cgroup on success. ERR_PTR is returned if the cgroup
cannot be found.

.. This file was automatic generated / don't edit.


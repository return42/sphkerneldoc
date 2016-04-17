.. -*- coding: utf-8; mode: rst -*-

========
cgroup.h
========


.. _`cgroup_subsys_enabled`:

cgroup_subsys_enabled
=====================

.. c:function:: cgroup_subsys_enabled ( ss)

    fast test on whether a subsys is enabled

    :param ss:
        subsystem in question



.. _`cgroup_subsys_on_dfl`:

cgroup_subsys_on_dfl
====================

.. c:function:: cgroup_subsys_on_dfl ( ss)

    fast test on whether a subsys is on default hierarchy

    :param ss:
        subsystem in question



.. _`css_for_each_child`:

css_for_each_child
==================

.. c:function:: css_for_each_child ( pos,  parent)

    iterate through children of a css

    :param pos:
        the css * to use as the loop cursor

    :param parent:
        css whose children to walk



.. _`css_for_each_child.description`:

Description
-----------

Walk ``parent``\ 's children.  Must be called under :c:func:`rcu_read_lock`.

If a subsystem synchronizes ->:c:func:`css_online` and the start of iteration, a
css which finished ->:c:func:`css_online` is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->:c:func:`css_online` or already finished
->:c:func:`css_offline` may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

It is allowed to temporarily drop RCU read lock during iteration.  The
caller is responsible for ensuring that ``pos`` remains accessible until
the start of the next iteration by, for example, bumping the css refcnt.



.. _`css_for_each_descendant_pre`:

css_for_each_descendant_pre
===========================

.. c:function:: css_for_each_descendant_pre ( pos,  css)

    pre-order walk of a css's descendants

    :param pos:
        the css * to use as the loop cursor

    :param css:

        *undescribed*



.. _`css_for_each_descendant_pre.description`:

Description
-----------

Walk ``root``\ 's descendants.  ``root`` is included in the iteration and the
first node to be visited.  Must be called under :c:func:`rcu_read_lock`.

If a subsystem synchronizes ->:c:func:`css_online` and the start of iteration, a
css which finished ->:c:func:`css_online` is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->:c:func:`css_online` or already finished
->:c:func:`css_offline` may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

For example, the following guarantees that a descendant can't escape
state updates of its ancestors.

my_online(\ ``css``\ )
{
Lock ``css``\ 's parent and ``css``\ ;
Inherit state from the parent;
Unlock both.

}

my_update_state(\ ``css``\ )
{
css_for_each_descendant_pre(\ ``pos``\ , ``css``\ ) {
Lock ``pos``\ ;
if (\ ``pos`` == ``css``\ )
Update ``css``\ 's state;
else
Verify ``pos`` is alive and inherit state from its parent;
Unlock ``pos``\ ;
}

}

As long as the inheriting step, including checking the parent state, is
enclosed inside ``pos`` locking, double-locking the parent isn't necessary
while inheriting.  The state update to the parent is guaranteed to be
visible by walking order and, as long as inheriting operations to the
same ``pos`` are atomic to each other, multiple updates racing each other
still result in the correct state.  It's guaranateed that at least one
inheritance happens for any css after the latest update to its parent.

If checking parent's state requires locking the parent, each inheriting
iteration should lock and unlock both ``pos``\ ->parent and ``pos``\ .

Alternatively, a subsystem may choose to use a single global lock to
synchronize ->:c:func:`css_online` and ->:c:func:`css_offline` against tree-walking
operations.

It is allowed to temporarily drop RCU read lock during iteration.  The
caller is responsible for ensuring that ``pos`` remains accessible until
the start of the next iteration by, for example, bumping the css refcnt.



.. _`css_for_each_descendant_post`:

css_for_each_descendant_post
============================

.. c:function:: css_for_each_descendant_post ( pos,  css)

    post-order walk of a css's descendants

    :param pos:
        the css * to use as the loop cursor

    :param css:
        css whose descendants to walk



.. _`css_for_each_descendant_post.description`:

Description
-----------

Similar to :c:func:`css_for_each_descendant_pre` but performs post-order
traversal instead.  ``root`` is included in the iteration and the last
node to be visited.

If a subsystem synchronizes ->:c:func:`css_online` and the start of iteration, a
css which finished ->:c:func:`css_online` is guaranteed to be visible in the
future iterations and will stay visible until the last reference is put.
A css which hasn't finished ->:c:func:`css_online` or already finished
->:c:func:`css_offline` may show up during traversal.  It's each subsystem's
responsibility to synchronize against on/offlining.

Note that the walk visibility guarantee example described in pre-order
walk doesn't apply the same to post-order walks.



.. _`cgroup_taskset_for_each`:

cgroup_taskset_for_each
=======================

.. c:function:: cgroup_taskset_for_each ( task,  dst_css,  tset)

    iterate cgroup_taskset

    :param task:
        the loop cursor

    :param dst_css:
        the destination css

    :param tset:
        taskset to iterate



.. _`cgroup_taskset_for_each.description`:

Description
-----------

``tset`` may contain multiple tasks and they may belong to multiple
processes.

On the v2 hierarchy, there may be tasks from multiple processes and they
may not share the source or destination csses.

On traditional hierarchies, when there are multiple tasks in ``tset``\ , if a
task of a process is in ``tset``\ , all tasks of the process are in ``tset``\ .
Also, all are guaranteed to share the same source and destination csses.

Iteration is not in any specific order.



.. _`cgroup_taskset_for_each_leader`:

cgroup_taskset_for_each_leader
==============================

.. c:function:: cgroup_taskset_for_each_leader ( leader,  dst_css,  tset)

    iterate group leaders in a cgroup_taskset

    :param leader:
        the loop cursor

    :param dst_css:
        the destination css

    :param tset:
        takset to iterate



.. _`cgroup_taskset_for_each_leader.description`:

Description
-----------

Iterate threadgroup leaders of ``tset``\ .  For single-task migrations, ``tset``
may not contain any.



.. _`css_get`:

css_get
=======

.. c:function:: void css_get (struct cgroup_subsys_state *css)

    obtain a reference on the specified css

    :param struct cgroup_subsys_state \*css:
        target css



.. _`css_get.description`:

Description
-----------

The caller must already have a reference.



.. _`css_get_many`:

css_get_many
============

.. c:function:: void css_get_many (struct cgroup_subsys_state *css, unsigned int n)

    obtain references on the specified css

    :param struct cgroup_subsys_state \*css:
        target css

    :param unsigned int n:
        number of references to get



.. _`css_get_many.description`:

Description
-----------

The caller must already have a reference.



.. _`css_tryget`:

css_tryget
==========

.. c:function:: bool css_tryget (struct cgroup_subsys_state *css)

    try to obtain a reference on the specified css

    :param struct cgroup_subsys_state \*css:
        target css



.. _`css_tryget.description`:

Description
-----------

Obtain a reference on ``css`` unless it already has reached zero and is
being released.  This function doesn't care whether ``css`` is on or
offline.  The caller naturally needs to ensure that ``css`` is accessible
but doesn't have to be holding a reference on it - IOW, RCU protected
access is good enough for this function.  Returns ``true`` if a reference
count was successfully obtained; ``false`` otherwise.



.. _`css_tryget_online`:

css_tryget_online
=================

.. c:function:: bool css_tryget_online (struct cgroup_subsys_state *css)

    try to obtain a reference on the specified css if online

    :param struct cgroup_subsys_state \*css:
        target css



.. _`css_tryget_online.description`:

Description
-----------

Obtain a reference on ``css`` if it's online.  The caller naturally needs
to ensure that ``css`` is accessible but doesn't have to be holding a
reference on it - IOW, RCU protected access is good enough for this
function.  Returns ``true`` if a reference count was successfully obtained;
``false`` otherwise.



.. _`css_put`:

css_put
=======

.. c:function:: void css_put (struct cgroup_subsys_state *css)

    put a css reference

    :param struct cgroup_subsys_state \*css:
        target css



.. _`css_put.description`:

Description
-----------

Put a reference obtained via :c:func:`css_get` and :c:func:`css_tryget_online`.



.. _`css_put_many`:

css_put_many
============

.. c:function:: void css_put_many (struct cgroup_subsys_state *css, unsigned int n)

    put css references

    :param struct cgroup_subsys_state \*css:
        target css

    :param unsigned int n:
        number of references to put



.. _`css_put_many.description`:

Description
-----------

Put references obtained via :c:func:`css_get` and :c:func:`css_tryget_online`.



.. _`task_css_check`:

task_css_check
==============

.. c:function:: task_css_check ( task,  subsys_id,  __c)

    obtain css for (task, subsys) w/ extra access conds

    :param task:
        the target task

    :param subsys_id:
        the target subsystem ID

    :param __c:
        extra condition expression to be passed to :c:func:`rcu_dereference_check`



.. _`task_css_check.description`:

Description
-----------

Return the cgroup_subsys_state for the (\ ``task``\ , ``subsys_id``\ ) pair.  The
synchronization rules are the same as :c:func:`task_css_set_check`.



.. _`task_css_set`:

task_css_set
============

.. c:function:: struct css_set *task_css_set (struct task_struct *task)

    obtain a task's css_set

    :param struct task_struct \*task:
        the task to obtain css_set for



.. _`task_css_set.description`:

Description
-----------

See :c:func:`task_css_set_check`.



.. _`task_css`:

task_css
========

.. c:function:: struct cgroup_subsys_state *task_css (struct task_struct *task, int subsys_id)

    obtain css for (task, subsys)

    :param struct task_struct \*task:
        the target task

    :param int subsys_id:
        the target subsystem ID



.. _`task_css.description`:

Description
-----------

See :c:func:`task_css_check`.



.. _`task_get_css`:

task_get_css
============

.. c:function:: struct cgroup_subsys_state *task_get_css (struct task_struct *task, int subsys_id)

    find and get the css for (task, subsys)

    :param struct task_struct \*task:
        the target task

    :param int subsys_id:
        the target subsystem ID



.. _`task_get_css.description`:

Description
-----------

Find the css for the (\ ``task``\ , ``subsys_id``\ ) combination, increment a
reference on and return it.  This function is guaranteed to return a
valid css.



.. _`task_css_is_root`:

task_css_is_root
================

.. c:function:: bool task_css_is_root (struct task_struct *task, int subsys_id)

    test whether a task belongs to the root css

    :param struct task_struct \*task:
        the target task

    :param int subsys_id:
        the target subsystem ID



.. _`task_css_is_root.description`:

Description
-----------

Test whether ``task`` belongs to the root css on the specified subsystem.
May be invoked in any context.



.. _`cgroup_is_descendant`:

cgroup_is_descendant
====================

.. c:function:: bool cgroup_is_descendant (struct cgroup *cgrp, struct cgroup *ancestor)

    test ancestry

    :param struct cgroup \*cgrp:
        the cgroup to be tested

    :param struct cgroup \*ancestor:
        possible ancestor of ``cgrp``



.. _`cgroup_is_descendant.description`:

Description
-----------

Test whether ``cgrp`` is a descendant of ``ancestor``\ .  It also returns ``true``
if ``cgrp`` == ``ancestor``\ .  This function is safe to call as long as ``cgrp``
and ``ancestor`` are accessible.


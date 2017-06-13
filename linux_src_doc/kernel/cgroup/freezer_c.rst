.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/freezer.c

.. _`freezer_css_online`:

freezer_css_online
==================

.. c:function:: int freezer_css_online(struct cgroup_subsys_state *css)

    commit creation of a freezer css

    :param struct cgroup_subsys_state \*css:
        css being created

.. _`freezer_css_online.description`:

Description
-----------

We're committing to creation of \ ``css``\ .  Mark it online and inherit
parent's freezing state while holding both parent's and our
freezer->lock.

.. _`freezer_css_offline`:

freezer_css_offline
===================

.. c:function:: void freezer_css_offline(struct cgroup_subsys_state *css)

    initiate destruction of a freezer css

    :param struct cgroup_subsys_state \*css:
        css being destroyed

.. _`freezer_css_offline.description`:

Description
-----------

@css is going away.  Mark it dead and decrement system_freezing_count if
it was holding one.

.. _`freezer_fork`:

freezer_fork
============

.. c:function:: void freezer_fork(struct task_struct *task)

    cgroup post fork callback

    :param struct task_struct \*task:
        a task which has just been forked

.. _`freezer_fork.description`:

Description
-----------

@task has just been created and should conform to the current state of
the cgroup_freezer it belongs to.  This function may race against
\ :c:func:`freezer_attach`\ .  Losing to \ :c:func:`freezer_attach`\  means that we don't have
to do anything as \ :c:func:`freezer_attach`\  will put \ ``task``\  into the appropriate
state.

.. _`update_if_frozen`:

update_if_frozen
================

.. c:function:: void update_if_frozen(struct cgroup_subsys_state *css)

    update whether a cgroup finished freezing

    :param struct cgroup_subsys_state \*css:
        css of interest

.. _`update_if_frozen.description`:

Description
-----------

Once FREEZING is initiated, transition to FROZEN is lazily updated by
calling this function.  If the current state is FREEZING but not FROZEN,
this function checks whether all tasks of this cgroup and the descendant
cgroups finished freezing and, if so, sets FROZEN.

The caller is responsible for grabbing RCU read lock and calling
\ :c:func:`update_if_frozen`\  on all descendants prior to invoking this function.

Task states and freezer state might disagree while tasks are being
migrated into or out of \ ``css``\ , so we can't verify task states against
\ ``freezer``\  state here.  See \ :c:func:`freezer_attach`\  for details.

.. _`freezer_apply_state`:

freezer_apply_state
===================

.. c:function:: void freezer_apply_state(struct freezer *freezer, bool freeze, unsigned int state)

    apply state change to a single cgroup_freezer

    :param struct freezer \*freezer:
        freezer to apply state change to

    :param bool freeze:
        whether to freeze or unfreeze

    :param unsigned int state:
        CGROUP_FREEZING\_\* flag to set or clear

.. _`freezer_apply_state.description`:

Description
-----------

Set or clear \ ``state``\  on \ ``cgroup``\  according to \ ``freeze``\ , and perform
freezing or thawing as necessary.

.. _`freezer_change_state`:

freezer_change_state
====================

.. c:function:: void freezer_change_state(struct freezer *freezer, bool freeze)

    change the freezing state of a cgroup_freezer

    :param struct freezer \*freezer:
        freezer of interest

    :param bool freeze:
        whether to freeze or thaw

.. _`freezer_change_state.description`:

Description
-----------

Freeze or thaw \ ``freezer``\  according to \ ``freeze``\ .  The operations are
recursive - all descendants of \ ``freezer``\  will be affected.

.. This file was automatic generated / don't edit.


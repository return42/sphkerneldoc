.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/context.h

.. _`aa_alloc_file_context`:

aa_alloc_file_context
=====================

.. c:function:: struct aa_file_cxt *aa_alloc_file_context(gfp_t gfp)

    allocate file_cxt

    :param gfp_t gfp:
        gfp flags for allocation

.. _`aa_alloc_file_context.return`:

Return
------

file_cxt or NULL on failure

.. _`aa_free_file_context`:

aa_free_file_context
====================

.. c:function:: void aa_free_file_context(struct aa_file_cxt *cxt)

    free a file_cxt

    :param struct aa_file_cxt \*cxt:
        file_cxt to free  (MAYBE_NULL)

.. _`aa_task_cxt`:

struct aa_task_cxt
==================

.. c:type:: struct aa_task_cxt

    primary label for confined tasks

.. _`aa_task_cxt.definition`:

Definition
----------

.. code-block:: c

    struct aa_task_cxt {
        struct aa_profile *profile;
        struct aa_profile *onexec;
        struct aa_profile *previous;
        u64 token;
    }

.. _`aa_task_cxt.members`:

Members
-------

profile
    the current profile   (NOT NULL)

onexec
    *undescribed*

previous
    profile the task may return to     (MAYBE NULL)

token
    magic value the task must know for returning to \ ``previous_profile``\ 

.. _`aa_task_cxt.description`:

Description
-----------

Contains the task's current profile (which could change due to
change_hat).  Plus the hat_magic needed during change_hat.

.. _`aa_task_cxt.todo`:

TODO
----

make so a task can be confined by a stack of contexts

.. _`aa_cred_profile`:

aa_cred_profile
===============

.. c:function:: struct aa_profile *aa_cred_profile(const struct cred *cred)

    obtain cred's profiles

    :param const struct cred \*cred:
        cred to obtain profiles from  (NOT NULL)

.. _`aa_cred_profile.return`:

Return
------

confining profile

does NOT increment reference count

.. _`__aa_task_profile`:

__aa_task_profile
=================

.. c:function:: struct aa_profile *__aa_task_profile(struct task_struct *task)

    retrieve another task's profile

    :param struct task_struct \*task:
        task to query  (NOT NULL)

.. _`__aa_task_profile.return`:

Return
------

\ ``task``\ 's profile without incrementing its ref count

If \ ``task``\  != current needs to be called in RCU safe critical section

.. _`__aa_task_is_confined`:

__aa_task_is_confined
=====================

.. c:function:: bool __aa_task_is_confined(struct task_struct *task)

    determine if \ ``task``\  has any confinement

    :param struct task_struct \*task:
        task to check confinement of  (NOT NULL)

.. _`__aa_task_is_confined.description`:

Description
-----------

If \ ``task``\  != current needs to be called in RCU safe critical section

.. _`__aa_current_profile`:

__aa_current_profile
====================

.. c:function:: struct aa_profile *__aa_current_profile( void)

    find the current tasks confining profile

    :param  void:
        no arguments

.. _`__aa_current_profile.return`:

Return
------

up to date confining profile or the ns unconfined profile (NOT NULL)

This fn will not update the tasks cred to the most up to date version
of the profile so it is safe to call when inside of locks.

.. _`aa_current_profile`:

aa_current_profile
==================

.. c:function:: struct aa_profile *aa_current_profile( void)

    find the current tasks confining profile and do updates

    :param  void:
        no arguments

.. _`aa_current_profile.return`:

Return
------

up to date confining profile or the ns unconfined profile (NOT NULL)

This fn will update the tasks cred structure if the profile has been
replaced.  Not safe to call inside locks

.. _`aa_clear_task_cxt_trans`:

aa_clear_task_cxt_trans
=======================

.. c:function:: void aa_clear_task_cxt_trans(struct aa_task_cxt *cxt)

    clear transition tracking info from the cxt

    :param struct aa_task_cxt \*cxt:
        task context to clear (NOT NULL)

.. This file was automatic generated / don't edit.


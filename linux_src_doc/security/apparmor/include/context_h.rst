.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/context.h

.. _`aa_task_ctx`:

struct aa_task_ctx
==================

.. c:type:: struct aa_task_ctx

    primary label for confined tasks

.. _`aa_task_ctx.definition`:

Definition
----------

.. code-block:: c

    struct aa_task_ctx {
        struct aa_label *label;
        struct aa_label *onexec;
        struct aa_label *previous;
        u64 token;
    }

.. _`aa_task_ctx.members`:

Members
-------

label
    the current label   (NOT NULL)

onexec
    *undescribed*

previous
    label the task may return to     (MAYBE NULL)

token
    magic value the task must know for returning to \ ``previous``\ 

.. _`aa_task_ctx.description`:

Description
-----------

Contains the task's current label (which could change due to
change_hat).  Plus the hat_magic needed during change_hat.

.. _`aa_task_ctx.todo`:

TODO
----

make so a task can be confined by a stack of contexts

.. _`aa_cred_raw_label`:

aa_cred_raw_label
=================

.. c:function:: struct aa_label *aa_cred_raw_label(const struct cred *cred)

    obtain cred's label

    :param const struct cred \*cred:
        cred to obtain label from  (NOT NULL)

.. _`aa_cred_raw_label.return`:

Return
------

confining label

does NOT increment reference count

.. _`aa_get_newest_cred_label`:

aa_get_newest_cred_label
========================

.. c:function:: struct aa_label *aa_get_newest_cred_label(const struct cred *cred)

    obtain the newest label on a cred

    :param const struct cred \*cred:
        cred to obtain label from (NOT NULL)

.. _`aa_get_newest_cred_label.return`:

Return
------

newest version of confining label

.. _`__aa_task_raw_label`:

\__aa_task_raw_label
====================

.. c:function:: struct aa_label *__aa_task_raw_label(struct task_struct *task)

    retrieve another task's label

    :param struct task_struct \*task:
        task to query  (NOT NULL)

.. _`__aa_task_raw_label.return`:

Return
------

\ ``task``\ 's label without incrementing its ref count

If \ ``task``\  != current needs to be called in RCU safe critical section

.. _`__aa_task_is_confined`:

\__aa_task_is_confined
======================

.. c:function:: bool __aa_task_is_confined(struct task_struct *task)

    determine if \ ``task``\  has any confinement

    :param struct task_struct \*task:
        task to check confinement of  (NOT NULL)

.. _`__aa_task_is_confined.description`:

Description
-----------

If \ ``task``\  != current needs to be called in RCU safe critical section

.. _`aa_current_raw_label`:

aa_current_raw_label
====================

.. c:function:: struct aa_label *aa_current_raw_label( void)

    find the current tasks confining label

    :param  void:
        no arguments

.. _`aa_current_raw_label.return`:

Return
------

up to date confining label or the ns unconfined label (NOT NULL)

This fn will not update the tasks cred to the most up to date version
of the label so it is safe to call when inside of locks.

.. _`aa_get_current_label`:

aa_get_current_label
====================

.. c:function:: struct aa_label *aa_get_current_label( void)

    get the newest version of the current tasks label

    :param  void:
        no arguments

.. _`aa_get_current_label.return`:

Return
------

newest version of confining label (NOT NULL)

This fn will not update the tasks cred, so it is safe inside of locks

The returned reference must be put with \ :c:func:`aa_put_label`\ 

.. _`end_current_label_crit_section`:

end_current_label_crit_section
==============================

.. c:function:: void end_current_label_crit_section(struct aa_label *label)

    put a reference found with begin_current_label..

    :param struct aa_label \*label:
        label reference to put

.. _`end_current_label_crit_section.description`:

Description
-----------

Should only be used with a reference obtained with
begin_current_label_crit_section and never used in situations where the
task cred may be updated

.. _`__begin_current_label_crit_section`:

\__begin_current_label_crit_section
===================================

.. c:function:: struct aa_label *__begin_current_label_crit_section( void)

    current's confining label

    :param  void:
        no arguments

.. _`__begin_current_label_crit_section.return`:

Return
------

up to date confining label or the ns unconfined label (NOT NULL)

safe to call inside locks

The returned reference must be put with \__end_current_label_crit_section()
This must NOT be used if the task cred could be updated within the
critical section between \__begin_current_label_crit_section() ..
\__end_current_label_crit_section()

.. _`begin_current_label_crit_section`:

begin_current_label_crit_section
================================

.. c:function:: struct aa_label *begin_current_label_crit_section( void)

    current's confining label and update it

    :param  void:
        no arguments

.. _`begin_current_label_crit_section.return`:

Return
------

up to date confining label or the ns unconfined label (NOT NULL)

Not safe to call inside locks

The returned reference must be put with \ :c:func:`end_current_label_crit_section`\ 
This must NOT be used if the task cred could be updated within the
critical section between \ :c:func:`begin_current_label_crit_section`\  ..
\ :c:func:`end_current_label_crit_section`\ 

.. _`aa_clear_task_ctx_trans`:

aa_clear_task_ctx_trans
=======================

.. c:function:: void aa_clear_task_ctx_trans(struct aa_task_ctx *ctx)

    clear transition tracking info from the ctx

    :param struct aa_task_ctx \*ctx:
        task context to clear (NOT NULL)

.. This file was automatic generated / don't edit.


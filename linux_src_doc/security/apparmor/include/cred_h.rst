.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/cred.h

.. _`aa_cred_raw_label`:

aa_cred_raw_label
=================

.. c:function:: struct aa_label *aa_cred_raw_label(const struct cred *cred)

    obtain cred's label

    :param cred:
        cred to obtain label from  (NOT NULL)
    :type cred: const struct cred \*

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

    :param cred:
        cred to obtain label from (NOT NULL)
    :type cred: const struct cred \*

.. _`aa_get_newest_cred_label.return`:

Return
------

newest version of confining label

.. _`__aa_task_raw_label`:

\__aa_task_raw_label
====================

.. c:function:: struct aa_label *__aa_task_raw_label(struct task_struct *task)

    retrieve another task's label

    :param task:
        task to query  (NOT NULL)
    :type task: struct task_struct \*

.. _`__aa_task_raw_label.return`:

Return
------

\ ``task``\ 's label without incrementing its ref count

If \ ``task``\  != current needs to be called in RCU safe critical section

.. _`aa_current_raw_label`:

aa_current_raw_label
====================

.. c:function:: struct aa_label *aa_current_raw_label( void)

    find the current tasks confining label

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

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

    :param label:
        label reference to put
    :type label: struct aa_label \*

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

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

.. _`begin_current_label_crit_section.return`:

Return
------

up to date confining label or the ns unconfined label (NOT NULL)

Not safe to call inside locks

The returned reference must be put with \ :c:func:`end_current_label_crit_section`\ 
This must NOT be used if the task cred could be updated within the
critical section between \ :c:func:`begin_current_label_crit_section`\  ..
\ :c:func:`end_current_label_crit_section`\ 

.. This file was automatic generated / don't edit.


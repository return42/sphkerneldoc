.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/task.c

.. _`aa_get_task_label`:

aa_get_task_label
=================

.. c:function:: struct aa_label *aa_get_task_label(struct task_struct *task)

    Get another task's label

    :param task:
        task to query  (NOT NULL)
    :type task: struct task_struct \*

.. _`aa_get_task_label.return`:

Return
------

counted reference to \ ``task``\ 's label

.. _`aa_replace_current_label`:

aa_replace_current_label
========================

.. c:function:: int aa_replace_current_label(struct aa_label *label)

    replace the current tasks label

    :param label:
        new label  (NOT NULL)
    :type label: struct aa_label \*

.. _`aa_replace_current_label.return`:

Return
------

0 or error on failure

.. _`aa_set_current_onexec`:

aa_set_current_onexec
=====================

.. c:function:: int aa_set_current_onexec(struct aa_label *label, bool stack)

    set the tasks change_profile to happen onexec

    :param label:
        system label to set at exec  (MAYBE NULL to clear value)
    :type label: struct aa_label \*

    :param stack:
        whether stacking should be done
    :type stack: bool

.. _`aa_set_current_onexec.return`:

Return
------

0 or error on failure

.. _`aa_set_current_hat`:

aa_set_current_hat
==================

.. c:function:: int aa_set_current_hat(struct aa_label *label, u64 token)

    set the current tasks hat

    :param label:
        label to set as the current hat  (NOT NULL)
    :type label: struct aa_label \*

    :param token:
        token value that must be specified to change from the hat
    :type token: u64

.. _`aa_set_current_hat.description`:

Description
-----------

Do switch of tasks hat.  If the task is currently in a hat
validate the token to match.

.. _`aa_set_current_hat.return`:

Return
------

0 or error on failure

.. _`aa_restore_previous_label`:

aa_restore_previous_label
=========================

.. c:function:: int aa_restore_previous_label(u64 token)

    exit from hat context restoring previous label

    :param token:
        the token that must be matched to exit hat context
    :type token: u64

.. _`aa_restore_previous_label.description`:

Description
-----------

Attempt to return out of a hat to the previous label.  The token
must match the stored token value.

.. _`aa_restore_previous_label.return`:

Return
------

0 or error of failure

.. This file was automatic generated / don't edit.


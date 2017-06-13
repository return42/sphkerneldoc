.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/context.c

.. _`aa_alloc_task_context`:

aa_alloc_task_context
=====================

.. c:function:: struct aa_task_ctx *aa_alloc_task_context(gfp_t flags)

    allocate a new task_ctx

    :param gfp_t flags:
        gfp flags for allocation

.. _`aa_alloc_task_context.return`:

Return
------

allocated buffer or NULL on failure

.. _`aa_free_task_context`:

aa_free_task_context
====================

.. c:function:: void aa_free_task_context(struct aa_task_ctx *ctx)

    free a task_ctx

    :param struct aa_task_ctx \*ctx:
        task_ctx to free (MAYBE NULL)

.. _`aa_dup_task_context`:

aa_dup_task_context
===================

.. c:function:: void aa_dup_task_context(struct aa_task_ctx *new, const struct aa_task_ctx *old)

    duplicate a task context, incrementing reference counts

    :param struct aa_task_ctx \*new:
        a blank task context      (NOT NULL)

    :param const struct aa_task_ctx \*old:
        the task context to copy  (NOT NULL)

.. _`aa_get_task_profile`:

aa_get_task_profile
===================

.. c:function:: struct aa_profile *aa_get_task_profile(struct task_struct *task)

    Get another task's profile

    :param struct task_struct \*task:
        task to query  (NOT NULL)

.. _`aa_get_task_profile.return`:

Return
------

counted reference to \ ``task``\ 's profile

.. _`aa_replace_current_profile`:

aa_replace_current_profile
==========================

.. c:function:: int aa_replace_current_profile(struct aa_profile *profile)

    replace the current tasks profiles

    :param struct aa_profile \*profile:
        new profile  (NOT NULL)

.. _`aa_replace_current_profile.return`:

Return
------

0 or error on failure

.. _`aa_set_current_onexec`:

aa_set_current_onexec
=====================

.. c:function:: int aa_set_current_onexec(struct aa_profile *profile)

    set the tasks change_profile to happen onexec

    :param struct aa_profile \*profile:
        system profile to set at exec  (MAYBE NULL to clear value)

.. _`aa_set_current_onexec.return`:

Return
------

0 or error on failure

.. _`aa_set_current_hat`:

aa_set_current_hat
==================

.. c:function:: int aa_set_current_hat(struct aa_profile *profile, u64 token)

    set the current tasks hat

    :param struct aa_profile \*profile:
        profile to set as the current hat  (NOT NULL)

    :param u64 token:
        token value that must be specified to change from the hat

.. _`aa_set_current_hat.description`:

Description
-----------

Do switch of tasks hat.  If the task is currently in a hat
validate the token to match.

.. _`aa_set_current_hat.return`:

Return
------

0 or error on failure

.. _`aa_restore_previous_profile`:

aa_restore_previous_profile
===========================

.. c:function:: int aa_restore_previous_profile(u64 token)

    exit from hat context restoring the profile

    :param u64 token:
        the token that must be matched to exit hat context

.. _`aa_restore_previous_profile.description`:

Description
-----------

Attempt to return out of a hat to the previous profile.  The token
must match the stored token value.

.. _`aa_restore_previous_profile.return`:

Return
------

0 or error of failure

.. This file was automatic generated / don't edit.


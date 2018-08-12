.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/task.h

.. _`aa_alloc_task_ctx`:

aa_alloc_task_ctx
=================

.. c:function:: struct aa_task_ctx *aa_alloc_task_ctx(gfp_t flags)

    allocate a new task_ctx

    :param gfp_t flags:
        gfp flags for allocation

.. _`aa_alloc_task_ctx.return`:

Return
------

allocated buffer or NULL on failure

.. _`aa_free_task_ctx`:

aa_free_task_ctx
================

.. c:function:: void aa_free_task_ctx(struct aa_task_ctx *ctx)

    free a task_ctx

    :param struct aa_task_ctx \*ctx:
        task_ctx to free (MAYBE NULL)

.. _`aa_dup_task_ctx`:

aa_dup_task_ctx
===============

.. c:function:: void aa_dup_task_ctx(struct aa_task_ctx *new, const struct aa_task_ctx *old)

    duplicate a task context, incrementing reference counts

    :param struct aa_task_ctx \*new:
        a blank task context      (NOT NULL)

    :param const struct aa_task_ctx \*old:
        the task context to copy  (NOT NULL)

.. _`aa_clear_task_ctx_trans`:

aa_clear_task_ctx_trans
=======================

.. c:function:: void aa_clear_task_ctx_trans(struct aa_task_ctx *ctx)

    clear transition tracking info from the ctx

    :param struct aa_task_ctx \*ctx:
        task context to clear (NOT NULL)

.. This file was automatic generated / don't edit.


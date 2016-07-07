.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/stackdepot.c

.. _`depot_save_stack`:

depot_save_stack
================

.. c:function:: depot_stack_handle_t depot_save_stack(struct stack_trace *trace, gfp_t alloc_flags)

    save stack in a stack depot. \ ``trace``\  - the stacktrace to save. \ ``alloc_flags``\  - flags for allocating additional memory if required.

    :param struct stack_trace \*trace:
        *undescribed*

    :param gfp_t alloc_flags:
        *undescribed*

.. _`depot_save_stack.description`:

Description
-----------

Returns the handle of the stack struct stored in depot.

.. This file was automatic generated / don't edit.


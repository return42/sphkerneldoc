.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blktrace_api.h

.. _`blk_add_cgroup_trace_msg`:

blk_add_cgroup_trace_msg
========================

.. c:function::  blk_add_cgroup_trace_msg( q,  cg,  fmt,  ...)

    Add a (simple) message to the blktrace stream

    :param q:
        queue the io is for
    :type q: 

    :param cg:
        *undescribed*
    :type cg: 

    :param fmt:
        format to print message in
        args...      Variable argument list for format
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`blk_add_cgroup_trace_msg.description`:

Description
-----------

Records a (simple) message onto the blktrace stream.

.. _`blk_add_cgroup_trace_msg.note`:

NOTE
----

BLK_TN_MAX_MSG characters are output at most.

Can not use 'static inline' due to presence of var args...

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

==============
blktrace_api.h
==============


.. _`blk_add_trace_msg`:

blk_add_trace_msg
=================

.. c:function:: blk_add_trace_msg ( q,  fmt,  ...)

    Add a (simple) message to the blktrace stream

    :param q:
        queue the io is for

    :param fmt:
        format to print message in
        args...        Variable argument list for format

    :param ...:
        variable arguments



.. _`blk_add_trace_msg.description`:

Description
-----------

Records a (simple) message onto the blktrace stream.



.. _`blk_add_trace_msg.note`:

NOTE
----

Can not use 'static inline' due to presence of var args...



.. _`blk_add_trace_msg.note`:

NOTE
----

Can not use 'static inline' due to presence of var args...


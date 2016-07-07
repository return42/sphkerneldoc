.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/thread-stack.h

.. _`call_return`:

struct call_return
==================

.. c:type:: struct call_return

    paired call/return information.

.. _`call_return.definition`:

Definition
----------

.. code-block:: c

    struct call_return {
        struct thread *thread;
        struct comm *comm;
        struct call_path *cp;
        u64 call_time;
        u64 return_time;
        u64 branch_count;
        u64 call_ref;
        u64 return_ref;
        u64 db_id;
        u32 flags;
    }

.. _`call_return.members`:

Members
-------

thread
    thread in which call/return occurred

comm
    comm in which call/return occurred

cp
    call path

call_time
    timestamp of call (if known)

return_time
    timestamp of return (if known)

branch_count
    number of branches seen between call and return

call_ref
    external reference to 'call' sample (e.g. db_id)

return_ref
    external reference to 'return' sample (e.g. db_id)

db_id
    id used for db-export

flags
    Call/Return flags

.. _`call_return_processor`:

struct call_return_processor
============================

.. c:type:: struct call_return_processor

    provides a call-back to consume call-return information.

.. _`call_return_processor.definition`:

Definition
----------

.. code-block:: c

    struct call_return_processor {
        struct call_path_root *cpr;
        int (* process) (struct call_return *cr, void *data);
        void *data;
    }

.. _`call_return_processor.members`:

Members
-------

cpr
    call path root

process
    call-back that accepts call/return information

data
    anonymous data for call-back

.. This file was automatic generated / don't edit.


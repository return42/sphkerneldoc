.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/thread-stack.c

.. _`thread_stack_entry`:

struct thread_stack_entry
=========================

.. c:type:: struct thread_stack_entry

    thread stack entry.

.. _`thread_stack_entry.definition`:

Definition
----------

.. code-block:: c

    struct thread_stack_entry {
        u64 ret_addr;
        u64 timestamp;
        u64 ref;
        u64 branch_count;
        struct call_path *cp;
        bool no_call;
        bool trace_end;
    }

.. _`thread_stack_entry.members`:

Members
-------

ret_addr
    return address

timestamp
    timestamp (if known)

ref
    external reference (e.g. db_id of sample)

branch_count
    the branch count when the entry was created

cp
    call path

no_call
    a 'call' was not seen

trace_end
    a 'call' but trace ended

.. _`thread_stack`:

struct thread_stack
===================

.. c:type:: struct thread_stack

    thread stack constructed from 'call' and 'return' branch samples.

.. _`thread_stack.definition`:

Definition
----------

.. code-block:: c

    struct thread_stack {
        struct thread_stack_entry *stack;
        size_t cnt;
        size_t sz;
        u64 trace_nr;
        u64 branch_count;
        u64 kernel_start;
        u64 last_time;
        struct call_return_processor *crp;
        struct comm *comm;
    }

.. _`thread_stack.members`:

Members
-------

stack
    array that holds the stack

cnt
    number of entries in the stack

sz
    current maximum stack size

trace_nr
    current trace number

branch_count
    running branch count

kernel_start
    kernel start address

last_time
    last timestamp

crp
    call/return processor

comm
    current comm

.. This file was automatic generated / don't edit.


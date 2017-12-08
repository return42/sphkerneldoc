.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/bpf_trace.c

.. _`trace_call_bpf`:

trace_call_bpf
==============

.. c:function:: unsigned int trace_call_bpf(struct trace_event_call *call, void *ctx)

    invoke BPF program

    :param struct trace_event_call \*call:
        tracepoint event

    :param void \*ctx:
        opaque context pointer

.. _`trace_call_bpf.description`:

Description
-----------

kprobe handlers execute BPF programs via this helper.
Can be used from static tracepoints in the future.

.. _`trace_call_bpf.return`:

Return
------

BPF programs always return an integer which is interpreted by

.. _`trace_call_bpf.kprobe-handler-as`:

kprobe handler as
-----------------

0 - return from kprobe (event is filtered out)
1 - store kprobe event into ring buffer
Other values are reserved and currently alias to 1

.. This file was automatic generated / don't edit.


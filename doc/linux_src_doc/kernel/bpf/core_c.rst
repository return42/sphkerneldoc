.. -*- coding: utf-8; mode: rst -*-

======
core.c
======


.. _`__bpf_prog_run`:

__bpf_prog_run
==============

.. c:function:: unsigned int __bpf_prog_run (void *ctx, const struct bpf_insn *insn)

    run eBPF program on a given context

    :param void \*ctx:
        is the data we are operating on

    :param const struct bpf_insn \*insn:
        is the array of eBPF instructions



.. _`__bpf_prog_run.description`:

Description
-----------

Decode and execute eBPF instructions.



.. _`bpf_prog_select_runtime`:

bpf_prog_select_runtime
=======================

.. c:function:: int bpf_prog_select_runtime (struct bpf_prog *fp)

    select exec runtime for BPF program

    :param struct bpf_prog \*fp:
        bpf_prog populated with internal BPF program



.. _`bpf_prog_select_runtime.description`:

Description
-----------

Try to JIT eBPF program, if JIT is not available, use interpreter.
The BPF program will be executed via :c:func:`BPF_PROG_RUN` macro.


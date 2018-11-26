.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/bpf/core.c

.. _`___bpf_prog_run`:

\___bpf_prog_run
================

.. c:function:: u64 ___bpf_prog_run(u64 *regs, const struct bpf_insn *insn, u64 *stack)

    run eBPF program on a given context

    :param regs:
        *undescribed*
    :type regs: u64 \*

    :param insn:
        is the array of eBPF instructions
    :type insn: const struct bpf_insn \*

    :param stack:
        *undescribed*
    :type stack: u64 \*

.. _`___bpf_prog_run.description`:

Description
-----------

Decode and execute eBPF instructions.

.. _`bpf_prog_select_runtime`:

bpf_prog_select_runtime
=======================

.. c:function:: struct bpf_prog *bpf_prog_select_runtime(struct bpf_prog *fp, int *err)

    select exec runtime for BPF program

    :param fp:
        bpf_prog populated with internal BPF program
    :type fp: struct bpf_prog \*

    :param err:
        pointer to error variable
    :type err: int \*

.. _`bpf_prog_select_runtime.description`:

Description
-----------

Try to JIT eBPF program, if JIT is not available, use interpreter.
The BPF program will be executed via \ :c:func:`BPF_PROG_RUN`\  macro.

.. This file was automatic generated / don't edit.


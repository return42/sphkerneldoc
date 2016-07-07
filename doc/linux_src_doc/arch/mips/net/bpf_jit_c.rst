.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/net/bpf_jit.c

.. _`jit_ctx`:

struct jit_ctx
==============

.. c:type:: struct jit_ctx

    JIT context

.. _`jit_ctx.definition`:

Definition
----------

.. code-block:: c

    struct jit_ctx {
        const struct bpf_prog *skf;
        unsigned int prologue_bytes;
        u32 idx;
        u32 flags;
        u32 *offsets;
        u32 *target;
    }

.. _`jit_ctx.members`:

Members
-------

skf
    The sk_filter

prologue_bytes
    Number of bytes for prologue

idx
    Instruction index

flags
    JIT flags

offsets
    Instruction offsets

target
    Memory location for the compiled filter

.. This file was automatic generated / don't edit.


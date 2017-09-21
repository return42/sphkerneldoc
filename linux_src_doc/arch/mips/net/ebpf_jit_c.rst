.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/net/ebpf_jit.c

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
        int stack_size;
        int tmp_offset;
        u32 idx;
        u32 flags;
        u32 *offsets;
        u32 *target;
        u64 *reg_val_types;
        unsigned int long_b_conversion:1;
        unsigned int gen_b_offsets:1;
        unsigned int use_bbit_insns:1;
    }

.. _`jit_ctx.members`:

Members
-------

skf
    The sk_filter

stack_size
    eBPF stack size

tmp_offset
    eBPF \ ``$sp``\  offset to 8-byte temporary memory

idx
    Instruction index

flags
    JIT flags

offsets
    Instruction offsets

target
    Memory location for the compiled filter
    \ ``reg_val_types``\        Packed enum reg_val_type for each register.

reg_val_types
    *undescribed*

long_b_conversion
    *undescribed*

gen_b_offsets
    *undescribed*

use_bbit_insns
    *undescribed*

.. This file was automatic generated / don't edit.


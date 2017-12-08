.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/bpf/main.h

.. _`nfp_insn_meta`:

struct nfp_insn_meta
====================

.. c:type:: struct nfp_insn_meta

    BPF instruction wrapper

.. _`nfp_insn_meta.definition`:

Definition
----------

.. code-block:: c

    struct nfp_insn_meta {
        struct bpf_insn insn;
        struct bpf_reg_state ptr;
        bool ptr_not_const;
        unsigned int off;
        unsigned short n;
        bool skip;
        instr_cb_t double_cb;
        struct list_head l;
    }

.. _`nfp_insn_meta.members`:

Members
-------

insn
    BPF instruction

ptr
    pointer type for memory operations

ptr_not_const
    pointer is not always constant

off
    index of first generated machine instruction (in nfp_prog.prog)

n
    eBPF instruction number

skip
    skip this instruction (optimized out)

double_cb
    callback for second part of the instruction

l
    link on nfp_prog->insns list

.. _`nfp_prog`:

struct nfp_prog
===============

.. c:type:: struct nfp_prog

    nfp BPF program

.. _`nfp_prog.definition`:

Definition
----------

.. code-block:: c

    struct nfp_prog {
        u64 *prog;
        unsigned int prog_len;
        unsigned int __prog_alloc_len;
        struct nfp_insn_meta *verifier_meta;
        enum bpf_prog_type type;
        unsigned int start_off;
        unsigned int tgt_out;
        unsigned int tgt_abort;
        unsigned int tgt_done;
        unsigned int n_translated;
        int error;
        unsigned int stack_depth;
        struct list_head insns;
    }

.. _`nfp_prog.members`:

Members
-------

prog
    machine code

prog_len
    number of valid instructions in \ ``prog``\  array

__prog_alloc_len
    alloc size of \ ``prog``\  array

verifier_meta
    temporary storage for verifier's insn meta

type
    BPF program type

start_off
    address of the first instruction in the memory

tgt_out
    jump target for normal exit

tgt_abort
    jump target for abort (e.g. access outside of packet buffer)

tgt_done
    jump target to get the next packet

n_translated
    number of successfully translated instructions (for errors)

error
    error code if something went wrong

stack_depth
    max stack depth from the verifier

insns
    list of BPF instruction wrappers (struct nfp_insn_meta)

.. This file was automatic generated / don't edit.


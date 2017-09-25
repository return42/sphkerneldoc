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
        enum nfp_bpf_action_type act;
        unsigned int num_regs;
        unsigned int regs_per_thread;
        unsigned int start_off;
        unsigned int tgt_out;
        unsigned int tgt_abort;
        unsigned int tgt_done;
        unsigned int n_translated;
        int error;
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

act
    BPF program/action type (TC DA, TC with action, XDP etc.)

num_regs
    number of registers used by this program

regs_per_thread
    number of basic registers allocated per thread

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

insns
    list of BPF instruction wrappers (struct nfp_insn_meta)

.. _`nfp_net_bpf_priv`:

struct nfp_net_bpf_priv
=======================

.. c:type:: struct nfp_net_bpf_priv

    per-vNIC BPF private data

.. _`nfp_net_bpf_priv.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_bpf_priv {
        struct nfp_stat_pair rx_filter, rx_filter_prev;
        unsigned long rx_filter_change;
        struct timer_list rx_filter_stats_timer;
        spinlock_t rx_filter_lock;
    }

.. _`nfp_net_bpf_priv.members`:

Members
-------

rx_filter
    Filter offload statistics - dropped packets/bytes

rx_filter_prev
    Filter offload statistics - values from previous update

rx_filter_change
    Jiffies when statistics last changed

rx_filter_stats_timer
    Timer for polling filter offload statistics

rx_filter_lock
    Lock protecting timer state changes (teardown)

.. This file was automatic generated / don't edit.


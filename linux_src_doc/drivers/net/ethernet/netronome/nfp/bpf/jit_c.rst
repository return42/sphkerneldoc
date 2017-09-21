.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/bpf/jit.c

.. _`nfp_bpf_jit`:

nfp_bpf_jit
===========

.. c:function:: int nfp_bpf_jit(struct bpf_prog *filter, void *prog_mem, enum nfp_bpf_action_type act, unsigned int prog_start, unsigned int prog_done, unsigned int prog_sz, struct nfp_bpf_result *res)

    translate BPF code into NFP assembly

    :param struct bpf_prog \*filter:
        kernel BPF filter struct

    :param void \*prog_mem:
        memory to store assembler instructions

    :param enum nfp_bpf_action_type act:
        action attached to this eBPF program

    :param unsigned int prog_start:
        offset of the first instruction when loaded

    :param unsigned int prog_done:
        where to jump on exit

    :param unsigned int prog_sz:
        size of \ ``prog_mem``\  in instructions

    :param struct nfp_bpf_result \*res:
        achieved parameters of translation results

.. This file was automatic generated / don't edit.


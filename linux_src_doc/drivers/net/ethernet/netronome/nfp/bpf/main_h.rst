.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/bpf/main.h

.. _`nfp_app_bpf`:

struct nfp_app_bpf
==================

.. c:type:: struct nfp_app_bpf

    bpf app priv structure

.. _`nfp_app_bpf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_app_bpf {
        struct nfp_app *app;
        struct bpf_offload_dev *bpf_dev;
        DECLARE_BITMAP(tag_allocator, U16_MAX + 1);
        u16 tag_alloc_next;
        u16 tag_alloc_last;
        struct sk_buff_head cmsg_replies;
        struct wait_queue_head cmsg_wq;
        unsigned int cmsg_key_sz;
        unsigned int cmsg_val_sz;
        struct list_head map_list;
        unsigned int maps_in_use;
        unsigned int map_elems_in_use;
        struct rhashtable maps_neutral;
        u32 abi_version;
        struct nfp_bpf_cap_adjust_head {
            u32 flags;
            int off_min;
            int off_max;
            int guaranteed_sub;
            int guaranteed_add;
        } adjust_head;
        struct {
            u32 types;
            u32 max_maps;
            u32 max_elems;
            u32 max_key_sz;
            u32 max_val_sz;
            u32 max_elem_sz;
        } maps;
        struct {
            u32 map_lookup;
            u32 map_update;
            u32 map_delete;
            u32 perf_event_output;
        } helpers;
        bool pseudo_random;
        bool queue_select;
        bool adjust_tail;
    }

.. _`nfp_app_bpf.members`:

Members
-------

app
    backpointer to the app

bpf_dev
    BPF offload device handle

tag_allocator
    bitmap of control message tags in use

tag_alloc_next
    next tag bit to allocate

tag_alloc_last
    next tag bit to be freed

cmsg_replies
    received cmsg replies waiting to be consumed

cmsg_wq
    work queue for waiting for cmsg replies

cmsg_key_sz
    size of key in cmsg element array

cmsg_val_sz
    size of value in cmsg element array

map_list
    list of offloaded maps

maps_in_use
    number of currently offloaded maps

map_elems_in_use
    number of elements allocated to offloaded maps

maps_neutral
    hash table of offload-neutral maps (on pointer)

abi_version
    global BPF ABI version

adjust_head
    adjust head capability

adjust_head.flags
    extra flags for adjust head

adjust_head.off_min
    minimal packet offset within buffer required

adjust_head.off_max
    maximum packet offset within buffer required

adjust_head.guaranteed_sub
    negative adjustment guaranteed possible

adjust_head.guaranteed_add
    positive adjustment guaranteed possible

maps
    map capability

maps.types
    supported map types

maps.max_maps
    max number of maps supported

maps.max_elems
    max number of entries in each map

maps.max_key_sz
    max size of map key

maps.max_val_sz
    max size of map value

maps.max_elem_sz
    max size of map entry (key + value)

helpers
    helper addressess for various calls

helpers.map_lookup
    map lookup helper address

helpers.map_update
    map update helper address

helpers.map_delete
    map delete helper address

helpers.perf_event_output
    output perf event to a ring buffer

pseudo_random
    FW initialized the pseudo-random machinery (CSRs)

queue_select
    BPF can set the RX queue ID in packet vector

adjust_tail
    BPF can simply trunc packet size for adjust tail

.. _`nfp_bpf_map`:

struct nfp_bpf_map
==================

.. c:type:: struct nfp_bpf_map

    private per-map data attached to BPF maps for offload

.. _`nfp_bpf_map.definition`:

Definition
----------

.. code-block:: c

    struct nfp_bpf_map {
        struct bpf_offloaded_map *offmap;
        struct nfp_app_bpf *bpf;
        u32 tid;
        struct list_head l;
        struct nfp_bpf_map_word use_map[];
    }

.. _`nfp_bpf_map.members`:

Members
-------

offmap
    pointer to the offloaded BPF map

bpf
    back pointer to bpf app private structure

tid
    table id identifying map on datapath

l
    link on the nfp_app_bpf->map_list list

use_map
    map of how the value is used (in 4B chunks)

.. _`nfp_bpf_reg_state`:

struct nfp_bpf_reg_state
========================

.. c:type:: struct nfp_bpf_reg_state

    register state for calls

.. _`nfp_bpf_reg_state.definition`:

Definition
----------

.. code-block:: c

    struct nfp_bpf_reg_state {
        struct bpf_reg_state reg;
        bool var_off;
    }

.. _`nfp_bpf_reg_state.members`:

Members
-------

reg
    BPF register state from latest path

var_off
    for stack arg - changes stack offset on different paths

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
        union {
            struct {
                struct bpf_reg_state ptr;
                struct bpf_insn *paired_st;
                s16 ldst_gather_len;
                bool ptr_not_const;
                struct {
                    s16 range_start;
                    s16 range_end;
                    bool do_init;
                } pkt_cache;
                bool xadd_over_16bit;
                bool xadd_maybe_16bit;
            } ;
            struct {
                struct nfp_insn_meta *jmp_dst;
                bool jump_neg_op;
                u32 num_insns_after_br;
            } ;
            struct {
                u32 func_id;
                struct bpf_reg_state arg1;
                struct nfp_bpf_reg_state arg2;
            } ;
            struct {
                u64 umin_src;
                u64 umax_src;
                u64 umin_dst;
                u64 umax_dst;
            } ;
        } ;
        unsigned int off;
        unsigned short n;
        unsigned short flags;
        unsigned short subprog_idx;
        bool skip;
        instr_cb_t double_cb;
        struct list_head l;
    }

.. _`nfp_insn_meta.members`:

Members
-------

insn
    BPF instruction

{unnamed_union}
    anonymous

{unnamed_struct}
    anonymous

ptr
    pointer type for memory operations

paired_st
    the paired store insn at the head of the sequence

ldst_gather_len
    memcpy length gathered from load/store sequence

ptr_not_const
    pointer is not always constant

pkt_cache
    packet data cache information

pkt_cache.range_start
    start offset for associated packet data cache

pkt_cache.range_end
    end offset for associated packet data cache

pkt_cache.do_init
    this read needs to initialize packet data cache

xadd_over_16bit
    16bit immediate is not guaranteed

xadd_maybe_16bit
    16bit immediate is possible

{unnamed_struct}
    anonymous

jmp_dst
    destination info for jump instructions

jump_neg_op
    jump instruction has inverted immediate, use ADD instead of SUB

num_insns_after_br
    number of insns following a branch jump, used for fixup

{unnamed_struct}
    anonymous

func_id
    function id for call instructions

arg1
    arg1 for call instructions

arg2
    arg2 for call instructions

{unnamed_struct}
    anonymous

umin_src
    copy of core verifier umin_value for src opearnd.

umax_src
    copy of core verifier umax_value for src operand.

umin_dst
    copy of core verifier umin_value for dst opearnd.

umax_dst
    copy of core verifier umax_value for dst operand.

off
    index of first generated machine instruction (in nfp_prog.prog)

n
    eBPF instruction number

flags
    eBPF instruction extra optimization flags

subprog_idx
    index of subprogram to which the instruction belongs

skip
    skip this instruction (optimized out)

double_cb
    callback for second part of the instruction

l
    link on nfp_prog->insns list

.. _`nfp_bpf_subprog_info`:

struct nfp_bpf_subprog_info
===========================

.. c:type:: struct nfp_bpf_subprog_info

    nfp BPF sub-program (a.k.a. function) info

.. _`nfp_bpf_subprog_info.definition`:

Definition
----------

.. code-block:: c

    struct nfp_bpf_subprog_info {
        u16 stack_depth;
        u8 needs_reg_push : 1;
    }

.. _`nfp_bpf_subprog_info.members`:

Members
-------

stack_depth
    maximum stack depth used by this sub-program

needs_reg_push
    whether sub-program uses callee-saved registers

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
        struct nfp_app_bpf *bpf;
        u64 *prog;
        unsigned int prog_len;
        unsigned int __prog_alloc_len;
        unsigned int stack_size;
        struct nfp_insn_meta *verifier_meta;
        enum bpf_prog_type type;
        unsigned int last_bpf_off;
        unsigned int tgt_out;
        unsigned int tgt_abort;
        unsigned int tgt_call_push_regs;
        unsigned int tgt_call_pop_regs;
        unsigned int n_translated;
        int error;
        unsigned int stack_frame_depth;
        unsigned int adjust_head_location;
        unsigned int map_records_cnt;
        unsigned int subprog_cnt;
        struct nfp_bpf_neutral_map **map_records;
        struct nfp_bpf_subprog_info *subprog;
        struct list_head insns;
    }

.. _`nfp_prog.members`:

Members
-------

bpf
    backpointer to the bpf app priv structure

prog
    machine code

prog_len
    number of valid instructions in \ ``prog``\  array

\__prog_alloc_len
    alloc size of \ ``prog``\  array

stack_size
    total amount of stack used

verifier_meta
    temporary storage for verifier's insn meta

type
    BPF program type

last_bpf_off
    address of the last instruction translated from BPF

tgt_out
    jump target for normal exit

tgt_abort
    jump target for abort (e.g. access outside of packet buffer)

tgt_call_push_regs
    jump target for subroutine for saving R6~R9 to stack

tgt_call_pop_regs
    jump target for subroutine used for restoring R6~R9

n_translated
    number of successfully translated instructions (for errors)

error
    error code if something went wrong

stack_frame_depth
    max stack depth for current frame

adjust_head_location
    if program has single adjust head call - the insn no.

map_records_cnt
    the number of map pointers recorded for this prog

subprog_cnt
    number of sub-programs, including main function

map_records
    the map record pointers from bpf->maps_neutral

subprog
    pointer to an array of objects holding info about sub-programs

insns
    list of BPF instruction wrappers (struct nfp_insn_meta)

.. _`nfp_bpf_vnic`:

struct nfp_bpf_vnic
===================

.. c:type:: struct nfp_bpf_vnic

    per-vNIC BPF priv structure

.. _`nfp_bpf_vnic.definition`:

Definition
----------

.. code-block:: c

    struct nfp_bpf_vnic {
        struct bpf_prog *tc_prog;
        unsigned int start_off;
        unsigned int tgt_done;
    }

.. _`nfp_bpf_vnic.members`:

Members
-------

tc_prog
    currently loaded cls_bpf program

start_off
    address of the first instruction in the memory

tgt_done
    jump target to get the next packet

.. This file was automatic generated / don't edit.


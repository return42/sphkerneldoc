.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etm4x.h

.. _`etmv4_config`:

struct etmv4_config
===================

.. c:type:: struct etmv4_config

    configuration information related to an ETMv4

.. _`etmv4_config.definition`:

Definition
----------

.. code-block:: c

    struct etmv4_config {
        u32 mode;
        u32 pe_sel;
        u32 cfg;
        u32 eventctrl0;
        u32 eventctrl1;
        u32 stall_ctrl;
        u32 ts_ctrl;
        u32 syncfreq;
        u32 ccctlr;
        u32 bb_ctrl;
        u32 vinst_ctrl;
        u32 viiectlr;
        u32 vissctlr;
        u32 vipcssctlr;
        u8 seq_idx;
        u32 seq_ctrl[ETM_MAX_SEQ_STATES];
        u32 seq_rst;
        u32 seq_state;
        u8 cntr_idx;
        u32 cntrldvr[ETMv4_MAX_CNTR];
        u32 cntr_ctrl[ETMv4_MAX_CNTR];
        u32 cntr_val[ETMv4_MAX_CNTR];
        u8 res_idx;
        u32 res_ctrl[ETM_MAX_RES_SEL];
        u32 ss_ctrl[ETM_MAX_SS_CMP];
        u32 ss_status[ETM_MAX_SS_CMP];
        u32 ss_pe_cmp[ETM_MAX_SS_CMP];
        u8 addr_idx;
        u64 addr_val[ETM_MAX_SINGLE_ADDR_CMP];
        u64 addr_acc[ETM_MAX_SINGLE_ADDR_CMP];
        u8 addr_type[ETM_MAX_SINGLE_ADDR_CMP];
        u8 ctxid_idx;
        u64 ctxid_pid[ETMv4_MAX_CTXID_CMP];
        u32 ctxid_mask0;
        u32 ctxid_mask1;
        u8 vmid_idx;
        u64 vmid_val[ETM_MAX_VMID_CMP];
        u32 vmid_mask0;
        u32 vmid_mask1;
        u32 ext_inp;
    }

.. _`etmv4_config.members`:

Members
-------

mode
    Controls various modes supported by this ETM.

pe_sel
    Controls which PE to trace.

cfg
    Controls the tracing options.

eventctrl0
    Controls the tracing of arbitrary events.

eventctrl1
    Controls the behavior of the events that \ ``event_ctrl0``\  selects.

stall_ctrl
    *undescribed*

ts_ctrl
    Controls the insertion of global timestamps in the
    trace streams.

syncfreq
    Controls how often trace synchronization requests occur.
    the TRCCCCTLR register.

ccctlr
    Sets the threshold value for cycle counting.

bb_ctrl
    *undescribed*

vinst_ctrl
    Controls instruction trace filtering.

viiectlr
    Set or read, the address range comparators.

vissctlr
    Set, or read, the single address comparators that control the
    ViewInst start-stop logic.

vipcssctlr
    Set, or read, which PE comparator inputs can control the
    ViewInst start-stop logic.

seq_idx
    Sequencor index selector.

seq_ctrl
    Control for the sequencer state transition control register.

seq_rst
    Moves the sequencer to state 0 when a programmed event occurs.

seq_state
    Set, or read the sequencer state.

cntr_idx
    Counter index seletor.

cntrldvr
    Sets or returns the reload count value for a counter.

cntr_ctrl
    Controls the operation of a counter.

cntr_val
    Sets or returns the value for a counter.

res_idx
    Resource index selector.

res_ctrl
    Controls the selection of the resources in the trace unit.

ss_ctrl
    Controls the corresponding single-shot comparator resource.

ss_status
    The status of the corresponding single-shot comparator.

ss_pe_cmp
    Selects the PE comparator inputs for Single-shot control.

addr_idx
    Address comparator index selector.

addr_val
    Value for address comparator.

addr_acc
    Address comparator access type.

addr_type
    Current status of the comparator register.

ctxid_idx
    Context ID index selector.

ctxid_pid
    Value of the context ID comparator.

ctxid_mask0
    Context ID comparator mask for comparator 0-3.

ctxid_mask1
    Context ID comparator mask for comparator 4-7.

vmid_idx
    VM ID index selector.

vmid_val
    Value of the VM ID comparator.

vmid_mask0
    VM ID comparator mask for comparator 0-3.

vmid_mask1
    VM ID comparator mask for comparator 4-7.

ext_inp
    External input selection.

.. _`etmv4_drvdata`:

struct etmv4_drvdata
====================

.. c:type:: struct etmv4_drvdata

    specifics associated to an ETM component

.. _`etmv4_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct etmv4_drvdata {
        void __iomem *base;
        struct device *dev;
        struct coresight_device *csdev;
        spinlock_t spinlock;
        local_t mode;
        int cpu;
        u8 arch;
        u8 nr_pe;
        u8 nr_pe_cmp;
        u8 nr_addr_cmp;
        u8 nr_cntr;
        u8 nr_ext_inp;
        u8 numcidc;
        u8 numvmidc;
        u8 nrseqstate;
        u8 nr_event;
        u8 nr_resource;
        u8 nr_ss_cmp;
        u8 trcid;
        u8 trcid_size;
        u8 ts_size;
        u8 ctxid_size;
        u8 vmid_size;
        u8 ccsize;
        u8 ccitmin;
        u8 s_ex_level;
        u8 ns_ex_level;
        u8 q_support;
        bool sticky_enable;
        bool boot_enable;
        bool os_unlock;
        bool instrp0;
        bool trcbb;
        bool trccond;
        bool retstack;
        bool trccci;
        bool trc_error;
        bool syncpr;
        bool stallctl;
        bool sysstall;
        bool nooverflow;
        bool atbtrig;
        bool lpoverride;
        struct etmv4_config config;
    }

.. _`etmv4_drvdata.members`:

Members
-------

base
    Memory mapped base address for this component.

dev
    The device entity associated to this component.

csdev
    Component vitals needed by the framework.

spinlock
    Only one at a time pls.

mode
    This tracer's mode, i.e sysFS, Perf or disabled.

cpu
    The cpu this component is affined to.

arch
    ETM version number.

nr_pe
    The number of processing entity available for tracing.

nr_pe_cmp
    The number of processing entity comparator inputs that are
    available for tracing.

nr_addr_cmp
    Number of pairs of address comparators available
    as found in ETMIDR4 0-3.

nr_cntr
    Number of counters as found in ETMIDR5 bit 28-30.

nr_ext_inp
    Number of external input.

numcidc
    Number of contextID comparators.

numvmidc
    Number of VMID comparators.

nrseqstate
    The number of sequencer states that are implemented.

nr_event
    Indicates how many events the trace unit support.

nr_resource
    The number of resource selection pairs available for tracing.

nr_ss_cmp
    Number of single-shot comparator controls that are available.

trcid
    value of the current ID for this component.

trcid_size
    Indicates the trace ID width.

ts_size
    Global timestamp size field.

ctxid_size
    Size of the context ID field to consider.

vmid_size
    Size of the VM ID comparator to consider.

ccsize
    Indicates the size of the cycle counter in bits.

ccitmin
    minimum value that can be programmed in

s_ex_level
    In secure state, indicates whether instruction tracing is
    supported for the corresponding Exception level.

ns_ex_level
    In non-secure state, indicates whether instruction tracing is
    supported for the corresponding Exception level.

q_support
    Q element support characteristics.

sticky_enable
    true if ETM base configuration has been done.

boot_enable
    True if we should start tracing at boot time.

os_unlock
    True if access to management registers is allowed.

instrp0
    Tracing of load and store instructions
    as P0 elements is supported.

trcbb
    Indicates if the trace unit supports branch broadcast tracing.

trccond
    If the trace unit supports conditional
    instruction tracing.

retstack
    Indicates if the implementation supports a return stack.

trccci
    Indicates if the trace unit supports cycle counting
    for instruction.

trc_error
    Whether a trace unit can trace a system
    error exception.

syncpr
    Indicates if an implementation has a fixed
    synchronization period.

stallctl
    *undescribed*

sysstall
    Does the system support stall control of the PE?

nooverflow
    Indicate if overflow prevention is supported.

atbtrig
    If the implementation can support ATB triggers

lpoverride
    If the implementation can support low-power state over.

config
    structure holding configuration parameters.

.. This file was automatic generated / don't edit.


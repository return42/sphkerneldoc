.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etm.h

.. _`etm_config`:

struct etm_config
=================

.. c:type:: struct etm_config

    configuration information related to an ETM

.. _`etm_config.definition`:

Definition
----------

.. code-block:: c

    struct etm_config {
        u32 mode;
        u32 ctrl;
        u32 trigger_event;
        u32 startstop_ctrl;
        u32 enable_event;
        u32 enable_ctrl1;
        u32 enable_ctrl2;
        u32 fifofull_level;
        u8 addr_idx;
        u32 addr_val[ETM_MAX_ADDR_CMP];
        u32 addr_acctype[ETM_MAX_ADDR_CMP];
        u32 addr_type[ETM_MAX_ADDR_CMP];
        u8 cntr_idx;
        u32 cntr_rld_val[ETM_MAX_CNTR];
        u32 cntr_event[ETM_MAX_CNTR];
        u32 cntr_rld_event[ETM_MAX_CNTR];
        u32 cntr_val[ETM_MAX_CNTR];
        u32 seq_12_event;
        u32 seq_21_event;
        u32 seq_23_event;
        u32 seq_31_event;
        u32 seq_32_event;
        u32 seq_13_event;
        u32 seq_curr_state;
        u8 ctxid_idx;
        u32 ctxid_pid[ETM_MAX_CTXID_CMP];
        u32 ctxid_mask;
        u32 sync_freq;
        u32 timestamp_event;
    }

.. _`etm_config.members`:

Members
-------

mode
    controls various modes supported by this ETM/PTM.

ctrl
    used in conjunction with \ ``mode``\ .

trigger_event
    setting for register ETMTRIGGER.

startstop_ctrl
    setting for register ETMTSSCR.

enable_event
    setting for register ETMTEEVR.

enable_ctrl1
    setting for register ETMTECR1.

enable_ctrl2
    setting for register ETMTECR2.

fifofull_level
    setting for register ETMFFLR.

addr_idx
    index for the address comparator selection.

addr_val
    value for address comparator register.

addr_acctype
    access type for address comparator register.

addr_type
    current status of the comparator register.

cntr_idx
    index for the counter register selection.

cntr_rld_val
    reload value of a counter register.

cntr_event
    control for counter enable register.

cntr_rld_event
    value for counter reload event register.

cntr_val
    counter value register.

seq_12_event
    event causing the transition from 1 to 2.

seq_21_event
    event causing the transition from 2 to 1.

seq_23_event
    event causing the transition from 2 to 3.

seq_31_event
    event causing the transition from 3 to 1.

seq_32_event
    event causing the transition from 3 to 2.

seq_13_event
    event causing the transition from 1 to 3.

seq_curr_state
    current value of the sequencer register.

ctxid_idx
    index for the context ID registers.

ctxid_pid
    value for the context ID to trigger on.

ctxid_mask
    mask applicable to all the context IDs.

sync_freq
    Synchronisation frequency.

timestamp_event
    Defines an event that requests the insertion
    of a timestamp into the trace stream.

.. _`etm_drvdata`:

struct etm_drvdata
==================

.. c:type:: struct etm_drvdata

    specifics associated to an ETM component

.. _`etm_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct etm_drvdata {
        void __iomem *base;
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
        spinlock_t spinlock;
        int cpu;
        int port_size;
        u8 arch;
        bool use_cp14;
        local_t mode;
        bool sticky_enable;
        bool boot_enable;
        bool os_unlock;
        u8 nr_addr_cmp;
        u8 nr_cntr;
        u8 nr_ext_inp;
        u8 nr_ext_out;
        u8 nr_ctxid_cmp;
        u32 etmccr;
        u32 etmccer;
        u32 traceid;
        struct etm_config config;
    }

.. _`etm_drvdata.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated to this component.

atclk
    optional clock for the core parts of the ETM.

csdev
    component vitals needed by the framework.

spinlock
    only one at a time pls.

cpu
    the cpu this component is affined to.

port_size
    port size as reported by ETMCR bit 4-6 and 21.

arch
    ETM/PTM version number.

use_cp14
    *undescribed*

mode
    this tracer's mode, i.e sysFS, Perf or disabled.

sticky_enable
    true if ETM base configuration has been done.

boot_enable
    true if we should start tracing at boot time.

os_unlock
    true if access to management registers is allowed.

nr_addr_cmp
    Number of pairs of address comparators as found in ETMCCR.

nr_cntr
    Number of counters as found in ETMCCR bit 13-15.

nr_ext_inp
    Number of external input as found in ETMCCR bit 17-19.

nr_ext_out
    Number of external output as found in ETMCCR bit 20-22.

nr_ctxid_cmp
    Number of contextID comparators as found in ETMCCR bit 24-25.

etmccr
    value of register ETMCCR.

etmccer
    value of register ETMCCER.

traceid
    value of the current ID for this component.

config
    structure holding configuration parameters.

.. This file was automatic generated / don't edit.


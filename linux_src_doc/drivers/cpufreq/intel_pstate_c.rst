.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/intel_pstate.c

.. _`sample`:

struct sample
=============

.. c:type:: struct sample

    Store performance sample

.. _`sample.definition`:

Definition
----------

.. code-block:: c

    struct sample {
        int32_t core_avg_perf;
        int32_t busy_scaled;
        u64 aperf;
        u64 mperf;
        u64 tsc;
        u64 time;
    }

.. _`sample.members`:

Members
-------

core_avg_perf
    Ratio of APERF/MPERF which is the actual average
    performance during last sample period

busy_scaled
    Scaled busy value which is used to calculate next
    P state. This can be different than core_avg_perf
    to account for cpu idle period

aperf
    Difference of actual performance frequency clock count
    read from APERF MSR between last and current sample

mperf
    Difference of maximum performance frequency clock count
    read from MPERF MSR between last and current sample

tsc
    Difference of time stamp counter between last and
    current sample

time
    Current time from scheduler

.. _`sample.description`:

Description
-----------

This structure is used in the cpudata structure to store performance sample
data for choosing next P State.

.. _`pstate_data`:

struct pstate_data
==================

.. c:type:: struct pstate_data

    Store P state data

.. _`pstate_data.definition`:

Definition
----------

.. code-block:: c

    struct pstate_data {
        int current_pstate;
        int min_pstate;
        int max_pstate;
        int max_pstate_physical;
        int scaling;
        int turbo_pstate;
        unsigned int max_freq;
        unsigned int turbo_freq;
    }

.. _`pstate_data.members`:

Members
-------

current_pstate
    Current requested P state

min_pstate
    Min P state possible for this platform

max_pstate
    Max P state possible for this platform

max_pstate_physical
    This is physical Max P state for a processor
    This can be higher than the max_pstate which can
    be limited by platform thermal design power limits

scaling
    Scaling factor to  convert frequency to cpufreq
    frequency units

turbo_pstate
    Max Turbo P state possible for this platform

max_freq
    \ ``max_pstate``\  frequency in cpufreq units

turbo_freq
    \ ``turbo_pstate``\  frequency in cpufreq units

.. _`pstate_data.description`:

Description
-----------

Stores the per cpu model P state limits and current P state.

.. _`vid_data`:

struct vid_data
===============

.. c:type:: struct vid_data

    Stores voltage information data

.. _`vid_data.definition`:

Definition
----------

.. code-block:: c

    struct vid_data {
        int min;
        int max;
        int turbo;
        int32_t ratio;
    }

.. _`vid_data.members`:

Members
-------

min
    VID data for this platform corresponding to
    the lowest P state

max
    VID data corresponding to the highest P State.

turbo
    VID data for turbo P state

ratio
    Ratio of (vid max - vid min) /
    (max P state - Min P State)

.. _`vid_data.description`:

Description
-----------

Stores the voltage data for DVFS (Dynamic Voltage and Frequency Scaling)
This data is used in Atom platforms, where in addition to target P state,
the voltage data needs to be specified to select next P State.

.. _`global_params`:

struct global_params
====================

.. c:type:: struct global_params

    Global parameters, mostly tunable via sysfs.

.. _`global_params.definition`:

Definition
----------

.. code-block:: c

    struct global_params {
        bool no_turbo;
        bool turbo_disabled;
        int max_perf_pct;
        int min_perf_pct;
    }

.. _`global_params.members`:

Members
-------

no_turbo
    Whether or not to use turbo P-states.

turbo_disabled
    Whethet or not turbo P-states are available at all,
    based on the MSR_IA32_MISC_ENABLE value and whether or
    not the maximum reported turbo P-state is different from
    the maximum reported non-turbo one.

max_perf_pct
    Maximum capacity limit in percent of the maximum turbo
    P-state capacity.

min_perf_pct
    Minimum capacity limit in percent of the maximum turbo
    P-state capacity.

.. _`cpudata`:

struct cpudata
==============

.. c:type:: struct cpudata

    Per CPU instance data storage

.. _`cpudata.definition`:

Definition
----------

.. code-block:: c

    struct cpudata {
        int cpu;
        unsigned int policy;
        struct update_util_data update_util;
        bool update_util_set;
        struct pstate_data pstate;
        struct vid_data vid;
        u64 last_update;
        u64 last_sample_time;
        u64 aperf_mperf_shift;
        u64 prev_aperf;
        u64 prev_mperf;
        u64 prev_tsc;
        u64 prev_cummulative_iowait;
        struct sample sample;
        int32_t min_perf_ratio;
        int32_t max_perf_ratio;
    #ifdef CONFIG_ACPI
        struct acpi_processor_performance acpi_perf_data;
        bool valid_pss_table;
    #endif
        unsigned int iowait_boost;
        s16 epp_powersave;
        s16 epp_policy;
        s16 epp_default;
        s16 epp_saved;
        u64 hwp_req_cached;
        u64 hwp_cap_cached;
        u64 last_io_update;
        unsigned int sched_flags;
        u32 hwp_boost_min;
    }

.. _`cpudata.members`:

Members
-------

cpu
    CPU number for this instance data

policy
    CPUFreq policy value

update_util
    CPUFreq utility callback information

update_util_set
    CPUFreq utility callback is set

pstate
    Stores P state limits for this CPU

vid
    Stores VID limits for this CPU

last_update
    Time of the last update.

last_sample_time
    Last Sample time

aperf_mperf_shift
    Number of clock cycles after aperf, merf is incremented
    This shift is a multiplier to mperf delta to
    calculate CPU busy.

prev_aperf
    Last APERF value read from APERF MSR

prev_mperf
    Last MPERF value read from MPERF MSR

prev_tsc
    Last timestamp counter (TSC) value

prev_cummulative_iowait
    IO Wait time difference from last and
    current sample

sample
    Storage for storing last Sample data

min_perf_ratio
    Minimum capacity in terms of PERF or HWP ratios

max_perf_ratio
    Maximum capacity in terms of PERF or HWP ratios

acpi_perf_data
    Stores ACPI perf information read from \_PSS

valid_pss_table
    Set to true for valid ACPI \_PSS entries found

iowait_boost
    iowait-related boost fraction

epp_powersave
    Last saved HWP energy performance preference
    (EPP) or energy performance bias (EPB),
    when policy switched to performance

epp_policy
    Last saved policy used to set EPP/EPB

epp_default
    Power on default HWP energy performance
    preference/bias

epp_saved
    Saved EPP/EPB during system suspend or CPU offline
    operation

hwp_req_cached
    Cached value of the last HWP Request MSR

hwp_cap_cached
    Cached value of the last HWP Capabilities MSR

last_io_update
    Last time when IO wake flag was set

sched_flags
    Store scheduler flags for possible cross CPU update

hwp_boost_min
    Last HWP boosted min performance

.. _`cpudata.description`:

Description
-----------

This structure stores per CPU instance data for all CPUs.

.. _`pstate_funcs`:

struct pstate_funcs
===================

.. c:type:: struct pstate_funcs

    Per CPU model specific callbacks

.. _`pstate_funcs.definition`:

Definition
----------

.. code-block:: c

    struct pstate_funcs {
        int (*get_max)(void);
        int (*get_max_physical)(void);
        int (*get_min)(void);
        int (*get_turbo)(void);
        int (*get_scaling)(void);
        int (*get_aperf_mperf_shift)(void);
        u64 (*get_val)(struct cpudata*, int pstate);
        void (*get_vid)(struct cpudata *);
    }

.. _`pstate_funcs.members`:

Members
-------

get_max
    Callback to get maximum non turbo effective P state

get_max_physical
    Callback to get maximum non turbo physical P state

get_min
    Callback to get minimum P state

get_turbo
    Callback to get turbo P state

get_scaling
    Callback to get frequency scaling factor

get_aperf_mperf_shift
    *undescribed*

get_val
    Callback to convert P state to actual MSR write value

get_vid
    Callback to get VID data for Atom platforms

.. _`pstate_funcs.description`:

Description
-----------

Core and Atom CPU models have different way to get P State limits. This
structure is used to store those callbacks.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/scmi_protocol.h

.. _`scmi_revision_info`:

struct scmi_revision_info
=========================

.. c:type:: struct scmi_revision_info

    version information structure

.. _`scmi_revision_info.definition`:

Definition
----------

.. code-block:: c

    struct scmi_revision_info {
        u16 major_ver;
        u16 minor_ver;
        u8 num_protocols;
        u8 num_agents;
        u32 impl_ver;
        char vendor_id[SCMI_MAX_STR_SIZE];
        char sub_vendor_id[SCMI_MAX_STR_SIZE];
    }

.. _`scmi_revision_info.members`:

Members
-------

major_ver
    Major ABI version. Change here implies risk of backward
    compatibility break.

minor_ver
    Minor ABI version. Change here implies new feature addition,
    or compatible change in ABI.

num_protocols
    Number of protocols that are implemented, excluding the
    base protocol.

num_agents
    Number of agents in the system.

impl_ver
    A vendor-specific implementation version.

vendor_id
    A vendor identifier(Null terminated ASCII string)

sub_vendor_id
    A sub-vendor identifier(Null terminated ASCII string)

.. _`scmi_clk_ops`:

struct scmi_clk_ops
===================

.. c:type:: struct scmi_clk_ops

    represents the various operations provided by SCMI Clock Protocol

.. _`scmi_clk_ops.definition`:

Definition
----------

.. code-block:: c

    struct scmi_clk_ops {
        int (*count_get)(const struct scmi_handle *handle);
        const struct scmi_clock_info *(*info_get) (const struct scmi_handle *handle, u32 clk_id);
        int (*rate_get)(const struct scmi_handle *handle, u32 clk_id, u64 *rate);
        int (*rate_set)(const struct scmi_handle *handle, u32 clk_id, u32 config, u64 rate);
        int (*enable)(const struct scmi_handle *handle, u32 clk_id);
        int (*disable)(const struct scmi_handle *handle, u32 clk_id);
    }

.. _`scmi_clk_ops.members`:

Members
-------

count_get
    get the count of clocks provided by SCMI

info_get
    get the information of the specified clock

rate_get
    request the current clock rate of a clock

rate_set
    set the clock rate of a clock

enable
    enables the specified clock

disable
    disables the specified clock

.. _`scmi_perf_ops`:

struct scmi_perf_ops
====================

.. c:type:: struct scmi_perf_ops

    represents the various operations provided by SCMI Performance Protocol

.. _`scmi_perf_ops.definition`:

Definition
----------

.. code-block:: c

    struct scmi_perf_ops {
        int (*limits_set)(const struct scmi_handle *handle, u32 domain, u32 max_perf, u32 min_perf);
        int (*limits_get)(const struct scmi_handle *handle, u32 domain, u32 *max_perf, u32 *min_perf);
        int (*level_set)(const struct scmi_handle *handle, u32 domain, u32 level, bool poll);
        int (*level_get)(const struct scmi_handle *handle, u32 domain, u32 *level, bool poll);
        int (*device_domain_id)(struct device *dev);
        int (*transition_latency_get)(const struct scmi_handle *handle, struct device *dev);
        int (*device_opps_add)(const struct scmi_handle *handle, struct device *dev);
        int (*freq_set)(const struct scmi_handle *handle, u32 domain, unsigned long rate, bool poll);
        int (*freq_get)(const struct scmi_handle *handle, u32 domain, unsigned long *rate, bool poll);
        int (*est_power_get)(const struct scmi_handle *handle, u32 domain, unsigned long *rate, unsigned long *power);
    }

.. _`scmi_perf_ops.members`:

Members
-------

limits_set
    sets limits on the performance level of a domain

limits_get
    gets limits on the performance level of a domain

level_set
    sets the performance level of a domain

level_get
    gets the performance level of a domain

device_domain_id
    gets the scmi domain id for a given device

transition_latency_get
    gets the DVFS transition latency for a given device

device_opps_add
    adds all the OPPs for a given device

freq_set
    sets the frequency for a given device using sustained frequency
    to sustained performance level mapping

freq_get
    gets the frequency for a given device using sustained frequency
    to sustained performance level mapping

est_power_get
    gets the estimated power cost for a given performance domain
    at a given frequency

.. _`scmi_power_ops`:

struct scmi_power_ops
=====================

.. c:type:: struct scmi_power_ops

    represents the various operations provided by SCMI Power Protocol

.. _`scmi_power_ops.definition`:

Definition
----------

.. code-block:: c

    struct scmi_power_ops {
        int (*num_domains_get)(const struct scmi_handle *handle);
        char *(*name_get)(const struct scmi_handle *handle, u32 domain);
    #define SCMI_POWER_STATE_TYPE_SHIFT 30
    #define SCMI_POWER_STATE_ID_MASK (BIT(28) - 1)
    #define SCMI_POWER_STATE_PARAM(type, id) \
        ((((type) & BIT(0)) << SCMI_POWER_STATE_TYPE_SHIFT) | \((id) & SCMI_POWER_STATE_ID_MASK)) #define SCMI_POWER_STATE_GENERIC_ON SCMI_POWER_STATE_PARAM(0, 0);
    #define SCMI_POWER_STATE_GENERIC_OFF SCMI_POWER_STATE_PARAM(1, 0)
        int (*state_set)(const struct scmi_handle *handle, u32 domain, u32 state);
        int (*state_get)(const struct scmi_handle *handle, u32 domain, u32 *state);
    }

.. _`scmi_power_ops.members`:

Members
-------

num_domains_get
    get the count of power domains provided by SCMI

name_get
    gets the name of a power domain

0
    *undescribed*

state_set
    sets the power state of a power domain

state_get
    gets the power state of a power domain

.. _`scmi_sensor_ops`:

struct scmi_sensor_ops
======================

.. c:type:: struct scmi_sensor_ops

    represents the various operations provided by SCMI Sensor Protocol

.. _`scmi_sensor_ops.definition`:

Definition
----------

.. code-block:: c

    struct scmi_sensor_ops {
        int (*count_get)(const struct scmi_handle *handle);
        const struct scmi_sensor_info *(*info_get) (const struct scmi_handle *handle, u32 sensor_id);
        int (*configuration_set)(const struct scmi_handle *handle, u32 sensor_id);
        int (*trip_point_set)(const struct scmi_handle *handle, u32 sensor_id, u8 trip_id, u64 trip_value);
        int (*reading_get)(const struct scmi_handle *handle, u32 sensor_id, bool async, u64 *value);
    }

.. _`scmi_sensor_ops.members`:

Members
-------

count_get
    get the count of sensors provided by SCMI

info_get
    get the information of the specified sensor

configuration_set
    control notifications on cross-over events for
    the trip-points

trip_point_set
    selects and configures a trip-point of interest

reading_get
    gets the current value of the sensor

.. _`scmi_handle`:

struct scmi_handle
==================

.. c:type:: struct scmi_handle

    Handle returned to ARM SCMI clients for usage.

.. _`scmi_handle.definition`:

Definition
----------

.. code-block:: c

    struct scmi_handle {
        struct device *dev;
        struct scmi_revision_info *version;
        struct scmi_perf_ops *perf_ops;
        struct scmi_clk_ops *clk_ops;
        struct scmi_power_ops *power_ops;
        struct scmi_sensor_ops *sensor_ops;
        void *perf_priv;
        void *clk_priv;
        void *power_priv;
        void *sensor_priv;
    }

.. _`scmi_handle.members`:

Members
-------

dev
    pointer to the SCMI device

version
    pointer to the structure containing SCMI version information

perf_ops
    pointer to set of performance protocol operations

clk_ops
    pointer to set of clock protocol operations

power_ops
    pointer to set of power protocol operations

sensor_ops
    pointer to set of sensor protocol operations

perf_priv
    pointer to private data structure specific to performance
    protocol(for internal use only)

clk_priv
    pointer to private data structure specific to clock
    protocol(for internal use only)

power_priv
    pointer to private data structure specific to power
    protocol(for internal use only)

sensor_priv
    pointer to private data structure specific to sensors
    protocol(for internal use only)

.. _`module_scmi_driver`:

module_scmi_driver
==================

.. c:function::  module_scmi_driver( __scmi_driver)

    Helper macro for registering a scmi driver

    :param __scmi_driver:
        scmi_driver structure
    :type __scmi_driver: 

.. _`module_scmi_driver.description`:

Description
-----------

Helper macro for scmi drivers to set up proper module init / exit
functions.  Replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\  and keeps people from
printing pointless things to the kernel log when their driver is loaded.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/scpi_protocol.h

.. _`scpi_ops`:

struct scpi_ops
===============

.. c:type:: struct scpi_ops

    represents the various operations provided by SCP through SCPI message protocol

.. _`scpi_ops.definition`:

Definition
----------

.. code-block:: c

    struct scpi_ops {
        u32 (*get_version)(void);
        int (*clk_get_range)(u16, unsigned long *, unsigned long *);
        unsigned long (*clk_get_val)(u16);
        int (*clk_set_val)(u16, unsigned long);
        int (*dvfs_get_idx)(u8);
        int (*dvfs_set_idx)(u8, u8);
        struct scpi_dvfs_info *(*dvfs_get_info)(u8);
        int (*device_domain_id)(struct device *);
        int (*get_transition_latency)(struct device *);
        int (*add_opps_to_device)(struct device *);
        int (*sensor_get_capability)(u16 *sensors);
        int (*sensor_get_info)(u16 sensor_id, struct scpi_sensor_info *);
        int (*sensor_get_value)(u16, u64 *);
        int (*device_get_power_state)(u16);
        int (*device_set_power_state)(u16, u8);
    }

.. _`scpi_ops.members`:

Members
-------

get_version
    returns the major and minor revision on the SCPI
    message protocol

clk_get_range
    gets clock range limit(min - max in Hz)

clk_get_val
    gets clock value(in Hz)

clk_set_val
    sets the clock value, setting to 0 will disable the
    clock (if supported)

dvfs_get_idx
    gets the Operating Point of the given power domain.
    OPP is an index to the list return by \ ``dvfs_get_info``\ 

dvfs_set_idx
    sets the Operating Point of the given power domain.
    OPP is an index to the list return by \ ``dvfs_get_info``\ 

dvfs_get_info
    returns the DVFS capabilities of the given power
    domain. It includes the OPP list and the latency information

device_domain_id
    *undescribed*

get_transition_latency
    *undescribed*

add_opps_to_device
    *undescribed*

sensor_get_capability
    *undescribed*

sensor_get_info
    *undescribed*

sensor_get_value
    *undescribed*

device_get_power_state
    *undescribed*

device_set_power_state
    *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/qcom/tsens.h

.. _`tsens_ops`:

struct tsens_ops
================

.. c:type:: struct tsens_ops

    operations as supported by the tsens device

.. _`tsens_ops.definition`:

Definition
----------

.. code-block:: c

    struct tsens_ops {
        int (*init)(struct tsens_device *);
        int (*calibrate)(struct tsens_device *);
        int (*get_temp)(struct tsens_device *, int, int *);
        int (*enable)(struct tsens_device *, int);
        void (*disable)(struct tsens_device *);
        int (*suspend)(struct tsens_device *);
        int (*resume)(struct tsens_device *);
        int (*get_trend)(struct tsens_device *, int, enum thermal_trend *);
    }

.. _`tsens_ops.members`:

Members
-------

init
    Function to initialize the tsens device

calibrate
    Function to calibrate the tsens device

get_temp
    Function which returns the temp in millidegC

enable
    Function to enable (clocks/power) tsens device

disable
    Function to disable the tsens device

suspend
    Function to suspend the tsens device

resume
    Function to resume the tsens device

get_trend
    Function to get the thermal/temp trend

.. _`tsens_data`:

struct tsens_data
=================

.. c:type:: struct tsens_data

    tsens instance specific data

.. _`tsens_data.definition`:

Definition
----------

.. code-block:: c

    struct tsens_data {
        const u32 num_sensors;
        const struct tsens_ops *ops;
        const u16 reg_offsets[REG_ARRAY_SIZE];
        unsigned int *hw_ids;
    }

.. _`tsens_data.members`:

Members
-------

num_sensors
    Max number of sensors supported by platform

ops
    operations the tsens instance supports

reg_offsets
    Register offsets for commonly used registers

hw_ids
    Subset of sensors ids supported by platform, if not the first n

.. This file was automatic generated / don't edit.


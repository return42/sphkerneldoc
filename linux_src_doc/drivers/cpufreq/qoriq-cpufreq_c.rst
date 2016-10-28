.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/qoriq-cpufreq.c

.. _`cpu_data`:

struct cpu_data
===============

.. c:type:: struct cpu_data


.. _`cpu_data.definition`:

Definition
----------

.. code-block:: c

    struct cpu_data {
        struct clk **pclk;
        struct cpufreq_frequency_table *table;
        struct thermal_cooling_device *cdev;
    }

.. _`cpu_data.members`:

Members
-------

pclk
    the parent clock of cpu

table
    frequency table

cdev
    *undescribed*

.. _`soc_data`:

struct soc_data
===============

.. c:type:: struct soc_data

    SoC specific data

.. _`soc_data.definition`:

Definition
----------

.. code-block:: c

    struct soc_data {
        u32 freq_mask[4];
        u32 flag;
    }

.. _`soc_data.members`:

Members
-------

freq_mask
    mask the disallowed frequencies

flag
    unique flags

.. This file was automatic generated / don't edit.


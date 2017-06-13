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
        u32 flags;
    }

.. _`soc_data.members`:

Members
-------

flags
    SOC_xxx

.. This file was automatic generated / don't edit.


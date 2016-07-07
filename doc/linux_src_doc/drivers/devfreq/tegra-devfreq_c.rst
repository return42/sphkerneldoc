.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/devfreq/tegra-devfreq.c

.. _`tegra_devfreq_device_config`:

struct tegra_devfreq_device_config
==================================

.. c:type:: struct tegra_devfreq_device_config

    configuration specific to an ACTMON device

.. _`tegra_devfreq_device_config.definition`:

Definition
----------

.. code-block:: c

    struct tegra_devfreq_device_config {
        u32 offset;
        u32 irq_mask;
        unsigned int boost_up_coeff;
        unsigned int boost_down_coeff;
        unsigned int boost_up_threshold;
        unsigned int boost_down_threshold;
        u32 avg_dependency_threshold;
    }

.. _`tegra_devfreq_device_config.members`:

Members
-------

offset
    *undescribed*

irq_mask
    *undescribed*

boost_up_coeff
    *undescribed*

boost_down_coeff
    *undescribed*

boost_up_threshold
    *undescribed*

boost_down_threshold
    *undescribed*

avg_dependency_threshold
    *undescribed*

.. _`tegra_devfreq_device_config.description`:

Description
-----------

Coefficients and thresholds are percentages unless otherwise noted

.. _`tegra_devfreq_device`:

struct tegra_devfreq_device
===========================

.. c:type:: struct tegra_devfreq_device

    state specific to an ACTMON device

.. _`tegra_devfreq_device.definition`:

Definition
----------

.. code-block:: c

    struct tegra_devfreq_device {
        const struct tegra_devfreq_device_config *config;
        void __iomem *regs;
        spinlock_t lock;
        u32 avg_count;
        unsigned long boost_freq;
        unsigned long target_freq;
    }

.. _`tegra_devfreq_device.members`:

Members
-------

config
    *undescribed*

regs
    *undescribed*

lock
    *undescribed*

avg_count
    *undescribed*

boost_freq
    *undescribed*

target_freq
    *undescribed*

.. _`tegra_devfreq_device.description`:

Description
-----------

Frequencies are in kHz.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/stm/stm32_sai.h

.. _`stm32_sai_conf`:

struct stm32_sai_conf
=====================

.. c:type:: struct stm32_sai_conf

    SAI configuration

.. _`stm32_sai_conf.definition`:

Definition
----------

.. code-block:: c

    struct stm32_sai_conf {
        int version;
        bool has_spdif;
    }

.. _`stm32_sai_conf.members`:

Members
-------

version
    SAI version

has_spdif
    SAI S/PDIF support flag

.. _`stm32_sai_data`:

struct stm32_sai_data
=====================

.. c:type:: struct stm32_sai_data

    private data of SAI instance driver

.. _`stm32_sai_data.definition`:

Definition
----------

.. code-block:: c

    struct stm32_sai_data {
        struct platform_device *pdev;
        void __iomem *base;
        struct clk *pclk;
        struct clk *clk_x8k;
        struct clk *clk_x11k;
        struct stm32_sai_conf *conf;
        int irq;
        int (*set_sync)(struct stm32_sai_data *sai, struct device_node *np_provider, int synco, int synci);
    }

.. _`stm32_sai_data.members`:

Members
-------

pdev
    device data pointer

base
    common register bank virtual base address

pclk
    SAI bus clock

clk_x8k
    SAI parent clock for sampling frequencies multiple of 8kHz

clk_x11k
    SAI parent clock for sampling frequencies multiple of 11kHz

conf
    *undescribed*

irq
    SAI interrupt line

set_sync
    pointer to synchro mode configuration callback

.. This file was automatic generated / don't edit.


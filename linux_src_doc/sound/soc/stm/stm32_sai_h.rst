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
    }

.. _`stm32_sai_conf.members`:

Members
-------

version
    SAI version

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
        struct clk *clk_x8k;
        struct clk *clk_x11k;
        struct stm32_sai_conf *conf;
        int irq;
    }

.. _`stm32_sai_data.members`:

Members
-------

pdev
    device data pointer

clk_x8k
    SAI parent clock for sampling frequencies multiple of 8kHz

clk_x11k
    SAI parent clock for sampling frequencies multiple of 11kHz

conf
    *undescribed*

irq
    SAI interrupt line

.. This file was automatic generated / don't edit.


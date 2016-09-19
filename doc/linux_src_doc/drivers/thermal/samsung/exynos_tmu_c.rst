.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/samsung/exynos_tmu.c

.. _`exynos_tmu_data`:

struct exynos_tmu_data
======================

.. c:type:: struct exynos_tmu_data

    A structure to hold the private data of the TMU

.. _`exynos_tmu_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos_tmu_data {
        int id;
        struct exynos_tmu_platform_data *pdata;
        void __iomem *base;
        void __iomem *base_second;
        int irq;
        enum soc_type soc;
        struct work_struct irq_work;
        struct mutex lock;
        struct clk *clk;
        struct clk * *clk_sec;
        struct clk * * *sclk;
        u16 temp_error1;
        u16 temp_error2;
        struct regulator *regulator;
        struct thermal_zone_device *tzd;
        unsigned int ntrip;
        int (*tmu_initialize)(struct platform_device *pdev);
        void (*tmu_control)(struct platform_device *pdev, bool on);
        int (*tmu_read)(struct exynos_tmu_data *data);
        void (*tmu_set_emulation)(struct exynos_tmu_data *data, int temp);
        void (*tmu_clear_irqs)(struct exynos_tmu_data *data);
    }

.. _`exynos_tmu_data.members`:

Members
-------

id
    identifier of the one instance of the TMU controller.

pdata
    pointer to the tmu platform/configuration data

base
    base address of the single instance of the TMU controller.

base_second
    base address of the common registers of the TMU controller.

irq
    irq number of the TMU controller.

soc
    id of the SOC type.

irq_work
    pointer to the irq work structure.

lock
    lock to implement synchronization.

clk
    pointer to the clock structure.

clk_sec
    pointer to the clock structure for accessing the base_second.

sclk
    pointer to the clock structure for accessing the tmu special clk.

temp_error1
    fused value of the first point trim.

temp_error2
    fused value of the second point trim.

regulator
    pointer to the TMU regulator structure.

tzd
    *undescribed*

ntrip
    number of supported trip points.

tmu_initialize
    SoC specific TMU initialization method

tmu_control
    SoC specific TMU control method

tmu_read
    SoC specific TMU temperature read method

tmu_set_emulation
    SoC specific TMU emulation setting method

tmu_clear_irqs
    SoC specific TMU interrupts clearing method

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/samsung/core.h

.. _`sec_pmic_dev`:

struct sec_pmic_dev
===================

.. c:type:: struct sec_pmic_dev

    s2m/s5m master device for sub-drivers

.. _`sec_pmic_dev.definition`:

Definition
----------

.. code-block:: c

    struct sec_pmic_dev {
        struct device *dev;
        struct sec_platform_data *pdata;
        struct regmap *regmap_pmic;
        struct i2c_client *i2c;
        unsigned long device_type;
        int irq_base;
        int irq;
        struct regmap_irq_chip_data *irq_data;
        bool wakeup;
    }

.. _`sec_pmic_dev.members`:

Members
-------

dev
    Master device of the chip

pdata
    Platform data populated with data from DTS
    or board files

regmap_pmic
    Regmap associated with PMIC's I2C address

i2c
    I2C client of the main driver

device_type
    Type of device, matches enum sec_device_type

irq_base
    Base IRQ number for device, required for IRQs

irq
    Generic IRQ number for device

irq_data
    Runtime data structure for IRQ controller

wakeup
    Whether or not this is a wakeup device

.. This file was automatic generated / don't edit.


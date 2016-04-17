.. -*- coding: utf-8; mode: rst -*-

=================
max8998-private.h
=================


.. _`max8998_dev`:

struct max8998_dev
==================

.. c:type:: max8998_dev

    max8998 master device for sub-drivers


.. _`max8998_dev.definition`:

Definition
----------

.. code-block:: c

  struct max8998_dev {
    struct device * dev;
    struct max8998_platform_data * pdata;
    struct i2c_client * i2c;
    struct i2c_client * rtc;
    struct mutex iolock;
    struct mutex irqlock;
    unsigned int irq_base;
    int irq;
    int ono;
    u8 irq_masks_cur[MAX8998_NUM_IRQ_REGS];
    u8 irq_masks_cache[MAX8998_NUM_IRQ_REGS];
    unsigned long type;
  };


.. _`max8998_dev.members`:

Members
-------

:``dev``:
    master device of the chip (can be used to access platform data)

:``pdata``:
    platform data for the driver and subdrivers

:``i2c``:
    i2c client private data for regulator

:``rtc``:
    i2c client private data for rtc

:``iolock``:
    mutex for serializing io access

:``irqlock``:
    mutex for buslock

:``irq_base``:
    base IRQ number for max8998, required for IRQs

:``irq``:
    generic IRQ number for max8998

:``ono``:
    power onoff IRQ number for max8998

:``irq_masks_cur[MAX8998_NUM_IRQ_REGS]``:
    currently active value

:``irq_masks_cache[MAX8998_NUM_IRQ_REGS]``:
    cached hardware value

:``type``:
    indicate which max8998 "variant" is used



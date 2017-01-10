.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-adc.c

.. _`stm32_adc`:

struct stm32_adc
================

.. c:type:: struct stm32_adc

    private data of each ADC IIO instance

.. _`stm32_adc.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc {
        struct stm32_adc_common *common;
        u32 offset;
        struct completion completion;
        u16 *buffer;
        struct clk *clk;
        int irq;
        spinlock_t lock;
    }

.. _`stm32_adc.members`:

Members
-------

common
    reference to ADC block common data

offset
    ADC instance register offset in ADC block

completion
    end of single conversion completion

buffer
    data buffer

clk
    clock for this adc instance

irq
    interrupt for this adc instance

lock
    spinlock

.. _`stm32_adc_chan_spec`:

struct stm32_adc_chan_spec
==========================

.. c:type:: struct stm32_adc_chan_spec

    specification of stm32 adc channel

.. _`stm32_adc_chan_spec.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_chan_spec {
        enum iio_chan_type type;
        int channel;
        const char *name;
    }

.. _`stm32_adc_chan_spec.members`:

Members
-------

type
    IIO channel type

channel
    channel number (single ended)

name
    channel name (single ended)

.. _`stm32_adc_readl`:

stm32_adc_readl
===============

.. c:function:: u32 stm32_adc_readl(struct stm32_adc *adc, u32 reg)

    :param struct stm32_adc \*adc:
        stm32 adc instance

    :param u32 reg:
        reg offset in adc instance

.. _`stm32_adc_readl.note`:

Note
----

All instances share same base, with 0x0, 0x100 or 0x200 offset resp.
for adc1, adc2 and adc3.

.. _`stm32_adc_conv_irq_enable`:

stm32_adc_conv_irq_enable
=========================

.. c:function:: void stm32_adc_conv_irq_enable(struct stm32_adc *adc)

    Enable end of conversion interrupt

    :param struct stm32_adc \*adc:
        stm32 adc instance

.. _`stm32_adc_conv_irq_disable`:

stm32_adc_conv_irq_disable
==========================

.. c:function:: void stm32_adc_conv_irq_disable(struct stm32_adc *adc)

    Disable end of conversion interrupt

    :param struct stm32_adc \*adc:
        stm32 adc instance

.. _`stm32_adc_start_conv`:

stm32_adc_start_conv
====================

.. c:function:: void stm32_adc_start_conv(struct stm32_adc *adc)

    Start conversions for regular channels.

    :param struct stm32_adc \*adc:
        stm32 adc instance

.. _`stm32_adc_single_conv`:

stm32_adc_single_conv
=====================

.. c:function:: int stm32_adc_single_conv(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, int *res)

    Performs a single conversion

    :param struct iio_dev \*indio_dev:
        IIO device

    :param const struct iio_chan_spec \*chan:
        IIO channel

    :param int \*res:
        conversion result

.. _`stm32_adc_single_conv.the-function-performs-a-single-conversion-on-a-given-channel`:

The function performs a single conversion on a given channel
------------------------------------------------------------

- Program sequencer with one channel (e.g. in SQ1 with len = 1)
- Use SW trigger
- Start conversion, then wait for interrupt completion.

.. _`stm32_adc_debugfs_reg_access`:

stm32_adc_debugfs_reg_access
============================

.. c:function:: int stm32_adc_debugfs_reg_access(struct iio_dev *indio_dev, unsigned reg, unsigned writeval, unsigned *readval)

    read or write register value

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param unsigned reg:
        *undescribed*

    :param unsigned writeval:
        *undescribed*

    :param unsigned \*readval:
        *undescribed*

.. _`stm32_adc_debugfs_reg_access.to-read-a-value-from-an-adc-register`:

To read a value from an ADC register
------------------------------------

echo [ADC reg offset] > direct_reg_access
cat direct_reg_access

.. _`stm32_adc_debugfs_reg_access.to-write-a-value-in-a-adc-register`:

To write a value in a ADC register
----------------------------------

echo [ADC_reg_offset] [value] > direct_reg_access

.. This file was automatic generated / don't edit.


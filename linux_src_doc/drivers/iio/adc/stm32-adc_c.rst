.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-adc.c

.. _`stm32_adc_trig_info`:

struct stm32_adc_trig_info
==========================

.. c:type:: struct stm32_adc_trig_info

    ADC trigger info

.. _`stm32_adc_trig_info.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_trig_info {
        const char *name;
        enum stm32_adc_extsel extsel;
    }

.. _`stm32_adc_trig_info.members`:

Members
-------

name
    name of the trigger, corresponding to its source

extsel
    trigger selection

.. _`stm32_adc_calib`:

struct stm32_adc_calib
======================

.. c:type:: struct stm32_adc_calib

    optional adc calibration data

.. _`stm32_adc_calib.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_calib {
        u32 calfact_s;
        u32 calfact_d;
        u32 lincalfact[STM32H7_LINCALFACT_NUM];
    }

.. _`stm32_adc_calib.members`:

Members
-------

calfact_s
    Calibration offset for single ended channels

calfact_d
    Calibration offset in differential

lincalfact
    Linearity calibration factor

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
        const struct stm32_adc_cfg *cfg;
        struct completion completion;
        u16 buffer[STM32_ADC_MAX_SQ];
        struct clk *clk;
        int irq;
        spinlock_t lock;
        unsigned int bufi;
        unsigned int num_conv;
        u32 res;
        u32 trigger_polarity;
        struct dma_chan *dma_chan;
        u8 *rx_buf;
        dma_addr_t rx_dma_buf;
        unsigned int rx_buf_sz;
        u32 difsel;
        u32 pcsel;
        u32 smpr_val[2];
        struct stm32_adc_calib cal;
        char chan_name[STM32_ADC_CH_MAX][STM32_ADC_CH_SZ];
    }

.. _`stm32_adc.members`:

Members
-------

common
    reference to ADC block common data

offset
    ADC instance register offset in ADC block

cfg
    compatible configuration data

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

bufi
    data buffer index

num_conv
    expected number of scan conversions

res
    data resolution (e.g. RES bitfield value)

trigger_polarity
    external trigger polarity (e.g. exten)

dma_chan
    dma channel

rx_buf
    dma rx buffer cpu address

rx_dma_buf
    dma rx buffer bus address

rx_buf_sz
    dma rx buffer size
    \ ``difsel``\               bitmask to set single-ended/differential channel
    \ ``pcsel``\                bitmask to preselect channels on some devices

difsel
    *undescribed*

pcsel
    *undescribed*

smpr_val
    sampling time settings (e.g. smpr1 / smpr2)

cal
    optional calibration data on some devices

chan_name
    channel name array

.. _`stm32_adc_info`:

struct stm32_adc_info
=====================

.. c:type:: struct stm32_adc_info

    stm32 ADC, per instance config data

.. _`stm32_adc_info.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_info {
        int max_channels;
        const unsigned int *resolutions;
        const unsigned int num_res;
    }

.. _`stm32_adc_info.members`:

Members
-------

max_channels
    Number of channels

resolutions
    available resolutions

num_res
    number of available resolutions

.. _`stm32_adc_readl`:

stm32_adc_readl
===============

.. c:function:: u32 stm32_adc_readl(struct stm32_adc *adc, u32 reg)

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

    :param reg:
        reg offset in adc instance
    :type reg: u32

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

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

.. _`stm32_adc_conv_irq_disable`:

stm32_adc_conv_irq_disable
==========================

.. c:function:: void stm32_adc_conv_irq_disable(struct stm32_adc *adc)

    Disable end of conversion interrupt

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

.. _`stm32f4_adc_start_conv`:

stm32f4_adc_start_conv
======================

.. c:function:: void stm32f4_adc_start_conv(struct stm32_adc *adc, bool dma)

    Start conversions for regular channels.

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

    :param dma:
        use dma to transfer conversion result
    :type dma: bool

.. _`stm32f4_adc_start_conv.description`:

Description
-----------

Start conversions for regular channels.
Also take care of normal or DMA mode. Circular DMA may be used for regular
conversions, in IIO buffer modes. Otherwise, use ADC interrupt with direct
DR read instead (e.g. read_raw, or triggered buffer mode without DMA).

.. _`stm32h7_adc_read_selfcalib`:

stm32h7_adc_read_selfcalib
==========================

.. c:function:: int stm32h7_adc_read_selfcalib(struct stm32_adc *adc)

    read calibration shadow regs, save result

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

.. _`stm32h7_adc_restore_selfcalib`:

stm32h7_adc_restore_selfcalib
=============================

.. c:function:: int stm32h7_adc_restore_selfcalib(struct stm32_adc *adc)

    Restore saved self-calibration result

    :param adc:
        stm32 adc instance
    :type adc: struct stm32_adc \*

.. _`stm32h7_adc_restore_selfcalib.note`:

Note
----

ADC must be enabled, with no on-going conversions.

.. _`stm32h7_adc_calib_timeout_us`:

STM32H7_ADC_CALIB_TIMEOUT_US
============================

.. c:function::  STM32H7_ADC_CALIB_TIMEOUT_US()

.. _`stm32h7_adc_calib_timeout_us.worst-cases`:

worst cases
-----------

- low clock frequency
- maximum prescalers

.. _`stm32h7_adc_calib_timeout_us.calibration-requires`:

Calibration requires
--------------------

- 131,072 ADC clock cycle for the linear calibration
- 20 ADC clock cycle for the offset calibration

Set to 100ms for now

.. _`stm32h7_adc_selfcalib`:

stm32h7_adc_selfcalib
=====================

.. c:function:: int stm32h7_adc_selfcalib(struct stm32_adc *adc)

    Procedure to calibrate ADC (from power down)

    :param adc:
        stm32 adc instance
        Exit from power down, calibrate ADC, then return to power down.
    :type adc: struct stm32_adc \*

.. _`stm32h7_adc_prepare`:

stm32h7_adc_prepare
===================

.. c:function:: int stm32h7_adc_prepare(struct stm32_adc *adc)

    Leave power down mode to enable ADC.

    :param adc:
        stm32 adc instance
        Leave power down mode.
        Configure channels as single ended or differential before enabling ADC.
        Enable ADC.
        Restore calibration data.
        Pre-select channels that may be used in PCSEL (required by input MUX / IO):
        - Only one input is selected for single ended (e.g. 'vinp')
        - Two inputs are selected for differential channels (e.g. 'vinp' & 'vinn')
    :type adc: struct stm32_adc \*

.. _`stm32_adc_conf_scan_seq`:

stm32_adc_conf_scan_seq
=======================

.. c:function:: int stm32_adc_conf_scan_seq(struct iio_dev *indio_dev, const unsigned long *scan_mask)

    Build regular channels scan sequence

    :param indio_dev:
        IIO device
    :type indio_dev: struct iio_dev \*

    :param scan_mask:
        channels to be converted
    :type scan_mask: const unsigned long \*

.. _`stm32_adc_conf_scan_seq.description`:

Description
-----------

Conversion sequence :
Apply sampling time settings for all channels.
Configure ADC scan sequence based on selected channels in scan_mask.
Add channels to SQR registers, from scan_mask LSB to MSB, then
program sequence len.

.. _`stm32_adc_get_trig_extsel`:

stm32_adc_get_trig_extsel
=========================

.. c:function:: int stm32_adc_get_trig_extsel(struct iio_dev *indio_dev, struct iio_trigger *trig)

    Get external trigger selection

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

    :param trig:
        trigger
    :type trig: struct iio_trigger \*

.. _`stm32_adc_get_trig_extsel.description`:

Description
-----------

Returns trigger extsel value, if trig matches, -EINVAL otherwise.

.. _`stm32_adc_set_trig`:

stm32_adc_set_trig
==================

.. c:function:: int stm32_adc_set_trig(struct iio_dev *indio_dev, struct iio_trigger *trig)

    Set a regular trigger

    :param indio_dev:
        IIO device
    :type indio_dev: struct iio_dev \*

    :param trig:
        IIO trigger
    :type trig: struct iio_trigger \*

.. _`stm32_adc_set_trig.description`:

Description
-----------

Set trigger source/polarity (e.g. SW, or HW with polarity) :
- if HW trigger disabled (e.g. trig == NULL, conversion launched by sw)
- if HW trigger enabled, set source & polarity

.. _`stm32_adc_single_conv`:

stm32_adc_single_conv
=====================

.. c:function:: int stm32_adc_single_conv(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, int *res)

    Performs a single conversion

    :param indio_dev:
        IIO device
    :type indio_dev: struct iio_dev \*

    :param chan:
        IIO channel
    :type chan: const struct iio_chan_spec \*

    :param res:
        conversion result
    :type res: int \*

.. _`stm32_adc_single_conv.the-function-performs-a-single-conversion-on-a-given-channel`:

The function performs a single conversion on a given channel
------------------------------------------------------------

- Apply sampling time settings
- Program sequencer with one channel (e.g. in SQ1 with len = 1)
- Use SW trigger
- Start conversion, then wait for interrupt completion.

.. _`stm32_adc_validate_trigger`:

stm32_adc_validate_trigger
==========================

.. c:function:: int stm32_adc_validate_trigger(struct iio_dev *indio_dev, struct iio_trigger *trig)

    validate trigger for stm32 adc

    :param indio_dev:
        IIO device
    :type indio_dev: struct iio_dev \*

    :param trig:
        new trigger
    :type trig: struct iio_trigger \*

.. _`stm32_adc_validate_trigger.return`:

Return
------

0 if trig matches one of the triggers registered by stm32 adc
driver, -EINVAL otherwise.

.. _`stm32_adc_debugfs_reg_access`:

stm32_adc_debugfs_reg_access
============================

.. c:function:: int stm32_adc_debugfs_reg_access(struct iio_dev *indio_dev, unsigned reg, unsigned writeval, unsigned *readval)

    read or write register value

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

    :param reg:
        *undescribed*
    :type reg: unsigned

    :param writeval:
        *undescribed*
    :type writeval: unsigned

    :param readval:
        *undescribed*
    :type readval: unsigned \*

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


.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/uniphier/aio-core.c

.. _`aio_iecout_set_enable`:

aio_iecout_set_enable
=====================

.. c:function:: void aio_iecout_set_enable(struct uniphier_aio_chip *chip, bool enable)

    setup IEC output via SoC glue

    :param chip:
        the AIO chip pointer
    :type chip: struct uniphier_aio_chip \*

    :param enable:
        false to stop the output, true to start
    :type enable: bool

.. _`aio_iecout_set_enable.description`:

Description
-----------

Set enabled or disabled S/PDIF signal output to out of SoC via AOnIEC pins.
This function need to call at driver startup.

The regmap of SoC glue is specified by 'socionext,syscon' optional property
of DT. This function has no effect if no property.

.. _`aio_chip_set_pll`:

aio_chip_set_pll
================

.. c:function:: int aio_chip_set_pll(struct uniphier_aio_chip *chip, int pll_id, unsigned int freq)

    set frequency to audio PLL

    :param chip:
        the AIO chip pointer
    :type chip: struct uniphier_aio_chip \*

    :param pll_id:
        *undescribed*
    :type pll_id: int

    :param freq:
        frequency in Hz, 0 is ignored
    :type freq: unsigned int

.. _`aio_chip_set_pll.description`:

Description
-----------

Sets frequency of audio PLL. This function can be called anytime,
but it takes time till PLL is locked.

.. _`aio_chip_set_pll.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_chip_init`:

aio_chip_init
=============

.. c:function:: void aio_chip_init(struct uniphier_aio_chip *chip)

    initialize AIO whole settings

    :param chip:
        the AIO chip pointer
    :type chip: struct uniphier_aio_chip \*

.. _`aio_chip_init.description`:

Description
-----------

Sets AIO fixed and whole device settings to AIO.
This function need to call once at driver startup.

The register area that is changed by this function is shared by all
modules of AIO. But there is not race condition since this function
has always set the same initialize values.

.. _`aio_init`:

aio_init
========

.. c:function:: int aio_init(struct uniphier_aio_sub *sub)

    initialize AIO substream

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

.. _`aio_init.description`:

Description
-----------

Sets fixed settings of each AIO substreams.
This function need to call once at substream startup.

.. _`aio_init.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_reset`:

aio_port_reset
==============

.. c:function:: void aio_port_reset(struct uniphier_aio_sub *sub)

    reset AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

.. _`aio_port_reset.description`:

Description
-----------

Resets the digital signal input/output port block of AIO.

.. _`aio_port_set_ch`:

aio_port_set_ch
===============

.. c:function:: int aio_port_set_ch(struct uniphier_aio_sub *sub)

    set channels of LPCM

    :param sub:
        the AIO substream pointer, PCM substream only
    :type sub: struct uniphier_aio_sub \*

.. _`aio_port_set_ch.description`:

Description
-----------

Set suitable slot selecting to input/output port block of AIO.

This function may return error if non-PCM substream.

.. _`aio_port_set_ch.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_set_rate`:

aio_port_set_rate
=================

.. c:function:: int aio_port_set_rate(struct uniphier_aio_sub *sub, int rate)

    set sampling rate of LPCM

    :param sub:
        the AIO substream pointer, PCM substream only
    :type sub: struct uniphier_aio_sub \*

    :param rate:
        Sampling rate in Hz.
    :type rate: int

.. _`aio_port_set_rate.description`:

Description
-----------

Set suitable I2S format settings to input/output port block of AIO.
Parameter is specified by \ :c:func:`hw_params`\ .

This function may return error if non-PCM substream.

.. _`aio_port_set_rate.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_set_fmt`:

aio_port_set_fmt
================

.. c:function:: int aio_port_set_fmt(struct uniphier_aio_sub *sub)

    set format of I2S data

    :param sub:
        the AIO substream pointer, PCM substream only
        This parameter has no effect if substream is I2S or PCM.
    :type sub: struct uniphier_aio_sub \*

.. _`aio_port_set_fmt.description`:

Description
-----------

Set suitable I2S format settings to input/output port block of AIO.
Parameter is specified by \ :c:func:`set_fmt`\ .

This function may return error if non-PCM substream.

.. _`aio_port_set_fmt.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_set_clk`:

aio_port_set_clk
================

.. c:function:: int aio_port_set_clk(struct uniphier_aio_sub *sub)

    set clock and divider of AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

.. _`aio_port_set_clk.description`:

Description
-----------

Set suitable PLL clock divider and relational settings to
input/output port block of AIO. Parameters are specified by
\ :c:func:`set_sysclk`\  and \ :c:func:`set_pll`\ .

.. _`aio_port_set_clk.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_set_param`:

aio_port_set_param
==================

.. c:function:: int aio_port_set_param(struct uniphier_aio_sub *sub, int pass_through, const struct snd_pcm_hw_params *params)

    set parameters of AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param pass_through:
        Zero if sound data is LPCM, otherwise if data is not LPCM.
        This parameter has no effect if substream is I2S or PCM.
    :type pass_through: int

    :param params:
        hardware parameters of ALSA
    :type params: const struct snd_pcm_hw_params \*

.. _`aio_port_set_param.description`:

Description
-----------

Set suitable setting to input/output port block of AIO to process the
specified in params.

.. _`aio_port_set_param.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_port_set_enable`:

aio_port_set_enable
===================

.. c:function:: void aio_port_set_enable(struct uniphier_aio_sub *sub, int enable)

    start or stop of AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param enable:
        zero to stop the block, otherwise to start
    :type enable: int

.. _`aio_port_set_enable.description`:

Description
-----------

Start or stop the signal input/output port block of AIO.

.. _`aio_port_get_volume`:

aio_port_get_volume
===================

.. c:function:: int aio_port_get_volume(struct uniphier_aio_sub *sub)

    get volume of AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

.. _`aio_port_get_volume.return`:

Return
------

current volume, range is 0x0000 - 0xffff

.. _`aio_port_set_volume`:

aio_port_set_volume
===================

.. c:function:: void aio_port_set_volume(struct uniphier_aio_sub *sub, int vol)

    set volume of AIO port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param vol:
        target volume, range is 0x0000 - 0xffff.
    :type vol: int

.. _`aio_port_set_volume.description`:

Description
-----------

Change digital volume and perfome fade-out/fade-in effect for specified
output slot of port. Gained PCM value can calculate as the following:
Gained = Original \* vol / 0x4000

.. _`aio_if_set_param`:

aio_if_set_param
================

.. c:function:: int aio_if_set_param(struct uniphier_aio_sub *sub, int pass_through)

    set parameters of AIO DMA I/F block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param pass_through:
        Zero if sound data is LPCM, otherwise if data is not LPCM.
        This parameter has no effect if substream is I2S or PCM.
    :type pass_through: int

.. _`aio_if_set_param.description`:

Description
-----------

Set suitable setting to DMA interface block of AIO to process the
specified in settings.

.. _`aio_if_set_param.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_oport_set_stream_type`:

aio_oport_set_stream_type
=========================

.. c:function:: int aio_oport_set_stream_type(struct uniphier_aio_sub *sub, enum IEC61937_PC pc)

    set parameters of AIO playback port block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param pc:
        Pc type of IEC61937
    :type pc: enum IEC61937_PC

.. _`aio_oport_set_stream_type.description`:

Description
-----------

Set special setting to output port block of AIO to output the stream
via S/PDIF.

.. _`aio_oport_set_stream_type.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. _`aio_src_reset`:

aio_src_reset
=============

.. c:function:: void aio_src_reset(struct uniphier_aio_sub *sub)

    reset AIO SRC block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

.. _`aio_src_reset.description`:

Description
-----------

Resets the digital signal input/output port with sampling rate converter
block of AIO.
This function has no effect if substream is not supported rate converter.

.. _`aio_src_set_param`:

aio_src_set_param
=================

.. c:function:: int aio_src_set_param(struct uniphier_aio_sub *sub, const struct snd_pcm_hw_params *params)

    set parameters of AIO SRC block

    :param sub:
        the AIO substream pointer
    :type sub: struct uniphier_aio_sub \*

    :param params:
        hardware parameters of ALSA
    :type params: const struct snd_pcm_hw_params \*

.. _`aio_src_set_param.description`:

Description
-----------

Set suitable setting to input/output port with sampling rate converter
block of AIO to process the specified in params.
This function has no effect if substream is not supported rate converter.

.. _`aio_src_set_param.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. This file was automatic generated / don't edit.


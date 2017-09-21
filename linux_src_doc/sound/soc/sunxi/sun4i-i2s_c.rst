.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/sunxi/sun4i-i2s.c

.. _`sun4i_i2s_quirks`:

struct sun4i_i2s_quirks
=======================

.. c:type:: struct sun4i_i2s_quirks

    Differences between SoC variants.

.. _`sun4i_i2s_quirks.definition`:

Definition
----------

.. code-block:: c

    struct sun4i_i2s_quirks {
        bool has_reset;
        bool has_slave_select_bit;
        bool has_fmt_set_lrck_period;
        bool has_chcfg;
        bool has_chsel_tx_chen;
        bool has_chsel_offset;
        unsigned int reg_offset_txdata;
        const struct regmap_config *sun4i_i2s_regmap;
        unsigned int mclk_offset;
        unsigned int bclk_offset;
        unsigned int fmt_offset;
        struct reg_field field_clkdiv_mclk_en;
        struct reg_field field_fmt_wss;
        struct reg_field field_fmt_sr;
        struct reg_field field_fmt_bclk;
        struct reg_field field_fmt_lrclk;
        struct reg_field field_fmt_mode;
        struct reg_field field_txchanmap;
        struct reg_field field_rxchanmap;
        struct reg_field field_txchansel;
        struct reg_field field_rxchansel;
    }

.. _`sun4i_i2s_quirks.members`:

Members
-------

has_reset
    SoC needs reset deasserted.

has_slave_select_bit
    SoC has a bit to enable slave mode.

has_fmt_set_lrck_period
    SoC requires lrclk period to be set.

has_chcfg
    tx and rx slot number need to be set.

has_chsel_tx_chen
    SoC requires that the tx channels are enabled.

has_chsel_offset
    SoC uses offset for selecting dai operational mode.

reg_offset_txdata
    offset of the tx fifo.

sun4i_i2s_regmap
    regmap config to use.

mclk_offset
    Value by which mclkdiv needs to be adjusted.

bclk_offset
    Value by which bclkdiv needs to be adjusted.

fmt_offset
    Value by which wss and sr needs to be adjusted.

field_clkdiv_mclk_en
    regmap field to enable mclk output.

field_fmt_wss
    regmap field to set word select size.

field_fmt_sr
    regmap field to set sample resolution.

field_fmt_bclk
    regmap field to set clk polarity.

field_fmt_lrclk
    regmap field to set frame polarity.

field_fmt_mode
    regmap field to set the operational mode.

field_txchanmap
    location of the tx channel mapping register.

field_rxchanmap
    location of the rx channel mapping register.

field_txchansel
    location of the tx channel select bit fields.

field_rxchansel
    location of the rx channel select bit fields.

.. This file was automatic generated / don't edit.


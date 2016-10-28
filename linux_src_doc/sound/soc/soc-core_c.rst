.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-core.c

.. _`snd_soc_find_dai`:

snd_soc_find_dai
================

.. c:function:: struct snd_soc_dai *snd_soc_find_dai(const struct snd_soc_dai_link_component *dlc)

    Find a registered DAI

    :param const struct snd_soc_dai_link_component \*dlc:
        name of the DAI and optional component info to match

.. _`snd_soc_find_dai.description`:

Description
-----------

This function will search all regsitered components and their DAIs to
find the DAI of the same name. The component's of_node and name
should also match if being specified.

.. _`snd_soc_find_dai.return`:

Return
------

pointer of DAI, or NULL if not found.

.. _`snd_soc_add_dai_link`:

snd_soc_add_dai_link
====================

.. c:function:: int snd_soc_add_dai_link(struct snd_soc_card *card, struct snd_soc_dai_link *dai_link)

    Add a DAI link dynamically

    :param struct snd_soc_card \*card:
        The ASoC card to which the DAI link is added

    :param struct snd_soc_dai_link \*dai_link:
        The new DAI link to add

.. _`snd_soc_add_dai_link.description`:

Description
-----------

This function adds a DAI link to the ASoC card's link list.

.. _`snd_soc_add_dai_link.note`:

Note
----

Topology can use this API to add DAI links when probing the
topology component. And machine drivers can still define static
DAI links in dai_link array.

.. _`snd_soc_remove_dai_link`:

snd_soc_remove_dai_link
=======================

.. c:function:: void snd_soc_remove_dai_link(struct snd_soc_card *card, struct snd_soc_dai_link *dai_link)

    Remove a DAI link from the list

    :param struct snd_soc_card \*card:
        The ASoC card that owns the link

    :param struct snd_soc_dai_link \*dai_link:
        The DAI link to remove

.. _`snd_soc_remove_dai_link.description`:

Description
-----------

This function removes a DAI link from the ASoC card's link list.

For DAI links previously added by topology, topology should
remove them by using the dobj embedded in the link.

.. _`snd_soc_runtime_set_dai_fmt`:

snd_soc_runtime_set_dai_fmt
===========================

.. c:function:: int snd_soc_runtime_set_dai_fmt(struct snd_soc_pcm_runtime *rtd, unsigned int dai_fmt)

    Change DAI link format for a ASoC runtime

    :param struct snd_soc_pcm_runtime \*rtd:
        The runtime for which the DAI link format should be changed

    :param unsigned int dai_fmt:
        The new DAI link format

.. _`snd_soc_runtime_set_dai_fmt.description`:

Description
-----------

This function updates the DAI link format for all DAIs connected to the DAI
link for the specified runtime.

.. _`snd_soc_runtime_set_dai_fmt.note`:

Note
----

For setups with a static format set the dai_fmt field in the
corresponding snd_dai_link struct instead of using this function.

Returns 0 on success, otherwise a negative error code.

.. _`snd_soc_cnew`:

snd_soc_cnew
============

.. c:function:: struct snd_kcontrol *snd_soc_cnew(const struct snd_kcontrol_new *_template, void *data, const char *long_name, const char *prefix)

    create new control

    :param const struct snd_kcontrol_new \*_template:
        control template

    :param void \*data:
        control private data

    :param const char \*long_name:
        control long name

    :param const char \*prefix:
        control name prefix

.. _`snd_soc_cnew.description`:

Description
-----------

Create a new mixer control from a template control.

Returns 0 for success, else error.

.. _`snd_soc_add_component_controls`:

snd_soc_add_component_controls
==============================

.. c:function:: int snd_soc_add_component_controls(struct snd_soc_component *component, const struct snd_kcontrol_new *controls, unsigned int num_controls)

    Add an array of controls to a component.

    :param struct snd_soc_component \*component:
        Component to add controls to

    :param const struct snd_kcontrol_new \*controls:
        Array of controls to add

    :param unsigned int num_controls:
        Number of elements in the array

.. _`snd_soc_add_component_controls.return`:

Return
------

0 for success, else error.

.. _`snd_soc_add_codec_controls`:

snd_soc_add_codec_controls
==========================

.. c:function:: int snd_soc_add_codec_controls(struct snd_soc_codec *codec, const struct snd_kcontrol_new *controls, unsigned int num_controls)

    add an array of controls to a codec. Convenience function to add a list of controls. Many codecs were duplicating this code.

    :param struct snd_soc_codec \*codec:
        codec to add controls to

    :param const struct snd_kcontrol_new \*controls:
        array of controls to add

    :param unsigned int num_controls:
        number of elements in the array

.. _`snd_soc_add_codec_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_add_platform_controls`:

snd_soc_add_platform_controls
=============================

.. c:function:: int snd_soc_add_platform_controls(struct snd_soc_platform *platform, const struct snd_kcontrol_new *controls, unsigned int num_controls)

    add an array of controls to a platform. Convenience function to add a list of controls.

    :param struct snd_soc_platform \*platform:
        platform to add controls to

    :param const struct snd_kcontrol_new \*controls:
        array of controls to add

    :param unsigned int num_controls:
        number of elements in the array

.. _`snd_soc_add_platform_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_add_card_controls`:

snd_soc_add_card_controls
=========================

.. c:function:: int snd_soc_add_card_controls(struct snd_soc_card *soc_card, const struct snd_kcontrol_new *controls, int num_controls)

    add an array of controls to a SoC card. Convenience function to add a list of controls.

    :param struct snd_soc_card \*soc_card:
        SoC card to add controls to

    :param const struct snd_kcontrol_new \*controls:
        array of controls to add

    :param int num_controls:
        number of elements in the array

.. _`snd_soc_add_card_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_add_dai_controls`:

snd_soc_add_dai_controls
========================

.. c:function:: int snd_soc_add_dai_controls(struct snd_soc_dai *dai, const struct snd_kcontrol_new *controls, int num_controls)

    add an array of controls to a DAI. Convienience function to add a list of controls.

    :param struct snd_soc_dai \*dai:
        DAI to add controls to

    :param const struct snd_kcontrol_new \*controls:
        array of controls to add

    :param int num_controls:
        number of elements in the array

.. _`snd_soc_add_dai_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_dai_set_sysclk`:

snd_soc_dai_set_sysclk
======================

.. c:function:: int snd_soc_dai_set_sysclk(struct snd_soc_dai *dai, int clk_id, unsigned int freq, int dir)

    configure DAI system or master clock.

    :param struct snd_soc_dai \*dai:
        DAI

    :param int clk_id:
        DAI specific clock ID

    :param unsigned int freq:
        new clock frequency in Hz

    :param int dir:
        new clock direction - input/output.

.. _`snd_soc_dai_set_sysclk.description`:

Description
-----------

Configures the DAI master (MCLK) or system (SYSCLK) clocking.

.. _`snd_soc_codec_set_sysclk`:

snd_soc_codec_set_sysclk
========================

.. c:function:: int snd_soc_codec_set_sysclk(struct snd_soc_codec *codec, int clk_id, int source, unsigned int freq, int dir)

    configure CODEC system or master clock.

    :param struct snd_soc_codec \*codec:
        CODEC

    :param int clk_id:
        DAI specific clock ID

    :param int source:
        Source for the clock

    :param unsigned int freq:
        new clock frequency in Hz

    :param int dir:
        new clock direction - input/output.

.. _`snd_soc_codec_set_sysclk.description`:

Description
-----------

Configures the CODEC master (MCLK) or system (SYSCLK) clocking.

.. _`snd_soc_dai_set_clkdiv`:

snd_soc_dai_set_clkdiv
======================

.. c:function:: int snd_soc_dai_set_clkdiv(struct snd_soc_dai *dai, int div_id, int div)

    configure DAI clock dividers.

    :param struct snd_soc_dai \*dai:
        DAI

    :param int div_id:
        DAI specific clock divider ID

    :param int div:
        new clock divisor.

.. _`snd_soc_dai_set_clkdiv.description`:

Description
-----------

Configures the clock dividers. This is used to derive the best DAI bit and
frame clocks from the system or master clock. It's best to set the DAI bit
and frame clocks as low as possible to save system power.

.. _`snd_soc_dai_set_pll`:

snd_soc_dai_set_pll
===================

.. c:function:: int snd_soc_dai_set_pll(struct snd_soc_dai *dai, int pll_id, int source, unsigned int freq_in, unsigned int freq_out)

    configure DAI PLL.

    :param struct snd_soc_dai \*dai:
        DAI

    :param int pll_id:
        DAI specific PLL ID

    :param int source:
        DAI specific source for the PLL

    :param unsigned int freq_in:
        PLL input clock frequency in Hz

    :param unsigned int freq_out:
        requested PLL output clock frequency in Hz

.. _`snd_soc_dai_set_pll.description`:

Description
-----------

Configures and enables PLL to generate output clock based on input clock.

.. _`snd_soc_dai_set_bclk_ratio`:

snd_soc_dai_set_bclk_ratio
==========================

.. c:function:: int snd_soc_dai_set_bclk_ratio(struct snd_soc_dai *dai, unsigned int ratio)

    configure BCLK to sample rate ratio.

    :param struct snd_soc_dai \*dai:
        DAI

    :param unsigned int ratio:
        Ratio of BCLK to Sample rate.

.. _`snd_soc_dai_set_bclk_ratio.description`:

Description
-----------

Configures the DAI for a preset BCLK to sample rate ratio.

.. _`snd_soc_dai_set_fmt`:

snd_soc_dai_set_fmt
===================

.. c:function:: int snd_soc_dai_set_fmt(struct snd_soc_dai *dai, unsigned int fmt)

    configure DAI hardware audio format.

    :param struct snd_soc_dai \*dai:
        DAI

    :param unsigned int fmt:
        SND_SOC_DAIFMT\_ format value.

.. _`snd_soc_dai_set_fmt.description`:

Description
-----------

Configures the DAI hardware format and clocking.

.. _`snd_soc_xlate_tdm_slot_mask`:

snd_soc_xlate_tdm_slot_mask
===========================

.. c:function:: int snd_soc_xlate_tdm_slot_mask(unsigned int slots, unsigned int *tx_mask, unsigned int *rx_mask)

    generate tx/rx slot mask.

    :param unsigned int slots:
        Number of slots in use.

    :param unsigned int \*tx_mask:
        bitmask representing active TX slots.

    :param unsigned int \*rx_mask:
        bitmask representing active RX slots.

.. _`snd_soc_xlate_tdm_slot_mask.description`:

Description
-----------

Generates the TDM tx and rx slot default masks for DAI.

.. _`snd_soc_dai_set_tdm_slot`:

snd_soc_dai_set_tdm_slot
========================

.. c:function:: int snd_soc_dai_set_tdm_slot(struct snd_soc_dai *dai, unsigned int tx_mask, unsigned int rx_mask, int slots, int slot_width)

    Configures a DAI for TDM operation

    :param struct snd_soc_dai \*dai:
        The DAI to configure

    :param unsigned int tx_mask:
        bitmask representing active TX slots.

    :param unsigned int rx_mask:
        bitmask representing active RX slots.

    :param int slots:
        Number of slots in use.

    :param int slot_width:
        Width in bits for each slot.

.. _`snd_soc_dai_set_tdm_slot.description`:

Description
-----------

This function configures the specified DAI for TDM operation. \ ``slot``\  contains
the total number of slots of the TDM stream and \ ``slot_with``\  the width of each
slot in bit clock cycles. \ ``tx_mask``\  and \ ``rx_mask``\  are bitmasks specifying the
active slots of the TDM stream for the specified DAI, i.e. which slots the
DAI should write to or read from. If a bit is set the corresponding slot is
active, if a bit is cleared the corresponding slot is inactive. Bit 0 maps to
the first slot, bit 1 to the second slot and so on. The first active slot
maps to the first channel of the DAI, the second active slot to the second
channel and so on.

TDM mode can be disabled by passing 0 for \ ``slots``\ . In this case \ ``tx_mask``\ ,
\ ``rx_mask``\  and \ ``slot_width``\  will be ignored.

Returns 0 on success, a negative error code otherwise.

.. _`snd_soc_dai_set_channel_map`:

snd_soc_dai_set_channel_map
===========================

.. c:function:: int snd_soc_dai_set_channel_map(struct snd_soc_dai *dai, unsigned int tx_num, unsigned int *tx_slot, unsigned int rx_num, unsigned int *rx_slot)

    configure DAI audio channel map

    :param struct snd_soc_dai \*dai:
        DAI

    :param unsigned int tx_num:
        how many TX channels

    :param unsigned int \*tx_slot:
        pointer to an array which imply the TX slot number channel
        0~num-1 uses

    :param unsigned int rx_num:
        how many RX channels

    :param unsigned int \*rx_slot:
        pointer to an array which imply the RX slot number channel
        0~num-1 uses

.. _`snd_soc_dai_set_channel_map.description`:

Description
-----------

configure the relationship between channel number and TDM slot number.

.. _`snd_soc_dai_set_tristate`:

snd_soc_dai_set_tristate
========================

.. c:function:: int snd_soc_dai_set_tristate(struct snd_soc_dai *dai, int tristate)

    configure DAI system or master clock.

    :param struct snd_soc_dai \*dai:
        DAI

    :param int tristate:
        tristate enable

.. _`snd_soc_dai_set_tristate.description`:

Description
-----------

Tristates the DAI so that others can use it.

.. _`snd_soc_dai_digital_mute`:

snd_soc_dai_digital_mute
========================

.. c:function:: int snd_soc_dai_digital_mute(struct snd_soc_dai *dai, int mute, int direction)

    configure DAI system or master clock.

    :param struct snd_soc_dai \*dai:
        DAI

    :param int mute:
        mute enable

    :param int direction:
        stream to mute

.. _`snd_soc_dai_digital_mute.description`:

Description
-----------

Mutes the DAI DAC.

.. _`snd_soc_register_card`:

snd_soc_register_card
=====================

.. c:function:: int snd_soc_register_card(struct snd_soc_card *card)

    Register a card with the ASoC core

    :param struct snd_soc_card \*card:
        Card to register

.. _`snd_soc_unregister_card`:

snd_soc_unregister_card
=======================

.. c:function:: int snd_soc_unregister_card(struct snd_soc_card *card)

    Unregister a card with the ASoC core

    :param struct snd_soc_card \*card:
        Card to unregister

.. _`snd_soc_unregister_dais`:

snd_soc_unregister_dais
=======================

.. c:function:: void snd_soc_unregister_dais(struct snd_soc_component *component)

    Unregister DAIs from the ASoC core

    :param struct snd_soc_component \*component:
        The component for which the DAIs should be unregistered

.. _`snd_soc_register_dais`:

snd_soc_register_dais
=====================

.. c:function:: int snd_soc_register_dais(struct snd_soc_component *component, struct snd_soc_dai_driver *dai_drv, size_t count, bool legacy_dai_naming)

    Register a DAI with the ASoC core

    :param struct snd_soc_component \*component:
        The component the DAIs are registered for

    :param struct snd_soc_dai_driver \*dai_drv:
        DAI driver to use for the DAIs

    :param size_t count:
        Number of DAIs

    :param bool legacy_dai_naming:
        Use the legacy naming scheme and let the DAI inherit the
        parent's name.

.. _`snd_soc_register_dai`:

snd_soc_register_dai
====================

.. c:function:: int snd_soc_register_dai(struct snd_soc_component *component, struct snd_soc_dai_driver *dai_drv)

    Register a DAI dynamically & create its widgets

    :param struct snd_soc_component \*component:
        The component the DAIs are registered for

    :param struct snd_soc_dai_driver \*dai_drv:
        DAI driver to use for the DAI

.. _`snd_soc_register_dai.description`:

Description
-----------

Topology can use this API to register DAIs when probing a component.
These DAIs's widgets will be freed in the card cleanup and the DAIs
will be freed in the component cleanup.

.. _`snd_soc_component_init_regmap`:

snd_soc_component_init_regmap
=============================

.. c:function:: void snd_soc_component_init_regmap(struct snd_soc_component *component, struct regmap *regmap)

    Initialize regmap instance for the component

    :param struct snd_soc_component \*component:
        The component for which to initialize the regmap instance

    :param struct regmap \*regmap:
        The regmap instance that should be used by the component

.. _`snd_soc_component_init_regmap.description`:

Description
-----------

This function allows deferred assignment of the regmap instance that is
associated with the component. Only use this if the regmap instance is not
yet ready when the component is registered. The function must also be called
before the first IO attempt of the component.

.. _`snd_soc_component_exit_regmap`:

snd_soc_component_exit_regmap
=============================

.. c:function:: void snd_soc_component_exit_regmap(struct snd_soc_component *component)

    De-initialize regmap instance for the component

    :param struct snd_soc_component \*component:
        The component for which to de-initialize the regmap instance

.. _`snd_soc_component_exit_regmap.description`:

Description
-----------

Calls \ :c:func:`regmap_exit`\  on the regmap instance associated to the component and
removes the regmap instance from the component.

This function should only be used if \ :c:func:`snd_soc_component_init_regmap`\  was used
to initialize the regmap instance.

.. _`snd_soc_unregister_component`:

snd_soc_unregister_component
============================

.. c:function:: void snd_soc_unregister_component(struct device *dev)

    Unregister a component from the ASoC core

    :param struct device \*dev:
        The device to unregister

.. _`snd_soc_add_platform`:

snd_soc_add_platform
====================

.. c:function:: int snd_soc_add_platform(struct device *dev, struct snd_soc_platform *platform, const struct snd_soc_platform_driver *platform_drv)

    Add a platform to the ASoC core

    :param struct device \*dev:
        The parent device for the platform

    :param struct snd_soc_platform \*platform:
        The platform to add

    :param const struct snd_soc_platform_driver \*platform_drv:
        The driver for the platform

.. _`snd_soc_register_platform`:

snd_soc_register_platform
=========================

.. c:function:: int snd_soc_register_platform(struct device *dev, const struct snd_soc_platform_driver *platform_drv)

    Register a platform with the ASoC core

    :param struct device \*dev:
        The device for the platform

    :param const struct snd_soc_platform_driver \*platform_drv:
        The driver for the platform

.. _`snd_soc_remove_platform`:

snd_soc_remove_platform
=======================

.. c:function:: void snd_soc_remove_platform(struct snd_soc_platform *platform)

    Remove a platform from the ASoC core

    :param struct snd_soc_platform \*platform:
        the platform to remove

.. _`snd_soc_unregister_platform`:

snd_soc_unregister_platform
===========================

.. c:function:: void snd_soc_unregister_platform(struct device *dev)

    Unregister a platform from the ASoC core

    :param struct device \*dev:
        platform to unregister

.. _`snd_soc_register_codec`:

snd_soc_register_codec
======================

.. c:function:: int snd_soc_register_codec(struct device *dev, const struct snd_soc_codec_driver *codec_drv, struct snd_soc_dai_driver *dai_drv, int num_dai)

    Register a codec with the ASoC core

    :param struct device \*dev:
        The parent device for this codec

    :param const struct snd_soc_codec_driver \*codec_drv:
        Codec driver

    :param struct snd_soc_dai_driver \*dai_drv:
        The associated DAI driver

    :param int num_dai:
        Number of DAIs

.. _`snd_soc_unregister_codec`:

snd_soc_unregister_codec
========================

.. c:function:: void snd_soc_unregister_codec(struct device *dev)

    Unregister a codec from the ASoC core

    :param struct device \*dev:
        codec to unregister

.. This file was automatic generated / don't edit.


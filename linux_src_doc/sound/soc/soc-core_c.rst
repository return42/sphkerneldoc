.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-core.c

.. _`snd_soc_find_dai`:

snd_soc_find_dai
================

.. c:function:: struct snd_soc_dai *snd_soc_find_dai(const struct snd_soc_dai_link_component *dlc)

    Find a registered DAI

    :param dlc:
        name of the DAI or the DAI driver and optional component info to match
    :type dlc: const struct snd_soc_dai_link_component \*

.. _`snd_soc_find_dai.description`:

Description
-----------

This function will search all registered components and their DAIs to
find the DAI of the same name. The component's of_node and name
should also match if being specified.

.. _`snd_soc_find_dai.return`:

Return
------

pointer of DAI, or NULL if not found.

.. _`snd_soc_find_dai_link`:

snd_soc_find_dai_link
=====================

.. c:function:: struct snd_soc_dai_link *snd_soc_find_dai_link(struct snd_soc_card *card, int id, const char *name, const char *stream_name)

    Find a DAI link

    :param card:
        soc card
    :type card: struct snd_soc_card \*

    :param id:
        DAI link ID to match
    :type id: int

    :param name:
        DAI link name to match, optional
    :type name: const char \*

    :param stream_name:
        DAI link stream name to match, optional
    :type stream_name: const char \*

.. _`snd_soc_find_dai_link.description`:

Description
-----------

This function will search all existing DAI links of the soc card to
find the link of the same ID. Since DAI links may not have their
unique ID, so name and stream name should also match if being
specified.

.. _`snd_soc_find_dai_link.return`:

Return
------

pointer of DAI link, or NULL if not found.

.. _`snd_soc_add_dai_link`:

snd_soc_add_dai_link
====================

.. c:function:: int snd_soc_add_dai_link(struct snd_soc_card *card, struct snd_soc_dai_link *dai_link)

    Add a DAI link dynamically

    :param card:
        The ASoC card to which the DAI link is added
    :type card: struct snd_soc_card \*

    :param dai_link:
        The new DAI link to add
    :type dai_link: struct snd_soc_dai_link \*

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

    :param card:
        The ASoC card that owns the link
    :type card: struct snd_soc_card \*

    :param dai_link:
        The DAI link to remove
    :type dai_link: struct snd_soc_dai_link \*

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

    :param rtd:
        The runtime for which the DAI link format should be changed
    :type rtd: struct snd_soc_pcm_runtime \*

    :param dai_fmt:
        The new DAI link format
    :type dai_fmt: unsigned int

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

.. _`snd_soc_set_dmi_name`:

snd_soc_set_dmi_name
====================

.. c:function:: int snd_soc_set_dmi_name(struct snd_soc_card *card, const char *flavour)

    Register DMI names to card

    :param card:
        The card to register DMI names
    :type card: struct snd_soc_card \*

    :param flavour:
        The flavour "differentiator" for the card amongst its peers.
    :type flavour: const char \*

.. _`snd_soc_set_dmi_name.description`:

Description
-----------

An Intel machine driver may be used by many different devices but are
difficult for userspace to differentiate, since machine drivers ususally
use their own name as the card short name and leave the card long name
blank. To differentiate such devices and fix bugs due to lack of
device-specific configurations, this function allows DMI info to be used
as the sound card long name, in the format of
"vendor-product-version-board"
(Character '-' is used to separate different DMI fields here).
This will help the user space to load the device-specific Use Case Manager
(UCM) configurations for the card.

.. _`snd_soc_set_dmi_name.possible-card-long-names-may-be`:

Possible card long names may be
-------------------------------

DellInc.-XPS139343-01-0310JH
ASUSTeKCOMPUTERINC.-T100TA-1.0-T100TA
Circuitco-MinnowboardMaxD0PLATFORM-D0-MinnowBoardMAX

This function also supports flavoring the card longname to provide
the extra differentiation, like "vendor-product-version-board-flavor".

We only keep number and alphabet characters and a few separator characters
in the card long name since UCM in the user space uses the card long names
as card configuration directory names and AudoConf cannot support special
charactors like SPACE.

Returns 0 on success, otherwise a negative error code.

.. _`snd_soc_cnew`:

snd_soc_cnew
============

.. c:function:: struct snd_kcontrol *snd_soc_cnew(const struct snd_kcontrol_new *_template, void *data, const char *long_name, const char *prefix)

    create new control

    :param _template:
        control template
    :type _template: const struct snd_kcontrol_new \*

    :param data:
        control private data
    :type data: void \*

    :param long_name:
        control long name
    :type long_name: const char \*

    :param prefix:
        control name prefix
    :type prefix: const char \*

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

    :param component:
        Component to add controls to
    :type component: struct snd_soc_component \*

    :param controls:
        Array of controls to add
    :type controls: const struct snd_kcontrol_new \*

    :param num_controls:
        Number of elements in the array
    :type num_controls: unsigned int

.. _`snd_soc_add_component_controls.return`:

Return
------

0 for success, else error.

.. _`snd_soc_add_card_controls`:

snd_soc_add_card_controls
=========================

.. c:function:: int snd_soc_add_card_controls(struct snd_soc_card *soc_card, const struct snd_kcontrol_new *controls, int num_controls)

    add an array of controls to a SoC card. Convenience function to add a list of controls.

    :param soc_card:
        SoC card to add controls to
    :type soc_card: struct snd_soc_card \*

    :param controls:
        array of controls to add
    :type controls: const struct snd_kcontrol_new \*

    :param num_controls:
        number of elements in the array
    :type num_controls: int

.. _`snd_soc_add_card_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_add_dai_controls`:

snd_soc_add_dai_controls
========================

.. c:function:: int snd_soc_add_dai_controls(struct snd_soc_dai *dai, const struct snd_kcontrol_new *controls, int num_controls)

    add an array of controls to a DAI. Convienience function to add a list of controls.

    :param dai:
        DAI to add controls to
    :type dai: struct snd_soc_dai \*

    :param controls:
        array of controls to add
    :type controls: const struct snd_kcontrol_new \*

    :param num_controls:
        number of elements in the array
    :type num_controls: int

.. _`snd_soc_add_dai_controls.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_dai_set_sysclk`:

snd_soc_dai_set_sysclk
======================

.. c:function:: int snd_soc_dai_set_sysclk(struct snd_soc_dai *dai, int clk_id, unsigned int freq, int dir)

    configure DAI system or master clock.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param clk_id:
        DAI specific clock ID
    :type clk_id: int

    :param freq:
        new clock frequency in Hz
    :type freq: unsigned int

    :param dir:
        new clock direction - input/output.
    :type dir: int

.. _`snd_soc_dai_set_sysclk.description`:

Description
-----------

Configures the DAI master (MCLK) or system (SYSCLK) clocking.

.. _`snd_soc_component_set_sysclk`:

snd_soc_component_set_sysclk
============================

.. c:function:: int snd_soc_component_set_sysclk(struct snd_soc_component *component, int clk_id, int source, unsigned int freq, int dir)

    configure COMPONENT system or master clock.

    :param component:
        COMPONENT
    :type component: struct snd_soc_component \*

    :param clk_id:
        DAI specific clock ID
    :type clk_id: int

    :param source:
        Source for the clock
    :type source: int

    :param freq:
        new clock frequency in Hz
    :type freq: unsigned int

    :param dir:
        new clock direction - input/output.
    :type dir: int

.. _`snd_soc_component_set_sysclk.description`:

Description
-----------

Configures the CODEC master (MCLK) or system (SYSCLK) clocking.

.. _`snd_soc_dai_set_clkdiv`:

snd_soc_dai_set_clkdiv
======================

.. c:function:: int snd_soc_dai_set_clkdiv(struct snd_soc_dai *dai, int div_id, int div)

    configure DAI clock dividers.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param div_id:
        DAI specific clock divider ID
    :type div_id: int

    :param div:
        new clock divisor.
    :type div: int

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

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param pll_id:
        DAI specific PLL ID
    :type pll_id: int

    :param source:
        DAI specific source for the PLL
    :type source: int

    :param freq_in:
        PLL input clock frequency in Hz
    :type freq_in: unsigned int

    :param freq_out:
        requested PLL output clock frequency in Hz
    :type freq_out: unsigned int

.. _`snd_soc_dai_set_pll.description`:

Description
-----------

Configures and enables PLL to generate output clock based on input clock.

.. _`snd_soc_dai_set_bclk_ratio`:

snd_soc_dai_set_bclk_ratio
==========================

.. c:function:: int snd_soc_dai_set_bclk_ratio(struct snd_soc_dai *dai, unsigned int ratio)

    configure BCLK to sample rate ratio.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param ratio:
        Ratio of BCLK to Sample rate.
    :type ratio: unsigned int

.. _`snd_soc_dai_set_bclk_ratio.description`:

Description
-----------

Configures the DAI for a preset BCLK to sample rate ratio.

.. _`snd_soc_dai_set_fmt`:

snd_soc_dai_set_fmt
===================

.. c:function:: int snd_soc_dai_set_fmt(struct snd_soc_dai *dai, unsigned int fmt)

    configure DAI hardware audio format.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param fmt:
        SND_SOC_DAIFMT_* format value.
    :type fmt: unsigned int

.. _`snd_soc_dai_set_fmt.description`:

Description
-----------

Configures the DAI hardware format and clocking.

.. _`snd_soc_xlate_tdm_slot_mask`:

snd_soc_xlate_tdm_slot_mask
===========================

.. c:function:: int snd_soc_xlate_tdm_slot_mask(unsigned int slots, unsigned int *tx_mask, unsigned int *rx_mask)

    generate tx/rx slot mask.

    :param slots:
        Number of slots in use.
    :type slots: unsigned int

    :param tx_mask:
        bitmask representing active TX slots.
    :type tx_mask: unsigned int \*

    :param rx_mask:
        bitmask representing active RX slots.
    :type rx_mask: unsigned int \*

.. _`snd_soc_xlate_tdm_slot_mask.description`:

Description
-----------

Generates the TDM tx and rx slot default masks for DAI.

.. _`snd_soc_dai_set_tdm_slot`:

snd_soc_dai_set_tdm_slot
========================

.. c:function:: int snd_soc_dai_set_tdm_slot(struct snd_soc_dai *dai, unsigned int tx_mask, unsigned int rx_mask, int slots, int slot_width)

    Configures a DAI for TDM operation

    :param dai:
        The DAI to configure
    :type dai: struct snd_soc_dai \*

    :param tx_mask:
        bitmask representing active TX slots.
    :type tx_mask: unsigned int

    :param rx_mask:
        bitmask representing active RX slots.
    :type rx_mask: unsigned int

    :param slots:
        Number of slots in use.
    :type slots: int

    :param slot_width:
        Width in bits for each slot.
    :type slot_width: int

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

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param tx_num:
        how many TX channels
    :type tx_num: unsigned int

    :param tx_slot:
        pointer to an array which imply the TX slot number channel
        0~num-1 uses
    :type tx_slot: unsigned int \*

    :param rx_num:
        how many RX channels
    :type rx_num: unsigned int

    :param rx_slot:
        pointer to an array which imply the RX slot number channel
        0~num-1 uses
    :type rx_slot: unsigned int \*

.. _`snd_soc_dai_set_channel_map.description`:

Description
-----------

configure the relationship between channel number and TDM slot number.

.. _`snd_soc_dai_get_channel_map`:

snd_soc_dai_get_channel_map
===========================

.. c:function:: int snd_soc_dai_get_channel_map(struct snd_soc_dai *dai, unsigned int *tx_num, unsigned int *tx_slot, unsigned int *rx_num, unsigned int *rx_slot)

    Get DAI audio channel map

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param tx_num:
        how many TX channels
    :type tx_num: unsigned int \*

    :param tx_slot:
        pointer to an array which imply the TX slot number channel
        0~num-1 uses
    :type tx_slot: unsigned int \*

    :param rx_num:
        how many RX channels
    :type rx_num: unsigned int \*

    :param rx_slot:
        pointer to an array which imply the RX slot number channel
        0~num-1 uses
    :type rx_slot: unsigned int \*

.. _`snd_soc_dai_set_tristate`:

snd_soc_dai_set_tristate
========================

.. c:function:: int snd_soc_dai_set_tristate(struct snd_soc_dai *dai, int tristate)

    configure DAI system or master clock.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param tristate:
        tristate enable
    :type tristate: int

.. _`snd_soc_dai_set_tristate.description`:

Description
-----------

Tristates the DAI so that others can use it.

.. _`snd_soc_dai_digital_mute`:

snd_soc_dai_digital_mute
========================

.. c:function:: int snd_soc_dai_digital_mute(struct snd_soc_dai *dai, int mute, int direction)

    configure DAI system or master clock.

    :param dai:
        DAI
    :type dai: struct snd_soc_dai \*

    :param mute:
        mute enable
    :type mute: int

    :param direction:
        stream to mute
    :type direction: int

.. _`snd_soc_dai_digital_mute.description`:

Description
-----------

Mutes the DAI DAC.

.. _`snd_soc_register_card`:

snd_soc_register_card
=====================

.. c:function:: int snd_soc_register_card(struct snd_soc_card *card)

    Register a card with the ASoC core

    :param card:
        Card to register
    :type card: struct snd_soc_card \*

.. _`snd_soc_unregister_card`:

snd_soc_unregister_card
=======================

.. c:function:: int snd_soc_unregister_card(struct snd_soc_card *card)

    Unregister a card with the ASoC core

    :param card:
        Card to unregister
    :type card: struct snd_soc_card \*

.. _`snd_soc_unregister_dais`:

snd_soc_unregister_dais
=======================

.. c:function:: void snd_soc_unregister_dais(struct snd_soc_component *component)

    Unregister DAIs from the ASoC core

    :param component:
        The component for which the DAIs should be unregistered
    :type component: struct snd_soc_component \*

.. _`snd_soc_register_dais`:

snd_soc_register_dais
=====================

.. c:function:: int snd_soc_register_dais(struct snd_soc_component *component, struct snd_soc_dai_driver *dai_drv, size_t count)

    Register a DAI with the ASoC core

    :param component:
        The component the DAIs are registered for
    :type component: struct snd_soc_component \*

    :param dai_drv:
        DAI driver to use for the DAIs
    :type dai_drv: struct snd_soc_dai_driver \*

    :param count:
        Number of DAIs
    :type count: size_t

.. _`snd_soc_register_dai`:

snd_soc_register_dai
====================

.. c:function:: int snd_soc_register_dai(struct snd_soc_component *component, struct snd_soc_dai_driver *dai_drv)

    Register a DAI dynamically & create its widgets

    :param component:
        The component the DAIs are registered for
    :type component: struct snd_soc_component \*

    :param dai_drv:
        DAI driver to use for the DAI
    :type dai_drv: struct snd_soc_dai_driver \*

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

    :param component:
        The component for which to initialize the regmap instance
    :type component: struct snd_soc_component \*

    :param regmap:
        The regmap instance that should be used by the component
    :type regmap: struct regmap \*

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

    :param component:
        The component for which to de-initialize the regmap instance
    :type component: struct snd_soc_component \*

.. _`snd_soc_component_exit_regmap.description`:

Description
-----------

Calls \ :c:func:`regmap_exit`\  on the regmap instance associated to the component and
removes the regmap instance from the component.

This function should only be used if \ :c:func:`snd_soc_component_init_regmap`\  was used
to initialize the regmap instance.

.. _`__snd_soc_unregister_component`:

__snd_soc_unregister_component
==============================

.. c:function:: int __snd_soc_unregister_component(struct device *dev)

    Unregister all related component from the ASoC core

    :param dev:
        The device to unregister
    :type dev: struct device \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-devres.c

.. _`devm_snd_soc_register_component`:

devm_snd_soc_register_component
===============================

.. c:function:: int devm_snd_soc_register_component(struct device *dev, const struct snd_soc_component_driver *cmpnt_drv, struct snd_soc_dai_driver *dai_drv, int num_dai)

    resource managed component registration

    :param dev:
        Device used to manage component
    :type dev: struct device \*

    :param cmpnt_drv:
        Component driver
    :type cmpnt_drv: const struct snd_soc_component_driver \*

    :param dai_drv:
        DAI driver
    :type dai_drv: struct snd_soc_dai_driver \*

    :param num_dai:
        Number of DAIs to register
    :type num_dai: int

.. _`devm_snd_soc_register_component.description`:

Description
-----------

Register a component with automatic unregistration when the device is
unregistered.

.. _`devm_snd_soc_register_card`:

devm_snd_soc_register_card
==========================

.. c:function:: int devm_snd_soc_register_card(struct device *dev, struct snd_soc_card *card)

    resource managed card registration

    :param dev:
        Device used to manage card
    :type dev: struct device \*

    :param card:
        Card to register
    :type card: struct snd_soc_card \*

.. _`devm_snd_soc_register_card.description`:

Description
-----------

Register a card with automatic unregistration when the device is
unregistered.

.. _`devm_snd_dmaengine_pcm_register`:

devm_snd_dmaengine_pcm_register
===============================

.. c:function:: int devm_snd_dmaengine_pcm_register(struct device *dev, const struct snd_dmaengine_pcm_config *config, unsigned int flags)

    resource managed dmaengine PCM registration

    :param dev:
        The parent device for the PCM device
    :type dev: struct device \*

    :param config:
        Platform specific PCM configuration
    :type config: const struct snd_dmaengine_pcm_config \*

    :param flags:
        Platform specific quirks
    :type flags: unsigned int

.. _`devm_snd_dmaengine_pcm_register.description`:

Description
-----------

Register a dmaengine based PCM device with automatic unregistration when the
device is unregistered.

.. This file was automatic generated / don't edit.


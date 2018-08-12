.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-devres.c

.. _`devm_snd_soc_register_component`:

devm_snd_soc_register_component
===============================

.. c:function:: int devm_snd_soc_register_component(struct device *dev, const struct snd_soc_component_driver *cmpnt_drv, struct snd_soc_dai_driver *dai_drv, int num_dai)

    resource managed component registration

    :param struct device \*dev:
        Device used to manage component

    :param const struct snd_soc_component_driver \*cmpnt_drv:
        Component driver

    :param struct snd_soc_dai_driver \*dai_drv:
        DAI driver

    :param int num_dai:
        Number of DAIs to register

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

    :param struct device \*dev:
        Device used to manage card

    :param struct snd_soc_card \*card:
        Card to register

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

    :param struct device \*dev:
        The parent device for the PCM device

    :param const struct snd_dmaengine_pcm_config \*config:
        Platform specific PCM configuration

    :param unsigned int flags:
        Platform specific quirks

.. _`devm_snd_dmaengine_pcm_register.description`:

Description
-----------

Register a dmaengine based PCM device with automatic unregistration when the
device is unregistered.

.. This file was automatic generated / don't edit.


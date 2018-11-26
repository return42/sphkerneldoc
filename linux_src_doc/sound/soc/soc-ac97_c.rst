.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-ac97.c

.. _`snd_soc_alloc_ac97_component`:

snd_soc_alloc_ac97_component
============================

.. c:function:: struct snd_ac97 *snd_soc_alloc_ac97_component(struct snd_soc_component *component)

    Allocate new a AC'97 device

    :param component:
        The COMPONENT for which to create the AC'97 device
    :type component: struct snd_soc_component \*

.. _`snd_soc_alloc_ac97_component.description`:

Description
-----------

Allocated a new snd_ac97 device and intializes it, but does not yet register
it. The caller is responsible to either call device_add(&ac97->dev) to
register the device, or to call put_device(&ac97->dev) to free the device.

.. _`snd_soc_alloc_ac97_component.return`:

Return
------

A snd_ac97 device or a PTR_ERR in case of an error.

.. _`snd_soc_new_ac97_component`:

snd_soc_new_ac97_component
==========================

.. c:function:: struct snd_ac97 *snd_soc_new_ac97_component(struct snd_soc_component *component, unsigned int id, unsigned int id_mask)

    initailise AC97 device

    :param component:
        audio component
    :type component: struct snd_soc_component \*

    :param id:
        The expected device ID
    :type id: unsigned int

    :param id_mask:
        Mask that is applied to the device ID before comparing with \ ``id``\ 
    :type id_mask: unsigned int

.. _`snd_soc_new_ac97_component.description`:

Description
-----------

Initialises AC97 component resources for use by ad-hoc devices only.

If \ ``id``\  is not 0 this function will reset the device, then read the ID from
the device and check if it matches the expected ID. If it doesn't match an
error will be returned and device will not be registered.

.. _`snd_soc_new_ac97_component.return`:

Return
------

A \ :c:func:`PTR_ERR`\  on failure or a valid snd_ac97 struct on success.

.. _`snd_soc_free_ac97_component`:

snd_soc_free_ac97_component
===========================

.. c:function:: void snd_soc_free_ac97_component(struct snd_ac97 *ac97)

    free AC97 component device

    :param ac97:
        snd_ac97 device to be freed
    :type ac97: struct snd_ac97 \*

.. _`snd_soc_free_ac97_component.description`:

Description
-----------

Frees AC97 component device resources.

.. _`snd_soc_set_ac97_ops_of_reset`:

snd_soc_set_ac97_ops_of_reset
=============================

.. c:function:: int snd_soc_set_ac97_ops_of_reset(struct snd_ac97_bus_ops *ops, struct platform_device *pdev)

    Set ac97 ops with generic ac97 reset functions

    :param ops:
        *undescribed*
    :type ops: struct snd_ac97_bus_ops \*

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`snd_soc_set_ac97_ops_of_reset.description`:

Description
-----------

This function sets the reset and warm_reset properties of ops and parses
the device node of pdev to get pinctrl states and gpio numbers to use.

.. This file was automatic generated / don't edit.


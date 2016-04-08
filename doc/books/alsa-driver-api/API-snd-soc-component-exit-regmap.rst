
.. _API-snd-soc-component-exit-regmap:

=============================
snd_soc_component_exit_regmap
=============================

*man snd_soc_component_exit_regmap(9)*

*4.6.0-rc1*

De-initialize regmap instance for the component


Synopsis
========

.. c:function:: void snd_soc_component_exit_regmap( struct snd_soc_component * component )

Arguments
=========

``component``
    The component for which to de-initialize the regmap instance


Description
===========

Calls ``regmap_exit`` on the regmap instance associated to the component and removes the regmap instance from the component.

This function should only be used if ``snd_soc_component_init_regmap`` was used to initialize the regmap instance.

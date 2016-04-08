
.. _API-snd-soc-component-init-regmap:

=============================
snd_soc_component_init_regmap
=============================

*man snd_soc_component_init_regmap(9)*

*4.6.0-rc1*

Initialize regmap instance for the component


Synopsis
========

.. c:function:: void snd_soc_component_init_regmap( struct snd_soc_component * component, struct regmap * regmap )

Arguments
=========

``component``
    The component for which to initialize the regmap instance

``regmap``
    The regmap instance that should be used by the component


Description
===========

This function allows deferred assignment of the regmap instance that is associated with the component. Only use this if the regmap instance is not yet ready when the component is
registered. The function must also be called before the first IO attempt of the component.

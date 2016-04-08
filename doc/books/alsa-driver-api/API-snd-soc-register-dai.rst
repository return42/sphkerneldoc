
.. _API-snd-soc-register-dai:

====================
snd_soc_register_dai
====================

*man snd_soc_register_dai(9)*

*4.6.0-rc1*

Register a DAI dynamically & create its widgets


Synopsis
========

.. c:function:: int snd_soc_register_dai( struct snd_soc_component * component, struct snd_soc_dai_driver * dai_drv )

Arguments
=========

``component``
    The component the DAIs are registered for

``dai_drv``
    DAI driver to use for the DAI


Description
===========

Topology can use this API to register DAIs when probing a component. These DAIs's widgets will be freed in the card cleanup and the DAIs will be freed in the component cleanup.

.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-register-dai:

====================
snd_soc_register_dai
====================

*man snd_soc_register_dai(9)*

*4.6.0-rc5*

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

Topology can use this API to register DAIs when probing a component.
These DAIs's widgets will be freed in the card cleanup and the DAIs will
be freed in the component cleanup.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

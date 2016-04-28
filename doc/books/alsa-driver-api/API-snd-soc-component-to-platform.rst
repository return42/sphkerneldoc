.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-component-to-platform:

=============================
snd_soc_component_to_platform
=============================

*man snd_soc_component_to_platform(9)*

*4.6.0-rc5*

Casts a component to the platform it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_platform * snd_soc_component_to_platform( struct snd_soc_component * component )

Arguments
=========

``component``
    The component to cast to a platform


Description
===========

This function must only be used on components that are known to be
platforms. Otherwise the behavior is undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-component-to-codec:

==========================
snd_soc_component_to_codec
==========================

*man snd_soc_component_to_codec(9)*

*4.6.0-rc5*

Casts a component to the CODEC it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_codec * snd_soc_component_to_codec( struct snd_soc_component * component )

Arguments
=========

``component``
    The component to cast to a CODEC


Description
===========

This function must only be used on components that are known to be
CODECs. Otherwise the behavior is undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

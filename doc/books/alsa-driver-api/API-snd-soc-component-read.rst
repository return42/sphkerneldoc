.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-component-read:

======================
snd_soc_component_read
======================

*man snd_soc_component_read(9)*

*4.6.0-rc5*

Read register value


Synopsis
========

.. c:function:: int snd_soc_component_read( struct snd_soc_component * component, unsigned int reg, unsigned int * val )

Arguments
=========

``component``
    Component to read from

``reg``
    Register to read

``val``
    Pointer to where the read value is stored


Return
======

0 on success, a negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

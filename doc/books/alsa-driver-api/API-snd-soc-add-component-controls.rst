.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-add-component-controls:

==============================
snd_soc_add_component_controls
==============================

*man snd_soc_add_component_controls(9)*

*4.6.0-rc5*

Add an array of controls to a component.


Synopsis
========

.. c:function:: int snd_soc_add_component_controls( struct snd_soc_component * component, const struct snd_kcontrol_new * controls, unsigned int num_controls )

Arguments
=========

``component``
    Component to add controls to

``controls``
    Array of controls to add

``num_controls``
    Number of elements in the array


Return
======

0 for success, else error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

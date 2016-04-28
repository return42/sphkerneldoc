.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-add-dai-controls:

========================
snd_soc_add_dai_controls
========================

*man snd_soc_add_dai_controls(9)*

*4.6.0-rc5*

add an array of controls to a DAI. Convienience function to add a list
of controls.


Synopsis
========

.. c:function:: int snd_soc_add_dai_controls( struct snd_soc_dai * dai, const struct snd_kcontrol_new * controls, int num_controls )

Arguments
=========

``dai``
    DAI to add controls to

``controls``
    array of controls to add

``num_controls``
    number of elements in the array


Description
===========

Return 0 for success, else error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

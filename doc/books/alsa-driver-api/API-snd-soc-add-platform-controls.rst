.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-add-platform-controls:

=============================
snd_soc_add_platform_controls
=============================

*man snd_soc_add_platform_controls(9)*

*4.6.0-rc5*

add an array of controls to a platform. Convenience function to add a
list of controls.


Synopsis
========

.. c:function:: int snd_soc_add_platform_controls( struct snd_soc_platform * platform, const struct snd_kcontrol_new * controls, unsigned int num_controls )

Arguments
=========

``platform``
    platform to add controls to

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

.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-add-codec-controls:

==========================
snd_soc_add_codec_controls
==========================

*man snd_soc_add_codec_controls(9)*

*4.6.0-rc5*

add an array of controls to a codec. Convenience function to add a list
of controls. Many codecs were duplicating this code.


Synopsis
========

.. c:function:: int snd_soc_add_codec_controls( struct snd_soc_codec * codec, const struct snd_kcontrol_new * controls, unsigned int num_controls )

Arguments
=========

``codec``
    codec to add controls to

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

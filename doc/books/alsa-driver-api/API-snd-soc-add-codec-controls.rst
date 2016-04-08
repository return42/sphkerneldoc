
.. _API-snd-soc-add-codec-controls:

==========================
snd_soc_add_codec_controls
==========================

*man snd_soc_add_codec_controls(9)*

*4.6.0-rc1*

add an array of controls to a codec. Convenience function to add a list of controls. Many codecs were duplicating this code.


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


.. _API-snd-soc-add-card-controls:

=========================
snd_soc_add_card_controls
=========================

*man snd_soc_add_card_controls(9)*

*4.6.0-rc1*

add an array of controls to a SoC card. Convenience function to add a list of controls.


Synopsis
========

.. c:function:: int snd_soc_add_card_controls( struct snd_soc_card * soc_card, const struct snd_kcontrol_new * controls, int num_controls )

Arguments
=========

``soc_card``
    SoC card to add controls to

``controls``
    array of controls to add

``num_controls``
    number of elements in the array


Description
===========

Return 0 for success, else error.

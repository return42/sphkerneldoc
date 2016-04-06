
.. _API-snd-component-add:

=================
snd_component_add
=================

*man snd_component_add(9)*

*4.6.0-rc1*

add a component string


Synopsis
========

.. c:function:: int snd_component_add( struct snd_card * card, const char * component )

Arguments
=========

``card``
    soundcard structure

``component``
    the component id string


Description
===========

This function adds the component id string to the supported list. The component can be referred from the alsa-lib.


Return
======

Zero otherwise a negative error code.

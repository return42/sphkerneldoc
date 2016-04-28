.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-component-add:

=================
snd_component_add
=================

*man snd_component_add(9)*

*4.6.0-rc5*

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

This function adds the component id string to the supported list. The
component can be referred from the alsa-lib.


Return
======

Zero otherwise a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-jack-set-key:

================
snd_jack_set_key
================

*man snd_jack_set_key(9)*

*4.6.0-rc5*

Set a key mapping on a jack


Synopsis
========

.. c:function:: int snd_jack_set_key( struct snd_jack * jack, enum snd_jack_types type, int keytype )

Arguments
=========

``jack``
    The jack to configure

``type``
    Jack report type for this key

``keytype``
    Input layer key type to be reported


Description
===========

Map a SND_JACK_BTN_ button type to an input layer key, allowing
reporting of keys on accessories via the jack abstraction. If no mapping
is provided but keys are enabled in the jack type then BTN_n numeric
buttons will be reported.

If jacks are not reporting via the input API this call will have no
effect.

Note that this is intended to be use by simple devices with small
numbers of keys that can be reported. It is also possible to access the
input device directly - devices with complex input capabilities on
accessories should consider doing this rather than using this
abstraction.

This function may only be called prior to registration of the jack.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

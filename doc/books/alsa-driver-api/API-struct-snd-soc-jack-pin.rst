.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-soc-jack-pin:

=======================
struct snd_soc_jack_pin
=======================

*man struct snd_soc_jack_pin(9)*

*4.6.0-rc5*

Describes a pin to update based on jack detection


Synopsis
========

.. code-block:: c

    struct snd_soc_jack_pin {
      struct list_head list;
      const char * pin;
      int mask;
      bool invert;
    };


Members
=======

list
    internal list entry

pin
    name of the pin to update

mask
    bits to check for in reported jack status

invert
    if non-zero then pin is enabled when status is not reported


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

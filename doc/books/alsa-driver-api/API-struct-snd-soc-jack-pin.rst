
.. _API-struct-snd-soc-jack-pin:

=======================
struct snd_soc_jack_pin
=======================

*man struct snd_soc_jack_pin(9)*

*4.6.0-rc1*

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

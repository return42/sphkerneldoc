.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-soc-jack-zone:

========================
struct snd_soc_jack_zone
========================

*man struct snd_soc_jack_zone(9)*

*4.6.0-rc5*

Describes voltage zones of jack detection


Synopsis
========

.. code-block:: c

    struct snd_soc_jack_zone {
      unsigned int min_mv;
      unsigned int max_mv;
      unsigned int jack_type;
      unsigned int debounce_time;
      struct list_head list;
    };


Members
=======

min_mv
    start voltage in mv

max_mv
    end voltage in mv

jack_type
    type of jack that is expected for this voltage

debounce_time
    debounce_time for jack, codec driver should wait for this duration
    before reading the adc for voltages

list
    internal list entry


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

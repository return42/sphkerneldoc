.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-soc-jack-gpio:

========================
struct snd_soc_jack_gpio
========================

*man struct snd_soc_jack_gpio(9)*

*4.6.0-rc5*

Describes a gpio pin for jack detection


Synopsis
========

.. code-block:: c

    struct snd_soc_jack_gpio {
      unsigned int gpio;
      unsigned int idx;
      struct device * gpiod_dev;
      const char * name;
      int report;
      int invert;
      int debounce_time;
      bool wake;
      int (* jack_status_check) (void *data);
    };


Members
=======

gpio
    legacy gpio number

idx
    gpio descriptor index within the function of the GPIO consumer
    device

gpiod_dev
    GPIO consumer device

name
    gpio name. Also as connection ID for the GPIO consumer device
    function name lookup

report
    value to report when jack detected

invert
    report presence in low state

debounce_time
    debounce time in ms

wake
    enable as wake source

jack_status_check
    callback function which overrides the detection to provide more
    complex checks (eg, reading an ADC).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

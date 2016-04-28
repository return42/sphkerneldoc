.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ff-device:

================
struct ff_device
================

*man struct ff_device(9)*

*4.6.0-rc5*

force-feedback part of an input device


Synopsis
========

.. code-block:: c

    struct ff_device {
      int (* upload) (struct input_dev *dev, struct ff_effect *effect,struct ff_effect *old);
      int (* erase) (struct input_dev *dev, int effect_id);
      int (* playback) (struct input_dev *dev, int effect_id, int value);
      void (* set_gain) (struct input_dev *dev, u16 gain);
      void (* set_autocenter) (struct input_dev *dev, u16 magnitude);
      void (* destroy) (struct ff_device *);
      void * private;
      unsigned long ffbit[BITS_TO_LONGS(FF_CNT)];
      struct mutex mutex;
      int max_effects;
      struct ff_effect * effects;
      struct file * effect_owners[];
    };


Members
=======

upload
    Called to upload an new effect into device

erase
    Called to erase an effect from device

playback
    Called to request device to start playing specified effect

set_gain
    Called to set specified gain

set_autocenter
    Called to auto-center device

destroy
    called by input core when parent input device is being destroyed

private
    driver-specific data, will be freed automatically

ffbit[BITS_TO_LONGS(FF_CNT)]
    bitmap of force feedback capabilities truly supported by device (not
    emulated like ones in input_dev->ffbit)

mutex
    mutex for serializing access to the device

max_effects
    maximum number of effects supported by device

effects
    pointer to an array of effects currently loaded into device

effect_owners[]
    array of effect owners; when file handle owning an effect gets
    closed the effect is automatically erased


Description
===========

Every force-feedback device must implement ``upload`` and ``playback``
methods; ``erase`` is optional. ``set_gain`` and ``set_autocenter`` need
only be implemented if driver sets up FF_GAIN and FF_AUTOCENTER bits.

Note that ``playback``, ``set_gain`` and ``set_autocenter`` are called
with dev->event_lock spinlock held and interrupts off and thus may not
sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

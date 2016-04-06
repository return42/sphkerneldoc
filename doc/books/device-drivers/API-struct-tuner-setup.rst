
.. _API-struct-tuner-setup:

==================
struct tuner_setup
==================

*man struct tuner_setup(9)*

*4.6.0-rc1*

setup the tuner chipsets


Synopsis
========

.. code-block:: c

    struct tuner_setup {
      unsigned short addr;
      unsigned int type;
      unsigned int mode_mask;
      void * config;
      int (* tuner_callback) (void *dev, int component, int cmd, int arg);
    };


Members
=======

addr
    I2C address used to control the tuner device/chipset

type
    Type of the tuner, as defined at the TUNER_⋆ macros. Each different tuner model should have an unique identifier.

mode_mask
    Mask with the allowed tuner modes: V4L2_TUNER_RADIO, V4L2_TUNER_ANALOG_TV and/or V4L2_TUNER_DIGITAL_TV, describing if the tuner should be used to support Radio, analog
    TV and/or digital TV.

config
    Used to send tuner-specific configuration for complex tuners that require extra parameters to be set. Only a very few tuners require it and its usage on newer tuners should be
    avoided.

tuner_callback
    Some tuners require to call back the bridge driver, in order to do some tasks like rising a GPIO at the bridge chipset, in order to do things like resetting the device.


Description
===========

Older boards only had a single tuner device. Nowadays multiple tuner devices may be present on a single board. Using TUNER_SET_TYPE_ADDR to pass the tuner_setup structure it is
possible to setup each tuner device in turn.

Since multiple devices may be present it is no longer sufficient to send a command to a single i2c device. Instead you should broadcast the command to all i2c devices.

By setting the mode_mask correctly you can select which commands are accepted by a specific tuner device. For example, set mode_mask to T_RADIO if the device is a radio-only
tuner. That specific tuner will only accept commands when the tuner is in radio mode and ignore them when the tuner is set to TV mode.

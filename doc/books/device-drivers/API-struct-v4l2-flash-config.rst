
.. _API-struct-v4l2-flash-config:

========================
struct v4l2_flash_config
========================

*man struct v4l2_flash_config(9)*

*4.6.0-rc1*

V4L2 Flash sub-device initialization data


Synopsis
========

.. code-block:: c

    struct v4l2_flash_config {
      char dev_name[32];
      struct led_flash_setting torch_intensity;
      struct led_flash_setting indicator_intensity;
      u32 flash_faults;
      unsigned int has_external_strobe:1;
    };


Members
=======

dev_name[32]
    the name of the media entity, unique in the system

torch_intensity
    constraints for the LED in torch mode

indicator_intensity
    constraints for the indicator LED

flash_faults
    bitmask of flash faults that the LED flash class device can report; corresponding LED_FAULT⋆ bit definitions are available in the header file <linux/led-class-flash.h>

has_external_strobe
    external strobe capability

.. -*- coding: utf-8; mode: rst -*-

============
tuner-core.c
============



.. _xref_set_type:

set_type
========

.. c:function:: void set_type (struct i2c_client * c, unsigned int type, unsigned int new_mode_mask, void * new_config, int (*tuner_callback) (void *dev, int component, int cmd, int arg)

    Sets the tuner type for a given device

    :param struct i2c_client * c:
        i2c_client descriptor

    :param unsigned int type:
        type of the tuner (e. g. tuner number)

    :param unsigned int new_mode_mask:
        Indicates if tuner supports TV and/or Radio

    :param void * new_config:
        an optional parameter used by a few tuners to adjust

    :param int (*) (void *dev, int component, int cmd, int arg) tuner_callback:
        an optional function to be called when switching
        			to analog mode



Description
-----------

This function applys the tuner config to tuner specified
by tun_setup structure. It contains several per-tuner initialization "magic"




.. _xref_tuner_s_type_addr:

tuner_s_type_addr
=================

.. c:function:: int tuner_s_type_addr (struct v4l2_subdev * sd, struct tuner_setup * tun_setup)

    Sets the tuner type for a device

    :param struct v4l2_subdev * sd:
        subdev descriptor

    :param struct tuner_setup * tun_setup:
        type to be associated to a given tuner i2c address



Description
-----------

This function applys the tuner config to tuner specified
by tun_setup structure.
If tuner I2C address is UNSET, then it will only set the device
if the tuner supports the mode specified in the call.
If the address is specified, the change will be applied only if
tuner I2C address matches.
The call can change the tuner number and the tuner mode.




.. _xref_tuner_s_config:

tuner_s_config
==============

.. c:function:: int tuner_s_config (struct v4l2_subdev * sd, const struct v4l2_priv_tun_config * cfg)

    Sets tuner configuration

    :param struct v4l2_subdev * sd:
        subdev descriptor

    :param const struct v4l2_priv_tun_config * cfg:
        tuner configuration



Description
-----------

Calls tuner :c:func:`set_config` private function to set some tuner-internal
parameters




.. _xref_tuner_lookup:

tuner_lookup
============

.. c:function:: void tuner_lookup (struct i2c_adapter * adap, struct tuner ** radio, struct tuner ** tv)

    Seek for tuner adapters

    :param struct i2c_adapter * adap:
        i2c_adapter struct

    :param struct tuner ** radio:
        pointer to be filled if the adapter is radio

    :param struct tuner ** tv:
        pointer to be filled if the adapter is TV



Description
-----------

Search for existing radio and/or TV tuners on the given I2C adapter,
discarding demod-only adapters (tda9887).


Note that when this function is called from tuner_probe you can be
certain no other devices will be added/deleted at the same time, I2C
core protects against that.




.. _xref_tuner_probe:

tuner_probe
===========

.. c:function:: int tuner_probe (struct i2c_client * client, const struct i2c_device_id * id)

    Probes the existing tuners on an I2C bus

    :param struct i2c_client * client:
        i2c_client descriptor

    :param const struct i2c_device_id * id:
        not used



Description
-----------

This routine probes for tuners at the expected I2C addresses. On most
cases, if a device answers to a given I2C address, it assumes that the
device is a tuner. On a few cases, however, an additional logic is needed
to double check if the device is really a tuner, or to identify the tuner
type, like on tea5767/5761 devices.


During client attach, set_type is called by adapter's attach_inform callback.
set_type must then be completed by tuner_probe.




.. _xref_tuner_remove:

tuner_remove
============

.. c:function:: int tuner_remove (struct i2c_client * client)

    detaches a tuner

    :param struct i2c_client * client:
        i2c_client descriptor




.. _xref_check_mode:

check_mode
==========

.. c:function:: int check_mode (struct tuner * t, enum v4l2_tuner_type mode)

    Verify if tuner supports the requested mode

    :param struct tuner * t:
        a pointer to the module's internal struct_tuner

    :param enum v4l2_tuner_type mode:

        _undescribed_



Description
-----------

This function checks if the tuner is capable of tuning analog TV,
digital TV or radio, depending on what the caller wants. If the
tuner can't support that mode, it returns -EINVAL. Otherwise, it
returns 0.
This function is needed for boards that have a separate tuner for
radio (like devices with tea5767).



NOTE
----

mt20xx uses V4L2_TUNER_DIGITAL_TV and calls set_tv_freq to
      select a TV frequency. So, t_mode = T_ANALOG_TV could actually
	 be used to represent a Digital TV too.




.. _xref_set_mode:

set_mode
========

.. c:function:: int set_mode (struct tuner * t, enum v4l2_tuner_type mode)

    Switch tuner to other mode.

    :param struct tuner * t:
        a pointer to the module's internal struct_tuner

    :param enum v4l2_tuner_type mode:
        enum v4l2_type (radio or TV)



Description
-----------

If tuner doesn't support the needed mode (radio or TV), prints a
debug message and returns -EINVAL, changing its state to standby.
Otherwise, changes the mode and returns 0.




.. _xref_set_freq:

set_freq
========

.. c:function:: void set_freq (struct tuner * t, unsigned int freq)

    Set the tuner to the desired frequency.

    :param struct tuner * t:
        a pointer to the module's internal struct_tuner

    :param unsigned int freq:
        frequency to set (0 means to use the current frequency)




.. _xref_set_tv_freq:

set_tv_freq
===========

.. c:function:: void set_tv_freq (struct i2c_client * c, unsigned int freq)

    Set tuner frequency, freq in Units of 62.5 kHz = 1/16MHz

    :param struct i2c_client * c:
        i2c_client descriptor

    :param unsigned int freq:
        frequency




.. _xref_tuner_fixup_std:

tuner_fixup_std
===============

.. c:function:: v4l2_std_id tuner_fixup_std (struct tuner * t, v4l2_std_id std)

    force a given video standard variant

    :param struct tuner * t:
        tuner internal struct

    :param v4l2_std_id std:
        TV standard



Description
-----------

A few devices or drivers have problem to detect some standard variations.
On other operational systems, the drivers generally have a per-country
code, and some logic to apply per-country hacks. V4L2 API doesn't provide
such hacks. Instead, it relies on a proper video standard selection from
the userspace application. However, as some apps are buggy, not allowing
to distinguish all video standard variations, a modprobe parameter can
be used to force a video standard match.




.. _xref_set_radio_freq:

set_radio_freq
==============

.. c:function:: void set_radio_freq (struct i2c_client * c, unsigned int freq)

    Set tuner frequency, freq in Units of 62.5 Hz = 1/16kHz

    :param struct i2c_client * c:
        i2c_client descriptor

    :param unsigned int freq:
        frequency




.. _xref_tuner_status:

tuner_status
============

.. c:function:: void tuner_status (struct dvb_frontend * fe)

    Dumps the current tuner status at dmesg

    :param struct dvb_frontend * fe:
        pointer to struct dvb_frontend



Description
-----------

This callback is used only for driver debug purposes, answering to
VIDIOC_LOG_STATUS. No changes should happen on this call.




.. _xref_tuner_s_power:

tuner_s_power
=============

.. c:function:: int tuner_s_power (struct v4l2_subdev * sd, int on)

    controls the power state of the tuner

    :param struct v4l2_subdev * sd:
        pointer to struct v4l2_subdev

    :param int on:
        a zero value puts the tuner to sleep, non-zero wakes it up




.. _xref_tuner_g_frequency:

tuner_g_frequency
=================

.. c:function:: int tuner_g_frequency (struct v4l2_subdev * sd, struct v4l2_frequency * f)

    Get the tuned frequency for the tuner

    :param struct v4l2_subdev * sd:
        pointer to struct v4l2_subdev

    :param struct v4l2_frequency * f:
        pointer to struct v4l2_frequency



Description
-----------

At return, the structure f will be filled with tuner frequency
if the tuner matches the f->type.



Note
----

f->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.




.. _xref_tuner_g_tuner:

tuner_g_tuner
=============

.. c:function:: int tuner_g_tuner (struct v4l2_subdev * sd, struct v4l2_tuner * vt)

    Fill in tuner information

    :param struct v4l2_subdev * sd:
        pointer to struct v4l2_subdev

    :param struct v4l2_tuner * vt:
        pointer to struct v4l2_tuner



Description
-----------

At return, the structure vt will be filled with tuner information
if the tuner matches vt->type.



Note
----

vt->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.




.. _xref_tuner_s_tuner:

tuner_s_tuner
=============

.. c:function:: int tuner_s_tuner (struct v4l2_subdev * sd, const struct v4l2_tuner * vt)

    Set the tuner's audio mode

    :param struct v4l2_subdev * sd:
        pointer to struct v4l2_subdev

    :param const struct v4l2_tuner * vt:
        pointer to struct v4l2_tuner



Description
-----------

Sets the audio mode if the tuner matches vt->type.



Note
----

vt->type should be initialized before calling it.
This is done by either video_ioctl2 or by the bridge driver.



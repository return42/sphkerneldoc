.. -*- coding: utf-8; mode: rst -*-

======
vpbe.c
======



.. _xref_vpbe_current_encoder_info:

vpbe_current_encoder_info
=========================

.. c:function:: struct encoder_config_info* vpbe_current_encoder_info (struct vpbe_device * vpbe_dev)

    Get config info for current encoder @vpbe_dev - vpbe device ptr

    :param struct vpbe_device * vpbe_dev:

        _undescribed_



Description
-----------



Return ptr to current encoder config info




.. _xref_vpbe_find_encoder_sd_index:

vpbe_find_encoder_sd_index
==========================

.. c:function:: int vpbe_find_encoder_sd_index (struct vpbe_config * cfg, int index)

    Given a name find encoder sd index

    :param struct vpbe_config * cfg:

        _undescribed_

    :param int index:

        _undescribed_



Description
-----------



**vpbe_config** - ptr to vpbe cfg
**output_index** - index used by application


Return sd index of the encoder




.. _xref_vpbe_g_cropcap:

vpbe_g_cropcap
==============

.. c:function:: int vpbe_g_cropcap (struct vpbe_device * vpbe_dev, struct v4l2_cropcap * cropcap)

    Get crop capabilities of the display @vpbe_dev - vpbe device ptr @cropcap - cropcap is a ptr to struct v4l2_cropcap

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct v4l2_cropcap * cropcap:

        _undescribed_



Description
-----------



Update the crop capabilities in crop cap for current
mode




.. _xref_vpbe_enum_outputs:

vpbe_enum_outputs
=================

.. c:function:: int vpbe_enum_outputs (struct vpbe_device * vpbe_dev, struct v4l2_output * output)

    enumerate outputs @vpbe_dev - vpbe device ptr @output - ptr to v4l2_output structure

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct v4l2_output * output:

        _undescribed_



Description
-----------



Enumerates the outputs available at the vpbe display
returns the status, -EINVAL if end of output list




.. _xref_vpbe_set_output:

vpbe_set_output
===============

.. c:function:: int vpbe_set_output (struct vpbe_device * vpbe_dev, int index)

    Set output @vpbe_dev - vpbe device ptr @index - index of output

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param int index:

        _undescribed_



Description
-----------



Set vpbe output to the output specified by the index




.. _xref_vpbe_get_output:

vpbe_get_output
===============

.. c:function:: unsigned int vpbe_get_output (struct vpbe_device * vpbe_dev)

    Get output @vpbe_dev - vpbe device ptr

    :param struct vpbe_device * vpbe_dev:

        _undescribed_



Description
-----------



return current vpbe output to the the index




.. _xref_vpbe_s_dv_timings:

vpbe_s_dv_timings
=================

.. c:function:: int vpbe_s_dv_timings (struct vpbe_device * vpbe_dev, struct v4l2_dv_timings * dv_timings)

    Set the given preset timings in the encoder

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct v4l2_dv_timings * dv_timings:

        _undescribed_



Description
-----------



Sets the timings if supported by the current encoder. Return the status.
0 - success & -EINVAL on error




.. _xref_vpbe_g_dv_timings:

vpbe_g_dv_timings
=================

.. c:function:: int vpbe_g_dv_timings (struct vpbe_device * vpbe_dev, struct v4l2_dv_timings * dv_timings)

    Get the timings in the current encoder

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct v4l2_dv_timings * dv_timings:

        _undescribed_



Description
-----------



Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_enum_dv_timings:

vpbe_enum_dv_timings
====================

.. c:function:: int vpbe_enum_dv_timings (struct vpbe_device * vpbe_dev, struct v4l2_enum_dv_timings * timings)

    Enumerate the dv timings in the current encoder

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct v4l2_enum_dv_timings * timings:

        _undescribed_



Description
-----------



Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_s_std:

vpbe_s_std
==========

.. c:function:: int vpbe_s_std (struct vpbe_device * vpbe_dev, v4l2_std_id std_id)

    Set the given standard in the encoder

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param v4l2_std_id std_id:

        _undescribed_



Description
-----------



Sets the standard if supported by the current encoder. Return the status.
0 - success & -EINVAL on error




.. _xref_vpbe_g_std:

vpbe_g_std
==========

.. c:function:: int vpbe_g_std (struct vpbe_device * vpbe_dev, v4l2_std_id * std_id)

    Get the standard in the current encoder

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param v4l2_std_id * std_id:

        _undescribed_



Description
-----------



Get the standard in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_set_mode:

vpbe_set_mode
=============

.. c:function:: int vpbe_set_mode (struct vpbe_device * vpbe_dev, struct vpbe_enc_mode_info * mode_info)

    Set mode in the current encoder using mode info

    :param struct vpbe_device * vpbe_dev:

        _undescribed_

    :param struct vpbe_enc_mode_info * mode_info:

        _undescribed_



Description
-----------



Use the mode string to decide what timings to set in the encoder
This is typically useful when fbset command is used to change the current
timings by specifying a string to indicate the timings.




.. _xref_vpbe_initialize:

vpbe_initialize
===============

.. c:function:: int vpbe_initialize (struct device * dev, struct vpbe_device * vpbe_dev)

    Initialize the vpbe display controller @vpbe_dev - vpbe device ptr

    :param struct device * dev:

        _undescribed_

    :param struct vpbe_device * vpbe_dev:

        _undescribed_



Description
-----------



Master frame buffer device drivers calls this to initialize vpbe
display controller. This will then registers v4l2 device and the sub
devices and sets a current encoder sub device for display. v4l2 display
device driver is the master and frame buffer display device driver is
the slave. Frame buffer display driver checks the initialized during
probe and exit if not initialized. Returns status.




.. _xref_vpbe_deinitialize:

vpbe_deinitialize
=================

.. c:function:: void vpbe_deinitialize (struct device * dev, struct vpbe_device * vpbe_dev)

    de-initialize the vpbe display controller @dev - Master and slave device ptr

    :param struct device * dev:

        _undescribed_

    :param struct vpbe_device * vpbe_dev:

        _undescribed_



Description
-----------



vpbe_master and slave frame buffer devices calls this to de-initialize
the display controller. It is called when master and slave device
driver modules are removed and no longer requires the display controller.



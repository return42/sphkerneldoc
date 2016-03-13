.. -*- coding: utf-8; mode: rst -*-

==============
vpbe_display.c
==============



.. _xref_vpbe_try_format:

vpbe_try_format
===============

.. c:function:: int vpbe_try_format (struct vpbe_display * disp_dev, struct v4l2_pix_format * pixfmt, int check)

    

    :param struct vpbe_display * disp_dev:

        _undescribed_

    :param struct v4l2_pix_format * pixfmt:

        _undescribed_

    :param int check:

        _undescribed_



Description
-----------

If user application provides width and height, and have bytesperline set
to zero, driver calculates bytesperline and sizeimage based on hardware
limits.




.. _xref_vpbe_display_s_std:

vpbe_display_s_std
==================

.. c:function:: int vpbe_display_s_std (struct file * file, void * priv, v4l2_std_id std_id)

    Set the given standard in the encoder

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param v4l2_std_id std_id:

        _undescribed_



Description
-----------



Sets the standard if supported by the current encoder. Return the status.
0 - success & -EINVAL on error




.. _xref_vpbe_display_g_std:

vpbe_display_g_std
==================

.. c:function:: int vpbe_display_g_std (struct file * file, void * priv, v4l2_std_id * std_id)

    Get the standard in the current encoder

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param v4l2_std_id * std_id:

        _undescribed_



Description
-----------



Get the standard in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_display_enum_output:

vpbe_display_enum_output
========================

.. c:function:: int vpbe_display_enum_output (struct file * file, void * priv, struct v4l2_output * output)

    enumerate outputs

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param struct v4l2_output * output:

        _undescribed_



Description
-----------



Enumerates the outputs available at the vpbe display
returns the status, -EINVAL if end of output list




.. _xref_vpbe_display_s_output:

vpbe_display_s_output
=====================

.. c:function:: int vpbe_display_s_output (struct file * file, void * priv, unsigned int i)

    Set output to the output specified by the index

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param unsigned int i:

        _undescribed_




.. _xref_vpbe_display_g_output:

vpbe_display_g_output
=====================

.. c:function:: int vpbe_display_g_output (struct file * file, void * priv, unsigned int * i)

    Get output from subdevice for a given by the index

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param unsigned int * i:

        _undescribed_




.. _xref_vpbe_display_enum_dv_timings:

vpbe_display_enum_dv_timings
============================

.. c:function:: int vpbe_display_enum_dv_timings (struct file * file, void * priv, struct v4l2_enum_dv_timings * timings)

    Enumerate the dv timings

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param struct v4l2_enum_dv_timings * timings:

        _undescribed_



Description
-----------



enum the timings in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_display_s_dv_timings:

vpbe_display_s_dv_timings
=========================

.. c:function:: int vpbe_display_s_dv_timings (struct file * file, void * priv, struct v4l2_dv_timings * timings)

    Set the dv timings

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param struct v4l2_dv_timings * timings:

        _undescribed_



Description
-----------



Set the timings in the current encoder. Return the status. 0 - success
-EINVAL on error




.. _xref_vpbe_display_g_dv_timings:

vpbe_display_g_dv_timings
=========================

.. c:function:: int vpbe_display_g_dv_timings (struct file * file, void * priv, struct v4l2_dv_timings * dv_timings)

    Set the dv timings

    :param struct file * file:

        _undescribed_

    :param void * priv:

        _undescribed_

    :param struct v4l2_dv_timings * dv_timings:

        _undescribed_



Description
-----------



Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error



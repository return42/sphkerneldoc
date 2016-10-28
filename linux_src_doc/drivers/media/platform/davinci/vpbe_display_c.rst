.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpbe_display.c

.. _`vpbe_try_format`:

vpbe_try_format
===============

.. c:function:: int vpbe_try_format(struct vpbe_display *disp_dev, struct v4l2_pix_format *pixfmt, int check)

    If user application provides width and height, and have bytesperline set to zero, driver calculates bytesperline and sizeimage based on hardware limits.

    :param struct vpbe_display \*disp_dev:
        *undescribed*

    :param struct v4l2_pix_format \*pixfmt:
        *undescribed*

    :param int check:
        *undescribed*

.. _`vpbe_display_s_std`:

vpbe_display_s_std
==================

.. c:function:: int vpbe_display_s_std(struct file *file, void *priv, v4l2_std_id std_id)

    Set the given standard in the encoder

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param v4l2_std_id std_id:
        *undescribed*

.. _`vpbe_display_s_std.description`:

Description
-----------

Sets the standard if supported by the current encoder. Return the status.
0 - success & -EINVAL on error

.. _`vpbe_display_g_std`:

vpbe_display_g_std
==================

.. c:function:: int vpbe_display_g_std(struct file *file, void *priv, v4l2_std_id *std_id)

    Get the standard in the current encoder

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param v4l2_std_id \*std_id:
        *undescribed*

.. _`vpbe_display_g_std.description`:

Description
-----------

Get the standard in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_display_enum_output`:

vpbe_display_enum_output
========================

.. c:function:: int vpbe_display_enum_output(struct file *file, void *priv, struct v4l2_output *output)

    enumerate outputs

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param struct v4l2_output \*output:
        *undescribed*

.. _`vpbe_display_enum_output.description`:

Description
-----------

Enumerates the outputs available at the vpbe display
returns the status, -EINVAL if end of output list

.. _`vpbe_display_s_output`:

vpbe_display_s_output
=====================

.. c:function:: int vpbe_display_s_output(struct file *file, void *priv, unsigned int i)

    Set output to the output specified by the index

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param unsigned int i:
        *undescribed*

.. _`vpbe_display_g_output`:

vpbe_display_g_output
=====================

.. c:function:: int vpbe_display_g_output(struct file *file, void *priv, unsigned int *i)

    Get output from subdevice for a given by the index

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param unsigned int \*i:
        *undescribed*

.. _`vpbe_display_enum_dv_timings`:

vpbe_display_enum_dv_timings
============================

.. c:function:: int vpbe_display_enum_dv_timings(struct file *file, void *priv, struct v4l2_enum_dv_timings *timings)

    Enumerate the dv timings

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param struct v4l2_enum_dv_timings \*timings:
        *undescribed*

.. _`vpbe_display_enum_dv_timings.description`:

Description
-----------

enum the timings in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_display_s_dv_timings`:

vpbe_display_s_dv_timings
=========================

.. c:function:: int vpbe_display_s_dv_timings(struct file *file, void *priv, struct v4l2_dv_timings *timings)

    Set the dv timings

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param struct v4l2_dv_timings \*timings:
        *undescribed*

.. _`vpbe_display_s_dv_timings.description`:

Description
-----------

Set the timings in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_display_g_dv_timings`:

vpbe_display_g_dv_timings
=========================

.. c:function:: int vpbe_display_g_dv_timings(struct file *file, void *priv, struct v4l2_dv_timings *dv_timings)

    Set the dv timings

    :param struct file \*file:
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param struct v4l2_dv_timings \*dv_timings:
        *undescribed*

.. _`vpbe_display_g_dv_timings.description`:

Description
-----------

Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error

.. This file was automatic generated / don't edit.


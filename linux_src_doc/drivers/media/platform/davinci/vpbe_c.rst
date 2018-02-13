.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpbe.c

.. _`vpbe_current_encoder_info`:

vpbe_current_encoder_info
=========================

.. c:function:: struct encoder_config_info*vpbe_current_encoder_info(struct vpbe_device *vpbe_dev)

    Get config info for current encoder \ ``vpbe_dev``\  - vpbe device ptr

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

.. _`vpbe_current_encoder_info.description`:

Description
-----------

Return ptr to current encoder config info

.. _`vpbe_find_encoder_sd_index`:

vpbe_find_encoder_sd_index
==========================

.. c:function:: int vpbe_find_encoder_sd_index(struct vpbe_config *cfg, int index)

    Given a name find encoder sd index

    :param struct vpbe_config \*cfg:
        *undescribed*

    :param int index:
        *undescribed*

.. _`vpbe_find_encoder_sd_index.description`:

Description
-----------

\ ``vpbe_config``\  - ptr to vpbe cfg
\ ``output_index``\  - index used by application

Return sd index of the encoder

.. _`vpbe_g_cropcap`:

vpbe_g_cropcap
==============

.. c:function:: int vpbe_g_cropcap(struct vpbe_device *vpbe_dev, struct v4l2_cropcap *cropcap)

    Get crop capabilities of the display \ ``vpbe_dev``\  - vpbe device ptr \ ``cropcap``\  - cropcap is a ptr to struct v4l2_cropcap

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct v4l2_cropcap \*cropcap:
        *undescribed*

.. _`vpbe_g_cropcap.description`:

Description
-----------

Update the crop capabilities in crop cap for current
mode

.. _`vpbe_enum_outputs`:

vpbe_enum_outputs
=================

.. c:function:: int vpbe_enum_outputs(struct vpbe_device *vpbe_dev, struct v4l2_output *output)

    enumerate outputs \ ``vpbe_dev``\  - vpbe device ptr \ ``output``\  - ptr to v4l2_output structure

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct v4l2_output \*output:
        *undescribed*

.. _`vpbe_enum_outputs.description`:

Description
-----------

Enumerates the outputs available at the vpbe display
returns the status, -EINVAL if end of output list

.. _`vpbe_set_output`:

vpbe_set_output
===============

.. c:function:: int vpbe_set_output(struct vpbe_device *vpbe_dev, int index)

    Set output \ ``vpbe_dev``\  - vpbe device ptr \ ``index``\  - index of output

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param int index:
        *undescribed*

.. _`vpbe_set_output.description`:

Description
-----------

Set vpbe output to the output specified by the index

.. _`vpbe_get_output`:

vpbe_get_output
===============

.. c:function:: unsigned int vpbe_get_output(struct vpbe_device *vpbe_dev)

    Get output \ ``vpbe_dev``\  - vpbe device ptr

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

.. _`vpbe_get_output.description`:

Description
-----------

return current vpbe output to the the index

.. _`vpbe_s_dv_timings`:

vpbe_s_dv_timings
=================

.. c:function:: int vpbe_s_dv_timings(struct vpbe_device *vpbe_dev, struct v4l2_dv_timings *dv_timings)

    Set the given preset timings in the encoder

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct v4l2_dv_timings \*dv_timings:
        *undescribed*

.. _`vpbe_s_dv_timings.description`:

Description
-----------

Sets the timings if supported by the current encoder. Return the status.
0 - success & -EINVAL on error

.. _`vpbe_g_dv_timings`:

vpbe_g_dv_timings
=================

.. c:function:: int vpbe_g_dv_timings(struct vpbe_device *vpbe_dev, struct v4l2_dv_timings *dv_timings)

    Get the timings in the current encoder

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct v4l2_dv_timings \*dv_timings:
        *undescribed*

.. _`vpbe_g_dv_timings.description`:

Description
-----------

Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_enum_dv_timings`:

vpbe_enum_dv_timings
====================

.. c:function:: int vpbe_enum_dv_timings(struct vpbe_device *vpbe_dev, struct v4l2_enum_dv_timings *timings)

    Enumerate the dv timings in the current encoder

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct v4l2_enum_dv_timings \*timings:
        *undescribed*

.. _`vpbe_enum_dv_timings.description`:

Description
-----------

Get the timings in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_s_std`:

vpbe_s_std
==========

.. c:function:: int vpbe_s_std(struct vpbe_device *vpbe_dev, v4l2_std_id std_id)

    Set the given standard in the encoder

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param v4l2_std_id std_id:
        *undescribed*

.. _`vpbe_s_std.description`:

Description
-----------

Sets the standard if supported by the current encoder. Return the status.
0 - success & -EINVAL on error

.. _`vpbe_g_std`:

vpbe_g_std
==========

.. c:function:: int vpbe_g_std(struct vpbe_device *vpbe_dev, v4l2_std_id *std_id)

    Get the standard in the current encoder

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param v4l2_std_id \*std_id:
        *undescribed*

.. _`vpbe_g_std.description`:

Description
-----------

Get the standard in the current encoder. Return the status. 0 - success
-EINVAL on error

.. _`vpbe_set_mode`:

vpbe_set_mode
=============

.. c:function:: int vpbe_set_mode(struct vpbe_device *vpbe_dev, struct vpbe_enc_mode_info *mode_info)

    Set mode in the current encoder using mode info

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

    :param struct vpbe_enc_mode_info \*mode_info:
        *undescribed*

.. _`vpbe_set_mode.description`:

Description
-----------

Use the mode string to decide what timings to set in the encoder
This is typically useful when fbset command is used to change the current
timings by specifying a string to indicate the timings.

.. _`vpbe_initialize`:

vpbe_initialize
===============

.. c:function:: int vpbe_initialize(struct device *dev, struct vpbe_device *vpbe_dev)

    Initialize the vpbe display controller \ ``vpbe_dev``\  - vpbe device ptr

    :param struct device \*dev:
        *undescribed*

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

.. _`vpbe_initialize.description`:

Description
-----------

Master frame buffer device drivers calls this to initialize vpbe
display controller. This will then registers v4l2 device and the sub
devices and sets a current encoder sub device for display. v4l2 display
device driver is the master and frame buffer display device driver is
the slave. Frame buffer display driver checks the initialized during
probe and exit if not initialized. Returns status.

.. _`vpbe_deinitialize`:

vpbe_deinitialize
=================

.. c:function:: void vpbe_deinitialize(struct device *dev, struct vpbe_device *vpbe_dev)

    de-initialize the vpbe display controller \ ``dev``\  - Master and slave device ptr

    :param struct device \*dev:
        *undescribed*

    :param struct vpbe_device \*vpbe_dev:
        *undescribed*

.. _`vpbe_deinitialize.description`:

Description
-----------

vpbe_master and slave frame buffer devices calls this to de-initialize
the display controller. It is called when master and slave device
driver modules are removed and no longer requires the display controller.

.. This file was automatic generated / don't edit.


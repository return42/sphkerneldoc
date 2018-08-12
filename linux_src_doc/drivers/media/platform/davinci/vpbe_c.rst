.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/davinci/vpbe.c

.. _`vpbe_current_encoder_info`:

vpbe_current_encoder_info
=========================

.. c:function:: struct encoder_config_info*vpbe_current_encoder_info(struct vpbe_device *vpbe_dev)

    Get config info for current encoder

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

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
        ptr to vpbe cfg

    :param int index:
        index used by application

.. _`vpbe_find_encoder_sd_index.description`:

Description
-----------

Return sd index of the encoder

.. _`vpbe_g_cropcap`:

vpbe_g_cropcap
==============

.. c:function:: int vpbe_g_cropcap(struct vpbe_device *vpbe_dev, struct v4l2_cropcap *cropcap)

    Get crop capabilities of the display

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

    :param struct v4l2_cropcap \*cropcap:
        cropcap is a ptr to struct v4l2_cropcap

.. _`vpbe_g_cropcap.description`:

Description
-----------

Update the crop capabilities in crop cap for current
mode

.. _`vpbe_enum_outputs`:

vpbe_enum_outputs
=================

.. c:function:: int vpbe_enum_outputs(struct vpbe_device *vpbe_dev, struct v4l2_output *output)

    enumerate outputs

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

    :param struct v4l2_output \*output:
        ptr to v4l2_output structure

.. _`vpbe_enum_outputs.description`:

Description
-----------

Enumerates the outputs available at the vpbe display
returns the status, -EINVAL if end of output list

.. _`vpbe_set_output`:

vpbe_set_output
===============

.. c:function:: int vpbe_set_output(struct vpbe_device *vpbe_dev, int index)

    Set output

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

    :param int index:
        index of output

.. _`vpbe_set_output.description`:

Description
-----------

Set vpbe output to the output specified by the index

.. _`vpbe_get_output`:

vpbe_get_output
===============

.. c:function:: unsigned int vpbe_get_output(struct vpbe_device *vpbe_dev)

    Get output

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

.. _`vpbe_get_output.description`:

Description
-----------

return current vpbe output to the the index

.. _`vpbe_initialize`:

vpbe_initialize
===============

.. c:function:: int vpbe_initialize(struct device *dev, struct vpbe_device *vpbe_dev)

    Initialize the vpbe display controller

    :param struct device \*dev:
        Master and slave device ptr

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

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

    de-initialize the vpbe display controller

    :param struct device \*dev:
        Master and slave device ptr

    :param struct vpbe_device \*vpbe_dev:
        vpbe device ptr

.. _`vpbe_deinitialize.description`:

Description
-----------

vpbe_master and slave frame buffer devices calls this to de-initialize
the display controller. It is called when master and slave device
driver modules are removed and no longer requires the display controller.

.. This file was automatic generated / don't edit.


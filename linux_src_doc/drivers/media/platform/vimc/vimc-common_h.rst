.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vimc/vimc-common.h

.. _`vimc_platform_data`:

struct vimc_platform_data
=========================

.. c:type:: struct vimc_platform_data

    platform data to components

.. _`vimc_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct vimc_platform_data {
        char entity_name[32];
    }

.. _`vimc_platform_data.members`:

Members
-------

entity_name
    The name of the entity to be created

.. _`vimc_platform_data.description`:

Description
-----------

Board setup code will often provide additional information using the device's
platform_data field to hold additional information.
When injecting a new platform_device in the component system the core needs
to provide to the corresponding submodules the name of the entity that should
be used when registering the subdevice in the Media Controller system.

.. _`vimc_pix_map`:

struct vimc_pix_map
===================

.. c:type:: struct vimc_pix_map

    maps media bus code with v4l2 pixel format

.. _`vimc_pix_map.definition`:

Definition
----------

.. code-block:: c

    struct vimc_pix_map {
        unsigned int code;
        unsigned int bpp;
        u32 pixelformat;
        bool bayer;
    }

.. _`vimc_pix_map.members`:

Members
-------

code
    media bus format code defined by MEDIA_BUS_FMT\_\* macros

bpp
    *undescribed*

pixelformat
    pixel format devined by V4L2_PIX_FMT\_\* macros

bayer
    *undescribed*

.. _`vimc_pix_map.description`:

Description
-----------

Struct which matches the MEDIA_BUS_FMT\_\* codes with the corresponding
V4L2_PIX_FMT\_\* fourcc pixelformat and its bytes per pixel (bpp)

.. _`vimc_ent_device`:

struct vimc_ent_device
======================

.. c:type:: struct vimc_ent_device

    core struct that represents a node in the topology

.. _`vimc_ent_device.definition`:

Definition
----------

.. code-block:: c

    struct vimc_ent_device {
        struct media_entity *ent;
        struct media_pad *pads;
        void (*process_frame)(struct vimc_ent_device *ved, struct media_pad *sink, const void *frame);
        void (*vdev_get_format)(struct vimc_ent_device *ved, struct v4l2_pix_format *fmt);
    }

.. _`vimc_ent_device.members`:

Members
-------

ent
    the pointer to struct media_entity for the node

pads
    the list of pads of the node

process_frame
    callback send a frame to that node

vdev_get_format
    callback that returns the current format a pad, used
    only when is_media_entity_v4l2_video_device(ent) returns
    true

.. _`vimc_ent_device.description`:

Description
-----------

Each node of the topology must create a vimc_ent_device struct. Depending on
the node it will be of an instance of v4l2_subdev or video_device struct
where both contains a struct media_entity.
Those structures should embedded the vimc_ent_device struct through
\ :c:func:`v4l2_set_subdevdata`\  and \ :c:func:`video_set_drvdata`\  respectivaly, allowing the
vimc_ent_device struct to be retrieved from the corresponding struct
media_entity

.. _`vimc_propagate_frame`:

vimc_propagate_frame
====================

.. c:function:: int vimc_propagate_frame(struct media_pad *src, const void *frame)

    propagate a frame through the topology

    :param src:
        the source pad where the frame is being originated
    :type src: struct media_pad \*

    :param frame:
        the frame to be propagated
    :type frame: const void \*

.. _`vimc_propagate_frame.description`:

Description
-----------

This function will call the process_frame callback from the vimc_ent_device
struct of the nodes directly connected to the \ ``src``\  pad

.. _`vimc_pads_init`:

vimc_pads_init
==============

.. c:function:: struct media_pad *vimc_pads_init(u16 num_pads, const unsigned long *pads_flag)

    initialize pads

    :param num_pads:
        number of pads to initialize
    :type num_pads: u16

    :param pads_flag:
        *undescribed*
    :type pads_flag: const unsigned long \*

.. _`vimc_pads_init.description`:

Description
-----------

Helper functions to allocate/initialize pads

.. _`vimc_pads_cleanup`:

vimc_pads_cleanup
=================

.. c:function:: void vimc_pads_cleanup(struct media_pad *pads)

    free pads

    :param pads:
        pointer to the pads
    :type pads: struct media_pad \*

.. _`vimc_pads_cleanup.description`:

Description
-----------

Helper function to free the pads initialized with vimc_pads_init

.. _`vimc_pipeline_s_stream`:

vimc_pipeline_s_stream
======================

.. c:function:: int vimc_pipeline_s_stream(struct media_entity *ent, int enable)

    start stream through the pipeline

    :param ent:
        the pointer to struct media_entity for the node
    :type ent: struct media_entity \*

    :param enable:
        1 to start the stream and 0 to stop
    :type enable: int

.. _`vimc_pipeline_s_stream.description`:

Description
-----------

Helper function to call the s_stream of the subdevices connected
in all the sink pads of the entity

.. _`vimc_pix_map_by_index`:

vimc_pix_map_by_index
=====================

.. c:function:: const struct vimc_pix_map *vimc_pix_map_by_index(unsigned int i)

    get vimc_pix_map struct by its index

    :param i:
        index of the vimc_pix_map struct in vimc_pix_map_list
    :type i: unsigned int

.. _`vimc_pix_map_by_code`:

vimc_pix_map_by_code
====================

.. c:function:: const struct vimc_pix_map *vimc_pix_map_by_code(u32 code)

    get vimc_pix_map struct by media bus code

    :param code:
        media bus format code defined by MEDIA_BUS_FMT\_\* macros
    :type code: u32

.. _`vimc_pix_map_by_pixelformat`:

vimc_pix_map_by_pixelformat
===========================

.. c:function:: const struct vimc_pix_map *vimc_pix_map_by_pixelformat(u32 pixelformat)

    get vimc_pix_map struct by v4l2 pixel format

    :param pixelformat:
        pixel format devined by V4L2_PIX_FMT\_\* macros
    :type pixelformat: u32

.. _`vimc_ent_sd_register`:

vimc_ent_sd_register
====================

.. c:function:: int vimc_ent_sd_register(struct vimc_ent_device *ved, struct v4l2_subdev *sd, struct v4l2_device *v4l2_dev, const char *const name, u32 function, u16 num_pads, const unsigned long *pads_flag, const struct v4l2_subdev_ops *sd_ops)

    initialize and register a subdev node

    :param ved:
        the vimc_ent_device struct to be initialize
    :type ved: struct vimc_ent_device \*

    :param sd:
        the v4l2_subdev struct to be initialize and registered
    :type sd: struct v4l2_subdev \*

    :param v4l2_dev:
        the v4l2 device to register the v4l2_subdev
    :type v4l2_dev: struct v4l2_device \*

    :param name:
        name of the sub-device. Please notice that the name must be
        unique.
    :type name: const char \*const

    :param function:
        media entity function defined by MEDIA_ENT_F\_\* macros
    :type function: u32

    :param num_pads:
        number of pads to initialize
    :type num_pads: u16

    :param pads_flag:
        flags to use in each pad
    :type pads_flag: const unsigned long \*

    :param sd_ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ .
    :type sd_ops: const struct v4l2_subdev_ops \*

.. _`vimc_ent_sd_register.description`:

Description
-----------

Helper function initialize and register the struct vimc_ent_device and struct
v4l2_subdev which represents a subdev node in the topology

.. _`vimc_ent_sd_unregister`:

vimc_ent_sd_unregister
======================

.. c:function:: void vimc_ent_sd_unregister(struct vimc_ent_device *ved, struct v4l2_subdev *sd)

    cleanup and unregister a subdev node

    :param ved:
        the vimc_ent_device struct to be cleaned up
    :type ved: struct vimc_ent_device \*

    :param sd:
        the v4l2_subdev struct to be unregistered
    :type sd: struct v4l2_subdev \*

.. _`vimc_ent_sd_unregister.description`:

Description
-----------

Helper function cleanup and unregister the struct vimc_ent_device and struct
v4l2_subdev which represents a subdev node in the topology

.. _`vimc_link_validate`:

vimc_link_validate
==================

.. c:function:: int vimc_link_validate(struct media_link *link)

    validates a media link

    :param link:
        pointer to \ :c:type:`struct media_link <media_link>`\ 
    :type link: struct media_link \*

.. _`vimc_link_validate.description`:

Description
-----------

This function calls validates if a media link is valid for streaming.

.. This file was automatic generated / don't edit.


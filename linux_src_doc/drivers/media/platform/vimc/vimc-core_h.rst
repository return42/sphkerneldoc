.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vimc/vimc-core.h

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
        void (*destroy)(struct vimc_ent_device *);
        void (*process_frame)(struct vimc_ent_device *ved, struct media_pad *sink, const void *frame);
    }

.. _`vimc_ent_device.members`:

Members
-------

ent
    the pointer to struct media_entity for the node

pads
    the list of pads of the node

destroy
    callback to destroy the node

process_frame
    callback send a frame to that node

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

    :param struct media_pad \*src:
        the source pad where the frame is being originated

    :param const void \*frame:
        the frame to be propagated

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

    :param u16 num_pads:
        number of pads to initialize

    :param const unsigned long \*pads_flag:
        *undescribed*

.. _`vimc_pads_init.description`:

Description
-----------

Helper functions to allocate/initialize pads

.. _`vimc_pads_cleanup`:

vimc_pads_cleanup
=================

.. c:function:: void vimc_pads_cleanup(struct media_pad *pads)

    free pads

    :param struct media_pad \*pads:
        pointer to the pads

.. _`vimc_pads_cleanup.description`:

Description
-----------

Helper function to free the pads initialized with vimc_pads_init

.. _`vimc_pix_map_by_code`:

vimc_pix_map_by_code
====================

.. c:function:: const struct vimc_pix_map *vimc_pix_map_by_code(u32 code)

    get vimc_pix_map struct by media bus code

    :param u32 code:
        media bus format code defined by MEDIA_BUS_FMT\_\* macros

.. _`vimc_pix_map_by_pixelformat`:

vimc_pix_map_by_pixelformat
===========================

.. c:function:: const struct vimc_pix_map *vimc_pix_map_by_pixelformat(u32 pixelformat)

    get vimc_pix_map struct by v4l2 pixel format

    :param u32 pixelformat:
        pixel format devined by V4L2_PIX_FMT\_\* macros

.. This file was automatic generated / don't edit.


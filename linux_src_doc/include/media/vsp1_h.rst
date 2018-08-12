.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/vsp1.h

.. _`vsp1_du_lif_config`:

struct vsp1_du_lif_config
=========================

.. c:type:: struct vsp1_du_lif_config

    VSP LIF configuration

.. _`vsp1_du_lif_config.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_du_lif_config {
        unsigned int width;
        unsigned int height;
        void (*callback)(void *data, bool completed, u32 crc);
        void *callback_data;
    }

.. _`vsp1_du_lif_config.members`:

Members
-------

width
    output frame width

height
    output frame height

callback
    frame completion callback function (optional). When a callback
    is provided, the VSP driver guarantees that it will be called once
    and only once for each \ :c:func:`vsp1_du_atomic_flush`\  call.

callback_data
    data to be passed to the frame completion callback

.. _`vsp1_du_atomic_config`:

struct vsp1_du_atomic_config
============================

.. c:type:: struct vsp1_du_atomic_config

    VSP atomic configuration parameters

.. _`vsp1_du_atomic_config.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_du_atomic_config {
        u32 pixelformat;
        unsigned int pitch;
        dma_addr_t mem[3];
        struct v4l2_rect src;
        struct v4l2_rect dst;
        unsigned int alpha;
        unsigned int zpos;
    }

.. _`vsp1_du_atomic_config.members`:

Members
-------

pixelformat
    plane pixel format (V4L2 4CC)

pitch
    line pitch in bytes, for all planes

mem
    DMA memory address for each plane of the frame buffer

src
    source rectangle in the frame buffer (integer coordinates)

dst
    destination rectangle on the display (integer coordinates)

alpha
    alpha value (0: fully transparent, 255: fully opaque)

zpos
    Z position of the plane (from 0 to number of planes minus 1)

.. _`vsp1_du_crc_source`:

enum vsp1_du_crc_source
=======================

.. c:type:: enum vsp1_du_crc_source

    Source used for CRC calculation

.. _`vsp1_du_crc_source.definition`:

Definition
----------

.. code-block:: c

    enum vsp1_du_crc_source {
        VSP1_DU_CRC_NONE,
        VSP1_DU_CRC_PLANE,
        VSP1_DU_CRC_OUTPUT
    };

.. _`vsp1_du_crc_source.constants`:

Constants
---------

VSP1_DU_CRC_NONE
    CRC calculation disabled

VSP1_DU_CRC_PLANE
    Perform CRC calculation on an input plane

VSP1_DU_CRC_OUTPUT
    Perform CRC calculation on the composed output

.. _`vsp1_du_crc_config`:

struct vsp1_du_crc_config
=========================

.. c:type:: struct vsp1_du_crc_config

    VSP CRC computation configuration parameters

.. _`vsp1_du_crc_config.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_du_crc_config {
        enum vsp1_du_crc_source source;
        unsigned int index;
    }

.. _`vsp1_du_crc_config.members`:

Members
-------

source
    source for CRC calculation

index
    index of the CRC source plane (when source is set to plane)

.. _`vsp1_du_atomic_pipe_config`:

struct vsp1_du_atomic_pipe_config
=================================

.. c:type:: struct vsp1_du_atomic_pipe_config

    VSP atomic pipe configuration parameters

.. _`vsp1_du_atomic_pipe_config.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_du_atomic_pipe_config {
        struct vsp1_du_crc_config crc;
    }

.. _`vsp1_du_atomic_pipe_config.members`:

Members
-------

crc
    CRC computation configuration

.. This file was automatic generated / don't edit.


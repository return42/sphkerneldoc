.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/rcar_fdp1.c

.. _`fdp1_fmt`:

struct fdp1_fmt
===============

.. c:type:: struct fdp1_fmt

    The FDP1 internal format data

.. _`fdp1_fmt.definition`:

Definition
----------

.. code-block:: c

    struct fdp1_fmt {
        u32 fourcc;
        u8 bpp[3];
        u8 num_planes;
        u8 hsub;
        u8 vsub;
        u8 fmt;
        bool swap_yc;
        bool swap_uv;
        u8 swap;
        u8 types;
    }

.. _`fdp1_fmt.members`:

Members
-------

fourcc
    the fourcc code, to match the V4L2 API

bpp
    bits per pixel per plane

num_planes
    number of planes

hsub
    horizontal subsampling factor

vsub
    vertical subsampling factor

fmt
    7-bit format code for the fdp1 hardware

swap_yc
    the Y and C components are swapped (Y comes before C)

swap_uv
    the U and V components are swapped (V comes before U)

swap
    swap register control

types
    types of queue this format is applicable to

.. This file was automatic generated / don't edit.


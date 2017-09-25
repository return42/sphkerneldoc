.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/include/linux/atomisp.h

.. _`atomisp_cont_capture_conf`:

struct atomisp_cont_capture_conf
================================

.. c:type:: struct atomisp_cont_capture_conf

    continuous capture parameters

.. _`atomisp_cont_capture_conf.definition`:

Definition
----------

.. code-block:: c

    struct atomisp_cont_capture_conf {
        int num_captures;
        unsigned int skip_frames;
        int offset;
        __u32 reserved[5];
    }

.. _`atomisp_cont_capture_conf.members`:

Members
-------

num_captures
    number of still images to capture

skip_frames
    number of frames to skip between 2 captures

offset
    offset in ring buffer to start capture

reserved
    *undescribed*

.. _`atomisp_cont_capture_conf.description`:

Description
-----------

For example, to capture 1 frame from past, current, and 1 from future
and skip one frame between each capture, parameters would be:
num_captures:3
skip_frames:1
offset:-2

.. This file was automatic generated / don't edit.


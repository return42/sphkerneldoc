.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vtc.c

.. _`xvtc_device`:

struct xvtc_device
==================

.. c:type:: struct xvtc_device

    Xilinx Video Timing Controller device structure

.. _`xvtc_device.definition`:

Definition
----------

.. code-block:: c

    struct xvtc_device {
        struct xvip_device xvip;
        struct list_head list;
        bool has_detector;
        bool has_generator;
        struct xvtc_config config;
    }

.. _`xvtc_device.members`:

Members
-------

xvip
    Xilinx Video IP device

list
    entry in the global VTC list

has_detector
    the VTC has a timing detector

has_generator
    the VTC has a timing generator

config
    generator timings configuration

.. This file was automatic generated / don't edit.


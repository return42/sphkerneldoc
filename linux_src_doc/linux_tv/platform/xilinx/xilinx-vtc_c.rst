.. -*- coding: utf-8; mode: rst -*-

============
xilinx-vtc.c
============



.. _xref_struct_xvtc_device:

struct xvtc_device
==================

.. c:type:: struct xvtc_device

    Xilinx Video Timing Controller device structure



Definition
----------

.. code-block:: c

  struct xvtc_device {
    struct xvip_device xvip;
    struct list_head list;
    bool has_detector;
    bool has_generator;
    struct xvtc_config config;
  };



Members
-------

:``struct xvip_device xvip``:
    Xilinx Video IP device

:``struct list_head list``:
    entry in the global VTC list

:``bool has_detector``:
    the VTC has a timing detector

:``bool has_generator``:
    the VTC has a timing generator

:``struct xvtc_config config``:
    generator timings configuration




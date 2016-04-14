.. -*- coding: utf-8; mode: rst -*-

===============
v4l2-mediabus.h
===============

.. _`v4l2_mbus_type`:

enum v4l2_mbus_type
===================

.. c:type:: enum v4l2_mbus_type

    media bus type



Constants
---------

:``V4L2_MBUS_PARALLEL``:
    parallel interface with hsync and vsync

:``V4L2_MBUS_BT656``:
    parallel interface with embedded synchronisation, can
    also be used for BT.1120

:``V4L2_MBUS_CSI2``:
    MIPI CSI-2 serial interface


.. _`v4l2_mbus_config`:

struct v4l2_mbus_config
=======================

.. c:type:: struct v4l2_mbus_config

    media bus configuration



Definition
----------

.. code-block:: c

  struct v4l2_mbus_config {
    enum v4l2_mbus_type type;
    unsigned int flags;
  };



Members
-------

:``type``:
    in: interface type

:``flags``:
    in / out: configuration flags, depending on ``type``



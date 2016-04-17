.. -*- coding: utf-8; mode: rst -*-

============
camera-mx2.h
============


.. _`mx2_camera_platform_data`:

struct mx2_camera_platform_data
===============================

.. c:type:: mx2_camera_platform_data

    optional platform data for mx2_camera


.. _`mx2_camera_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct mx2_camera_platform_data {
    unsigned long flags;
    unsigned long clk;
  };


.. _`mx2_camera_platform_data.members`:

Members
-------

:``flags``:
    any combination of MX2_CAMERA\_\*

:``clk``:
    clock rate of the csi block / 2



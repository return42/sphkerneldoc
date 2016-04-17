.. -*- coding: utf-8; mode: rst -*-

============
soc_camera.h
============


.. _`soc_camera_format_xlate`:

struct soc_camera_format_xlate
==============================

.. c:type:: soc_camera_format_xlate

    match between host and sensor formats


.. _`soc_camera_format_xlate.definition`:

Definition
----------

.. code-block:: c

  struct soc_camera_format_xlate {
    u32 code;
    const struct soc_mbus_pixelfmt * host_fmt;
  };


.. _`soc_camera_format_xlate.members`:

Members
-------

:``code``:
    code of a sensor provided format

:``host_fmt``:
    host format after host translation from code




.. _`soc_camera_format_xlate.description`:

Description
-----------

Host and sensor translation structure. Used in table of host and sensor
formats matchings in soc_camera_device. A host can override the generic list
generation by implementing :c:func:`get_formats`, and use it for format checks and
format setup.


.. -*- coding: utf-8; mode: rst -*-

======================
raspberrypi-firmware.h
======================


.. _`rpi_firmware_property_tag_header`:

struct rpi_firmware_property_tag_header
=======================================

.. c:type:: rpi_firmware_property_tag_header

    Firmware property tag header


.. _`rpi_firmware_property_tag_header.definition`:

Definition
----------

.. code-block:: c

  struct rpi_firmware_property_tag_header {
    u32 tag;
    u32 buf_size;
    u32 req_resp_size;
  };


.. _`rpi_firmware_property_tag_header.members`:

Members
-------

:``tag``:
    One of enum_mbox_property_tag.

:``buf_size``:
    The number of bytes in the value buffer following this
    struct.

:``req_resp_size``:
    On submit, the length of the request (though it doesn't
    appear to be currently used by the firmware).  On return,
    the length of the response (always 4 byte aligned), with
    the low bit set.



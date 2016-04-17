.. -*- coding: utf-8; mode: rst -*-

==========
cycx_cfm.h
==========


.. _`cycx_fw_info`:

struct cycx_fw_info
===================

.. c:type:: cycx_fw_info

    firmware module information. @codeid - firmware ID @version - firmware version number @adapter - compatible adapter types @memsize - minimum memory size @reserved - reserved @startoffs - entry point offset @winoffs - dual-port memory window offset @codeoffs - code load offset @codesize - code size @dataoffs - configuration data load offset @datasize - configuration data size


.. _`cycx_fw_info.definition`:

Definition
----------

.. code-block:: c

  struct cycx_fw_info {
  };


.. _`cycx_fw_info.members`:

Members
-------




.. _`cycx_firmware`:

struct cycx_firmware
====================

.. c:type:: cycx_firmware

    CYCX firmware file structure @signature - CFM file signature @version - file format version @checksum - info + image @reserved - reserved @descr - description string @info - firmware module info @image - code image (variable size)


.. _`cycx_firmware.definition`:

Definition
----------

.. code-block:: c

  struct cycx_firmware {
  };


.. _`cycx_firmware.members`:

Members
-------




.. _API-enum-vga-switcheroo-client-id:

=============================
enum vga_switcheroo_client_id
=============================

*man enum vga_switcheroo_client_id(9)*

*4.6.0-rc1*

client identifier


Synopsis
========

.. code-block:: c

    enum vga_switcheroo_client_id {
      VGA_SWITCHEROO_UNKNOWN_ID,
      VGA_SWITCHEROO_IGD,
      VGA_SWITCHEROO_DIS,
      VGA_SWITCHEROO_MAX_CLIENTS
    };


Constants
=========

VGA_SWITCHEROO_UNKNOWN_ID
    initial identifier assigned to vga clients. Determining the id requires the handler, so GPUs are given their true id in a delayed fashion in ``vga_switcheroo_enable``

VGA_SWITCHEROO_IGD
    integrated graphics device

VGA_SWITCHEROO_DIS
    discrete graphics device

VGA_SWITCHEROO_MAX_CLIENTS
    currently no more than two GPUs are supported


Description
===========

Client identifier. Audio clients use the same identifier & 0x100.

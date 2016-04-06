
.. _API-enum-dmx-frontend-source:

========================
enum dmx_frontend_source
========================

*man enum dmx_frontend_source(9)*

*4.6.0-rc1*

Used to identify the type of frontend


Synopsis
========

.. code-block:: c

    enum dmx_frontend_source {
      DMX_MEMORY_FE,
      DMX_FRONTEND_0
    };


Constants
=========

DMX_MEMORY_FE
    The source of the demux is memory. It means that the MPEG-TS to be filtered comes from userspace, via ``write`` syscall.

DMX_FRONTEND_0
    The source of the demux is a frontend connected to the demux.

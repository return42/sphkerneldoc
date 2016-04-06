
.. _API-struct-uio-port:

===============
struct uio_port
===============

*man struct uio_port(9)*

*4.6.0-rc1*

description of a UIO port region


Synopsis
========

.. code-block:: c

    struct uio_port {
      const char * name;
      unsigned long start;
      unsigned long size;
      int porttype;
      struct uio_portio * portio;
    };


Members
=======

name
    name of the port region for identification

start
    start of port region

size
    size of port region

porttype
    type of port (see UIO_PORT_⋆ below)

portio
    for use by the UIO core only.

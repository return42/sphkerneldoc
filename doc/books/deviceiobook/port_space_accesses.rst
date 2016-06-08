.. -*- coding: utf-8; mode: rst -*-

.. _port_space_accesses:

*******************
Port Space Accesses
*******************


.. _port_space_explained:

Port Space Explained
====================

Another form of IO commonly supported is Port Space. This is a range of
addresses separate to the normal memory address space. Access to these
addresses is generally not as fast as accesses to the memory mapped
addresses, and it also has a potentially smaller address space.

Unlike memory mapped IO, no preparation is required to access port
space.


.. _accessing_port_space:

Accessing Port Space
====================

Accesses to this space are provided through a set of functions which
allow 8-bit, 16-bit and 32-bit accesses; also known as byte, word and
long. These functions are ``inb``, ``inw``, ``inl``, ``outb``, ``outw``
and ``outl``.

Some variants are provided for these functions. Some devices require
that accesses to their ports are slowed down. This functionality is
provided by appending a ``_p`` to the end of the function. There are
also equivalents to memcpy. The ``ins`` and ``outs`` functions copy
bytes, words or longs to the given port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

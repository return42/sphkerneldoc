.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/wil6210_uapi.h

.. _`wil_ioctl_memio`:

WIL_IOCTL_MEMIO
===============

.. c:function::  WIL_IOCTL_MEMIO()

    bit I/O operation to the card memory

.. _`wil_ioctl_memio.user-code-should-arrange-data-in-memory-like-this`:

User code should arrange data in memory like this
-------------------------------------------------


struct wil_memio io;
struct ifreq ifr = {
.ifr_data = \ :c:type:`struct io <io>`,
};

.. _`wil_ioctl_memio_block`:

WIL_IOCTL_MEMIO_BLOCK
=====================

.. c:function::  WIL_IOCTL_MEMIO_BLOCK()

.. _`wil_ioctl_memio_block.user-code-should-arrange-data-in-memory-like-this`:

User code should arrange data in memory like this
-------------------------------------------------


void \*buf;
struct wil_memio_block io = {
.block = buf,
};
struct ifreq ifr = {
.ifr_data = \ :c:type:`struct io <io>`,
};

.. This file was automatic generated / don't edit.


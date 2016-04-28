.. -*- coding: utf-8; mode: rst -*-

.. _userspace_driver:

=============================
Writing a driver in userspace
=============================

Once you have a working kernel module for your hardware, you can write
the userspace part of your driver. You don't need any special libraries,
your driver can be written in any reasonable language, you can use
floating point numbers and so on. In short, you can use all the tools
and libraries you'd normally use for writing a userspace application.


.. _getting_uio_information:

Getting information about your UIO device
=========================================

Information about all UIO devices is available in sysfs. The first thing
you should do in your driver is check ``name`` and ``version`` to make
sure your talking to the right device and that its kernel driver has the
version you expect.

You should also make sure that the memory mapping you need exists and
has the size you expect.

There is a tool called ``lsuio`` that lists UIO devices and their
attributes. It is available here:

`http://www.osadl.org/projects/downloads/UIO/user/ <http://www.osadl.org/projects/downloads/UIO/user/>`__

With ``lsuio`` you can quickly check if your kernel module is loaded and
which attributes it exports. Have a look at the manpage for details.

The source code of ``lsuio`` can serve as an example for getting
information about an UIO device. The file ``uio_helper.c`` contains a
lot of functions you could use in your userspace driver code.


.. _mmap_device_memory:

mmap() device memory
====================

After you made sure you've got the right device with the memory mappings
you need, all you have to do is to call ``mmap()`` to map the device's
memory to userspace.

The parameter ``offset`` of the ``mmap()`` call has a special meaning
for UIO devices: It is used to select which mapping of your device you
want to map. To map the memory of mapping N, you have to use N times the
page size as your offset:


.. code-block:: c

        offset = N * getpagesize();

N starts from zero, so if you've got only one memory range to map, set
``offset = 0``. A drawback of this technique is that memory is always
mapped beginning with its start address.


.. _wait_for_interrupts:

Waiting for interrupts
======================

After you successfully mapped your devices memory, you can access it
like an ordinary array. Usually, you will perform some initialization.
After that, your hardware starts working and will generate an interrupt
as soon as it's finished, has some data available, or needs your
attention because an error occurred.

``/dev/uioX`` is a read-only file. A ``read()`` will always block until
an interrupt occurs. There is only one legal value for the ``count``
parameter of ``read()``, and that is the size of a signed 32 bit integer
(4). Any other value for ``count`` causes ``read()`` to fail. The signed
32 bit integer read is the interrupt count of your device. If the value
is one more than the value you read the last time, everything is OK. If
the difference is greater than one, you missed interrupts.

You can also use ``select()`` on ``/dev/uioX``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

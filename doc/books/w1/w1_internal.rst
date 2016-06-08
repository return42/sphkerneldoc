.. -*- coding: utf-8; mode: rst -*-

.. _w1_internal:

*****************************
W1 API internal to the kernel
*****************************


.. _w1_internal_api:

W1 API internal to the kernel
=============================


.. _w1.h:

drivers/w1/w1.h
---------------

W1 core functions.


.. kernel-doc:: drivers/w1/w1.h
    :internal:

.. _w1.c:

drivers/w1/w1.c
---------------

W1 core functions.


.. kernel-doc:: drivers/w1/w1.c
    :internal:

.. _w1_family.h:

drivers/w1/w1_family.h
----------------------

Allows registering device family operations.


.. kernel-doc:: drivers/w1/w1_family.h
    :internal:

.. _w1_family.c:

drivers/w1/w1_family.c
----------------------

Allows registering device family operations.


.. kernel-doc:: drivers/w1/w1_family.c
    :export:

.. _w1_int.c:

drivers/w1/w1_int.c
-------------------

W1 internal initialization for master devices.


.. kernel-doc:: drivers/w1/w1_int.c
    :export:

.. _w1_netlink.h:

drivers/w1/w1_netlink.h
-----------------------

W1 external netlink API structures and commands.


.. kernel-doc:: drivers/w1/w1_netlink.h
    :internal:

.. _w1_io.c:

drivers/w1/w1_io.c
------------------

W1 input/output.


.. kernel-doc:: drivers/w1/w1_io.c
    :export:

.. kernel-doc:: drivers/w1/w1_io.c
    :internal:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

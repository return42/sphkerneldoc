.. -*- coding: utf-8; mode: rst -*-

+++++++++++++++++++++++
The Userspace I/O HOWTO
+++++++++++++++++++++++

**Copyright** 2006-2008 : Hans-Jürgen Koch.

**Copyright** 2009 : Red Hat Inc, Michael S. Tsirkin (mst@redhat.com)

This documentation is Free Software licensed under the terms of the GPL
version 2.

2006-12-11
    This HOWTO describes concept and usage of Linux kernel's Userspace
    I/O system.


:revision: 0.9 / 2009-07-16 (*mst*)

Added generic pci driver


:revision: 0.8 / 2008-12-24 (*hjk*)

Added name attributes in mem and portio sysfs directories.


:revision: 0.7 / 2008-12-23 (*hjk*)

Added generic platform drivers and offset attribute.


:revision: 0.6 / 2008-12-05 (*hjk*)

Added description of portio sysfs attributes.


:revision: 0.5 / 2008-05-22 (*hjk*)

Added description of write() function.


:revision: 0.4 / 2007-11-26 (*hjk*)

Removed section about uio_dummy.


:revision: 0.3 / 2007-04-29 (*hjk*)

Added section about userspace drivers.


:revision: 0.2 / 2007-02-13 (*hjk*)

Update after multiple mappings were added.


:revision: 0.1 / 2006-12-11 (*hjk*)

First draft.


.. toctree::
    :maxdepth: 1

    aboutthisdoc
    about
    custom_kernel_module
    userspace_driver
    uio_pci_generic


.. _app1:

===================
Further information
===================

-  `OSADL homepage. <http://www.osadl.org>`__

-  `Linutronix homepage. <http://www.linutronix.de>`__


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


Retrieval
=========

* :ref:`genindex`

.. todolist::

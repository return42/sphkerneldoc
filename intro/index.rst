.. -*- coding: utf-8; mode: rst -*-
.. include:: article_refs.txt


================================================================================
                          Linux Kernel's documentation
================================================================================

Welcome to the Linux Kernel's documentation. Here you will find the Linux Kernel
documentation maintained in -- or converted to -- the reStructuredText
(**reST**) format. This is a *POC* to demonstrate how a *straight forward*
documentation build might look like.  At this time, not all of this POC is a
part of the Linux kernel source tree. If you wan't to read more about reST,
Sphinx and this POC jump to:

.. toctree::
   :maxdepth: 1

   poc_sphkerneldoc/index

HTML rendered *kernel-doc* comments
===================================

The *kernel-doc* comments from Kernel's source code are parsed and converted to
reST with the kernel-doc parser from the :ref:`LinuxDoc project
<linuxdoc:linuxdoc>` (see :ref:`kernel-doc <linuxdoc:kernel-doc>`). Be aware,
that this is in a experimental state, see :ref:`xref_linux_src_doc`.

* HTML: `Linux kernel source <linux_src_doc/index.html>`_
* reST: `reST linux_src_doc`_

Linux Kernel's documentation (reST)
===================================

User-oriented documentation
---------------------------

The following manuals are written for *users* of the kernel — those who are
trying to get it to work optimally on a given system.

* `The Linux kernel user's and administrator's guide <books/admin-guide/index.html>`_

Introduction to kernel development
----------------------------------

These manuals contain overall information about how to develop the kernel.
The kernel community is quite large, with thousands of developers
contributing over the course of a year.  As with any large community,
knowing how things are done will make the process of getting your changes
merged much easier.

* `Working with the kernel development community <books/process/index.html>`_
* `Development tools for the kernel <books/dev-tools/index.html>`_

The following 2 or 3 documents are a part of this POC / take it as a *prospect*
;-) ... it is not, of "what" the kernel community has unified (`ref
<https://www.kernel.org/doc/html/latest/kernel-documentation.html>`__)!

* `kernel-doc HOWTO <books/kernel-doc-HOWTO/index.html>`_
* `template book <books/template-book/index.html>`_
* There is also a :ref:`reST-nano-HOWTO` with additional informations about
  :ref:`xref_rest_and_sphinx`.

Kernel API documentation
------------------------

These books get into the details of how specific kernel subsystems work
from the point of view of a kernel developer.  Much of the information here
is taken directly from the kernel source, with supplemental material added
as needed (or at least as we managed to add it — probably *not* all that is
needed).

* `The Linux driver implementer's API guide <books/driver-api/index.html>`_
* `Linux Media Infrastructure API (linux-tv) <books/media/index.html>`_
* `Linux GPU Driver Developer's Guide <books/gpu/index.html>`_
* `The 802.11 subsystems <books/80211/index.html>`_

.. _xref_migrated_docbook:

Linux Kernel's documentation (DocBook)
======================================

This section list DocBooks (`ref <https://www.kernel.org/doc/htmldocs>`__)
content, which was has been automatic converted by this POC to the reST markup
(and compiled to HTML). If you want to see the reST markup jump to the
`sources <https://github.com/return42/sphkerneldoc/tree/master/Documentation/books_migrated>`__.
The DocBook/reST conversion is done with the reST with the :ref:`DocBook-XML to
reST project <dbxml2rst:dbxml2rst>` (see :ref:`dbxml2rst_migration`).

* `The ALSA Driver API <books/alsa-driver-api/index.html>`_
* `Linux Kernel Crypto API <books/crypto-API/index.html>`_
* `Debug objects life time <books/debugobjects/index.html>`_
* `Bus-Independent Device Accesses <books/deviceiobook/index.html>`_
* `Linux Filesystems API <books/filesystems/index.html>`_
* `USB Gadget API for Linux <books/gadget/index.html>`_
* `Linux generic IRQ handling <books/genericirq/index.html>`_
* `Industrial I/O driver developer's guide <books/iio/index.html>`_
* `The Linux Kernel API <books/kernel-api/index.html>`_
* `Unreliable Guide To Hacking The Linux Kernel <books/kernel-hacking/index.html>`_
* `Unreliable Guide To Locking <books/kernel-locking/index.html>`_
* `Using kgdb, kdb and the kernel debugger internals <books/kgdb/index.html>`_
* `libATA Developer's Guide <books/libata/index.html>`_
* `Reed-Solomon Library Programming Interface <books/librs/index.html>`_
* `LSM kernel patch <books/lsm/index.html>`_
* `MTD NAND Driver Programming Interface <books/mtdnand/index.html>`_
* `Linux Networking and Network Devices APIs <books/networking/index.html>`_
* `RapidIO Subsystem Guide <books/rapidio/index.html>`_
* `Voltage and current regulator API <books/regulator/index.html>`_
* `Writing s390 channel device drivers <books/s390-drivers/index.html>`_
* `SCSI Interfaces Guide <books/scsi/index.html>`_
* `SuperH Interfaces Guide <books/sh/index.html>`_
* `The Linux Kernel Tracepoint API <books/tracepoint/index.html>`_
* `The Userspace I/O HOWTO <books/uio-howto/index.html>`_
* `The Linux-USB Host Side API <books/usb/index.html>`_
* `W1: Dallas' 1-wire bus <books/w1/index.html>`_
* `Writing an ALSA Driver <books/writing-an-alsa-driver/index.html>`_
* `Writing an MUSB Glue Layer <books/writing_musb_glue_layer/index.html>`_
* `Writing USB Device Drivers <books/writing_usb_driver/index.html>`_
* `Z8530 Programming Guide <books/z8530book/index.html>`_

Collection of articles
======================

The following documents are a part of this POC (not of Kernel's sources!).

.. toctree::
   :maxdepth: 1
   :glob:

   reST-nano-HOWTO

.. -*- coding: utf-8; mode: rst -*-
.. include:: article_refs.txt

================================================================================
                          Linux Kernel's documentation
================================================================================

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
  (`pdf <books/admin-guide/pdf>`__, `man <books/admin-guide/man>`__)

Introduction to kernel development
----------------------------------

These manuals contain overall information about how to develop the kernel.
The kernel community is quite large, with thousands of developers
contributing over the course of a year.  As with any large community,
knowing how things are done will make the process of getting your changes
merged much easier.

* `Working with the kernel development community <books/process/index.html>`_
  (`pdf <books/process/pdf>`__, `man <books/process/man>`__)

* `Development tools for the kernel <books/dev-tools/index.html>`_
  (`pdf <books/dev-tools/pdf>`__, `man <books/dev-tools/man>`__)

The following 2 or 3 documents are a part of this POC / take it as a *prospect*
;-) ... it is not, of "what" the kernel community has unified (`ref
<https://www.kernel.org/doc/html/latest/kernel-documentation.html>`__)!

* `kernel-doc HOWTO <books/kernel-doc-HOWTO/index.html>`_
  (`pdf <books/kernel-doc-HOWTO/pdf>`__, `man <books/kernel-doc-HOWTO/man>`__)

* `template book <books/template-book/index.html>`_
  (`pdf <books/template-book/pdf>`__, `man <books/template-book/man>`__)

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
  (`pdf <books/driver-api/pdf>`__, `man <books/driver-api/man>`__)

* FIXME: not yet `Linux Media Infrastructure API (linux-tv) <books/media/index.html>`_
  (`pdf <books/media/pdf>`__, `man <books/media/man>`__)

* `Linux GPU Driver Developer's Guide <books/gpu/index.html>`_
  (`pdf <books/gpu/pdf>`__, `man <books/gpu/man>`__)

* `The 802.11 subsystems <books/80211/index.html>`_
  (`pdf <books/80211/pdf>`__, `man <books/80211/man>`__)

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
  (`pdf <books/alsa-driver-api/pdf>`__, `man <books/alsa-driver-api/man>`__)

* `Linux Kernel Crypto API <books/crypto-API/index.html>`_
  (`pdf <books/crypto-API/pdf>`__, `man <books/crypto-API/man>`__)

* `Debug objects life time <books/debugobjects/index.html>`_
  (`pdf <books/debugobjects/pdf>`__, `man <books/debugobjects/man>`__)

* `Bus-Independent Device Accesses <books/deviceiobook/index.html>`_
  (`pdf <books/deviceiobook/pdf>`__, `man <books/deviceiobook/man>`__)

* `Linux Filesystems API <books/filesystems/index.html>`_
  (`pdf <books/filesystems/pdf>`__, `man <books/filesystems/man>`__)

* `USB Gadget API for Linux <books/gadget/index.html>`_
  (`pdf <books/gadget/pdf>`__, `man <books/gadget/man>`__)

* `Linux generic IRQ handling <books/genericirq/index.html>`_
  (`pdf <books/genericirq/pdf>`__, `man <books/genericirq/man>`__)

* `Industrial I/O driver developer's guide <books/iio/index.html>`_
  (`pdf <books/iio/pdf>`__, `man <books/iio/man>`__)

* `The Linux Kernel API <books/kernel-api/index.html>`_
  (`pdf <books/kernel-api/pdf>`__, `man <books/kernel-api/man>`__)

* `Unreliable Guide To Hacking The Linux Kernel <books/kernel-hacking/index.html>`_
  (`pdf <books/kernel-hacking/pdf>`__, `man <books/kernel-hacking/man>`__)

* `Unreliable Guide To Locking <books/kernel-locking/index.html>`_
  (`pdf <books/kernel-locking/pdf>`__, `man <books/kernel-locking/man>`__)

* `Using kgdb, kdb and the kernel debugger internals <books/kgdb/index.html>`_
  (`pdf <books/kgdb/pdf>`__, `man <books/kgdb/man>`__)

* `libATA Developer's Guide <books/libata/index.html>`_
  (`pdf <books/libata/pdf>`__, `man <books/libata/man>`__)

* `Reed-Solomon Library Programming Interface <books/librs/index.html>`_
  (`pdf <books/librs/pdf>`__, `man <books/librs/man>`__)

* `LSM kernel patch <books/lsm/index.html>`_
  (`pdf <books/lsm/pdf>`__, `man <books/lsm/man>`__)

* `MTD NAND Driver Programming Interface <books/mtdnand/index.html>`_
  (`pdf <books/mtdnand/pdf>`__, `man <books/mtdnand/man>`__)

* `Linux Networking and Network Devices APIs <books/networking/index.html>`_
  (`pdf <books/networking/pdf>`__, `man <books/networking/man>`__)

* `RapidIO Subsystem Guide <books/rapidio/index.html>`_
  (`pdf <books/rapidio/pdf>`__, `man <books/rapidio/man>`__)

* `Voltage and current regulator API <books/regulator/index.html>`_
  (`pdf <books/regulator/pdf>`__, `man <books/regulator/man>`__)

* `Writing s390 channel device drivers <books/s390-drivers/index.html>`_
  (`pdf <books/s390-drivers/pdf>`__, `man <books/s390-drivers/man>`__)

* `SCSI Interfaces Guide <books/scsi/index.html>`_
  (`pdf <books/scsi/pdf>`__, `man <books/scsi/man>`__)

* `SuperH Interfaces Guide <books/sh/index.html>`_
  (`pdf <books/sh/pdf>`__, `man <books/sh/man>`__)

* `The Linux Kernel Tracepoint API <books/tracepoint/index.html>`_
  (`pdf <books/tracepoint/pdf>`__, `man <books/tracepoint/man>`__)

* `The Userspace I/O HOWTO <books/uio-howto/index.html>`_
  (`pdf <books/uio-howto/pdf>`__, `man <books/uio-howto/man>`__)

* `The Linux-USB Host Side API <books/usb/index.html>`_
  (`pdf <books/usb/pdf>`__, `man <books/usb/man>`__)

* `W1: Dallas' 1-wire bus <books/w1/index.html>`_
  (`pdf <books/w1/pdf>`__, `man <books/w1/man>`__)

* `Writing an ALSA Driver <books/writing-an-alsa-driver/index.html>`_
  (`pdf <books/writing-an-alsa-driver/pdf>`__, `man <books/writing-an-alsa-driver/man>`__)

* `Writing an MUSB Glue Layer <books/writing_musb_glue_layer/index.html>`_
  (`pdf <books/writing_musb_glue_layer/pdf>`__, `man <books/writing_musb_glue_layer/man>`__)

* `Writing USB Device Drivers <books/writing_usb_driver/index.html>`_
  (`pdf <books/writing_usb_driver/pdf>`__, `man <books/writing_usb_driver/man>`__)

* `Z8530 Programming Guide <books/z8530book/index.html>`_
  (`pdf <books/z8530book/pdf>`__, `man <books/z8530book/man>`__)

.. -*- coding: utf-8; mode: rst -*-
.. include:: article_refs.txt

.. _xref_migrated_docbock:

================================================================================
                          Linux Kernel's documentation
================================================================================

Welcome to the Linux Kernel's documentation. Here you will find the Linux Kernel
documentation maintained in -- or migrated to -- the reStructuredText (**reST**)
format.  At this time, not all of this POC is a part of the Linux kernel source
tree. This *POC* demonstrate how a *straight forward* solution works. It is an
approach to extend the current sphinx concepts of the linux kernel sources, by
using the libraries:

* :ref:`LinuxDoc project <linuxdoc:linuxdoc>`
* :ref:`DocBook-XML to reST project <dbxml2rst:dbxml2rst>` (see
  :ref:`dbxml2rst_migration`).

The source of this POC is available at:

* https://github.com/return42/sphkerneldoc


Collection of articles
=======================

The collection of the following articles is searchable from the search-bar
*here*.

.. toctree::
   :maxdepth: 1
   :glob:

   articles/*


References to books
===================

Each book is chunked into a small *project*. Each project has it's own
search-bar.

* `kernel-doc HOWTO <books/kernel-doc-HOWTO/index.html>`_
* `template book <books/template-book/index.html>`_
* `The 802.11 subsystems <books/80211/index.html>`_
* `The ALSA Driver API <books/alsa-driver-api/index.html>`_
* `Linux Kernel Crypto API <books/crypto-API/index.html>`_
* `Debug objects life time <books/debugobjects/index.html>`_
* `Linux Device Drivers <books/device-drivers/index.html>`_
* `Bus-Independent Device Accesses <books/deviceiobook/index.html>`_
* `Linux Filesystems API <books/filesystems/index.html>`_
* `USB Gadget API for Linux <books/gadget/index.html>`_
* `Linux generic IRQ handling <books/genericirq/index.html>`_
* `Linux GPU Driver Developer's Guide <books/gpu/index.html>`_
* `Industrial I/O driver developer's guide <books/iio/index.html>`_
* `The Linux Kernel API <books/kernel-api/index.html>`_
* `Unreliable Guide To Hacking The Linux Kernel <books/kernel-hacking/index.html>`_
* `Unreliable Guide To Locking <books/kernel-locking/index.html>`_
* `Using kgdb, kdb and the kernel debugger internals <books/kgdb/index.html>`_
* `libATA Developer's Guide <books/libata/index.html>`_
* `Reed-Solomon Library Programming Interface <books/librs/index.html>`_
* `Linux Media Infrastructure API (linux-tv) <books/linux_tv/index.html>`_
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


.. _xref_about_this_poc:

About this POC
===============

.. toctree::
   :maxdepth: 1
   :glob:

   poc_sphkerneldoc/why_rest
   poc_sphkerneldoc/linux_src_doc
   poc_sphkerneldoc/LICENSE

There is also a :ref:`reST-nano-HOWTO` with additional informations to
:ref:`xref_faq`.

.. -*- coding: utf-8; mode: rst -*-

.. _how-to-put-your-driver:

*************************************
How To Put Your Driver Into ALSA Tree
*************************************


General
=======

So far, you've learned how to write the driver codes. And you might have
a question now: how to put my own driver into the ALSA driver tree? Here
(finally :) the standard procedure is described briefly.

Suppose that you create a new PCI driver for the card “xyz”. The card
module name would be snd-xyz. The new driver is usually put into the
alsa-driver tree, ``alsa-driver/pci`` directory in the case of PCI
cards. Then the driver is evaluated, audited and tested by developers
and users. After a certain time, the driver will go to the alsa-kernel
tree (to the corresponding directory, such as ``alsa-kernel/pci``) and
eventually will be integrated into the Linux 2.6 tree (the directory
would be ``linux/sound/pci``).

In the following sections, the driver code is supposed to be put into
alsa-driver tree. The two cases are covered: a driver consisting of a
single source file and one consisting of several source files.


Driver with A Single Source File
================================

1. Modify alsa-driver/pci/Makefile

   Suppose you have a file xyz.c. Add the following two lines


   .. code-block:: c

         snd-xyz-objs := xyz.o
         obj-$(CONFIG_SND_XYZ) += snd-xyz.o

2. Create the Kconfig entry

   Add the new entry of Kconfig for your xyz driver.


   .. code-block:: c

         config SND_XYZ
                 tristate "Foobar XYZ"
                 depends on SND
                 select SND_PCM
                 help
                   Say Y here to include support for Foobar XYZ soundcard.

                   To compile this driver as a module, choose M here: the module
                   will be called snd-xyz.

   the line, select SND_PCM, specifies that the driver xyz supports
   PCM. In addition to SND_PCM, the following components are supported
   for select command: SND_RAWMIDI, SND_TIMER, SND_HWDEP,
   SND_MPU401_UART, SND_OPL3_LIB, SND_OPL4_LIB, SND_VX_LIB,
   SND_AC97_CODEC. Add the select command for each supported
   component.

   Note that some selections imply the lowlevel selections. For example,
   PCM includes TIMER, MPU401_UART includes RAWMIDI, AC97_CODEC
   includes PCM, and OPL3_LIB includes HWDEP. You don't need to give
   the lowlevel selections again.

   For the details of Kconfig script, refer to the kbuild documentation.

3. Run cvscompile script to re-generate the configure script and build
   the whole stuff again.


Drivers with Several Source Files
=================================

Suppose that the driver snd-xyz have several source files. They are
located in the new subdirectory, pci/xyz.

1. Add a new directory (``xyz``) in ``alsa-driver/pci/Makefile`` as
   below


   .. code-block:: c

         obj-$(CONFIG_SND) += xyz/

2. Under the directory ``xyz``, create a Makefile


   .. code-block:: c

         ifndef SND_TOPDIR
         SND_TOPDIR=../..
         endif

         include $(SND_TOPDIR)/toplevel.config
         include $(SND_TOPDIR)/Makefile.conf

         snd-xyz-objs := xyz.o abc.o def.o

         obj-$(CONFIG_SND_XYZ) += snd-xyz.o

         include $(SND_TOPDIR)/Rules.make

3. Create the Kconfig entry

   This procedure is as same as in the last section.

4. Run cvscompile script to re-generate the configure script and build
   the whole stuff again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

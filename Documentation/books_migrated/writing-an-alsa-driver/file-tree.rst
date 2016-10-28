.. -*- coding: utf-8; mode: rst -*-

.. _file-tree:

*******************
File Tree Structure
*******************


.. _file-tree-general:

General
=======

The ALSA drivers are provided in two ways.

One is the trees provided as a tarball or via cvs from the ALSA's ftp
site, and another is the 2.6 (or later) Linux kernel tree. To
synchronize both, the ALSA driver tree is split into two different
trees: alsa-kernel and alsa-driver. The former contains purely the
source code for the Linux 2.6 (or later) tree. This tree is designed
only for compilation on 2.6 or later environment. The latter,
alsa-driver, contains many subtle files for compiling ALSA drivers
outside of the Linux kernel tree, wrapper functions for older 2.2 and
2.4 kernels, to adapt the latest kernel API, and additional drivers
which are still in development or in tests. The drivers in alsa-driver
tree will be moved to alsa-kernel (and eventually to the 2.6 kernel
tree) when they are finished and confirmed to work fine.

The file tree structure of ALSA driver is depicted below. Both
alsa-kernel and alsa-driver have almost the same file structure, except
for “core” directory. It's named as “acore” in alsa-driver tree.



::

            sound
                    /core
                            /oss
                            /seq
                                    /oss
                                    /instr
                    /ioctl32
                    /include
                    /drivers
                            /mpu401
                            /opl3
                    /i2c
                            /l3
                    /synth
                            /emux
                    /pci
                            /(cards)
                    /isa
                            /(cards)
                    /arm
                    /ppc
                    /sparc
                    /usb
                    /pcmcia /(cards)
                    /oss

.. _file-tree-core-directory:

core directory
==============

This directory contains the middle layer which is the heart of ALSA
drivers. In this directory, the native ALSA modules are stored. The
sub-directories contain different modules and are dependent upon the
kernel config.


.. _file-tree-core-directory-oss:

core/oss
--------

The codes for PCM and mixer OSS emulation modules are stored in this
directory. The rawmidi OSS emulation is included in the ALSA rawmidi
code since it's quite small. The sequencer code is stored in
``core/seq/oss`` directory (see
:ref:`below <file-tree-core-directory-seq-oss>`).


.. _file-tree-core-directory-ioctl32:

core/ioctl32
------------

This directory contains the 32bit-ioctl wrappers for 64bit architectures
such like x86-64, ppc64 and sparc64. For 32bit and alpha architectures,
these are not compiled.


.. _file-tree-core-directory-seq:

core/seq
--------

This directory and its sub-directories are for the ALSA sequencer. This
directory contains the sequencer core and primary sequencer modules such
like snd-seq-midi, snd-seq-virmidi, etc. They are compiled only when
``CONFIG_SND_SEQUENCER`` is set in the kernel config.


.. _file-tree-core-directory-seq-oss:

core/seq/oss
------------

This contains the OSS sequencer emulation codes.


.. _file-tree-core-directory-deq-instr:

core/seq/instr
--------------

This directory contains the modules for the sequencer instrument layer.


.. _file-tree-include-directory:

include directory
=================

This is the place for the public header files of ALSA drivers, which are
to be exported to user-space, or included by several files at different
directories. Basically, the private header files should not be placed in
this directory, but you may still find files there, due to historical
reasons :)


.. _file-tree-drivers-directory:

drivers directory
=================

This directory contains code shared among different drivers on different
architectures. They are hence supposed not to be architecture-specific.
For example, the dummy pcm driver and the serial MIDI driver are found
in this directory. In the sub-directories, there is code for components
which are independent from bus and cpu architectures.


.. _file-tree-drivers-directory-mpu401:

drivers/mpu401
--------------

The MPU401 and MPU401-UART modules are stored here.


.. _file-tree-drivers-directory-opl3:

drivers/opl3 and opl4
---------------------

The OPL3 and OPL4 FM-synth stuff is found here.


.. _file-tree-i2c-directory:

i2c directory
=============

This contains the ALSA i2c components.

Although there is a standard i2c layer on Linux, ALSA has its own i2c
code for some cards, because the soundcard needs only a simple operation
and the standard i2c API is too complicated for such a purpose.


.. _file-tree-i2c-directory-l3:

i2c/l3
------

This is a sub-directory for ARM L3 i2c.


.. _file-tree-synth-directory:

synth directory
===============

This contains the synth middle-level modules.

So far, there is only Emu8000/Emu10k1 synth driver under the
``synth/emux`` sub-directory.


.. _file-tree-pci-directory:

pci directory
=============

This directory and its sub-directories hold the top-level card modules
for PCI soundcards and the code specific to the PCI BUS.

The drivers compiled from a single file are stored directly in the pci
directory, while the drivers with several source files are stored on
their own sub-directory (e.g. emu10k1, ice1712).


.. _file-tree-isa-directory:

isa directory
=============

This directory and its sub-directories hold the top-level card modules
for ISA soundcards.


.. _file-tree-arm-ppc-sparc-directories:

arm, ppc, and sparc directories
===============================

They are used for top-level card modules which are specific to one of
these architectures.


.. _file-tree-usb-directory:

usb directory
=============

This directory contains the USB-audio driver. In the latest version, the
USB MIDI driver is integrated in the usb-audio driver.


.. _file-tree-pcmcia-directory:

pcmcia directory
================

The PCMCIA, especially PCCard drivers will go here. CardBus drivers will
be in the pci directory, because their API is identical to that of
standard PCI cards.


.. _file-tree-oss-directory:

oss directory
=============

The OSS/Lite source files are stored here in Linux 2.6 (or later) tree.
In the ALSA driver tarball, this directory is empty, of course :)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------

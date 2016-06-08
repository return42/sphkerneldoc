.. -*- coding: utf-8; mode: rst -*-

######################
Writing an ALSA Driver
######################
0.3.7
    This document describes how to write an ALSA (Advanced Linux Sound
    Architecture) driver.

Copyright (c) 2002-2005 Takashi Iwai tiwai@suse.de

This document is free; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your
option) any later version.

This document is distributed in the hope that it will be useful, but
*WITHOUT ANY WARRANTY*; without even the implied warranty of
*MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE*. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


.. _preface:

=======
Preface
=======

This document describes how to write an
`ALSA (Advanced Linux Sound Architecture) <http://www.alsa-project.org/>`__
driver. The document focuses mainly on PCI soundcards. In the case of
other device types, the API might be different, too. However, at least
the ALSA kernel API is consistent, and therefore it would be still a bit
help for writing them.

This document targets people who already have enough C language skills
and have basic linux kernel programming knowledge. This document doesn't
explain the general topic of linux kernel coding and doesn't cover
low-level driver implementation details. It only describes the standard
way to write a PCI sound driver on ALSA.

If you are already familiar with the older ALSA ver.0.5.x API, you can
check the drivers such as ``sound/pci/es1938.c`` or
``sound/pci/maestro3.c`` which have also almost the same code-base in
the ALSA 0.5.x tree, so you can compare the differences.

This document is still a draft version. Any feedback and corrections,
please!!


.. toctree::
    :maxdepth: 1

    file-tree
    basic-flow
    card-management
    pci-resource
    pcm-interface
    control-interface
    api-ac97
    midi-interface
    rawmidi-interface
    misc-devices
    buffer-and-memory
    proc-interface
    power-management
    module-parameters
    how-to-put-your-driver
    useful-functions
    acknowledgments




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

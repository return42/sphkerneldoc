.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/p1022_rdk.c

.. _`ccsr_guts_pmuxcr_uart0_i2c1_mask`:

CCSR_GUTS_PMUXCR_UART0_I2C1_MASK
================================

.. c:function::  CCSR_GUTS_PMUXCR_UART0_I2C1_MASK()

.. _`ccsr_guts_pmuxcr_uart0_i2c1_mask.author`:

Author
------

Timur Tabi <timur@freescale.com>

Copyright 2012 Freescale Semiconductor, Inc.

This file is licensed under the terms of the GNU General Public License
version 2.  This program is licensed "as is" without any warranty of any
kind, whether express or implied.

.. _`ccsr_guts_pmuxcr_uart0_i2c1_mask.note`:

Note
----

in order for audio to work correctly, the output controls need
to be enabled, because they control the clock.  So for playback, for

.. _`ccsr_guts_pmuxcr_uart0_i2c1_mask.example`:

example
-------

.. code-block:: c


    amixer sset 'Left Output Mixer PCM' on
    amixer sset 'Right Output Mixer PCM' on


.. _`p1022_rdk_machine_probe`:

p1022_rdk_machine_probe
=======================

.. c:function:: int p1022_rdk_machine_probe(struct snd_soc_card *card)

    initialize the board

    :param card:
        *undescribed*
    :type card: struct snd_soc_card \*

.. _`p1022_rdk_machine_probe.description`:

Description
-----------

This function is used to initialize the board-specific hardware.

Here we program the DMACR and PMUXCR registers.

.. _`p1022_rdk_startup`:

p1022_rdk_startup
=================

.. c:function:: int p1022_rdk_startup(struct snd_pcm_substream *substream)

    program the board with various hardware parameters

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

.. _`p1022_rdk_startup.description`:

Description
-----------

This function takes board-specific information, like clock frequencies
and serial data formats, and passes that information to the codec and
transport drivers.

.. _`p1022_rdk_machine_remove`:

p1022_rdk_machine_remove
========================

.. c:function:: int p1022_rdk_machine_remove(struct snd_soc_card *card)

    Remove the sound device

    :param card:
        *undescribed*
    :type card: struct snd_soc_card \*

.. _`p1022_rdk_machine_remove.description`:

Description
-----------

This function is called to remove the sound device for one SSI.  We
de-program the DMACR and PMUXCR register.

.. _`p1022_rdk_probe`:

p1022_rdk_probe
===============

.. c:function:: int p1022_rdk_probe(struct platform_device *pdev)

    platform probe function for the machine driver

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`p1022_rdk_probe.description`:

Description
-----------

Although this is a machine driver, the SSI node is the "master" node with
respect to audio hardware connections.  Therefore, we create a new ASoC
device for each new SSI node that has a codec attached.

.. _`p1022_rdk_remove`:

p1022_rdk_remove
================

.. c:function:: int p1022_rdk_remove(struct platform_device *pdev)

    remove the platform device

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`p1022_rdk_remove.description`:

Description
-----------

This function is called when the platform device is removed.

.. _`p1022_rdk_init`:

p1022_rdk_init
==============

.. c:function:: int p1022_rdk_init( void)

    machine driver initialization.

    :param void:
        no arguments
    :type void: 

.. _`p1022_rdk_init.description`:

Description
-----------

This function is called when this module is loaded.

.. _`p1022_rdk_exit`:

p1022_rdk_exit
==============

.. c:function:: void __exit p1022_rdk_exit( void)

    machine driver exit

    :param void:
        no arguments
    :type void: 

.. _`p1022_rdk_exit.description`:

Description
-----------

This function is called when this driver is unloaded.

.. This file was automatic generated / don't edit.


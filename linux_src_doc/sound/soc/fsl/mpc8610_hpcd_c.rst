.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/mpc8610_hpcd.c

.. _`mpc8610_hpcd_machine_probe`:

mpc8610_hpcd_machine_probe
==========================

.. c:function:: int mpc8610_hpcd_machine_probe(struct snd_soc_card *card)

    initialize the board

    :param card:
        *undescribed*
    :type card: struct snd_soc_card \*

.. _`mpc8610_hpcd_machine_probe.description`:

Description
-----------

This function is used to initialize the board-specific hardware.

Here we program the DMACR and PMUXCR registers.

.. _`mpc8610_hpcd_startup`:

mpc8610_hpcd_startup
====================

.. c:function:: int mpc8610_hpcd_startup(struct snd_pcm_substream *substream)

    program the board with various hardware parameters

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

.. _`mpc8610_hpcd_startup.description`:

Description
-----------

This function takes board-specific information, like clock frequencies
and serial data formats, and passes that information to the codec and
transport drivers.

.. _`mpc8610_hpcd_machine_remove`:

mpc8610_hpcd_machine_remove
===========================

.. c:function:: int mpc8610_hpcd_machine_remove(struct snd_soc_card *card)

    Remove the sound device

    :param card:
        *undescribed*
    :type card: struct snd_soc_card \*

.. _`mpc8610_hpcd_machine_remove.description`:

Description
-----------

This function is called to remove the sound device for one SSI.  We
de-program the DMACR and PMUXCR register.

.. _`mpc8610_hpcd_probe`:

mpc8610_hpcd_probe
==================

.. c:function:: int mpc8610_hpcd_probe(struct platform_device *pdev)

    platform probe function for the machine driver

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`mpc8610_hpcd_probe.description`:

Description
-----------

Although this is a machine driver, the SSI node is the "master" node with
respect to audio hardware connections.  Therefore, we create a new ASoC
device for each new SSI node that has a codec attached.

.. _`mpc8610_hpcd_remove`:

mpc8610_hpcd_remove
===================

.. c:function:: int mpc8610_hpcd_remove(struct platform_device *pdev)

    remove the platform device

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`mpc8610_hpcd_remove.description`:

Description
-----------

This function is called when the platform device is removed.

.. _`mpc8610_hpcd_init`:

mpc8610_hpcd_init
=================

.. c:function:: int mpc8610_hpcd_init( void)

    machine driver initialization.

    :param void:
        no arguments
    :type void: 

.. _`mpc8610_hpcd_init.description`:

Description
-----------

This function is called when this module is loaded.

.. _`mpc8610_hpcd_exit`:

mpc8610_hpcd_exit
=================

.. c:function:: void __exit mpc8610_hpcd_exit( void)

    machine driver exit

    :param void:
        no arguments
    :type void: 

.. _`mpc8610_hpcd_exit.description`:

Description
-----------

This function is called when this driver is unloaded.

.. This file was automatic generated / don't edit.


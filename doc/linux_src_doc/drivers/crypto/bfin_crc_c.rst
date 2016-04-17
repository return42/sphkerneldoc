.. -*- coding: utf-8; mode: rst -*-

==========
bfin_crc.c
==========


.. _`bfin_crypto_crc_suspend`:

bfin_crypto_crc_suspend
=======================

.. c:function:: int bfin_crypto_crc_suspend (struct platform_device *pdev, pm_message_t state)

    suspend crc device

    :param struct platform_device \*pdev:
        device being suspended

    :param pm_message_t state:
        requested suspend state



.. _`bfin_crypto_crc_probe`:

bfin_crypto_crc_probe
=====================

.. c:function:: int bfin_crypto_crc_probe (struct platform_device *pdev)

    Initialize module

    :param struct platform_device \*pdev:

        *undescribed*



.. _`bfin_crypto_crc_remove`:

bfin_crypto_crc_remove
======================

.. c:function:: int bfin_crypto_crc_remove (struct platform_device *pdev)

    Initialize module

    :param struct platform_device \*pdev:

        *undescribed*



.. _`bfin_crypto_crc_remove.description`:

Description
-----------




.. _`bfin_crypto_crc_mod_init`:

bfin_crypto_crc_mod_init
========================

.. c:function:: int bfin_crypto_crc_mod_init ( void)

    Initialize module

    :param void:
        no arguments



.. _`bfin_crypto_crc_mod_init.description`:

Description
-----------


Checks the module params and registers the platform driver.
Real work is in the platform probe function.



.. _`bfin_crypto_crc_mod_exit`:

bfin_crypto_crc_mod_exit
========================

.. c:function:: void __exit bfin_crypto_crc_mod_exit ( void)

    Deinitialize module

    :param void:
        no arguments


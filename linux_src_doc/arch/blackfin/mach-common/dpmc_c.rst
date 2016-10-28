.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/blackfin/mach-common/dpmc.c

.. _`bfin_set_vlev`:

bfin_set_vlev
=============

.. c:function:: void bfin_set_vlev(unsigned int vlev)

    Update VLEV field in VR_CTL Reg. Avoid BYPASS sequence

    :param unsigned int vlev:
        *undescribed*

.. _`bfin_get_vlev`:

bfin_get_vlev
=============

.. c:function:: unsigned int bfin_get_vlev(unsigned int freq)

    Get CPU specific VLEV from platform device data

    :param unsigned int freq:
        *undescribed*

.. _`bfin_dpmc_probe`:

bfin_dpmc_probe
===============

.. c:function:: int bfin_dpmc_probe(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        *undescribed*

.. _`bfin_dpmc_remove`:

bfin_dpmc_remove
================

.. c:function:: int bfin_dpmc_remove(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        *undescribed*

.. This file was automatic generated / don't edit.


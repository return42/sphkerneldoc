.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_init.c

.. _`pm8001_phy_init`:

pm8001_phy_init
===============

.. c:function:: void pm8001_phy_init(struct pm8001_hba_info *pm8001_ha, int phy_id)

    initiate our adapter phys \ ``pm8001_ha``\ : our hba structure. \ ``phy_id``\ : phy id.

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

    :param int phy_id:
        *undescribed*

.. _`pm8001_free`:

pm8001_free
===========

.. c:function:: void pm8001_free(struct pm8001_hba_info *pm8001_ha)

    free hba \ ``pm8001_ha``\ :   our hba structure.

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

.. _`pm8001_tasklet`:

pm8001_tasklet
==============

.. c:function:: void pm8001_tasklet(unsigned long opaque)

    x interrupt handler

    :param unsigned long opaque:
        the passed general host adapter struct

.. _`pm8001_tasklet.note`:

Note
----

pm8001_tasklet is common for pm8001 & pm80xx

.. _`pm8001_interrupt_handler_msix`:

pm8001_interrupt_handler_msix
=============================

.. c:function:: irqreturn_t pm8001_interrupt_handler_msix(int irq, void *opaque)

    main MSIX interrupt handler. It obtains the vector number and calls the equivalent bottom half or services directly.

    :param int irq:
        *undescribed*

    :param void \*opaque:
        the passed outbound queue/vector. Host structure is
        retrieved from the same.

.. _`pm8001_interrupt_handler_intx`:

pm8001_interrupt_handler_intx
=============================

.. c:function:: irqreturn_t pm8001_interrupt_handler_intx(int irq, void *dev_id)

    main INTx interrupt handler.

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        sas_ha structure. The HBA is retrieved from sas_has structure.

.. _`pm8001_alloc`:

pm8001_alloc
============

.. c:function:: int pm8001_alloc(struct pm8001_hba_info *pm8001_ha, const struct pci_device_id *ent)

    initiate our hba structure and 6 DMAs area.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba structure.

    :param const struct pci_device_id \*ent:
        *undescribed*

.. _`pm8001_ioremap`:

pm8001_ioremap
==============

.. c:function:: int pm8001_ioremap(struct pm8001_hba_info *pm8001_ha)

    remap the pci high physical address to kernal virtual address so that we can access them.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba structure.

.. _`pm8001_pci_alloc`:

pm8001_pci_alloc
================

.. c:function:: struct pm8001_hba_info *pm8001_pci_alloc(struct pci_dev *pdev, const struct pci_device_id *ent, struct Scsi_Host *shost)

    initialize our ha card structure

    :param struct pci_dev \*pdev:
        pci device.

    :param const struct pci_device_id \*ent:
        ent

    :param struct Scsi_Host \*shost:
        scsi host struct which has been initialized before.

.. _`pci_go_44`:

pci_go_44
=========

.. c:function:: int pci_go_44(struct pci_dev *pdev)

    pm8001 specified, its DMA is 44 bit rather than 64 bit

    :param struct pci_dev \*pdev:
        pci device.

.. _`pm8001_prep_sas_ha_init`:

pm8001_prep_sas_ha_init
=======================

.. c:function:: int pm8001_prep_sas_ha_init(struct Scsi_Host *shost, const struct pm8001_chip_info *chip_info)

    allocate memory in general hba struct && init them.

    :param struct Scsi_Host \*shost:
        scsi host which has been allocated outside.

    :param const struct pm8001_chip_info \*chip_info:
        our ha struct.

.. _`pm8001_post_sas_ha_init`:

pm8001_post_sas_ha_init
=======================

.. c:function:: void pm8001_post_sas_ha_init(struct Scsi_Host *shost, const struct pm8001_chip_info *chip_info)

    initialize general hba struct defined in libsas

    :param struct Scsi_Host \*shost:
        scsi host which has been allocated outside

    :param const struct pm8001_chip_info \*chip_info:
        our ha struct.

.. _`pm8001_init_sas_add`:

pm8001_init_sas_add
===================

.. c:function:: void pm8001_init_sas_add(struct pm8001_hba_info *pm8001_ha)

    initialize sas address

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

.. _`pm8001_init_sas_add.description`:

Description
-----------

Currently we just set the fixed SAS address to our HBA,for manufacture,
it should read from the EEPROM

.. _`pm8001_get_internal_phy_settings`:

pm8001_get_internal_phy_settings
================================

.. c:function:: void pm8001_get_internal_phy_settings(struct pm8001_hba_info *pm8001_ha, struct pm8001_mpi3_phy_pg_trx_config *phycfg)

    Retrieves the internal PHY settings

    :param struct pm8001_hba_info \*pm8001_ha:
        our adapter

    :param struct pm8001_mpi3_phy_pg_trx_config \*phycfg:
        PHY config page to populate

.. _`pm8001_get_external_phy_settings`:

pm8001_get_external_phy_settings
================================

.. c:function:: void pm8001_get_external_phy_settings(struct pm8001_hba_info *pm8001_ha, struct pm8001_mpi3_phy_pg_trx_config *phycfg)

    Retrieves the external PHY settings

    :param struct pm8001_hba_info \*pm8001_ha:
        our adapter

    :param struct pm8001_mpi3_phy_pg_trx_config \*phycfg:
        PHY config page to populate

.. _`pm8001_get_phy_mask`:

pm8001_get_phy_mask
===================

.. c:function:: void pm8001_get_phy_mask(struct pm8001_hba_info *pm8001_ha, int *phymask)

    Retrieves the mask that denotes if a PHY is int/ext

    :param struct pm8001_hba_info \*pm8001_ha:
        our adapter

    :param int \*phymask:
        The PHY mask

.. _`pm8001_set_phy_settings_ven_117c_12g`:

pm8001_set_phy_settings_ven_117c_12G
====================================

.. c:function:: int pm8001_set_phy_settings_ven_117c_12G(struct pm8001_hba_info *pm8001_ha)

    Configure ATTO 12Gb PHY settings

    :param struct pm8001_hba_info \*pm8001_ha:
        our adapter

.. _`pm8001_configure_phy_settings`:

pm8001_configure_phy_settings
=============================

.. c:function:: int pm8001_configure_phy_settings(struct pm8001_hba_info *pm8001_ha)

    Configures PHY settings based on vendor ID.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba.

.. _`pm8001_setup_msix`:

pm8001_setup_msix
=================

.. c:function:: u32 pm8001_setup_msix(struct pm8001_hba_info *pm8001_ha)

    enable MSI-X interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

.. _`pm8001_request_irq`:

pm8001_request_irq
==================

.. c:function:: u32 pm8001_request_irq(struct pm8001_hba_info *pm8001_ha)

    register interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

.. _`pm8001_pci_probe`:

pm8001_pci_probe
================

.. c:function:: int pm8001_pci_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    probe supported device

    :param struct pci_dev \*pdev:
        pci device which kernel has been prepared for.

    :param const struct pci_device_id \*ent:
        pci device id

.. _`pm8001_pci_probe.description`:

Description
-----------

This function is the main initialization function, when register a new
pci driver it is invoked, all struct an hardware initilization should be done
here, also, register interrupt

.. _`pm8001_pci_suspend`:

pm8001_pci_suspend
==================

.. c:function:: int pm8001_pci_suspend(struct pci_dev *pdev, pm_message_t state)

    power management suspend main entry point

    :param struct pci_dev \*pdev:
        PCI device struct

    :param pm_message_t state:
        PM state change to (usually PCI_D3)

.. _`pm8001_pci_suspend.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`pm8001_pci_resume`:

pm8001_pci_resume
=================

.. c:function:: int pm8001_pci_resume(struct pci_dev *pdev)

    power management resume main entry point

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`pm8001_pci_resume.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`pm8001_init`:

pm8001_init
===========

.. c:function:: int pm8001_init( void)

    initialize scsi transport template

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


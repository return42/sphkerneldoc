.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_init.c

.. _`pm8001_phy_init`:

pm8001_phy_init
===============

.. c:function:: void pm8001_phy_init(struct pm8001_hba_info *pm8001_ha, int phy_id)

    initiate our adapter phys \ ``pm8001_ha``\ : our hba structure. \ ``phy_id``\ : phy id.

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phy_id:
        *undescribed*
    :type phy_id: int

.. _`pm8001_free`:

pm8001_free
===========

.. c:function:: void pm8001_free(struct pm8001_hba_info *pm8001_ha)

    free hba \ ``pm8001_ha``\ :   our hba structure.

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_tasklet`:

pm8001_tasklet
==============

.. c:function:: void pm8001_tasklet(unsigned long opaque)

    x interrupt handler

    :param opaque:
        the passed general host adapter struct
    :type opaque: unsigned long

.. _`pm8001_tasklet.note`:

Note
----

pm8001_tasklet is common for pm8001 & pm80xx

.. _`pm8001_interrupt_handler_msix`:

pm8001_interrupt_handler_msix
=============================

.. c:function:: irqreturn_t pm8001_interrupt_handler_msix(int irq, void *opaque)

    main MSIX interrupt handler. It obtains the vector number and calls the equivalent bottom half or services directly.

    :param irq:
        *undescribed*
    :type irq: int

    :param opaque:
        the passed outbound queue/vector. Host structure is
        retrieved from the same.
    :type opaque: void \*

.. _`pm8001_interrupt_handler_intx`:

pm8001_interrupt_handler_intx
=============================

.. c:function:: irqreturn_t pm8001_interrupt_handler_intx(int irq, void *dev_id)

    main INTx interrupt handler.

    :param irq:
        *undescribed*
    :type irq: int

    :param dev_id:
        sas_ha structure. The HBA is retrieved from sas_has structure.
    :type dev_id: void \*

.. _`pm8001_alloc`:

pm8001_alloc
============

.. c:function:: int pm8001_alloc(struct pm8001_hba_info *pm8001_ha, const struct pci_device_id *ent)

    initiate our hba structure and 6 DMAs area.

    :param pm8001_ha:
        our hba structure.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ent:
        *undescribed*
    :type ent: const struct pci_device_id \*

.. _`pm8001_ioremap`:

pm8001_ioremap
==============

.. c:function:: int pm8001_ioremap(struct pm8001_hba_info *pm8001_ha)

    remap the pci high physical address to kernal virtual address so that we can access them.

    :param pm8001_ha:
        our hba structure.
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_pci_alloc`:

pm8001_pci_alloc
================

.. c:function:: struct pm8001_hba_info *pm8001_pci_alloc(struct pci_dev *pdev, const struct pci_device_id *ent, struct Scsi_Host *shost)

    initialize our ha card structure

    :param pdev:
        pci device.
    :type pdev: struct pci_dev \*

    :param ent:
        ent
    :type ent: const struct pci_device_id \*

    :param shost:
        scsi host struct which has been initialized before.
    :type shost: struct Scsi_Host \*

.. _`pci_go_44`:

pci_go_44
=========

.. c:function:: int pci_go_44(struct pci_dev *pdev)

    pm8001 specified, its DMA is 44 bit rather than 64 bit

    :param pdev:
        pci device.
    :type pdev: struct pci_dev \*

.. _`pm8001_prep_sas_ha_init`:

pm8001_prep_sas_ha_init
=======================

.. c:function:: int pm8001_prep_sas_ha_init(struct Scsi_Host *shost, const struct pm8001_chip_info *chip_info)

    allocate memory in general hba struct && init them.

    :param shost:
        scsi host which has been allocated outside.
    :type shost: struct Scsi_Host \*

    :param chip_info:
        our ha struct.
    :type chip_info: const struct pm8001_chip_info \*

.. _`pm8001_post_sas_ha_init`:

pm8001_post_sas_ha_init
=======================

.. c:function:: void pm8001_post_sas_ha_init(struct Scsi_Host *shost, const struct pm8001_chip_info *chip_info)

    initialize general hba struct defined in libsas

    :param shost:
        scsi host which has been allocated outside
    :type shost: struct Scsi_Host \*

    :param chip_info:
        our ha struct.
    :type chip_info: const struct pm8001_chip_info \*

.. _`pm8001_init_sas_add`:

pm8001_init_sas_add
===================

.. c:function:: void pm8001_init_sas_add(struct pm8001_hba_info *pm8001_ha)

    initialize sas address

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

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

    :param pm8001_ha:
        our adapter
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phycfg:
        PHY config page to populate
    :type phycfg: struct pm8001_mpi3_phy_pg_trx_config \*

.. _`pm8001_get_external_phy_settings`:

pm8001_get_external_phy_settings
================================

.. c:function:: void pm8001_get_external_phy_settings(struct pm8001_hba_info *pm8001_ha, struct pm8001_mpi3_phy_pg_trx_config *phycfg)

    Retrieves the external PHY settings

    :param pm8001_ha:
        our adapter
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phycfg:
        PHY config page to populate
    :type phycfg: struct pm8001_mpi3_phy_pg_trx_config \*

.. _`pm8001_get_phy_mask`:

pm8001_get_phy_mask
===================

.. c:function:: void pm8001_get_phy_mask(struct pm8001_hba_info *pm8001_ha, int *phymask)

    Retrieves the mask that denotes if a PHY is int/ext

    :param pm8001_ha:
        our adapter
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phymask:
        The PHY mask
    :type phymask: int \*

.. _`pm8001_set_phy_settings_ven_117c_12g`:

pm8001_set_phy_settings_ven_117c_12G
====================================

.. c:function:: int pm8001_set_phy_settings_ven_117c_12G(struct pm8001_hba_info *pm8001_ha)

    Configure ATTO 12Gb PHY settings

    :param pm8001_ha:
        our adapter
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_configure_phy_settings`:

pm8001_configure_phy_settings
=============================

.. c:function:: int pm8001_configure_phy_settings(struct pm8001_hba_info *pm8001_ha)

    Configures PHY settings based on vendor ID.

    :param pm8001_ha:
        our hba.
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_setup_msix`:

pm8001_setup_msix
=================

.. c:function:: u32 pm8001_setup_msix(struct pm8001_hba_info *pm8001_ha)

    enable MSI-X interrupt

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_request_irq`:

pm8001_request_irq
==================

.. c:function:: u32 pm8001_request_irq(struct pm8001_hba_info *pm8001_ha)

    register interrupt

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_pci_probe`:

pm8001_pci_probe
================

.. c:function:: int pm8001_pci_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    probe supported device

    :param pdev:
        pci device which kernel has been prepared for.
    :type pdev: struct pci_dev \*

    :param ent:
        pci device id
    :type ent: const struct pci_device_id \*

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

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

    :param state:
        PM state change to (usually PCI_D3)
    :type state: pm_message_t

.. _`pm8001_pci_suspend.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`pm8001_pci_resume`:

pm8001_pci_resume
=================

.. c:function:: int pm8001_pci_resume(struct pci_dev *pdev)

    power management resume main entry point

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`pm8001_pci_resume.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`pm8001_init`:

pm8001_init
===========

.. c:function:: int pm8001_init( void)

    initialize scsi transport template

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


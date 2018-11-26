.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libahci.c

.. _`ahci_rpm_get_port`:

ahci_rpm_get_port
=================

.. c:function:: int ahci_rpm_get_port(struct ata_port *ap)

    Make sure the port is powered on

    :param ap:
        Port to power on
    :type ap: struct ata_port \*

.. _`ahci_rpm_get_port.description`:

Description
-----------

Whenever there is need to access the AHCI host registers outside of
normal execution paths, call this function to make sure the host is
actually powered on.

.. _`ahci_rpm_put_port`:

ahci_rpm_put_port
=================

.. c:function:: void ahci_rpm_put_port(struct ata_port *ap)

    Undoes \ :c:func:`ahci_rpm_get_port`\ 

    :param ap:
        Port to power down
    :type ap: struct ata_port \*

.. _`ahci_rpm_put_port.description`:

Description
-----------

Undoes \ :c:func:`ahci_rpm_get_port`\  and possibly powers down the AHCI host
if it has no more active users.

.. _`ahci_save_initial_config`:

ahci_save_initial_config
========================

.. c:function:: void ahci_save_initial_config(struct device *dev, struct ahci_host_priv *hpriv)

    Save and fixup initial config values

    :param dev:
        target AHCI device
    :type dev: struct device \*

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_save_initial_config.description`:

Description
-----------

Some registers containing configuration info might be setup by
BIOS and might be cleared on reset.  This function saves the
initial values of those registers into \ ``hpriv``\  such that they
can be restored after controller reset.

If inconsistent, config values are fixed up by this function.

If it is not set already this function sets hpriv->start_engine to
ahci_start_engine.

.. _`ahci_save_initial_config.locking`:

LOCKING
-------

None.

.. _`ahci_restore_initial_config`:

ahci_restore_initial_config
===========================

.. c:function:: void ahci_restore_initial_config(struct ata_host *host)

    Restore initial config

    :param host:
        target ATA host
    :type host: struct ata_host \*

.. _`ahci_restore_initial_config.description`:

Description
-----------

Restore initial config stored by \ :c:func:`ahci_save_initial_config`\ .

.. _`ahci_restore_initial_config.locking`:

LOCKING
-------

None.

.. _`ahci_host_activate`:

ahci_host_activate
==================

.. c:function:: int ahci_host_activate(struct ata_host *host, struct scsi_host_template *sht)

    start AHCI host, request IRQs and register it

    :param host:
        target ATA host
    :type host: struct ata_host \*

    :param sht:
        scsi_host_template to use when registering the host
    :type sht: struct scsi_host_template \*

.. _`ahci_host_activate.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ahci_host_activate.return`:

Return
------

0 on success, -errno otherwise.

.. This file was automatic generated / don't edit.


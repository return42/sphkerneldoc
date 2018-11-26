.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/init.c

.. _`isci_register_sas_ha`:

isci_register_sas_ha
====================

.. c:function:: int isci_register_sas_ha(struct isci_host *isci_host)

    This method initializes various lldd specific members of the sas_ha struct and calls the libsas \ :c:func:`sas_register_ha`\  function.

    :param isci_host:
        This parameter specifies the lldd specific wrapper for the
        libsas sas_ha struct.
    :type isci_host: struct isci_host \*

.. _`isci_register_sas_ha.description`:

Description
-----------

This method returns an error code indicating success or failure. The user
should check for possible memory allocation error return otherwise, a zero
indicates success.

.. This file was automatic generated / don't edit.


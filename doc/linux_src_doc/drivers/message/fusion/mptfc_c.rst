.. -*- coding: utf-8; mode: rst -*-

=======
mptfc.c
=======

.. _`mptfc_init`:

mptfc_init
==========

.. c:function:: int mptfc_init ( void)

    Register MPT adapter(s) as SCSI host(s) with SCSI mid-layer.

    :param void:
        no arguments


.. _`mptfc_init.description`:

Description
-----------


Returns 0 for success, non-zero for failure.


.. _`mptfc_remove`:

mptfc_remove
============

.. c:function:: void mptfc_remove (struct pci_dev *pdev)

    Remove fc infrastructure for devices

    :param struct pci_dev \*pdev:
        Pointer to pci_dev structure


.. _`mptfc_exit`:

mptfc_exit
==========

.. c:function:: void __exit mptfc_exit ( void)

    Unregisters MPT adapter(s)

    :param void:
        no arguments


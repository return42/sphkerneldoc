.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_sysfs.c

.. _`eeh_show_attr`:

EEH_SHOW_ATTR
=============

.. c:function::  EEH_SHOW_ATTR( _name,  _memb,  _format)

    - Create sysfs entry for eeh statistic

    :param _name:
        name of file in sysfs directory
    :type _name: 

    :param _memb:
        name of member in struct pci_dn to access
    :type _memb: 

    :param _format:
        printf format for display
    :type _format: 

.. _`eeh_show_attr.description`:

Description
-----------

All of the attributes look very similar, so just
auto-gen a cut-n-paste routine to display them.

.. This file was automatic generated / don't edit.


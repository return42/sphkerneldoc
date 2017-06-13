.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/pci/atomisp2/css2400/sh_css_internal.h

.. _`calc_alignment_member`:

CALC_ALIGNMENT_MEMBER
=====================

.. c:function::  CALC_ALIGNMENT_MEMBER( x,  y)

    the representation is compiler dependent.

    :param  x:
        *undescribed*

    :param  y:
        *undescribed*

.. _`calc_alignment_member.description`:

Description
-----------

The structs that are communicated between host and SP/ISP should have the
exact same object representation. The compiler that is used to compile the
firmware is hivecc.

To check if a different compiler, used to compile a host application, uses
another object representation, macros are defined specifying the size of
the structs as expected by the firmware.

A host application shall verify that a sizeof( ) of the struct is equal to
the SIZE_OF_XXX macro of the corresponding struct. If they are not
equal, functionality will break.

.. This file was automatic generated / don't edit.


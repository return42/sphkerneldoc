.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/eeh.h

.. _`eeh_possible_error`:

EEH_POSSIBLE_ERROR
==================

.. c:function::  EEH_POSSIBLE_ERROR( val,  type)

    - test for possible MMIO failure.

    :param val:
        *undescribed*
    :type val: 

    :param type:
        *undescribed*
    :type type: 

.. _`eeh_possible_error.description`:

Description
-----------

If this macro yields TRUE, the caller relays to \ :c:func:`eeh_check_failure`\ 
which does further tests out of line.

.. This file was automatic generated / don't edit.


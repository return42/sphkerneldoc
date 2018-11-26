.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/mem_detect.h

.. _`for_each_mem_detect_block`:

for_each_mem_detect_block
=========================

.. c:function::  for_each_mem_detect_block( i,  p_start,  p_end)

    early online memory range iterator

    :param i:
        an integer used as loop variable
    :type i: 

    :param p_start:
        ptr to unsigned long for start address of the range
    :type p_start: 

    :param p_end:
        ptr to unsigned long for end address of the range
    :type p_end: 

.. _`for_each_mem_detect_block.description`:

Description
-----------

Walks over detected online memory ranges.

.. This file was automatic generated / don't edit.


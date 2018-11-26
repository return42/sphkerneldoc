.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/include/asm/kvm_hyp.h

.. _`hyp_alternate_select`:

hyp_alternate_select
====================

.. c:function::  hyp_alternate_select( fname,  orig,  alt,  cond)

    Generates patchable code sequences that are used to switch between two implementations of a function, depending on the availability of a feature.

    :param fname:
        a symbol name that will be defined as a function returning a
        function pointer whose type will match \ ``orig``\  and \ ``alt``\ 
    :type fname: 

    :param orig:
        A pointer to the default function, as returned by \ ``fname``\  when
        \ ``cond``\  doesn't hold
    :type orig: 

    :param alt:
        A pointer to the alternate function, as returned by \ ``fname``\ 
        when \ ``cond``\  holds
    :type alt: 

    :param cond:
        a CPU feature (as described in asm/cpufeature.h)
    :type cond: 

.. This file was automatic generated / don't edit.


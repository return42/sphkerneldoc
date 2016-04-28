.. -*- coding: utf-8; mode: rst -*-

.. _API-bpf-prog-create-from-user:

=========================
bpf_prog_create_from_user
=========================

*man bpf_prog_create_from_user(9)*

*4.6.0-rc5*

create an unattached filter from user buffer


Synopsis
========

.. c:function:: int bpf_prog_create_from_user( struct bpf_prog ** pfp, struct sock_fprog * fprog, bpf_aux_classic_check_t trans, bool save_orig )

Arguments
=========

``pfp``
    the unattached filter that is created

``fprog``
    the filter program

``trans``
    post-classic verifier transformation handler

``save_orig``
    save classic BPF program


Description
===========

This function effectively does the same as ``bpf_prog_create``, only
that it builds up its insns buffer from user space provided buffer. It
also allows for passing a bpf_aux_classic_check_t handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

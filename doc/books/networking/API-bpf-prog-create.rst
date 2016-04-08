
.. _API-bpf-prog-create:

===============
bpf_prog_create
===============

*man bpf_prog_create(9)*

*4.6.0-rc1*

create an unattached filter


Synopsis
========

.. c:function:: int bpf_prog_create( struct bpf_prog ** pfp, struct sock_fprog_kern * fprog )

Arguments
=========

``pfp``
    the unattached filter that is created

``fprog``
    the filter program


Description
===========

Create a filter independent of any socket. We first run some sanity checks on it to make sure it does not explode on us later. If an error occurs or there is insufficient memory
for the filter a negative errno code is returned. On success the return is zero.

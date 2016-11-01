.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/filter.c

.. _`sk_filter_trim_cap`:

sk_filter_trim_cap
==================

.. c:function:: int sk_filter_trim_cap(struct sock *sk, struct sk_buff *skb, unsigned int cap)

    run a packet through a socket filter

    :param struct sock \*sk:
        sock associated with \ :c:type:`struct sk_buff <sk_buff>`\ 

    :param struct sk_buff \*skb:
        buffer to filter

    :param unsigned int cap:
        limit on how short the eBPF program may trim the packet

.. _`sk_filter_trim_cap.description`:

Description
-----------

Run the eBPF program and then cut skb->data to correct size returned by
the program. If pkt_len is 0 we toss packet. If skb->len is smaller
than pkt_len we keep whole skb->data. This is the socket level
wrapper to BPF_PROG_RUN. It returns 0 if the packet should
be accepted or -EPERM if the packet should be tossed.

.. _`bpf_convert_filter`:

bpf_convert_filter
==================

.. c:function:: int bpf_convert_filter(struct sock_filter *prog, int len, struct bpf_insn *new_prog, int *new_len)

    convert filter program

    :param struct sock_filter \*prog:
        the user passed filter program

    :param int len:
        the length of the user passed filter program

    :param struct bpf_insn \*new_prog:
        buffer where converted program will be stored

    :param int \*new_len:
        pointer to store length of converted program

.. _`bpf_convert_filter.description`:

Description
-----------

Remap 'sock_filter' style BPF instruction set to 'sock_filter_ext' style.

.. _`bpf_convert_filter.conversion-workflow`:

Conversion workflow
-------------------


1) First pass for calculating the new program length:
bpf_convert_filter(old_prog, old_len, NULL, \ :c:type:`struct new_len <new_len>`\ )

2) 2nd pass to remap in two passes: 1st pass finds new
jump offsets, 2nd pass remapping:
new_prog = kmalloc(sizeof(struct bpf_insn) \* new_len);
bpf_convert_filter(old_prog, old_len, new_prog, \ :c:type:`struct new_len <new_len>`\ );

.. _`bpf_check_classic`:

bpf_check_classic
=================

.. c:function:: int bpf_check_classic(const struct sock_filter *filter, unsigned int flen)

    verify socket filter code

    :param const struct sock_filter \*filter:
        filter to verify

    :param unsigned int flen:
        length of filter

.. _`bpf_check_classic.description`:

Description
-----------

Check the user's filter code. If we let some ugly
filter code slip through kaboom! The filter must contain
no references or jumps that are out of range, no illegal
instructions, and must end with a RET instruction.

All jumps are forward as they are not signed.

Returns 0 if the rule set is legal or -EINVAL if not.

.. _`sk_filter_release_rcu`:

sk_filter_release_rcu
=====================

.. c:function:: void sk_filter_release_rcu(struct rcu_head *rcu)

    Release a socket filter by rcu_head

    :param struct rcu_head \*rcu:
        rcu_head that contains the sk_filter to free

.. _`sk_filter_release`:

sk_filter_release
=================

.. c:function:: void sk_filter_release(struct sk_filter *fp)

    release a socket filter

    :param struct sk_filter \*fp:
        filter to remove

.. _`sk_filter_release.description`:

Description
-----------

Remove a filter from a socket and release its resources.

.. _`bpf_prog_create`:

bpf_prog_create
===============

.. c:function:: int bpf_prog_create(struct bpf_prog **pfp, struct sock_fprog_kern *fprog)

    create an unattached filter

    :param struct bpf_prog \*\*pfp:
        the unattached filter that is created

    :param struct sock_fprog_kern \*fprog:
        the filter program

.. _`bpf_prog_create.description`:

Description
-----------

Create a filter independent of any socket. We first run some
sanity checks on it to make sure it does not explode on us later.
If an error occurs or there is insufficient memory for the filter
a negative errno code is returned. On success the return is zero.

.. _`bpf_prog_create_from_user`:

bpf_prog_create_from_user
=========================

.. c:function:: int bpf_prog_create_from_user(struct bpf_prog **pfp, struct sock_fprog *fprog, bpf_aux_classic_check_t trans, bool save_orig)

    create an unattached filter from user buffer

    :param struct bpf_prog \*\*pfp:
        the unattached filter that is created

    :param struct sock_fprog \*fprog:
        the filter program

    :param bpf_aux_classic_check_t trans:
        post-classic verifier transformation handler

    :param bool save_orig:
        save classic BPF program

.. _`bpf_prog_create_from_user.description`:

Description
-----------

This function effectively does the same as \ :c:func:`bpf_prog_create`\ , only
that it builds up its insns buffer from user space provided buffer.
It also allows for passing a bpf_aux_classic_check_t handler.

.. _`sk_attach_filter`:

sk_attach_filter
================

.. c:function:: int sk_attach_filter(struct sock_fprog *fprog, struct sock *sk)

    attach a socket filter

    :param struct sock_fprog \*fprog:
        the filter program

    :param struct sock \*sk:
        the socket to use

.. _`sk_attach_filter.description`:

Description
-----------

Attach the user's filter code. We first run some sanity checks on
it to make sure it does not explode on us later. If an error
occurs or there is insufficient memory for the filter a negative
errno code is returned. On success the return is zero.

.. This file was automatic generated / don't edit.


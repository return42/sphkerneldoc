.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/bpf/cgroup.c

.. _`cgroup_bpf_put`:

cgroup_bpf_put
==============

.. c:function:: void cgroup_bpf_put(struct cgroup *cgrp)

    put references of all bpf programs

    :param struct cgroup \*cgrp:
        the cgroup to modify

.. _`cgroup_bpf_inherit`:

cgroup_bpf_inherit
==================

.. c:function:: int cgroup_bpf_inherit(struct cgroup *cgrp)

    inherit effective programs from parent

    :param struct cgroup \*cgrp:
        the cgroup to modify

.. _`__cgroup_bpf_attach`:

\__cgroup_bpf_attach
====================

.. c:function:: int __cgroup_bpf_attach(struct cgroup *cgrp, struct bpf_prog *prog, enum bpf_attach_type type, u32 flags)

    Attach the program to a cgroup, and propagate the change to descendants

    :param struct cgroup \*cgrp:
        The cgroup which descendants to traverse

    :param struct bpf_prog \*prog:
        A program to attach

    :param enum bpf_attach_type type:
        Type of attach operation

    :param u32 flags:
        *undescribed*

.. _`__cgroup_bpf_attach.description`:

Description
-----------

Must be called with cgroup_mutex held.

.. _`__cgroup_bpf_detach`:

\__cgroup_bpf_detach
====================

.. c:function:: int __cgroup_bpf_detach(struct cgroup *cgrp, struct bpf_prog *prog, enum bpf_attach_type type, u32 unused_flags)

    Detach the program from a cgroup, and propagate the change to descendants

    :param struct cgroup \*cgrp:
        The cgroup which descendants to traverse

    :param struct bpf_prog \*prog:
        A program to detach or NULL

    :param enum bpf_attach_type type:
        Type of detach operation

    :param u32 unused_flags:
        *undescribed*

.. _`__cgroup_bpf_detach.description`:

Description
-----------

Must be called with cgroup_mutex held.

.. _`__cgroup_bpf_run_filter_skb`:

\__cgroup_bpf_run_filter_skb
============================

.. c:function:: int __cgroup_bpf_run_filter_skb(struct sock *sk, struct sk_buff *skb, enum bpf_attach_type type)

    Run a program for packet filtering

    :param struct sock \*sk:
        The socket sending or receiving traffic

    :param struct sk_buff \*skb:
        The skb that is being sent or received

    :param enum bpf_attach_type type:
        The type of program to be exectuted

.. _`__cgroup_bpf_run_filter_skb.description`:

Description
-----------

If no socket is passed, or the socket is not of type INET or INET6,
this function does nothing and returns 0.

The program type passed in via \ ``type``\  must be suitable for network
filtering. No further check is performed to assert that.

This function will return \ ``-EPERM``\  if any if an attached program was found
and if it returned != 1 during execution. In all other cases, 0 is returned.

.. _`__cgroup_bpf_run_filter_sk`:

\__cgroup_bpf_run_filter_sk
===========================

.. c:function:: int __cgroup_bpf_run_filter_sk(struct sock *sk, enum bpf_attach_type type)

    Run a program on a sock

    :param struct sock \*sk:
        sock structure to manipulate

    :param enum bpf_attach_type type:
        The type of program to be exectuted

.. _`__cgroup_bpf_run_filter_sk.description`:

Description
-----------

socket is passed is expected to be of type INET or INET6.

The program type passed in via \ ``type``\  must be suitable for sock
filtering. No further check is performed to assert that.

This function will return \ ``-EPERM``\  if any if an attached program was found
and if it returned != 1 during execution. In all other cases, 0 is returned.

.. _`__cgroup_bpf_run_filter_sock_addr`:

\__cgroup_bpf_run_filter_sock_addr
==================================

.. c:function:: int __cgroup_bpf_run_filter_sock_addr(struct sock *sk, struct sockaddr *uaddr, enum bpf_attach_type type, void *t_ctx)

    Run a program on a sock and provided by user sockaddr

    :param struct sock \*sk:
        sock struct that will use sockaddr

    :param struct sockaddr \*uaddr:
        sockaddr struct provided by user

    :param enum bpf_attach_type type:
        The type of program to be exectuted

    :param void \*t_ctx:
        Pointer to attach type specific context

.. _`__cgroup_bpf_run_filter_sock_addr.description`:

Description
-----------

socket is expected to be of type INET or INET6.

This function will return \ ``-EPERM``\  if an attached program is found and
returned value != 1 during execution. In all other cases, 0 is returned.

.. _`__cgroup_bpf_run_filter_sock_ops`:

\__cgroup_bpf_run_filter_sock_ops
=================================

.. c:function:: int __cgroup_bpf_run_filter_sock_ops(struct sock *sk, struct bpf_sock_ops_kern *sock_ops, enum bpf_attach_type type)

    Run a program on a sock

    :param struct sock \*sk:
        socket to get cgroup from

    :param struct bpf_sock_ops_kern \*sock_ops:
        bpf_sock_ops_kern struct to pass to program. Contains
        sk with connection information (IP addresses, etc.) May not contain
        cgroup info if it is a req sock.

    :param enum bpf_attach_type type:
        The type of program to be exectuted

.. _`__cgroup_bpf_run_filter_sock_ops.description`:

Description
-----------

socket passed is expected to be of type INET or INET6.

The program type passed in via \ ``type``\  must be suitable for sock_ops
filtering. No further check is performed to assert that.

This function will return \ ``-EPERM``\  if any if an attached program was found
and if it returned != 1 during execution. In all other cases, 0 is returned.

.. This file was automatic generated / don't edit.


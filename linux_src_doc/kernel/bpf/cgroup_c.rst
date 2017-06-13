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

.. c:function:: void cgroup_bpf_inherit(struct cgroup *cgrp, struct cgroup *parent)

    inherit effective programs from parent

    :param struct cgroup \*cgrp:
        the cgroup to modify

    :param struct cgroup \*parent:
        the parent to inherit from

.. _`__cgroup_bpf_update`:

__cgroup_bpf_update
===================

.. c:function:: int __cgroup_bpf_update(struct cgroup *cgrp, struct cgroup *parent, struct bpf_prog *prog, enum bpf_attach_type type, bool new_overridable)

    Update the pinned program of a cgroup, and propagate the change to descendants

    :param struct cgroup \*cgrp:
        The cgroup which descendants to traverse

    :param struct cgroup \*parent:
        The parent of \ ``cgrp``\ , or \ ``NULL``\  if \ ``cgrp``\  is the root

    :param struct bpf_prog \*prog:
        A new program to pin

    :param enum bpf_attach_type type:
        Type of pinning operation (ingress/egress)

    :param bool new_overridable:
        *undescribed*

.. _`__cgroup_bpf_update.description`:

Description
-----------

Each cgroup has a set of two pointers for bpf programs; one for eBPF
programs it owns, and which is effective for execution.

If \ ``prog``\  is not \ ``NULL``\ , this function attaches a new program to the cgroup
and releases the one that is currently attached, if any. \ ``prog``\  is then made
the effective program of type \ ``type``\  in that cgroup.

If \ ``prog``\  is \ ``NULL``\ , the currently attached program of type \ ``type``\  is released,
and the effective program of the parent cgroup (if any) is inherited to
\ ``cgrp``\ .

Then, the descendants of \ ``cgrp``\  are walked and the effective program for
each of them is set to the effective program of \ ``cgrp``\  unless the
descendant has its own program attached, in which case the subbranch is
skipped. This ensures that delegated subcgroups with own programs are left
untouched.

Must be called with cgroup_mutex held.

.. _`__cgroup_bpf_run_filter_skb`:

__cgroup_bpf_run_filter_skb
===========================

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

__cgroup_bpf_run_filter_sk
==========================

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

.. This file was automatic generated / don't edit.


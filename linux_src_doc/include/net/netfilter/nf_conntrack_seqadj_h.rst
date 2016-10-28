.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netfilter/nf_conntrack_seqadj.h

.. _`nf_ct_seqadj`:

struct nf_ct_seqadj
===================

.. c:type:: struct nf_ct_seqadj

    sequence number adjustment information

.. _`nf_ct_seqadj.definition`:

Definition
----------

.. code-block:: c

    struct nf_ct_seqadj {
        u32 correction_pos;
        s32 offset_before;
        s32 offset_after;
    }

.. _`nf_ct_seqadj.members`:

Members
-------

correction_pos
    position of the last TCP sequence number modification

offset_before
    sequence number offset before last modification

offset_after
    sequence number offset after last modification

.. This file was automatic generated / don't edit.


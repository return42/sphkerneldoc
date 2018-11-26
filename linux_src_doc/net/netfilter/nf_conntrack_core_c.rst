.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netfilter/nf_conntrack_core.c

.. _`nf_ct_iterate_destroy`:

nf_ct_iterate_destroy
=====================

.. c:function:: void nf_ct_iterate_destroy(int (*iter)(struct nf_conn *i, void *data), void *data)

    destroy unconfirmed conntracks and iterate table

    :param int (\*iter)(struct nf_conn \*i, void \*data):
        callback to invoke for each conntrack

    :param data:
        data to pass to \ ``iter``\ 
    :type data: void \*

.. _`nf_ct_iterate_destroy.description`:

Description
-----------

Like nf_ct_iterate_cleanup, but first marks conntracks on the
unconfirmed list as dying (so they will not be inserted into
main table).

Can only be called in module exit path.

.. This file was automatic generated / don't edit.


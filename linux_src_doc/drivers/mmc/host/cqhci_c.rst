.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/cqhci.c

.. _`cqhci_host_alloc_tdl`:

cqhci_host_alloc_tdl
====================

.. c:function:: int cqhci_host_alloc_tdl(struct cqhci_host *cq_host)

    :param struct cqhci_host \*cq_host:
        *undescribed*

.. _`cqhci_host_alloc_tdl.looks-like`:

looks like
----------

\|----------\|
\|task desc \|  \|->\|----------\|
\|----------\|  \|  \|trans desc\|
\|link desc-\|->\|  \|----------\|
\|----------\|          .
.                .
no. of slots      max-segs
.           \|----------\|
\|----------\|
The idea here is to create the [task+trans] table and mark & point the
link desc to the transfer desc table on a per slot basis.

.. This file was automatic generated / don't edit.


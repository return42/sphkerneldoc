.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/client-buffers.c

.. _`ishtp_cl_alloc_rx_ring`:

ishtp_cl_alloc_rx_ring
======================

.. c:function:: int ishtp_cl_alloc_rx_ring(struct ishtp_cl *cl)

    Allocate RX ring buffers

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_alloc_rx_ring.description`:

Description
-----------

Allocate and initialize RX ring buffers

.. _`ishtp_cl_alloc_rx_ring.return`:

Return
------

0 on success else -ENOMEM

.. _`ishtp_cl_alloc_tx_ring`:

ishtp_cl_alloc_tx_ring
======================

.. c:function:: int ishtp_cl_alloc_tx_ring(struct ishtp_cl *cl)

    Allocate TX ring buffers

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_alloc_tx_ring.description`:

Description
-----------

Allocate and initialize TX ring buffers

.. _`ishtp_cl_alloc_tx_ring.return`:

Return
------

0 on success else -ENOMEM

.. _`ishtp_cl_free_rx_ring`:

ishtp_cl_free_rx_ring
=====================

.. c:function:: void ishtp_cl_free_rx_ring(struct ishtp_cl *cl)

    Free RX ring buffers

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_free_rx_ring.description`:

Description
-----------

Free RX ring buffers

.. _`ishtp_cl_free_tx_ring`:

ishtp_cl_free_tx_ring
=====================

.. c:function:: void ishtp_cl_free_tx_ring(struct ishtp_cl *cl)

    Free TX ring buffers

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_free_tx_ring.description`:

Description
-----------

Free TX ring buffers

.. _`ishtp_io_rb_free`:

ishtp_io_rb_free
================

.. c:function:: void ishtp_io_rb_free(struct ishtp_cl_rb *rb)

    Free IO request block

    :param struct ishtp_cl_rb \*rb:
        IO request block

.. _`ishtp_io_rb_free.description`:

Description
-----------

Free io request block memory

.. _`ishtp_io_rb_init`:

ishtp_io_rb_init
================

.. c:function:: struct ishtp_cl_rb *ishtp_io_rb_init(struct ishtp_cl *cl)

    Allocate and init IO request block

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_io_rb_init.description`:

Description
-----------

Allocate and initialize request block

.. _`ishtp_io_rb_init.return`:

Return
------

Allocted IO request block pointer

.. _`ishtp_io_rb_alloc_buf`:

ishtp_io_rb_alloc_buf
=====================

.. c:function:: int ishtp_io_rb_alloc_buf(struct ishtp_cl_rb *rb, size_t length)

    Allocate and init response buffer

    :param struct ishtp_cl_rb \*rb:
        IO request block

    :param size_t length:
        length of response buffer

.. _`ishtp_io_rb_alloc_buf.description`:

Description
-----------

Allocate respose buffer

.. _`ishtp_io_rb_alloc_buf.return`:

Return
------

0 on success else -ENOMEM

.. _`ishtp_cl_io_rb_recycle`:

ishtp_cl_io_rb_recycle
======================

.. c:function:: int ishtp_cl_io_rb_recycle(struct ishtp_cl_rb *rb)

    Recycle IO request blocks

    :param struct ishtp_cl_rb \*rb:
        IO request block

.. _`ishtp_cl_io_rb_recycle.description`:

Description
-----------

Re-append rb to its client's free list and send flow control if needed

.. _`ishtp_cl_io_rb_recycle.return`:

Return
------

0 on success else -EFAULT

.. This file was automatic generated / don't edit.


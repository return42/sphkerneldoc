.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-mem.c

.. _`cvm_oct_fill_hw_skbuff`:

cvm_oct_fill_hw_skbuff
======================

.. c:function:: int cvm_oct_fill_hw_skbuff(int pool, int size, int elements)

    fill the supplied hardware pool with skbuffs

    :param pool:
        Pool to allocate an skbuff for
    :type pool: int

    :param size:
        Size of the buffer needed for the pool
    :type size: int

    :param elements:
        Number of buffers to allocate
    :type elements: int

.. _`cvm_oct_fill_hw_skbuff.description`:

Description
-----------

Returns the actual number of buffers allocated.

.. _`cvm_oct_free_hw_skbuff`:

cvm_oct_free_hw_skbuff
======================

.. c:function:: void cvm_oct_free_hw_skbuff(int pool, int size, int elements)

    free hardware pool skbuffs

    :param pool:
        Pool to allocate an skbuff for
    :type pool: int

    :param size:
        Size of the buffer needed for the pool
    :type size: int

    :param elements:
        Number of buffers to allocate
    :type elements: int

.. _`cvm_oct_fill_hw_memory`:

cvm_oct_fill_hw_memory
======================

.. c:function:: int cvm_oct_fill_hw_memory(int pool, int size, int elements)

    fill a hardware pool with memory.

    :param pool:
        Pool to populate
    :type pool: int

    :param size:
        Size of each buffer in the pool
    :type size: int

    :param elements:
        Number of buffers to allocate
    :type elements: int

.. _`cvm_oct_fill_hw_memory.description`:

Description
-----------

Returns the actual number of buffers allocated.

.. _`cvm_oct_free_hw_memory`:

cvm_oct_free_hw_memory
======================

.. c:function:: void cvm_oct_free_hw_memory(int pool, int size, int elements)

    Free memory allocated by cvm_oct_fill_hw_memory

    :param pool:
        FPA pool to free
    :type pool: int

    :param size:
        Size of each buffer in the pool
    :type size: int

    :param elements:
        Number of buffers that should be in the pool
    :type elements: int

.. This file was automatic generated / don't edit.


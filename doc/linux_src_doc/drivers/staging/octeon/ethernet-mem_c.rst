.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-mem.c

.. _`cvm_oct_fill_hw_skbuff`:

cvm_oct_fill_hw_skbuff
======================

.. c:function:: int cvm_oct_fill_hw_skbuff(int pool, int size, int elements)

    fill the supplied hardware pool with skbuffs

    :param int pool:
        Pool to allocate an skbuff for

    :param int size:
        Size of the buffer needed for the pool

    :param int elements:
        Number of buffers to allocate

.. _`cvm_oct_fill_hw_skbuff.description`:

Description
-----------

Returns the actual number of buffers allocated.

.. _`cvm_oct_free_hw_skbuff`:

cvm_oct_free_hw_skbuff
======================

.. c:function:: void cvm_oct_free_hw_skbuff(int pool, int size, int elements)

    free hardware pool skbuffs

    :param int pool:
        Pool to allocate an skbuff for

    :param int size:
        Size of the buffer needed for the pool

    :param int elements:
        Number of buffers to allocate

.. _`cvm_oct_fill_hw_memory`:

cvm_oct_fill_hw_memory
======================

.. c:function:: int cvm_oct_fill_hw_memory(int pool, int size, int elements)

    fill a hardware pool with memory.

    :param int pool:
        Pool to populate

    :param int size:
        Size of each buffer in the pool

    :param int elements:
        Number of buffers to allocate

.. _`cvm_oct_fill_hw_memory.description`:

Description
-----------

Returns the actual number of buffers allocated.

.. _`cvm_oct_free_hw_memory`:

cvm_oct_free_hw_memory
======================

.. c:function:: void cvm_oct_free_hw_memory(int pool, int size, int elements)

    Free memory allocated by cvm_oct_fill_hw_memory

    :param int pool:
        FPA pool to free

    :param int size:
        Size of each buffer in the pool

    :param int elements:
        Number of buffers that should be in the pool

.. This file was automatic generated / don't edit.


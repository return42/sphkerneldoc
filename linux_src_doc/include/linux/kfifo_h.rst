.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kfifo.h

.. _`declare_kfifo_ptr`:

DECLARE_KFIFO_PTR
=================

.. c:function::  DECLARE_KFIFO_PTR( fifo,  type)

    macro to declare a fifo pointer object

    :param  fifo:
        name of the declared fifo

    :param  type:
        type of the fifo elements

.. _`declare_kfifo`:

DECLARE_KFIFO
=============

.. c:function::  DECLARE_KFIFO( fifo,  type,  size)

    macro to declare a fifo object

    :param  fifo:
        name of the declared fifo

    :param  type:
        type of the fifo elements

    :param  size:
        the number of elements in the fifo, this must be a power of 2

.. _`init_kfifo`:

INIT_KFIFO
==========

.. c:function::  INIT_KFIFO( fifo)

    Initialize a fifo declared by DECLARE_KFIFO

    :param  fifo:
        name of the declared fifo datatype

.. _`define_kfifo`:

DEFINE_KFIFO
============

.. c:function::  DEFINE_KFIFO( fifo,  type,  size)

    macro to define and initialize a fifo

    :param  fifo:
        name of the declared fifo datatype

    :param  type:
        type of the fifo elements

    :param  size:
        the number of elements in the fifo, this must be a power of 2

.. _`define_kfifo.note`:

Note
----

the macro can be used for global and local fifo data type variables.

.. _`kfifo_initialized`:

kfifo_initialized
=================

.. c:function::  kfifo_initialized( fifo)

    Check if the fifo is initialized

    :param  fifo:
        address of the fifo to check

.. _`kfifo_initialized.description`:

Description
-----------

Return \ ``true``\  if fifo is initialized, otherwise \ ``false``\ .
Assumes the fifo was 0 before.

.. _`kfifo_esize`:

kfifo_esize
===========

.. c:function::  kfifo_esize( fifo)

    returns the size of the element managed by the fifo

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_recsize`:

kfifo_recsize
=============

.. c:function::  kfifo_recsize( fifo)

    returns the size of the record length field

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_size`:

kfifo_size
==========

.. c:function::  kfifo_size( fifo)

    returns the size of the fifo in elements

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_reset`:

kfifo_reset
===========

.. c:function::  kfifo_reset( fifo)

    removes the entire fifo content

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_reset.note`:

Note
----

usage of \ :c:func:`kfifo_reset`\  is dangerous. It should be only called when the
fifo is exclusived locked or when it is secured that no other thread is
accessing the fifo.

.. _`kfifo_reset_out`:

kfifo_reset_out
===============

.. c:function::  kfifo_reset_out( fifo)

    skip fifo content

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_reset_out.note`:

Note
----

The usage of \ :c:func:`kfifo_reset_out`\  is safe until it will be only called
from the reader thread and there is only one concurrent reader. Otherwise
it is dangerous and must be handled in the same way as \ :c:func:`kfifo_reset`\ .

.. _`kfifo_len`:

kfifo_len
=========

.. c:function::  kfifo_len( fifo)

    returns the number of used elements in the fifo

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_is_empty`:

kfifo_is_empty
==============

.. c:function::  kfifo_is_empty( fifo)

    returns true if the fifo is empty

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_is_full`:

kfifo_is_full
=============

.. c:function::  kfifo_is_full( fifo)

    returns true if the fifo is full

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_avail`:

kfifo_avail
===========

.. c:function::  kfifo_avail( fifo)

    returns the number of unused elements in the fifo

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_skip`:

kfifo_skip
==========

.. c:function::  kfifo_skip( fifo)

    skip output data

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_peek_len`:

kfifo_peek_len
==============

.. c:function::  kfifo_peek_len( fifo)

    gets the size of the next fifo record

    :param  fifo:
        address of the fifo to be used

.. _`kfifo_peek_len.description`:

Description
-----------

This function returns the size of the next fifo record in number of bytes.

.. _`kfifo_alloc`:

kfifo_alloc
===========

.. c:function::  kfifo_alloc( fifo,  size,  gfp_mask)

    dynamically allocates a new fifo buffer

    :param  fifo:
        pointer to the fifo

    :param  size:
        the number of elements in the fifo, this must be a power of 2

    :param  gfp_mask:
        get_free_pages mask, passed to \ :c:func:`kmalloc`\ 

.. _`kfifo_alloc.description`:

Description
-----------

This macro dynamically allocates a new fifo buffer.

The number of elements will be rounded-up to a power of 2.
The fifo will be release with \ :c:func:`kfifo_free`\ .
Return 0 if no error, otherwise an error code.

.. _`kfifo_free`:

kfifo_free
==========

.. c:function::  kfifo_free( fifo)

    frees the fifo

    :param  fifo:
        the fifo to be freed

.. _`kfifo_init`:

kfifo_init
==========

.. c:function::  kfifo_init( fifo,  buffer,  size)

    initialize a fifo using a preallocated buffer

    :param  fifo:
        the fifo to assign the buffer

    :param  buffer:
        the preallocated buffer to be used

    :param  size:
        the size of the internal buffer, this have to be a power of 2

.. _`kfifo_init.description`:

Description
-----------

This macro initializes a fifo using a preallocated buffer.

The number of elements will be rounded-up to a power of 2.
Return 0 if no error, otherwise an error code.

.. _`kfifo_put`:

kfifo_put
=========

.. c:function::  kfifo_put( fifo,  val)

    put data into the fifo

    :param  fifo:
        address of the fifo to be used

    :param  val:
        the data to be added

.. _`kfifo_put.description`:

Description
-----------

This macro copies the given value into the fifo.
It returns 0 if the fifo was full. Otherwise it returns the number
processed elements.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_get`:

kfifo_get
=========

.. c:function::  kfifo_get( fifo,  val)

    get data from the fifo

    :param  fifo:
        address of the fifo to be used

    :param  val:
        address where to store the data

.. _`kfifo_get.description`:

Description
-----------

This macro reads the data from the fifo.
It returns 0 if the fifo was empty. Otherwise it returns the number
processed elements.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_peek`:

kfifo_peek
==========

.. c:function::  kfifo_peek( fifo,  val)

    get data from the fifo without removing

    :param  fifo:
        address of the fifo to be used

    :param  val:
        address where to store the data

.. _`kfifo_peek.description`:

Description
-----------

This reads the data from the fifo without removing it from the fifo.
It returns 0 if the fifo was empty. Otherwise it returns the number
processed elements.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_in`:

kfifo_in
========

.. c:function::  kfifo_in( fifo,  buf,  n)

    put data into the fifo

    :param  fifo:
        address of the fifo to be used

    :param  buf:
        the data to be added

    :param  n:
        number of elements to be added

.. _`kfifo_in.description`:

Description
-----------

This macro copies the given buffer into the fifo and returns the
number of copied elements.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_in_spinlocked`:

kfifo_in_spinlocked
===================

.. c:function::  kfifo_in_spinlocked( fifo,  buf,  n,  lock)

    put data into the fifo using a spinlock for locking

    :param  fifo:
        address of the fifo to be used

    :param  buf:
        the data to be added

    :param  n:
        number of elements to be added

    :param  lock:
        pointer to the spinlock to use for locking

.. _`kfifo_in_spinlocked.description`:

Description
-----------

This macro copies the given values buffer into the fifo and returns the
number of copied elements.

.. _`kfifo_out`:

kfifo_out
=========

.. c:function::  kfifo_out( fifo,  buf,  n)

    get data from the fifo

    :param  fifo:
        address of the fifo to be used

    :param  buf:
        pointer to the storage buffer

    :param  n:
        max. number of elements to get

.. _`kfifo_out.description`:

Description
-----------

This macro get some data from the fifo and return the numbers of elements
copied.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_out_spinlocked`:

kfifo_out_spinlocked
====================

.. c:function::  kfifo_out_spinlocked( fifo,  buf,  n,  lock)

    get data from the fifo using a spinlock for locking

    :param  fifo:
        address of the fifo to be used

    :param  buf:
        pointer to the storage buffer

    :param  n:
        max. number of elements to get

    :param  lock:
        pointer to the spinlock to use for locking

.. _`kfifo_out_spinlocked.description`:

Description
-----------

This macro get the data from the fifo and return the numbers of elements
copied.

.. _`kfifo_from_user`:

kfifo_from_user
===============

.. c:function::  kfifo_from_user( fifo,  from,  len,  copied)

    puts some data from user space into the fifo

    :param  fifo:
        address of the fifo to be used

    :param  from:
        pointer to the data to be added

    :param  len:
        the length of the data to be added

    :param  copied:
        pointer to output variable to store the number of copied bytes

.. _`kfifo_from_user.description`:

Description
-----------

This macro copies at most \ ``len``\  bytes from the \ ``from``\  into the
fifo, depending of the available space and returns -EFAULT/0.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_to_user`:

kfifo_to_user
=============

.. c:function::  kfifo_to_user( fifo,  to,  len,  copied)

    copies data from the fifo into user space

    :param  fifo:
        address of the fifo to be used

    :param  to:
        where the data must be copied

    :param  len:
        the size of the destination buffer

    :param  copied:
        pointer to output variable to store the number of copied bytes

.. _`kfifo_to_user.description`:

Description
-----------

This macro copies at most \ ``len``\  bytes from the fifo into the
\ ``to``\  buffer and returns -EFAULT/0.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. _`kfifo_dma_in_prepare`:

kfifo_dma_in_prepare
====================

.. c:function::  kfifo_dma_in_prepare( fifo,  sgl,  nents,  len)

    setup a scatterlist for DMA input

    :param  fifo:
        address of the fifo to be used

    :param  sgl:
        pointer to the scatterlist array

    :param  nents:
        number of entries in the scatterlist array

    :param  len:
        number of elements to transfer

.. _`kfifo_dma_in_prepare.description`:

Description
-----------

This macro fills a scatterlist for DMA input.
It returns the number entries in the scatterlist array.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macros.

.. _`kfifo_dma_in_finish`:

kfifo_dma_in_finish
===================

.. c:function::  kfifo_dma_in_finish( fifo,  len)

    finish a DMA IN operation

    :param  fifo:
        address of the fifo to be used

    :param  len:
        number of bytes to received

.. _`kfifo_dma_in_finish.description`:

Description
-----------

This macro finish a DMA IN operation. The in counter will be updated by
the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macros.

.. _`kfifo_dma_out_prepare`:

kfifo_dma_out_prepare
=====================

.. c:function::  kfifo_dma_out_prepare( fifo,  sgl,  nents,  len)

    setup a scatterlist for DMA output

    :param  fifo:
        address of the fifo to be used

    :param  sgl:
        pointer to the scatterlist array

    :param  nents:
        number of entries in the scatterlist array

    :param  len:
        number of elements to transfer

.. _`kfifo_dma_out_prepare.description`:

Description
-----------

This macro fills a scatterlist for DMA output which at most \ ``len``\  bytes
to transfer.
It returns the number entries in the scatterlist array.
A zero means there is no space available and the scatterlist is not filled.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macros.

.. _`kfifo_dma_out_finish`:

kfifo_dma_out_finish
====================

.. c:function::  kfifo_dma_out_finish( fifo,  len)

    finish a DMA OUT operation

    :param  fifo:
        address of the fifo to be used

    :param  len:
        number of bytes transferred

.. _`kfifo_dma_out_finish.description`:

Description
-----------

This macro finish a DMA OUT operation. The out counter will be updated by
the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macros.

.. _`kfifo_out_peek`:

kfifo_out_peek
==============

.. c:function::  kfifo_out_peek( fifo,  buf,  n)

    gets some data from the fifo

    :param  fifo:
        address of the fifo to be used

    :param  buf:
        pointer to the storage buffer

    :param  n:
        max. number of elements to get

.. _`kfifo_out_peek.description`:

Description
-----------

This macro get the data from the fifo and return the numbers of elements
copied. The data is not removed from the fifo.

Note that with only one concurrent reader and one concurrent
writer, you don't need extra locking to use these macro.

.. This file was automatic generated / don't edit.


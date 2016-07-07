.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/atomic.h

.. _`atomic_read`:

atomic_read
===========

.. c:function::  atomic_read( v)

    read atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`atomic_set`:

atomic_set
==========

.. c:function::  atomic_set( v,  i)

    set atomic variable

    :param  v:
        pointer of type atomic_t

    :param  i:
        required value

.. _`atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. This file was automatic generated / don't edit.


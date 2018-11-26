.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon/ethernet-util.h

.. _`cvm_oct_get_buffer_ptr`:

cvm_oct_get_buffer_ptr
======================

.. c:function:: void *cvm_oct_get_buffer_ptr(union cvmx_buf_ptr packet_ptr)

    convert packet data address to pointer

    :param packet_ptr:
        Packet data hardware address
    :type packet_ptr: union cvmx_buf_ptr

.. _`cvm_oct_get_buffer_ptr.description`:

Description
-----------

Returns Packet buffer pointer

.. _`interface`:

INTERFACE
=========

.. c:function:: int INTERFACE(int ipd_port)

    convert IPD port to logical interface

    :param ipd_port:
        Port to check
    :type ipd_port: int

.. _`interface.description`:

Description
-----------

Returns Logical interface

.. _`index`:

INDEX
=====

.. c:function:: int INDEX(int ipd_port)

    convert IPD/PKO port number to the port's interface index

    :param ipd_port:
        Port to check
    :type ipd_port: int

.. _`index.description`:

Description
-----------

Returns Index into interface port list

.. This file was automatic generated / don't edit.


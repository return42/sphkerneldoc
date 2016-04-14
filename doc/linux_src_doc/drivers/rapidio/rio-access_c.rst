.. -*- coding: utf-8; mode: rst -*-

============
rio-access.c
============

.. _`rio_lop_read`:

RIO_LOP_READ
============

.. c:function:: RIO_LOP_READ ( size,  type,  len)

    Generate rio_local_read_config_* functions

    :param size:
        Size of configuration space read (8, 16, 32 bits)

    :param type:
        C type of value argument

    :param len:
        Length of configuration space read (1, 2, 4 bytes)


.. _`rio_lop_read.description`:

Description
-----------

Generates rio_local_read_config_\* functions used to access
configuration space registers on the local device.


.. _`rio_lop_write`:

RIO_LOP_WRITE
=============

.. c:function:: RIO_LOP_WRITE ( size,  type,  len)

    Generate rio_local_write_config_* functions

    :param size:
        Size of configuration space write (8, 16, 32 bits)

    :param type:
        C type of value argument

    :param len:
        Length of configuration space write (1, 2, 4 bytes)


.. _`rio_lop_write.description`:

Description
-----------

Generates rio_local_write_config_\* functions used to access
configuration space registers on the local device.


.. _`rio_op_read`:

RIO_OP_READ
===========

.. c:function:: RIO_OP_READ ( size,  type,  len)

    Generate rio_mport_read_config_* functions

    :param size:
        Size of configuration space read (8, 16, 32 bits)

    :param type:
        C type of value argument

    :param len:
        Length of configuration space read (1, 2, 4 bytes)


.. _`rio_op_read.description`:

Description
-----------

Generates rio_mport_read_config_\* functions used to access
configuration space registers on the local device.


.. _`rio_op_write`:

RIO_OP_WRITE
============

.. c:function:: RIO_OP_WRITE ( size,  type,  len)

    Generate rio_mport_write_config_* functions

    :param size:
        Size of configuration space write (8, 16, 32 bits)

    :param type:
        C type of value argument

    :param len:
        Length of configuration space write (1, 2, 4 bytes)


.. _`rio_op_write.description`:

Description
-----------

Generates rio_mport_write_config_\* functions used to access
configuration space registers on the local device.


.. _`rio_mport_send_doorbell`:

rio_mport_send_doorbell
=======================

.. c:function:: int rio_mport_send_doorbell (struct rio_mport *mport, u16 destid, u16 data)

    Send a doorbell message

    :param struct rio_mport \*mport:
        RIO master port

    :param u16 destid:
        RIO device destination ID

    :param u16 data:
        Doorbell message data


.. _`rio_mport_send_doorbell.description`:

Description
-----------

Send a doorbell message to a RIO device. The doorbell message
has a 16-bit info field provided by the data argument.


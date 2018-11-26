.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/isc.c

.. _`isc_register`:

isc_register
============

.. c:function:: void isc_register(unsigned int isc)

    register an I/O interruption subclass.

    :param isc:
        I/O interruption subclass to register
    :type isc: unsigned int

.. _`isc_register.description`:

Description
-----------

The number of users for \ ``isc``\  is increased. If this is the first user to
register \ ``isc``\ , the corresponding I/O interruption subclass mask is enabled.

.. _`isc_register.context`:

Context
-------

This function must not be called in interrupt context.

.. _`isc_unregister`:

isc_unregister
==============

.. c:function:: void isc_unregister(unsigned int isc)

    unregister an I/O interruption subclass.

    :param isc:
        I/O interruption subclass to unregister
    :type isc: unsigned int

.. _`isc_unregister.description`:

Description
-----------

The number of users for \ ``isc``\  is decreased. If this is the last user to
unregister \ ``isc``\ , the corresponding I/O interruption subclass mask is
disabled.

.. _`isc_unregister.note`:

Note
----

This function must not be called if \ :c:func:`isc_register`\  hasn't been called
before by the driver for \ ``isc``\ .

.. _`isc_unregister.context`:

Context
-------

This function must not be called in interrupt context.

.. This file was automatic generated / don't edit.


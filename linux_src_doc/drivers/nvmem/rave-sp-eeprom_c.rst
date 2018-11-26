.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvmem/rave-sp-eeprom.c

.. _`rave_sp_eeprom_access_type`:

enum rave_sp_eeprom_access_type
===============================

.. c:type:: enum rave_sp_eeprom_access_type

    Supported types of EEPROM access

.. _`rave_sp_eeprom_access_type.definition`:

Definition
----------

.. code-block:: c

    enum rave_sp_eeprom_access_type {
        RAVE_SP_EEPROM_WRITE,
        RAVE_SP_EEPROM_READ
    };

.. _`rave_sp_eeprom_access_type.constants`:

Constants
---------

RAVE_SP_EEPROM_WRITE
    EEPROM write

RAVE_SP_EEPROM_READ
    EEPROM read

.. _`rave_sp_eeprom_header_size`:

enum rave_sp_eeprom_header_size
===============================

.. c:type:: enum rave_sp_eeprom_header_size

    EEPROM command header sizes

.. _`rave_sp_eeprom_header_size.definition`:

Definition
----------

.. code-block:: c

    enum rave_sp_eeprom_header_size {
        RAVE_SP_EEPROM_HEADER_SMALL,
        RAVE_SP_EEPROM_HEADER_BIG
    };

.. _`rave_sp_eeprom_header_size.constants`:

Constants
---------

RAVE_SP_EEPROM_HEADER_SMALL
    EEPROM header size for "small" devices (< 8K)

RAVE_SP_EEPROM_HEADER_BIG
    EEPROM header size for "big" devices (> 8K)

.. _`rave_sp_eeprom_page`:

struct rave_sp_eeprom_page
==========================

.. c:type:: struct rave_sp_eeprom_page

    RAVE SP EEPROM page

.. _`rave_sp_eeprom_page.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_eeprom_page {
        u8 type;
        u8 success;
        u8 data[RAVE_SP_EEPROM_PAGE_SIZE];
    }

.. _`rave_sp_eeprom_page.members`:

Members
-------

type
    Access type (see enum rave_sp_eeprom_access_type)

success
    Success flag (Success = 1, Failure = 0)

data
    Read data
    Note this structure corresponds to RSP\_\*\_EEPROM payload from RAVE
    SP ICD

.. _`rave_sp_eeprom`:

struct rave_sp_eeprom
=====================

.. c:type:: struct rave_sp_eeprom

    RAVE SP EEPROM device

.. _`rave_sp_eeprom.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_eeprom {
        struct rave_sp *sp;
        struct mutex mutex;
        u8 address;
        unsigned int header_size;
        struct device *dev;
    }

.. _`rave_sp_eeprom.members`:

Members
-------

sp
    Pointer to parent RAVE SP device

mutex
    Lock protecting access to EEPROM

address
    EEPROM device address

header_size
    Size of EEPROM command header for this device

dev
    Pointer to corresponding struct device used for logging

.. _`rave_sp_eeprom_io`:

rave_sp_eeprom_io
=================

.. c:function:: int rave_sp_eeprom_io(struct rave_sp_eeprom *eeprom, enum rave_sp_eeprom_access_type type, u16 idx, struct rave_sp_eeprom_page *page)

    Low-level part of EEPROM page access

    :param eeprom:
        EEPROM device to write to
    :type eeprom: struct rave_sp_eeprom \*

    :param type:
        EEPROM access type (read or write)
    :type type: enum rave_sp_eeprom_access_type

    :param idx:
        number of the EEPROM page
    :type idx: u16

    :param page:
        Data to write or buffer to store result (via page->data)
    :type page: struct rave_sp_eeprom_page \*

.. _`rave_sp_eeprom_io.description`:

Description
-----------

This function does all of the low-level work required to perform a
EEPROM access. This includes formatting correct command payload,
sending it and checking received results.

Returns zero in case of success or negative error code in
case of failure.

.. _`rave_sp_eeprom_page_access`:

rave_sp_eeprom_page_access
==========================

.. c:function:: int rave_sp_eeprom_page_access(struct rave_sp_eeprom *eeprom, enum rave_sp_eeprom_access_type type, unsigned int offset, u8 *data, size_t data_len)

    Access single EEPROM page

    :param eeprom:
        EEPROM device to access
    :type eeprom: struct rave_sp_eeprom \*

    :param type:
        Access type to perform (read or write)
    :type type: enum rave_sp_eeprom_access_type

    :param offset:
        Offset within EEPROM to access
    :type offset: unsigned int

    :param data:
        Data buffer
    :type data: u8 \*

    :param data_len:
        Size of the data buffer
    :type data_len: size_t

.. _`rave_sp_eeprom_page_access.description`:

Description
-----------

This function performs a generic access to a single page or a
portion thereof. Requested access MUST NOT cross the EEPROM page
boundary.

Returns zero in case of success or negative error code in
case of failure.

.. _`rave_sp_eeprom_access`:

rave_sp_eeprom_access
=====================

.. c:function:: int rave_sp_eeprom_access(struct rave_sp_eeprom *eeprom, enum rave_sp_eeprom_access_type type, unsigned int offset, u8 *data, unsigned int data_len)

    Access EEPROM data

    :param eeprom:
        EEPROM device to access
    :type eeprom: struct rave_sp_eeprom \*

    :param type:
        Access type to perform (read or write)
    :type type: enum rave_sp_eeprom_access_type

    :param offset:
        Offset within EEPROM to access
    :type offset: unsigned int

    :param data:
        Data buffer
    :type data: u8 \*

    :param data_len:
        Size of the data buffer
    :type data_len: unsigned int

.. _`rave_sp_eeprom_access.description`:

Description
-----------

This function performs a generic access (either read or write) at
arbitrary offset (not necessary page aligned) of arbitrary length
(is not constrained by EEPROM page size).

Returns zero in case of success or negative error code in case of
failure.

.. This file was automatic generated / don't edit.


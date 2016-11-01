.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec-edid.h

.. _`cec_get_edid_phys_addr`:

cec_get_edid_phys_addr
======================

.. c:function:: u16 cec_get_edid_phys_addr(const u8 *edid, unsigned int size, unsigned int *offset)

    find and return the physical address

    :param const u8 \*edid:
        pointer to the EDID data

    :param unsigned int size:
        size in bytes of the EDID data

    :param unsigned int \*offset:
        If not \ ``NULL``\  then the location of the physical address
        bytes in the EDID will be returned here. This is set to 0
        if there is no physical address found.

.. _`cec_get_edid_phys_addr.return`:

Return
------

the physical address or CEC_PHYS_ADDR_INVALID if there is none.

.. _`cec_set_edid_phys_addr`:

cec_set_edid_phys_addr
======================

.. c:function:: void cec_set_edid_phys_addr(u8 *edid, unsigned int size, u16 phys_addr)

    find and set the physical address

    :param u8 \*edid:
        pointer to the EDID data

    :param unsigned int size:
        size in bytes of the EDID data

    :param u16 phys_addr:
        the new physical address

.. _`cec_set_edid_phys_addr.description`:

Description
-----------

This function finds the location of the physical address in the EDID
and fills in the given physical address and updates the checksum
at the end of the EDID block. It does nothing if the EDID doesn't
contain a physical address.

.. _`cec_phys_addr_for_input`:

cec_phys_addr_for_input
=======================

.. c:function:: u16 cec_phys_addr_for_input(u16 phys_addr, u8 input)

    calculate the PA for an input

    :param u16 phys_addr:
        the physical address of the parent

    :param u8 input:
        the number of the input port, must be between 1 and 15

.. _`cec_phys_addr_for_input.description`:

Description
-----------

This function calculates a new physical address based on the input
port number. For example:

PA = 0.0.0.0 and input = 2 becomes 2.0.0.0

PA = 3.0.0.0 and input = 1 becomes 3.1.0.0

PA = 3.2.1.0 and input = 5 becomes 3.2.1.5

PA = 3.2.1.3 and input = 5 becomes f.f.f.f since it maxed out the depth.

.. _`cec_phys_addr_for_input.return`:

Return
------

the new physical address or CEC_PHYS_ADDR_INVALID.

.. _`cec_phys_addr_validate`:

cec_phys_addr_validate
======================

.. c:function:: int cec_phys_addr_validate(u16 phys_addr, u16 *parent, u16 *port)

    validate a physical address from an EDID

    :param u16 phys_addr:
        the physical address to validate

    :param u16 \*parent:
        if not \ ``NULL``\ , then this is filled with the parents PA.

    :param u16 \*port:
        if not \ ``NULL``\ , then this is filled with the input port.

.. _`cec_phys_addr_validate.description`:

Description
-----------

This validates a physical address as read from an EDID. If the
PA is invalid (such as 1.0.1.0 since '0' is only allowed at the end),
then it will return -EINVAL.

The parent PA is passed into \ ``parent``\  and the input port is passed into
\ ``port``\ . For example:

PA = 0.0.0.0: has parent 0.0.0.0 and input port 0.

PA = 1.0.0.0: has parent 0.0.0.0 and input port 1.

PA = 3.2.0.0: has parent 3.0.0.0 and input port 2.

PA = f.f.f.f: has parent f.f.f.f and input port 0.

.. _`cec_phys_addr_validate.return`:

Return
------

0 if the PA is valid, -EINVAL if not.

.. This file was automatic generated / don't edit.


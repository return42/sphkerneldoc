.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/swphy.c

.. _`swphy_validate_state`:

swphy_validate_state
====================

.. c:function:: int swphy_validate_state(const struct fixed_phy_status *state)

    validate the software phy status

    :param const struct fixed_phy_status \*state:
        software phy status

.. _`swphy_validate_state.description`:

Description
-----------

This checks that we can represent the state stored in \ ``state``\  can be
represented in the emulated MII registers.  Returns 0 if it can,
otherwise returns -EINVAL.

.. _`swphy_read_reg`:

swphy_read_reg
==============

.. c:function:: int swphy_read_reg(int reg, const struct fixed_phy_status *state)

    return a MII register from the fixed phy state

    :param int reg:
        MII register

    :param const struct fixed_phy_status \*state:
        fixed phy status

.. _`swphy_read_reg.description`:

Description
-----------

Return the MII \ ``reg``\  register generated from the fixed phy state \ ``state``\ .

.. This file was automatic generated / don't edit.

